from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archive_annotation_schema_request import ArchiveAnnotationSchemaRequest
from ...models.archive_annotation_schema_response import ArchiveAnnotationSchemaResponse
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: ArchiveAnnotationSchemaRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/annotation-schemas/{name}:archive".format(
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ArchiveAnnotationSchemaResponse | None:
    if response.status_code == 200:
        response_200 = ArchiveAnnotationSchemaResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ArchiveAnnotationSchemaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ArchiveAnnotationSchemaRequest,
) -> Response[ArchiveAnnotationSchemaResponse]:
    """Archive a schema config version (stamp archived_at; never hard-delete) in the caller's tenant.

    Args:
        name (str):
        body (ArchiveAnnotationSchemaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveAnnotationSchemaResponse]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ArchiveAnnotationSchemaRequest,
) -> ArchiveAnnotationSchemaResponse | None:
    """Archive a schema config version (stamp archived_at; never hard-delete) in the caller's tenant.

    Args:
        name (str):
        body (ArchiveAnnotationSchemaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveAnnotationSchemaResponse
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ArchiveAnnotationSchemaRequest,
) -> Response[ArchiveAnnotationSchemaResponse]:
    """Archive a schema config version (stamp archived_at; never hard-delete) in the caller's tenant.

    Args:
        name (str):
        body (ArchiveAnnotationSchemaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveAnnotationSchemaResponse]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ArchiveAnnotationSchemaRequest,
) -> ArchiveAnnotationSchemaResponse | None:
    """Archive a schema config version (stamp archived_at; never hard-delete) in the caller's tenant.

    Args:
        name (str):
        body (ArchiveAnnotationSchemaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveAnnotationSchemaResponse
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
