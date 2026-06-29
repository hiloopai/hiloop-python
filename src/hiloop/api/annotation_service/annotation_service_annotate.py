from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.annotate_request import AnnotateRequest
from ...models.annotate_response import AnnotateResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AnnotateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/telemetry/annotations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AnnotateResponse | None:
    if response.status_code == 200:
        response_200 = AnnotateResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AnnotateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AnnotateRequest,
) -> Response[AnnotateResponse]:
    r"""Annotate a single target event in a run. Mints one `signal = \"annotation\"` event, validates its
     payload against the named schema, and durably appends it; returns the minted `event_id`.

    Args:
        body (AnnotateRequest): A point annotation about a single target event.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnnotateResponse]
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
    body: AnnotateRequest,
) -> AnnotateResponse | None:
    r"""Annotate a single target event in a run. Mints one `signal = \"annotation\"` event, validates its
     payload against the named schema, and durably appends it; returns the minted `event_id`.

    Args:
        body (AnnotateRequest): A point annotation about a single target event.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnnotateResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AnnotateRequest,
) -> Response[AnnotateResponse]:
    r"""Annotate a single target event in a run. Mints one `signal = \"annotation\"` event, validates its
     payload against the named schema, and durably appends it; returns the minted `event_id`.

    Args:
        body (AnnotateRequest): A point annotation about a single target event.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnnotateResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AnnotateRequest,
) -> AnnotateResponse | None:
    r"""Annotate a single target event in a run. Mints one `signal = \"annotation\"` event, validates its
     payload against the named schema, and durably appends it; returns the minted `event_id`.

    Args:
        body (AnnotateRequest): A point annotation about a single target event.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnnotateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
