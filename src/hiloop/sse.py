"""Typed helpers for hiloop's Server-Sent Events surfaces."""

from __future__ import annotations

import base64
import json
from collections.abc import AsyncIterator, Iterator, Mapping
from typing import Any, Generic, TypeVar, cast

import httpx
from attrs import define

from .client import AuthenticatedClient, Client
from .models.error_body import ErrorBody

T = TypeVar("T")
SdkClient = AuthenticatedClient | Client


@define(frozen=True)
class SseEvent(Generic[T]):
    """One decoded SSE frame, including its resume metadata."""

    data: T
    id: str | None = None
    event: str | None = None
    retry: int | None = None


@define(frozen=True)
class ExecExit:
    """The terminal disposition of a streamed execution."""

    exit_code: int
    signal: int


@define(frozen=True)
class ExecOutputEvent:
    """A stdout chunk, stderr chunk, or terminal exit from an execution."""

    stdout: bytes | None = None
    stderr: bytes | None = None
    exit: ExecExit | None = None


@define(frozen=True)
class StreamError:
    """A gRPC status delivered after an execution stream has opened."""

    code: int
    message: str


class _SseDecoder:
    def __init__(self) -> None:
        self._buffer = ""
        self._pending_cr = False

    def feed(self, chunk: str, *, final: bool = False) -> list[SseEvent[object]]:
        normalized = ""
        if self._pending_cr and (chunk or final):
            normalized = "\n"
            if chunk.startswith("\n"):
                chunk = chunk[1:]
            self._pending_cr = False
        if not final and chunk.endswith("\r"):
            chunk = chunk[:-1]
            self._pending_cr = True
        self._buffer += normalized + chunk.replace("\r\n", "\n").replace("\r", "\n")
        blocks = self._buffer.split("\n\n")
        self._buffer = blocks.pop()
        events: list[SseEvent[object]] = []
        for block in blocks:
            event = self._decode_block(block)
            if event is not None:
                events.append(event)
        return events

    @staticmethod
    def _decode_block(block: str) -> SseEvent[object] | None:
        data_lines: list[str] = []
        event_id = None
        event_name = None
        retry = None
        for line in block.split("\n"):
            if not line or line.startswith(":"):
                continue
            field, separator, value = line.partition(":")
            if separator and value.startswith(" "):
                value = value[1:]
            if field == "data":
                data_lines.append(value)
            elif field == "id":
                event_id = value
            elif field == "event":
                event_name = value
            elif field == "retry":
                try:
                    retry = int(value)
                except ValueError:
                    pass
        if not data_lines:
            return None
        raw = "\n".join(data_lines)
        try:
            data: object = json.loads(raw)
        except json.JSONDecodeError:
            data = raw
        return SseEvent(data=data, id=event_id, event=event_name, retry=retry)


def _error_body(response: httpx.Response) -> ErrorBody | None:
    response.read()
    try:
        body = response.json()
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None
    if not isinstance(body, Mapping):
        return None
    try:
        return ErrorBody.from_dict(cast("Mapping[str, Any]", body))
    except (KeyError, TypeError, ValueError):
        return None


async def _error_body_async(response: httpx.Response) -> ErrorBody | None:
    await response.aread()
    try:
        body = response.json()
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None
    if not isinstance(body, Mapping):
        return None
    try:
        return ErrorBody.from_dict(cast("Mapping[str, Any]", body))
    except (KeyError, TypeError, ValueError):
        return None


def _open(
    client: SdkClient,
    path: str,
    *,
    params: Mapping[str, str] | None = None,
) -> httpx.Response | ErrorBody | None:
    http = client.get_httpx_client()
    request = http.build_request("GET", path, params=params, headers={"Accept": "text/event-stream"})
    response = http.send(request, stream=True)
    if response.is_success:
        return response
    error = _error_body(response)
    response.close()
    return error


async def _open_async(
    client: SdkClient,
    path: str,
    *,
    params: Mapping[str, str] | None = None,
) -> httpx.Response | ErrorBody | None:
    http = client.get_async_httpx_client()
    request = http.build_request("GET", path, params=params, headers={"Accept": "text/event-stream"})
    response = await http.send(request, stream=True)
    if response.is_success:
        return response
    error = await _error_body_async(response)
    await response.aclose()
    return error


def _frames(response: httpx.Response) -> Iterator[SseEvent[object]]:
    decoder = _SseDecoder()
    try:
        for chunk in response.iter_text():
            yield from decoder.feed(chunk)
        yield from decoder.feed("", final=True)
    finally:
        response.close()


async def _frames_async(response: httpx.Response) -> AsyncIterator[SseEvent[object]]:
    decoder = _SseDecoder()
    try:
        async for chunk in response.aiter_text():
            for event in decoder.feed(chunk):
                yield event
        for event in decoder.feed("", final=True):
            yield event
    finally:
        await response.aclose()


