"""Ergonomic sandbox lifecycle helpers over the generated hiloop client."""

from __future__ import annotations

import asyncio
import time
import uuid
from collections.abc import AsyncIterator, Iterator
from typing import TypeVar, cast

from attrs import define, evolve

from .api.runtime_service import (
    runtime_service_create_sandbox,
    runtime_service_create_snapshot,
    runtime_service_execute_sandbox,
    runtime_service_expose_port,
    runtime_service_file_from_artifact,
    runtime_service_file_to_artifact,
    runtime_service_fork_sandbox,
    runtime_service_get_operation,
    runtime_service_get_sandbox,
    runtime_service_list_exposed_ports,
    runtime_service_start_execution,
    runtime_service_unexpose_port,
)
from .client import AuthenticatedClient, Client
from .models.command_spec import CommandSpec
from .models.create_sandbox_request import CreateSandboxRequest
from .models.create_snapshot_request import CreateSnapshotRequest
from .models.error_body import ErrorBody
from .models.execute_result import ExecuteResult
from .models.execute_sandbox_request import ExecuteSandboxRequest
from .models.expose_port_request import ExposePortRequest
from .models.expose_port_request_auth_mode import ExposePortRequestAuthMode
from .models.expose_port_response import ExposePortResponse
from .models.file_from_artifact_request import FileFromArtifactRequest
from .models.file_from_artifact_result import FileFromArtifactResult
from .models.file_to_artifact_request import FileToArtifactRequest
from .models.file_to_artifact_result import FileToArtifactResult
from .models.fork_sandbox_request import ForkSandboxRequest
from .models.list_exposed_ports_response import ListExposedPortsResponse
from .models.operation import Operation
from .models.sandbox import Sandbox as SandboxModel
from .models.snapshot_result import SnapshotResult
from .models.start_execution_request import StartExecutionRequest
from .models.unexpose_port_request import UnexposePortRequest
from .models.unexpose_port_response import UnexposePortResponse
from .sse import ExecOutputEvent, StreamError, stream_execution, stream_execution_async
from .types import UNSET, Unset

SdkClient = AuthenticatedClient | Client
T = TypeVar("T")
TERMINAL_OPERATION_STATES = frozenset({"succeeded", "failed", "cancelled"})


class OperationFailed(RuntimeError):
    """A submitted sandbox operation reached a failed or cancelled terminal state."""

    def __init__(self, operation: Operation) -> None:
        self.operation = operation
        error = None if isinstance(operation.error, Unset) else operation.error
        self.code = None if error is None or isinstance(error.code, Unset) else error.code
        message = None if error is None or isinstance(error.message, Unset) else error.message
        super().__init__(f"operation {operation.id} ended {operation.state}: {message or self.code or 'unknown error'}")


def _required(value: T | Unset | None, field: str) -> T:
    if value is None or isinstance(value, Unset):
        raise ValueError(f"API response is missing required {field}")
    return cast("T", value)


def _wait_operation(
    client: SdkClient, operation_id: str, *, timeout: float, poll_interval: float
) -> Operation | ErrorBody | None:
    deadline = time.monotonic() + timeout
    while True:
        response = runtime_service_get_operation.sync(id=operation_id, client=client)
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "operation")
        if operation.state in TERMINAL_OPERATION_STATES:
            if operation.state != "succeeded":
                raise OperationFailed(operation)
            return operation
        if time.monotonic() >= deadline:
            raise TimeoutError(f"operation {operation_id} did not finish within {timeout}s")
        time.sleep(poll_interval)


async def _wait_operation_async(
    client: SdkClient, operation_id: str, *, timeout: float, poll_interval: float
) -> Operation | ErrorBody | None:
    deadline = time.monotonic() + timeout
    while True:
        response = await runtime_service_get_operation.asyncio(id=operation_id, client=client)
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "operation")
        if operation.state in TERMINAL_OPERATION_STATES:
            if operation.state != "succeeded":
                raise OperationFailed(operation)
            return operation
        if time.monotonic() >= deadline:
            raise TimeoutError(f"operation {operation_id} did not finish within {timeout}s")
        await asyncio.sleep(poll_interval)


