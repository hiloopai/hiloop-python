from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.resolve_effective_egress_request import ResolveEffectiveEgressRequest
from ...models.resolve_effective_egress_response import ResolveEffectiveEgressResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ResolveEffectiveEgressRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tenant/egress-policy/effective",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | ResolveEffectiveEgressResponse | None:
    if response.status_code == 200:
        response_200 = ResolveEffectiveEgressResponse.from_dict(response.json())

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
) -> Response[ErrorBody | ResolveEffectiveEgressResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ResolveEffectiveEgressRequest,
) -> Response[ErrorBody | ResolveEffectiveEgressResponse]:
    """Resolve the effective egress policy for an identity selector: the tenant baseline narrowed by the
     most-specific matching binding (or, when a proposed policy is supplied, by that unsaved policy at
     the selector's tier), plus which binding won, what the baseline ceiling clamped away, and how many
     identities the selector covers. This runs the same resolution the runtime enforces, server-side,
     so callers never re-derive it. It reveals binding structure and serves the operator management
     surfaces, so it requires an owner or admin in the tenant.

    Args:
        body (ResolveEffectiveEgressRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ResolveEffectiveEgressResponse]
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
    body: ResolveEffectiveEgressRequest,
) -> ErrorBody | ResolveEffectiveEgressResponse | None:
    """Resolve the effective egress policy for an identity selector: the tenant baseline narrowed by the
     most-specific matching binding (or, when a proposed policy is supplied, by that unsaved policy at
     the selector's tier), plus which binding won, what the baseline ceiling clamped away, and how many
     identities the selector covers. This runs the same resolution the runtime enforces, server-side,
     so callers never re-derive it. It reveals binding structure and serves the operator management
     surfaces, so it requires an owner or admin in the tenant.

    Args:
        body (ResolveEffectiveEgressRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ResolveEffectiveEgressResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ResolveEffectiveEgressRequest,
) -> Response[ErrorBody | ResolveEffectiveEgressResponse]:
    """Resolve the effective egress policy for an identity selector: the tenant baseline narrowed by the
     most-specific matching binding (or, when a proposed policy is supplied, by that unsaved policy at
     the selector's tier), plus which binding won, what the baseline ceiling clamped away, and how many
     identities the selector covers. This runs the same resolution the runtime enforces, server-side,
     so callers never re-derive it. It reveals binding structure and serves the operator management
     surfaces, so it requires an owner or admin in the tenant.

    Args:
        body (ResolveEffectiveEgressRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ResolveEffectiveEgressResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ResolveEffectiveEgressRequest,
) -> ErrorBody | ResolveEffectiveEgressResponse | None:
    """Resolve the effective egress policy for an identity selector: the tenant baseline narrowed by the
     most-specific matching binding (or, when a proposed policy is supplied, by that unsaved policy at
     the selector's tier), plus which binding won, what the baseline ceiling clamped away, and how many
     identities the selector covers. This runs the same resolution the runtime enforces, server-side,
     so callers never re-derive it. It reveals binding structure and serves the operator management
     surfaces, so it requires an owner or admin in the tenant.

    Args:
        body (ResolveEffectiveEgressRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ResolveEffectiveEgressResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
