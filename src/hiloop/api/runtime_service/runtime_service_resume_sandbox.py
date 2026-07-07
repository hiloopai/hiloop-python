from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ResumeSandboxResponse | None:
    if response.status_code == 200:
        response_200 = ResumeSandboxResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResumeSandboxResponse]:
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
) -> Response[ResumeSandboxResponse]:
    """Resume a stopped sandbox whose state was preserved at stop time, returning it to running with
     its filesystem and process state intact. Resuming a sandbox that is already running succeeds
     without effect; a sandbox whose workload was torn down (stopped without state preservation, or
     deleted) cannot be resumed and reports a conflict.

    Args:
        id (str):
        body (ResumeSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResumeSandboxResponse]
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
) -> ResumeSandboxResponse | None:
    """Resume a stopped sandbox whose state was preserved at stop time, returning it to running with
     its filesystem and process state intact. Resuming a sandbox that is already running succeeds
     without effect; a sandbox whose workload was torn down (stopped without state preservation, or
     deleted) cannot be resumed and reports a conflict.

    Args:
        id (str):
        body (ResumeSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResumeSandboxResponse
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
) -> Response[ResumeSandboxResponse]:
    """Resume a stopped sandbox whose state was preserved at stop time, returning it to running with
     its filesystem and process state intact. Resuming a sandbox that is already running succeeds
     without effect; a sandbox whose workload was torn down (stopped without state preservation, or
     deleted) cannot be resumed and reports a conflict.

    Args:
        id (str):
        body (ResumeSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResumeSandboxResponse]
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
) -> ResumeSandboxResponse | None:
    """Resume a stopped sandbox whose state was preserved at stop time, returning it to running with
     its filesystem and process state intact. Resuming a sandbox that is already running succeeds
     without effect; a sandbox whose workload was torn down (stopped without state preservation, or
     deleted) cannot be resumed and reports a conflict.

    Args:
        id (str):
        body (ResumeSandboxRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResumeSandboxResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
