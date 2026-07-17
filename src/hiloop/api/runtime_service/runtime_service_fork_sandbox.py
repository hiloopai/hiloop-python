from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.fork_sandbox_request import ForkSandboxRequest
from ...models.fork_sandbox_response import ForkSandboxResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_sandbox_id: str,
    *,
    body: ForkSandboxRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sandboxes/{source_sandbox_id}:fork".format(
            source_sandbox_id=quote(str(source_sandbox_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | ForkSandboxResponse | None:
    if response.status_code == 200:
        response_200 = ForkSandboxResponse.from_dict(response.json())

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
) -> Response[ErrorBody | ForkSandboxResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ForkSandboxRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorBody | ForkSandboxResponse]:
    """Retired fork compatibility RPC. Clean sandbox-cell deployments return unsupported.

    Args:
        source_sandbox_id (str):
        idempotency_key (str | Unset):
        body (ForkSandboxRequest): Retired fork compatibility request. Clean sandbox-cell
            deployments return unsupported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ForkSandboxResponse]
    """

    kwargs = _get_kwargs(
        source_sandbox_id=source_sandbox_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ForkSandboxRequest,
    idempotency_key: str | Unset = UNSET,
) -> ErrorBody | ForkSandboxResponse | None:
    """Retired fork compatibility RPC. Clean sandbox-cell deployments return unsupported.

    Args:
        source_sandbox_id (str):
        idempotency_key (str | Unset):
        body (ForkSandboxRequest): Retired fork compatibility request. Clean sandbox-cell
            deployments return unsupported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ForkSandboxResponse
    """

    return sync_detailed(
        source_sandbox_id=source_sandbox_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    source_sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ForkSandboxRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorBody | ForkSandboxResponse]:
    """Retired fork compatibility RPC. Clean sandbox-cell deployments return unsupported.

    Args:
        source_sandbox_id (str):
        idempotency_key (str | Unset):
        body (ForkSandboxRequest): Retired fork compatibility request. Clean sandbox-cell
            deployments return unsupported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ForkSandboxResponse]
    """

    kwargs = _get_kwargs(
        source_sandbox_id=source_sandbox_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ForkSandboxRequest,
    idempotency_key: str | Unset = UNSET,
) -> ErrorBody | ForkSandboxResponse | None:
    """Retired fork compatibility RPC. Clean sandbox-cell deployments return unsupported.

    Args:
        source_sandbox_id (str):
        idempotency_key (str | Unset):
        body (ForkSandboxRequest): Retired fork compatibility request. Clean sandbox-cell
            deployments return unsupported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ForkSandboxResponse
    """

    return (
        await asyncio_detailed(
            source_sandbox_id=source_sandbox_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
