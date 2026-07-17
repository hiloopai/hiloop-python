from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.attach_volume_request import AttachVolumeRequest
from ...models.attach_volume_response import AttachVolumeResponse
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    volume_id: str,
    *,
    body: AttachVolumeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/volumes/{volume_id}:attach".format(
            volume_id=quote(str(volume_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AttachVolumeResponse | ErrorBody | None:
    if response.status_code == 200:
        response_200 = AttachVolumeResponse.from_dict(response.json())

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
) -> Response[AttachVolumeResponse | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    volume_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttachVolumeRequest,
) -> Response[AttachVolumeResponse | ErrorBody]:
    """Attach a volume to a running sandbox read-only, pinning the volume's current version at
     admission — so a long-lived sandbox can pick up a new dataset or checkpoint version without
     being recreated. The mount is read-only in v1. The volume and sandbox must share a project. A
     volume with no published version, or a sandbox that already has something mounted at the path,
     is a conflict.

    Args:
        volume_id (str):
        body (AttachVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachVolumeResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        volume_id=volume_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    volume_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttachVolumeRequest,
) -> AttachVolumeResponse | ErrorBody | None:
    """Attach a volume to a running sandbox read-only, pinning the volume's current version at
     admission — so a long-lived sandbox can pick up a new dataset or checkpoint version without
     being recreated. The mount is read-only in v1. The volume and sandbox must share a project. A
     volume with no published version, or a sandbox that already has something mounted at the path,
     is a conflict.

    Args:
        volume_id (str):
        body (AttachVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachVolumeResponse | ErrorBody
    """

    return sync_detailed(
        volume_id=volume_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    volume_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttachVolumeRequest,
) -> Response[AttachVolumeResponse | ErrorBody]:
    """Attach a volume to a running sandbox read-only, pinning the volume's current version at
     admission — so a long-lived sandbox can pick up a new dataset or checkpoint version without
     being recreated. The mount is read-only in v1. The volume and sandbox must share a project. A
     volume with no published version, or a sandbox that already has something mounted at the path,
     is a conflict.

    Args:
        volume_id (str):
        body (AttachVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachVolumeResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        volume_id=volume_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    volume_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttachVolumeRequest,
) -> AttachVolumeResponse | ErrorBody | None:
    """Attach a volume to a running sandbox read-only, pinning the volume's current version at
     admission — so a long-lived sandbox can pick up a new dataset or checkpoint version without
     being recreated. The mount is read-only in v1. The volume and sandbox must share a project. A
     volume with no published version, or a sandbox that already has something mounted at the path,
     is a conflict.

    Args:
        volume_id (str):
        body (AttachVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachVolumeResponse | ErrorBody
    """

    return (
        await asyncio_detailed(
            volume_id=volume_id,
            client=client,
            body=body,
        )
    ).parsed
