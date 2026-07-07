from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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
) -> RestoreSnapshotResponse | None:
    if response.status_code == 200:
        response_200 = RestoreSnapshotResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestoreSnapshotResponse]:
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
) -> Response[RestoreSnapshotResponse]:
    """Create a new sandbox from a snapshot — fork-from-snapshot. The source sandbox may be stopped
     or deleted; only the snapshot must be ready. A snapshot that records its source run mints the
     new sandbox's run as a child branched at the snapshot's recorded anchor, so the restored
     sandbox extends the source's run lineage.

    Args:
        snapshot_id (str):
        idempotency_key (str | Unset):
        body (RestoreSnapshotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestoreSnapshotResponse]
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
) -> RestoreSnapshotResponse | None:
    """Create a new sandbox from a snapshot — fork-from-snapshot. The source sandbox may be stopped
     or deleted; only the snapshot must be ready. A snapshot that records its source run mints the
     new sandbox's run as a child branched at the snapshot's recorded anchor, so the restored
     sandbox extends the source's run lineage.

    Args:
        snapshot_id (str):
        idempotency_key (str | Unset):
        body (RestoreSnapshotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestoreSnapshotResponse
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
) -> Response[RestoreSnapshotResponse]:
    """Create a new sandbox from a snapshot — fork-from-snapshot. The source sandbox may be stopped
     or deleted; only the snapshot must be ready. A snapshot that records its source run mints the
     new sandbox's run as a child branched at the snapshot's recorded anchor, so the restored
     sandbox extends the source's run lineage.

    Args:
        snapshot_id (str):
        idempotency_key (str | Unset):
        body (RestoreSnapshotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestoreSnapshotResponse]
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
) -> RestoreSnapshotResponse | None:
    """Create a new sandbox from a snapshot — fork-from-snapshot. The source sandbox may be stopped
     or deleted; only the snapshot must be ready. A snapshot that records its source run mints the
     new sandbox's run as a child branched at the snapshot's recorded anchor, so the restored
     sandbox extends the source's run lineage.

    Args:
        snapshot_id (str):
        idempotency_key (str | Unset):
        body (RestoreSnapshotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestoreSnapshotResponse
    """

    return (
        await asyncio_detailed(
            snapshot_id=snapshot_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
