from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.register_annotation_schema_request import RegisterAnnotationSchemaRequest
from ...models.register_annotation_schema_response import RegisterAnnotationSchemaResponse
from ...types import Response


def _get_kwargs(
    *,
    body: RegisterAnnotationSchemaRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/annotation-schemas",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RegisterAnnotationSchemaResponse | None:
    if response.status_code == 200:
        response_200 = RegisterAnnotationSchemaResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RegisterAnnotationSchemaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RegisterAnnotationSchemaRequest,
) -> Response[RegisterAnnotationSchemaResponse]:
    """Register a schema config in the caller's tenant. An unseen name starts at version 1; an existing
     name creates the next version after a backward-compatibility check against the latest live
     version (an incompatible change is rejected).

    Args:
        body (RegisterAnnotationSchemaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegisterAnnotationSchemaResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RegisterAnnotationSchemaRequest,
) -> RegisterAnnotationSchemaResponse | None:
    """Register a schema config in the caller's tenant. An unseen name starts at version 1; an existing
     name creates the next version after a backward-compatibility check against the latest live
     version (an incompatible change is rejected).

    Args:
        body (RegisterAnnotationSchemaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegisterAnnotationSchemaResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RegisterAnnotationSchemaRequest,
) -> Response[RegisterAnnotationSchemaResponse]:
    """Register a schema config in the caller's tenant. An unseen name starts at version 1; an existing
     name creates the next version after a backward-compatibility check against the latest live
     version (an incompatible change is rejected).

    Args:
        body (RegisterAnnotationSchemaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegisterAnnotationSchemaResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RegisterAnnotationSchemaRequest,
) -> RegisterAnnotationSchemaResponse | None:
    """Register a schema config in the caller's tenant. An unseen name starts at version 1; an existing
     name creates the next version after a backward-compatibility check against the latest live
     version (an incompatible change is rejected).

    Args:
        body (RegisterAnnotationSchemaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegisterAnnotationSchemaResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
