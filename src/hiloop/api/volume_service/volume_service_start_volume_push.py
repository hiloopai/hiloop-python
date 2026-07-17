from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.start_volume_push_request import StartVolumePushRequest
from ...models.start_volume_push_response import StartVolumePushResponse
from ...types import Response


def _get_kwargs(
    volume_id: str,
    *,
    body: StartVolumePushRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/volumes/{volume_id}:start-push".format(
            volume_id=quote(str(volume_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | StartVolumePushResponse | None:
    if response.status_code == 200:
        response_200 = StartVolumePushResponse.from_dict(response.json())

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
) -> Response[ErrorBody | StartVolumePushResponse]:
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
    body: StartVolumePushRequest,
) -> Response[ErrorBody | StartVolumePushResponse]:
    """Start pushing a new version to a volume: returns a push handle and a short-lived URL to
     upload the manifest (the file listing) to. Content bytes never ride this API — they go
     directly to the volume store through the URLs the push RPCs hand out.

     The push flow: StartVolumePush → upload the manifest → RequestVolumeBlobUploads (in batches)
     → upload the missing blobs → PublishVolumeVersion. An abandoned push needs no cleanup; its
     staged manifest expires on its own.

    Args:
        volume_id (str):
        body (StartVolumePushRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | StartVolumePushResponse]
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
    body: StartVolumePushRequest,
) -> ErrorBody | StartVolumePushResponse | None:
    """Start pushing a new version to a volume: returns a push handle and a short-lived URL to
     upload the manifest (the file listing) to. Content bytes never ride this API — they go
     directly to the volume store through the URLs the push RPCs hand out.

     The push flow: StartVolumePush → upload the manifest → RequestVolumeBlobUploads (in batches)
     → upload the missing blobs → PublishVolumeVersion. An abandoned push needs no cleanup; its
     staged manifest expires on its own.

    Args:
        volume_id (str):
        body (StartVolumePushRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | StartVolumePushResponse
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
    body: StartVolumePushRequest,
) -> Response[ErrorBody | StartVolumePushResponse]:
    """Start pushing a new version to a volume: returns a push handle and a short-lived URL to
     upload the manifest (the file listing) to. Content bytes never ride this API — they go
     directly to the volume store through the URLs the push RPCs hand out.

     The push flow: StartVolumePush → upload the manifest → RequestVolumeBlobUploads (in batches)
     → upload the missing blobs → PublishVolumeVersion. An abandoned push needs no cleanup; its
     staged manifest expires on its own.

    Args:
        volume_id (str):
        body (StartVolumePushRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | StartVolumePushResponse]
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
    body: StartVolumePushRequest,
) -> ErrorBody | StartVolumePushResponse | None:
    """Start pushing a new version to a volume: returns a push handle and a short-lived URL to
     upload the manifest (the file listing) to. Content bytes never ride this API — they go
     directly to the volume store through the URLs the push RPCs hand out.

     The push flow: StartVolumePush → upload the manifest → RequestVolumeBlobUploads (in batches)
     → upload the missing blobs → PublishVolumeVersion. An abandoned push needs no cleanup; its
     staged manifest expires on its own.

    Args:
        volume_id (str):
        body (StartVolumePushRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | StartVolumePushResponse
    """

    return (
        await asyncio_detailed(
            volume_id=volume_id,
            client=client,
            body=body,
        )
    ).parsed
