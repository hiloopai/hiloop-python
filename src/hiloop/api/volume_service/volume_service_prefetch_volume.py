from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.prefetch_volume_request import PrefetchVolumeRequest
from ...models.prefetch_volume_response import PrefetchVolumeResponse
from ...types import Response


def _get_kwargs(
    volume_id: str,
    *,
    body: PrefetchVolumeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/volumes/{volume_id}:prefetch".format(
            volume_id=quote(str(volume_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | PrefetchVolumeResponse | None:
    if response.status_code == 200:
        response_200 = PrefetchVolumeResponse.from_dict(response.json())

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
) -> Response[ErrorBody | PrefetchVolumeResponse]:
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
    body: PrefetchVolumeRequest,
) -> Response[ErrorBody | PrefetchVolumeResponse]:
    """Pre-warm a volume version into the node-side cache ahead of a planned wave of sandbox
     creates, so their attaches find the content already local instead of each paying the cold
     fill from the volume store. The call returns once every node has accepted the fill;
     hydration continues in the background, and re-issuing is safe — fills are deduplicated, so
     a repeat never restarts one that is already warming or warm. Prefetch is purely an
     optimization: it never changes the volume or any sandbox, and an attach works without it
     (the attach path hydrates on demand). A volume with no published version is a conflict.

    Args:
        volume_id (str):
        body (PrefetchVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | PrefetchVolumeResponse]
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
    body: PrefetchVolumeRequest,
) -> ErrorBody | PrefetchVolumeResponse | None:
    """Pre-warm a volume version into the node-side cache ahead of a planned wave of sandbox
     creates, so their attaches find the content already local instead of each paying the cold
     fill from the volume store. The call returns once every node has accepted the fill;
     hydration continues in the background, and re-issuing is safe — fills are deduplicated, so
     a repeat never restarts one that is already warming or warm. Prefetch is purely an
     optimization: it never changes the volume or any sandbox, and an attach works without it
     (the attach path hydrates on demand). A volume with no published version is a conflict.

    Args:
        volume_id (str):
        body (PrefetchVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | PrefetchVolumeResponse
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
    body: PrefetchVolumeRequest,
) -> Response[ErrorBody | PrefetchVolumeResponse]:
    """Pre-warm a volume version into the node-side cache ahead of a planned wave of sandbox
     creates, so their attaches find the content already local instead of each paying the cold
     fill from the volume store. The call returns once every node has accepted the fill;
     hydration continues in the background, and re-issuing is safe — fills are deduplicated, so
     a repeat never restarts one that is already warming or warm. Prefetch is purely an
     optimization: it never changes the volume or any sandbox, and an attach works without it
     (the attach path hydrates on demand). A volume with no published version is a conflict.

    Args:
        volume_id (str):
        body (PrefetchVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | PrefetchVolumeResponse]
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
    body: PrefetchVolumeRequest,
) -> ErrorBody | PrefetchVolumeResponse | None:
    """Pre-warm a volume version into the node-side cache ahead of a planned wave of sandbox
     creates, so their attaches find the content already local instead of each paying the cold
     fill from the volume store. The call returns once every node has accepted the fill;
     hydration continues in the background, and re-issuing is safe — fills are deduplicated, so
     a repeat never restarts one that is already warming or warm. Prefetch is purely an
     optimization: it never changes the volume or any sandbox, and an attach works without it
     (the attach path hydrates on demand). A volume with no published version is a conflict.

    Args:
        volume_id (str):
        body (PrefetchVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | PrefetchVolumeResponse
    """

    return (
        await asyncio_detailed(
            volume_id=volume_id,
            client=client,
            body=body,
        )
    ).parsed
