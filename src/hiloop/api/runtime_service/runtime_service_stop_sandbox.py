from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
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


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | StopSandboxResponse | None:
    if response.status_code == 200:
        response_200 = StopSandboxResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        # The edge can reject a request before a body exists (for example a denied
        # credential, or its pre-credential rate-limit floor), so tolerate a missing or
        # undecodable error envelope instead of raising: parsed stays None and the raw
        # bytes remain on Response.content.
        try:
            response_429 = ErrorBody.from_dict(response.json())
        except ValueError:
            response_429 = None

        return response_429

    # The edge can reject a request before a body exists (for example a denied
    # credential, or its pre-credential rate-limit floor), so tolerate a missing or
    # undecodable error envelope instead of raising: parsed stays None and the raw
    # bytes remain on Response.content.
    try:
        response_default = ErrorBody.from_dict(response.json())
    except ValueError:
        response_default = None

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorBody | StopSandboxResponse]:
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
) -> Response[ErrorBody | StopSandboxResponse]:
    """Gracefully stop a running sandbox. The sandbox comes to rest in a stopped state and its record
     is retained so it stays inspectable — distinct from DeleteSandbox. A versioned BranchFS
     workspace is destroyed only after its exact terminal bytes are sealed; ResumeSandbox boots a
     new generation from that immutable change. Process and memory state do not survive that path.
     Ephemeral scratch storage has no continuation and requires fresh_workspace on resume.

    Args:
        id (str):
        body (StopSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | StopSandboxResponse]
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
) -> ErrorBody | StopSandboxResponse | None:
    """Gracefully stop a running sandbox. The sandbox comes to rest in a stopped state and its record
     is retained so it stays inspectable — distinct from DeleteSandbox. A versioned BranchFS
     workspace is destroyed only after its exact terminal bytes are sealed; ResumeSandbox boots a
     new generation from that immutable change. Process and memory state do not survive that path.
     Ephemeral scratch storage has no continuation and requires fresh_workspace on resume.

    Args:
        id (str):
        body (StopSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | StopSandboxResponse
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
) -> Response[ErrorBody | StopSandboxResponse]:
    """Gracefully stop a running sandbox. The sandbox comes to rest in a stopped state and its record
     is retained so it stays inspectable — distinct from DeleteSandbox. A versioned BranchFS
     workspace is destroyed only after its exact terminal bytes are sealed; ResumeSandbox boots a
     new generation from that immutable change. Process and memory state do not survive that path.
     Ephemeral scratch storage has no continuation and requires fresh_workspace on resume.

    Args:
        id (str):
        body (StopSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | StopSandboxResponse]
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
) -> ErrorBody | StopSandboxResponse | None:
    """Gracefully stop a running sandbox. The sandbox comes to rest in a stopped state and its record
     is retained so it stays inspectable — distinct from DeleteSandbox. A versioned BranchFS
     workspace is destroyed only after its exact terminal bytes are sealed; ResumeSandbox boots a
     new generation from that immutable change. Process and memory state do not survive that path.
     Ephemeral scratch storage has no continuation and requires fresh_workspace on resume.

    Args:
        id (str):
        body (StopSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | StopSandboxResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
