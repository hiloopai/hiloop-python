from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_annotation_schema_response import GetAnnotationSchemaResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/annotation-schemas/{name}".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAnnotationSchemaResponse | None:
    if response.status_code == 200:
        response_200 = GetAnnotationSchemaResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAnnotationSchemaResponse]:
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
    version: str | Unset = UNSET,
) -> Response[GetAnnotationSchemaResponse]:
    """Get a schema config by name (latest live version, or a specific version) in the caller's tenant.

    Args:
        name (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAnnotationSchemaResponse]
    """

    kwargs = _get_kwargs(
        name=name,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
) -> GetAnnotationSchemaResponse | None:
    """Get a schema config by name (latest live version, or a specific version) in the caller's tenant.

    Args:
        name (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAnnotationSchemaResponse
    """

    return sync_detailed(
        name=name,
        client=client,
        version=version,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
) -> Response[GetAnnotationSchemaResponse]:
    """Get a schema config by name (latest live version, or a specific version) in the caller's tenant.

    Args:
        name (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAnnotationSchemaResponse]
    """

    kwargs = _get_kwargs(
        name=name,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
) -> GetAnnotationSchemaResponse | None:
    """Get a schema config by name (latest live version, or a specific version) in the caller's tenant.

    Args:
        name (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAnnotationSchemaResponse
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            version=version,
        )
    ).parsed
