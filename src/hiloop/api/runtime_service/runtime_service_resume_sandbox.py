from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.resume_sandbox_request import ResumeSandboxRequest
from ...models.resume_sandbox_response import ResumeSandboxResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: ResumeSandboxRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sandboxes/{id}:resume".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | ResumeSandboxResponse | None:
    if response.status_code == 200:
        response_200 = ResumeSandboxResponse.from_dict(response.json())

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
) -> Response[ErrorBody | ResumeSandboxResponse]:
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
    body: ResumeSandboxRequest,
) -> Response[ErrorBody | ResumeSandboxResponse]:
    """Resume a stopped sandbox. A sealed BranchFS continuation boots a fresh runtime generation from
     the exact immutable change; it preserves filesystem bytes, not process or memory state. Without
     a sealed continuation, resume provisions fresh scratch storage only when fresh_workspace is
     explicitly set.

    Args:
        id (str):
        body (ResumeSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ResumeSandboxResponse]
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
    body: ResumeSandboxRequest,
) -> ErrorBody | ResumeSandboxResponse | None:
    """Resume a stopped sandbox. A sealed BranchFS continuation boots a fresh runtime generation from
     the exact immutable change; it preserves filesystem bytes, not process or memory state. Without
     a sealed continuation, resume provisions fresh scratch storage only when fresh_workspace is
     explicitly set.

    Args:
        id (str):
        body (ResumeSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ResumeSandboxResponse
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
    body: ResumeSandboxRequest,
) -> Response[ErrorBody | ResumeSandboxResponse]:
    """Resume a stopped sandbox. A sealed BranchFS continuation boots a fresh runtime generation from
     the exact immutable change; it preserves filesystem bytes, not process or memory state. Without
     a sealed continuation, resume provisions fresh scratch storage only when fresh_workspace is
     explicitly set.

    Args:
        id (str):
        body (ResumeSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ResumeSandboxResponse]
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
    body: ResumeSandboxRequest,
) -> ErrorBody | ResumeSandboxResponse | None:
    """Resume a stopped sandbox. A sealed BranchFS continuation boots a fresh runtime generation from
     the exact immutable change; it preserves filesystem bytes, not process or memory state. Without
     a sealed continuation, resume provisions fresh scratch storage only when fresh_workspace is
     explicitly set.

    Args:
        id (str):
        body (ResumeSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ResumeSandboxResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