def _result(operation: Operation, field: str) -> object:
    result = _required(operation.result, "operation.result")
    return _required(getattr(result, field), f"operation.result.{field}")


def _idempotency_key(value: str | None) -> str:
    return value or str(uuid.uuid4())


@define(frozen=True)
class Sandbox:
    """A connected sandbox with lifecycle, execution, file, snapshot, and port helpers."""

    client: SdkClient
    model: SandboxModel

    @property
    def id(self) -> str:
        """The sandbox's canonical id."""
        return _required(self.model.id, "sandbox.id")

    @classmethod
    def create(
        cls,
        *,
        client: SdkClient,
        body: CreateSandboxRequest,
        timeout: float = 300,
        poll_interval: float = 0.25,
        idempotency_key: str | None = None,
    ) -> Sandbox | ErrorBody | None:
        """Create a sandbox, wait for its operation, and return the ready sandbox."""
        response = runtime_service_create_sandbox.sync(
            client=client, body=body, idempotency_key=_idempotency_key(idempotency_key)
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "create operation")
        settled = _wait_operation(
            client,
            _required(operation.id, "operation.id"),
            timeout=timeout,
            poll_interval=poll_interval,
        )
        if settled is None or isinstance(settled, ErrorBody):
            return settled
        sandbox = _required(response.sandbox, "sandbox")
        return cls.connect(_required(sandbox.id, "sandbox.id"), client=client)

    @classmethod
    async def create_async(
        cls,
        *,
        client: SdkClient,
        body: CreateSandboxRequest,
        timeout: float = 300,
        poll_interval: float = 0.25,
        idempotency_key: str | None = None,
    ) -> Sandbox | ErrorBody | None:
        """Create and await a sandbox with the generated async client."""
        response = await runtime_service_create_sandbox.asyncio(
            client=client, body=body, idempotency_key=_idempotency_key(idempotency_key)
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "create operation")
        settled = await _wait_operation_async(
            client,
            _required(operation.id, "operation.id"),
            timeout=timeout,
            poll_interval=poll_interval,
        )
        if settled is None or isinstance(settled, ErrorBody):
            return settled
        sandbox = _required(response.sandbox, "sandbox")
        return await cls.connect_async(_required(sandbox.id, "sandbox.id"), client=client)

    @classmethod
    def connect(cls, sandbox_id: str, *, client: SdkClient) -> Sandbox | ErrorBody | None:
        """Connect to an existing sandbox by id."""
        response = runtime_service_get_sandbox.sync(id=sandbox_id, client=client)
        if response is None or isinstance(response, ErrorBody):
            return response
        return cls(client=client, model=_required(response.sandbox, "sandbox"))

    @classmethod
    async def connect_async(cls, sandbox_id: str, *, client: SdkClient) -> Sandbox | ErrorBody | None:
        """Connect to an existing sandbox by id with the async client."""
        response = await runtime_service_get_sandbox.asyncio(id=sandbox_id, client=client)
        if response is None or isinstance(response, ErrorBody):
            return response
        return cls(client=client, model=_required(response.sandbox, "sandbox"))

    def exec(
        self,
        command: CommandSpec,
        *,
        stdin: str | Unset = UNSET,
        timeout: float = 300,
        poll_interval: float = 0.25,
        idempotency_key: str | None = None,
    ) -> ExecuteResult | ErrorBody | None:
        """Run a buffered command and wait for its typed execution result."""
        response = runtime_service_execute_sandbox.sync(
            sandbox_id=self.id,
            client=self.client,
            body=ExecuteSandboxRequest(sandbox_id=self.id, command=command, stdin=stdin),
            idempotency_key=_idempotency_key(idempotency_key),
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "execute operation")
        settled = _wait_operation(
            self.client,
            _required(operation.id, "operation.id"),
            timeout=timeout,
            poll_interval=poll_interval,
        )
        if settled is None or isinstance(settled, ErrorBody):
            return settled
        return cast("ExecuteResult", _result(settled, "execute"))

    async def exec_async(
        self,
        command: CommandSpec,
        *,
        stdin: str | Unset = UNSET,
        timeout: float = 300,
        poll_interval: float = 0.25,
        idempotency_key: str | None = None,
    ) -> ExecuteResult | ErrorBody | None:
        """Run a buffered command with the async client."""
        response = await runtime_service_execute_sandbox.asyncio(
            sandbox_id=self.id,
            client=self.client,
            body=ExecuteSandboxRequest(sandbox_id=self.id, command=command, stdin=stdin),
            idempotency_key=_idempotency_key(idempotency_key),
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "execute operation")
        settled = await _wait_operation_async(
            self.client,
            _required(operation.id, "operation.id"),
            timeout=timeout,
            poll_interval=poll_interval,
        )
        if settled is None or isinstance(settled, ErrorBody):
            return settled
        return cast("ExecuteResult", _result(settled, "execute"))

    def exec_stream(
        self,
        command: CommandSpec,
        *,
        stdin: str | Unset = UNSET,
        pty: bool | Unset = UNSET,
        idempotency_key: str | None = None,
    ) -> Iterator[ExecOutputEvent | StreamError] | ErrorBody | None:
        """Start an execution and stream typed stdout, stderr, exit, and status events."""
        response = runtime_service_start_execution.sync(
            sandbox_id=self.id,
            client=self.client,
            body=StartExecutionRequest(sandbox_id=self.id, command=command, stdin=stdin, pty=pty),
            idempotency_key=_idempotency_key(idempotency_key),
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        execution = _required(response.execution, "execution")
        return stream_execution(client=self.client, execution_id=_required(execution.id, "execution.id"))

    async def exec_stream_async(
        self,
        command: CommandSpec,
        *,
        stdin: str | Unset = UNSET,
        pty: bool | Unset = UNSET,
        idempotency_key: str | None = None,
    ) -> AsyncIterator[ExecOutputEvent | StreamError] | ErrorBody | None:
        """Start and stream an execution with the async client."""
        response = await runtime_service_start_execution.asyncio(
            sandbox_id=self.id,
            client=self.client,
            body=StartExecutionRequest(sandbox_id=self.id, command=command, stdin=stdin, pty=pty),
            idempotency_key=_idempotency_key(idempotency_key),
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        execution = _required(response.execution, "execution")
        return await stream_execution_async(client=self.client, execution_id=_required(execution.id, "execution.id"))

    def fork(
        self,
        body: ForkSandboxRequest,
        *,
        timeout: float = 300,
        poll_interval: float = 0.25,
        idempotency_key: str | None = None,
    ) -> Sandbox | ErrorBody | None:
        """Fork this sandbox, wait for the child, and return it connected."""
        response = runtime_service_fork_sandbox.sync(
            source_sandbox_id=self.id,
            client=self.client,
            body=evolve(body, source_sandbox_id=self.id),
            idempotency_key=_idempotency_key(idempotency_key),
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "fork operation")
        settled = _wait_operation(
            self.client,
            _required(operation.id, "operation.id"),
            timeout=timeout,
            poll_interval=poll_interval,
        )
        if settled is None or isinstance(settled, ErrorBody):
            return settled
        sandbox = _required(response.sandbox, "sandbox")
        return self.connect(_required(sandbox.id, "sandbox.id"), client=self.client)

    async def fork_async(
        self,
        body: ForkSandboxRequest,
        *,
        timeout: float = 300,
        poll_interval: float = 0.25,
        idempotency_key: str | None = None,
    ) -> Sandbox | ErrorBody | None:
        """Fork this sandbox with the async client."""
        response = await runtime_service_fork_sandbox.asyncio(
            source_sandbox_id=self.id,
            client=self.client,
            body=evolve(body, source_sandbox_id=self.id),
            idempotency_key=_idempotency_key(idempotency_key),
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "fork operation")
        settled = await _wait_operation_async(
            self.client,
            _required(operation.id, "operation.id"),
            timeout=timeout,
            poll_interval=poll_interval,
        )
        if settled is None or isinstance(settled, ErrorBody):
            return settled
        sandbox = _required(response.sandbox, "sandbox")
        return await self.connect_async(_required(sandbox.id, "sandbox.id"), client=self.client)

    def snapshot(
        self,
        body: CreateSnapshotRequest | None = None,
        *,
        timeout: float = 300,
        poll_interval: float = 0.25,
        idempotency_key: str | None = None,
    ) -> SnapshotResult | ErrorBody | None:
        """Capture a snapshot and wait for its typed result."""
        request = evolve(body or CreateSnapshotRequest(), sandbox_id=self.id)
        response = runtime_service_create_snapshot.sync(
            sandbox_id=self.id,
            client=self.client,
            body=request,
            idempotency_key=_idempotency_key(idempotency_key),
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "snapshot operation")
        settled = _wait_operation(
            self.client,
            _required(operation.id, "operation.id"),
            timeout=timeout,
            poll_interval=poll_interval,
        )
        if settled is None or isinstance(settled, ErrorBody):
            return settled
        return cast("SnapshotResult", _result(settled, "snapshot"))

    async def snapshot_async(
        self,
        body: CreateSnapshotRequest | None = None,
        *,
        timeout: float = 300,
        poll_interval: float = 0.25,
        idempotency_key: str | None = None,
    ) -> SnapshotResult | ErrorBody | None:
        """Capture a snapshot with the async client."""
        request = evolve(body or CreateSnapshotRequest(), sandbox_id=self.id)
        response = await runtime_service_create_snapshot.asyncio(
            sandbox_id=self.id,
            client=self.client,
            body=request,
            idempotency_key=_idempotency_key(idempotency_key),
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "snapshot operation")
        settled = await _wait_operation_async(
            self.client,
            _required(operation.id, "operation.id"),
            timeout=timeout,
            poll_interval=poll_interval,
        )
        if settled is None or isinstance(settled, ErrorBody):
            return settled
        return cast("SnapshotResult", _result(settled, "snapshot"))

    def file_to_artifact(
        self,
        path: str,
        *,
        media_type: str | Unset = UNSET,
        timeout: float = 300,
        poll_interval: float = 0.25,
        idempotency_key: str | None = None,
    ) -> FileToArtifactResult | ErrorBody | None:
        """Archive a sandbox file and return its artifact result."""
        response = runtime_service_file_to_artifact.sync(
            sandbox_id=self.id,
            client=self.client,
            body=FileToArtifactRequest(sandbox_id=self.id, path=path, media_type=media_type),
            idempotency_key=_idempotency_key(idempotency_key),
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "file export operation")
        settled = _wait_operation(
            self.client,
            _required(operation.id, "operation.id"),
            timeout=timeout,
            poll_interval=poll_interval,
        )
        if settled is None or isinstance(settled, ErrorBody):
            return settled
        return cast("FileToArtifactResult", _result(settled, "file_to_artifact"))

    async def file_to_artifact_async(
        self,
        path: str,
        *,
        media_type: str | Unset = UNSET,
        timeout: float = 300,
        poll_interval: float = 0.25,
        idempotency_key: str | None = None,
    ) -> FileToArtifactResult | ErrorBody | None:
        """Archive a sandbox file with the async client."""
        response = await runtime_service_file_to_artifact.asyncio(
            sandbox_id=self.id,
            client=self.client,
            body=FileToArtifactRequest(sandbox_id=self.id, path=path, media_type=media_type),
            idempotency_key=_idempotency_key(idempotency_key),
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "file export operation")
        settled = await _wait_operation_async(
            self.client,
            _required(operation.id, "operation.id"),
            timeout=timeout,
            poll_interval=poll_interval,
        )
        if settled is None or isinstance(settled, ErrorBody):
            return settled
        return cast("FileToArtifactResult", _result(settled, "file_to_artifact"))

    def file_from_artifact(
        self,
        artifact_id: str,
        path: str,
        *,
        timeout: float = 300,
        poll_interval: float = 0.25,
        idempotency_key: str | None = None,
    ) -> FileFromArtifactResult | ErrorBody | None:
        """Materialize an artifact into this sandbox and return the move result."""
        response = runtime_service_file_from_artifact.sync(
            sandbox_id=self.id,
            client=self.client,
            body=FileFromArtifactRequest(sandbox_id=self.id, artifact_id=artifact_id, path=path),
            idempotency_key=_idempotency_key(idempotency_key),
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "file import operation")
        settled = _wait_operation(
            self.client,
            _required(operation.id, "operation.id"),
            timeout=timeout,
            poll_interval=poll_interval,
        )
        if settled is None or isinstance(settled, ErrorBody):
            return settled
        return cast("FileFromArtifactResult", _result(settled, "file_from_artifact"))

    async def file_from_artifact_async(
        self,
        artifact_id: str,
        path: str,
        *,
        timeout: float = 300,
        poll_interval: float = 0.25,
        idempotency_key: str | None = None,
    ) -> FileFromArtifactResult | ErrorBody | None:
        """Materialize an artifact with the async client."""
        response = await runtime_service_file_from_artifact.asyncio(
            sandbox_id=self.id,
            client=self.client,
            body=FileFromArtifactRequest(sandbox_id=self.id, artifact_id=artifact_id, path=path),
            idempotency_key=_idempotency_key(idempotency_key),
        )
        if response is None or isinstance(response, ErrorBody):
            return response
        operation = _required(response.operation, "file import operation")
        settled = await _wait_operation_async(
            self.client,
            _required(operation.id, "operation.id"),
            timeout=timeout,
            poll_interval=poll_interval,
        )
        if settled is None or isinstance(settled, ErrorBody):
            return settled
        return cast("FileFromArtifactResult", _result(settled, "file_from_artifact"))

    def expose_port(
        self,
        port: int,
        *,
        auth_mode: ExposePortRequestAuthMode | Unset = UNSET,
    ) -> ExposePortResponse | ErrorBody | None:
        """Expose a guest port through the preview edge."""
        return runtime_service_expose_port.sync(
            sandbox_id=self.id,
            client=self.client,
            body=ExposePortRequest(sandbox_id=self.id, port=port, auth_mode=auth_mode),
        )

    async def expose_port_async(
        self,
        port: int,
        *,
        auth_mode: ExposePortRequestAuthMode | Unset = UNSET,
    ) -> ExposePortResponse | ErrorBody | None:
        """Expose a guest port with the async client."""
        return await runtime_service_expose_port.asyncio(
            sandbox_id=self.id,
            client=self.client,
            body=ExposePortRequest(sandbox_id=self.id, port=port, auth_mode=auth_mode),
        )

    def unexpose_port(self, port: int) -> UnexposePortResponse | ErrorBody | None:
        """Revoke one exposed guest port."""
        return runtime_service_unexpose_port.sync(
            sandbox_id=self.id,
            client=self.client,
            body=UnexposePortRequest(sandbox_id=self.id, port=port),
        )

    async def unexpose_port_async(self, port: int) -> UnexposePortResponse | ErrorBody | None:
        """Revoke one exposed guest port with the async client."""
        return await runtime_service_unexpose_port.asyncio(
            sandbox_id=self.id,
            client=self.client,
            body=UnexposePortRequest(sandbox_id=self.id, port=port),
        )

    def list_exposed_ports(self) -> ListExposedPortsResponse | ErrorBody | None:
        """List this sandbox's active port exposures."""
        return runtime_service_list_exposed_ports.sync(sandbox_id=self.id, client=self.client)

    async def list_exposed_ports_async(self) -> ListExposedPortsResponse | ErrorBody | None:
        """List active port exposures with the async client."""
        return await runtime_service_list_exposed_ports.asyncio(sandbox_id=self.id, client=self.client)