def _exec_event(data: object) -> ExecOutputEvent | StreamError | None:
    if not isinstance(data, Mapping):
        raise ValueError("execution stream frame is not a JSON object")
    fields = cast("Mapping[str, object]", data)
    if not fields:
        return None
    code = fields.get("code")
    if isinstance(code, int):
        return StreamError(code=code, message=str(fields.get("message", "")))
    if "stdoutChunk" in fields:
        return ExecOutputEvent(stdout=base64.b64decode(str(fields.get("stdoutChunk")), validate=True))
    if "stderrChunk" in fields:
        return ExecOutputEvent(stderr=base64.b64decode(str(fields.get("stderrChunk")), validate=True))
    exit_value = fields.get("exit")
    if isinstance(exit_value, Mapping):
        exit_fields = cast("Mapping[str, object]", exit_value)
        return ExecOutputEvent(
            exit=ExecExit(
                exit_code=_integer(exit_fields.get("exitCode", 0), "exit.exitCode"),
                signal=_integer(exit_fields.get("signal", 0), "exit.signal"),
            )
        )
    raise ValueError("execution stream frame has no stdoutChunk, stderrChunk, exit, or status")


def _integer(value: object, field: str) -> int:
    if isinstance(value, (str, bytes, bytearray, int, float)):
        return int(value)
    raise ValueError(f"execution stream {field} is not an integer")


def stream_execution(
    *, client: SdkClient, execution_id: str
) -> Iterator[ExecOutputEvent | StreamError] | ErrorBody | None:
    """Open an execution stream, preserving typed HTTP errors at connection time."""
    opened = _open(client, f"/v1/executions/{execution_id}:stream")
    if not isinstance(opened, httpx.Response):
        return opened

    def events() -> Iterator[ExecOutputEvent | StreamError]:
        for frame in _frames(opened):
            event = _exec_event(frame.data)
            if event is not None:
                yield event

    return events()


async def stream_execution_async(
    *, client: SdkClient, execution_id: str
) -> AsyncIterator[ExecOutputEvent | StreamError] | ErrorBody | None:
    """Open an execution stream with the generated client's async HTTP transport."""
    opened = await _open_async(client, f"/v1/executions/{execution_id}:stream")
    if not isinstance(opened, httpx.Response):
        return opened

    async def events() -> AsyncIterator[ExecOutputEvent | StreamError]:
        async for frame in _frames_async(opened):
            event = _exec_event(frame.data)
            if event is not None:
                yield event

    return events()


def tail_run(
    *,
    client: SdkClient,
    run_id: str,
    lineage_path: str | None = None,
    signal: str | None = None,
    cursor: str | None = None,
) -> Iterator[SseEvent[dict[str, Any]]] | ErrorBody | None:
    """Tail canonical telemetry events for a run, including each resume cursor."""
    params = {"run_id": run_id}
    params.update(
        {
            key: value
            for key, value in {
                "lineage_path": lineage_path,
                "signal": signal,
                "cursor": cursor,
            }.items()
            if value
        }
    )
    opened = _open(client, "/v1/telemetry/tail", params=params)
    if not isinstance(opened, httpx.Response):
        return opened

    def events() -> Iterator[SseEvent[dict[str, Any]]]:
        for frame in _frames(opened):
            if not isinstance(frame.data, dict):
                raise ValueError("run tail frame is not a JSON object")
            data = cast("dict[str, Any]", frame.data)
            yield SseEvent(data=data, id=frame.id, event=frame.event, retry=frame.retry)

    return events()


async def tail_run_async(
    *,
    client: SdkClient,
    run_id: str,
    lineage_path: str | None = None,
    signal: str | None = None,
    cursor: str | None = None,
) -> AsyncIterator[SseEvent[dict[str, Any]]] | ErrorBody | None:
    """Tail canonical telemetry events with the generated client's async transport."""
    params = {"run_id": run_id}
    params.update(
        {
            key: value
            for key, value in {
                "lineage_path": lineage_path,
                "signal": signal,
                "cursor": cursor,
            }.items()
            if value
        }
    )
    opened = await _open_async(client, "/v1/telemetry/tail", params=params)
    if not isinstance(opened, httpx.Response):
        return opened

    async def events() -> AsyncIterator[SseEvent[dict[str, Any]]]:
        async for frame in _frames_async(opened):
            if not isinstance(frame.data, dict):
                raise ValueError("run tail frame is not a JSON object")
            data = cast("dict[str, Any]", frame.data)
            yield SseEvent(data=data, id=frame.id, event=frame.event, retry=frame.retry)

    return events()
