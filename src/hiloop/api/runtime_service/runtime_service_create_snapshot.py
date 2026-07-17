from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_snapshot_request import CreateSnapshotRequest
from ...models.create_snapshot_response import CreateSnapshotResponse
from ...models.error_body import ErrorBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sandbox_id: str,
    *,
    body: CreateSnapshotRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sandboxes/{sandbox_id}/snapshots".format(
            sandbox_id=quote(str(sandbox_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateSnapshotResponse | ErrorBody | None:
    if response.status_code == 200:
        response_200 = CreateSnapshotResponse.from_dict(response.json())

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
) -> Response[CreateSnapshotResponse | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateSnapshotRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateSnapshotResponse | ErrorBody]:
    """Retired snapshot compatibility RPC. Clean sandbox-cell deployments return unsupported; use a
     BranchFS workspace plus stop/resume for filesystem continuity.

    Args:
        sandbox_id (str):
        idempotency_key (str | Unset):
        body (CreateSnapshotRequest): Retired snapshot compatibility request. Clean sandbox-cell
            deployments return unsupported; use
             a BranchFS workspace plus stop/resume for filesystem continuity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSnapshotResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        sandbox_id=sandbox_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateSnapshotRequest,
    idempotency_key: str | Unset = UNSET,
) -> CreateSnapshotResponse | ErrorBody | None:
    """Retired snapshot compatibility RPC. Clean sandbox-cell deployments return unsupported; use a
     BranchFS workspace plus stop/resume for filesystem continuity.

    Args:
        sandbox_id (str):
        idempotency_key (str | Unset):
        body (CreateSnapshotRequest): Retired snapshot compatibility request. Clean sandbox-cell
            deployments return unsupported; use
             a BranchFS workspace plus stop/resume for filesystem continuity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSnapshotResponse | ErrorBody
    """

    return sync_detailed(
        sandbox_id=sandbox_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateSnapshotRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateSnapshotResponse | ErrorBody]:
    """Retired snapshot compatibility RPC. Clean sandbox-cell deployments return unsupported; use a
     BranchFS workspace plus stop/resume for filesystem continuity.

    Args:
        sandbox_id (str):
        idempotency_key (str | Unset):
        body (CreateSnapshotRequest): Retired snapshot compatibility request. Clean sandbox-cell
            deployments return unsupported; use
             a BranchFS workspace plus stop/resume for filesystem continuity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSnapshotResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        sandbox_id=sandbox_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateSnapshotRequest,
    idempotency_key: str | Unset = UNSET,
) -> CreateSnapshotResponse | ErrorBody | None:
    """Retired snapshot compatibility RPC. Clean sandbox-cell deployments return unsupported; use a
     BranchFS workspace plus stop/resume for filesystem continuity.

    Args:
        sandbox_id (str):
        idempotency_key (str | Unset):
        body (CreateSnapshotRequest): Retired snapshot compatibility request. Clean sandbox-cell
            deployments return unsupported; use
             a BranchFS workspace plus stop/resume for filesystem continuity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSnapshotResponse | ErrorBody
    """

    return (
        await asyncio_detailed(
            sandbox_id=sandbox_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
