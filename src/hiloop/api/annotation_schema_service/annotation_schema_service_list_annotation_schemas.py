from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.list_annotation_schemas_response import ListAnnotationSchemasResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_archived: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_archived"] = include_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/annotation-schemas",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | ListAnnotationSchemasResponse | None:
    if response.status_code == 200:
        response_200 = ListAnnotationSchemasResponse.from_dict(response.json())

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
) -> Response[ErrorBody | ListAnnotationSchemasResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = UNSET,
) -> Response[ErrorBody | ListAnnotationSchemasResponse]:
    """List the schema configs in the caller's tenant. By default the latest live version per name.

    Args:
        include_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ListAnnotationSchemasResponse]
    """

    kwargs = _get_kwargs(
        include_archived=include_archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = UNSET,
) -> ErrorBody | ListAnnotationSchemasResponse | None:
    """List the schema configs in the caller's tenant. By default the latest live version per name.

    Args:
        include_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ListAnnotationSchemasResponse
    """

    return sync_detailed(
        client=client,
        include_archived=include_archived,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = UNSET,
) -> Response[ErrorBody | ListAnnotationSchemasResponse]:
    """List the schema configs in the caller's tenant. By default the latest live version per name.

    Args:
        include_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ListAnnotationSchemasResponse]
    """

    kwargs = _get_kwargs(
        include_archived=include_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = UNSET,
) -> ErrorBody | ListAnnotationSchemasResponse | None:
    """List the schema configs in the caller's tenant. By default the latest live version per name.

    Args:
        include_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ListAnnotationSchemasResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            include_archived=include_archived,
        )
    ).parsed
