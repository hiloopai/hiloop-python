from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.acquire_lease_request import AcquireLeaseRequest
from ...models.acquire_lease_response import AcquireLeaseResponse
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    *,
    body: AcquireLeaseRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/leases",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AcquireLeaseResponse | ErrorBody | None:
    if response.status_code == 200:
        response_200 = AcquireLeaseResponse.from_dict(response.json())

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
) -> Response[AcquireLeaseResponse | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AcquireLeaseRequest,
) -> Response[AcquireLeaseResponse | ErrorBody]:
    """Acquire a project-scoped lease by name. Succeeds when the name is free — or held by a lease
     whose TTL has lapsed, which the acquire atomically takes over — and returns the new lease with
     a freshly minted id. While a live holder exists the call fails with error code `lease_held`
     (HTTP 409); the CLI surfaces that as exit code 1 so contention loops can branch on it.

    Args:
        body (AcquireLeaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcquireLeaseResponse | ErrorBody]
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
    body: AcquireLeaseRequest,
) -> AcquireLeaseResponse | ErrorBody | None:
    """Acquire a project-scoped lease by name. Succeeds when the name is free — or held by a lease
     whose TTL has lapsed, which the acquire atomically takes over — and returns the new lease with
     a freshly minted id. While a live holder exists the call fails with error code `lease_held`
     (HTTP 409); the CLI surfaces that as exit code 1 so contention loops can branch on it.

    Args:
        body (AcquireLeaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcquireLeaseResponse | ErrorBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AcquireLeaseRequest,
) -> Response[AcquireLeaseResponse | ErrorBody]:
    """Acquire a project-scoped lease by name. Succeeds when the name is free — or held by a lease
     whose TTL has lapsed, which the acquire atomically takes over — and returns the new lease with
     a freshly minted id. While a live holder exists the call fails with error code `lease_held`
     (HTTP 409); the CLI surfaces that as exit code 1 so contention loops can branch on it.

    Args:
        body (AcquireLeaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcquireLeaseResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AcquireLeaseRequest,
) -> AcquireLeaseResponse | ErrorBody | None:
    """Acquire a project-scoped lease by name. Succeeds when the name is free — or held by a lease
     whose TTL has lapsed, which the acquire atomically takes over — and returns the new lease with
     a freshly minted id. While a live holder exists the call fails with error code `lease_held`
     (HTTP 409); the CLI surfaces that as exit code 1 so contention loops can branch on it.

    Args:
        body (AcquireLeaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcquireLeaseResponse | ErrorBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
