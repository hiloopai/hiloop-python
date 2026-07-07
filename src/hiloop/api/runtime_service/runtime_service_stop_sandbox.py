from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stop_sandbox_request import StopSandboxRequest
from ...models.stop_sandbox_response import StopSandboxResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: StopSandboxRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sandboxes/{id}:stop".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StopSandboxResponse | None:
    if response.status_code == 200:
        response_200 = StopSandboxResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StopSandboxResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StopSandboxRequest,
) -> Response[StopSandboxResponse]:
    """Gracefully stop a running sandbox. The sandbox comes to rest in a stopped state and its record
     is retained so it stays inspectable — distinct from DeleteSandbox, which tears the sandbox down
     entirely. Where the provider supports state-preserving suspension, the workload's filesystem
     and process state are preserved and ResumeSandbox brings it back; otherwise the workload is
     terminated and the stop is final. Work that completed before the stop is reported as succeeded
     rather than interrupted.

    Args:
        id (str):
        body (StopSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StopSandboxResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StopSandboxRequest,
) -> StopSandboxResponse | None:
    """Gracefully stop a running sandbox. The sandbox comes to rest in a stopped state and its record
     is retained so it stays inspectable — distinct from DeleteSandbox, which tears the sandbox down
     entirely. Where the provider supports state-preserving suspension, the workload's filesystem
     and process state are preserved and ResumeSandbox brings it back; otherwise the workload is
     terminated and the stop is final. Work that completed before the stop is reported as succeeded
     rather than interrupted.

    Args:
        id (str):
        body (StopSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StopSandboxResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StopSandboxRequest,
) -> Response[StopSandboxResponse]:
    """Gracefully stop a running sandbox. The sandbox comes to rest in a stopped state and its record
     is retained so it stays inspectable — distinct from DeleteSandbox, which tears the sandbox down
     entirely. Where the provider supports state-preserving suspension, the workload's filesystem
     and process state are preserved and ResumeSandbox brings it back; otherwise the workload is
     terminated and the stop is final. Work that completed before the stop is reported as succeeded
     rather than interrupted.

    Args:
        id (str):
        body (StopSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StopSandboxResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StopSandboxRequest,
) -> StopSandboxResponse | None:
    """Gracefully stop a running sandbox. The sandbox comes to rest in a stopped state and its record
     is retained so it stays inspectable — distinct from DeleteSandbox, which tears the sandbox down
     entirely. Where the provider supports state-preserving suspension, the workload's filesystem
     and process state are preserved and ResumeSandbox brings it back; otherwise the workload is
     terminated and the stop is final. Work that completed before the stop is reported as succeeded
     rather than interrupted.

    Args:
        id (str):
        body (StopSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StopSandboxResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
