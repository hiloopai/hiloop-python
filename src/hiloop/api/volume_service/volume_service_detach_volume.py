from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.detach_volume_request import DetachVolumeRequest
from ...models.detach_volume_response import DetachVolumeResponse
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    attachment_id: str,
    *,
    body: DetachVolumeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/volumes/attachments/{attachment_id}:detach".format(
            attachment_id=quote(str(attachment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DetachVolumeResponse | ErrorBody | None:
    if response.status_code == 200:
        response_200 = DetachVolumeResponse.from_dict(response.json())

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
) -> Response[DetachVolumeResponse | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DetachVolumeRequest,
) -> Response[DetachVolumeResponse | ErrorBody]:
    """Detach a volume attachment by id, unmounting it from the sandbox. Detaching an unknown or
     already-detached attachment is a not-found error, so a caller holding a stale handle finds out.

    Args:
        attachment_id (str):
        body (DetachVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DetachVolumeResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        attachment_id=attachment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DetachVolumeRequest,
) -> DetachVolumeResponse | ErrorBody | None:
    """Detach a volume attachment by id, unmounting it from the sandbox. Detaching an unknown or
     already-detached attachment is a not-found error, so a caller holding a stale handle finds out.

    Args:
        attachment_id (str):
        body (DetachVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DetachVolumeResponse | ErrorBody
    """

    return sync_detailed(
        attachment_id=attachment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DetachVolumeRequest,
) -> Response[DetachVolumeResponse | ErrorBody]:
    """Detach a volume attachment by id, unmounting it from the sandbox. Detaching an unknown or
     already-detached attachment is a not-found error, so a caller holding a stale handle finds out.

    Args:
        attachment_id (str):
        body (DetachVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DetachVolumeResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        attachment_id=attachment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DetachVolumeRequest,
) -> DetachVolumeResponse | ErrorBody | None:
    """Detach a volume attachment by id, unmounting it from the sandbox. Detaching an unknown or
     already-detached attachment is a not-found error, so a caller holding a stale handle finds out.

    Args:
        attachment_id (str):
        body (DetachVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DetachVolumeResponse | ErrorBody
    """

    return (
        await asyncio_detailed(
            attachment_id=attachment_id,
            client=client,
            body=body,
        )
    ).parsed
