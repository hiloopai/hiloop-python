from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.annotate_range_request import AnnotateRangeRequest
from ...models.annotate_response import AnnotateResponse
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    *,
    body: AnnotateRangeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/telemetry/annotations:range",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AnnotateResponse | ErrorBody | None:
    if response.status_code == 200:
        response_200 = AnnotateResponse.from_dict(response.json())

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
) -> Response[AnnotateResponse | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AnnotateRangeRequest,
) -> Response[AnnotateResponse | ErrorBody]:
    r"""Annotate a wall-clock range within a run. Mints one `signal = \"annotation\"` range event, validates
     its payload against the named schema, and durably appends it; returns the minted `event_id`.

    Args:
        body (AnnotateRangeRequest): A range annotation spanning a window within a run (rather
            than a single target event). The window
             is either a pair of wall-clock nanosecond bounds or a pair of event ids whose recorded
            timestamps
             become the bounds — supply exactly one form.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnnotateResponse | ErrorBody]
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
    body: AnnotateRangeRequest,
) -> AnnotateResponse | ErrorBody | None:
    r"""Annotate a wall-clock range within a run. Mints one `signal = \"annotation\"` range event, validates
     its payload against the named schema, and durably appends it; returns the minted `event_id`.

    Args:
        body (AnnotateRangeRequest): A range annotation spanning a window within a run (rather
            than a single target event). The window
             is either a pair of wall-clock nanosecond bounds or a pair of event ids whose recorded
            timestamps
             become the bounds — supply exactly one form.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnnotateResponse | ErrorBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AnnotateRangeRequest,
) -> Response[AnnotateResponse | ErrorBody]:
    r"""Annotate a wall-clock range within a run. Mints one `signal = \"annotation\"` range event, validates
     its payload against the named schema, and durably appends it; returns the minted `event_id`.

    Args:
        body (AnnotateRangeRequest): A range annotation spanning a window within a run (rather
            than a single target event). The window
             is either a pair of wall-clock nanosecond bounds or a pair of event ids whose recorded
            timestamps
             become the bounds — supply exactly one form.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnnotateResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AnnotateRangeRequest,
) -> AnnotateResponse | ErrorBody | None:
    r"""Annotate a wall-clock range within a run. Mints one `signal = \"annotation\"` range event, validates
     its payload against the named schema, and durably appends it; returns the minted `event_id`.

    Args:
        body (AnnotateRangeRequest): A range annotation spanning a window within a run (rather
            than a single target event). The window
             is either a pair of wall-clock nanosecond bounds or a pair of event ids whose recorded
            timestamps
             become the bounds — supply exactly one form.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnnotateResponse | ErrorBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
