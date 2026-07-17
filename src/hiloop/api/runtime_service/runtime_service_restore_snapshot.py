from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.restore_snapshot_request import RestoreSnapshotRequest
from ...models.restore_snapshot_response import RestoreSnapshotResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    snapshot_id: str,
    *,
    body: RestoreSnapshotRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/snapshots/{snapshot_id}:restore".format(
            snapshot_id=quote(str(snapshot_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | RestoreSnapshotResponse | None:
    if response.status_code == 200:
        response_200 = RestoreSnapshotResponse.from_dict(response.json())

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
) -> Response[ErrorBody | RestoreSnapshotResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestoreSnapshotRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorBody | RestoreSnapshotResponse]:
    """Retired snapshot-restore compatibility RPC. Clean sandbox-cell deployments return unsupported;
     resume an exact sealed BranchFS workspace into a fresh runtime generation instead.

    Args:
        snapshot_id (str):
        idempotency_key (str | Unset):
        body (RestoreSnapshotRequest): Retired snapshot-restore compatibility request. Clean
            sandbox-cell deployments return
             unsupported; resume an exact sealed BranchFS workspace into a fresh runtime generation
            instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | RestoreSnapshotResponse]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestoreSnapshotRequest,
    idempotency_key: str | Unset = UNSET,
) -> ErrorBody | RestoreSnapshotResponse | None:
    """Retired snapshot-restore compatibility RPC. Clean sandbox-cell deployments return unsupported;
     resume an exact sealed BranchFS workspace into a fresh runtime generation instead.

    Args:
        snapshot_id (str):
        idempotency_key (str | Unset):
        body (RestoreSnapshotRequest): Retired snapshot-restore compatibility request. Clean
            sandbox-cell deployments return
             unsupported; resume an exact sealed BranchFS workspace into a fresh runtime generation
            instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | RestoreSnapshotResponse
    """

    return sync_detailed(
        snapshot_id=snapshot_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestoreSnapshotRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorBody | RestoreSnapshotResponse]:
    """Retired snapshot-restore compatibility RPC. Clean sandbox-cell deployments return unsupported;
     resume an exact sealed BranchFS workspace into a fresh runtime generation instead.

    Args:
        snapshot_id (str):
        idempotency_key (str | Unset):
        body (RestoreSnapshotRequest): Retired snapshot-restore compatibility request. Clean
            sandbox-cell deployments return
             unsupported; resume an exact sealed BranchFS workspace into a fresh runtime generation
            instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | RestoreSnapshotResponse]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestoreSnapshotRequest,
    idempotency_key: str | Unset = UNSET,
) -> ErrorBody | RestoreSnapshotResponse | None:
    """Retired snapshot-restore compatibility RPC. Clean sandbox-cell deployments return unsupported;
     resume an exact sealed BranchFS workspace into a fresh runtime generation instead.

    Args:
        snapshot_id (str):
        idempotency_key (str | Unset):
        body (RestoreSnapshotRequest): Retired snapshot-restore compatibility request. Clean
            sandbox-cell deployments return
             unsupported; resume an exact sealed BranchFS workspace into a fresh runtime generation
            instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | RestoreSnapshotResponse
    """

    return (
        await asyncio_detailed(
            snapshot_id=snapshot_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
