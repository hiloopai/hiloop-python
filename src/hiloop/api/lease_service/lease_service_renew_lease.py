from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.renew_lease_request import RenewLeaseRequest
from ...models.renew_lease_response import RenewLeaseResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: RenewLeaseRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/leases/{id}/renew".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | RenewLeaseResponse | None:
    if response.status_code == 200:
        response_200 = RenewLeaseResponse.from_dict(response.json())

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
) -> Response[ErrorBody | RenewLeaseResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RenewLeaseRequest,
) -> Response[ErrorBody | RenewLeaseResponse]:
    """Renew a held lease by id, resetting its expiry to now + the requested TTL. The id is the
     capability: possession of it proves the caller's claim on this acquisition generation. A lease
     whose TTL already lapsed cannot be renewed — the call fails with `lease_expired` (the lease is
     gone; acquire again) — and an id that no longer names a live lease (released, expired, or taken
     over) is `not_found`.

    Args:
        id (str):
        body (RenewLeaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | RenewLeaseResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RenewLeaseRequest,
) -> ErrorBody | RenewLeaseResponse | None:
    """Renew a held lease by id, resetting its expiry to now + the requested TTL. The id is the
     capability: possession of it proves the caller's claim on this acquisition generation. A lease
     whose TTL already lapsed cannot be renewed — the call fails with `lease_expired` (the lease is
     gone; acquire again) — and an id that no longer names a live lease (released, expired, or taken
     over) is `not_found`.

    Args:
        id (str):
        body (RenewLeaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | RenewLeaseResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RenewLeaseRequest,
) -> Response[ErrorBody | RenewLeaseResponse]:
    """Renew a held lease by id, resetting its expiry to now + the requested TTL. The id is the
     capability: possession of it proves the caller's claim on this acquisition generation. A lease
     whose TTL already lapsed cannot be renewed — the call fails with `lease_expired` (the lease is
     gone; acquire again) — and an id that no longer names a live lease (released, expired, or taken
     over) is `not_found`.

    Args:
        id (str):
        body (RenewLeaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | RenewLeaseResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RenewLeaseRequest,
) -> ErrorBody | RenewLeaseResponse | None:
    """Renew a held lease by id, resetting its expiry to now + the requested TTL. The id is the
     capability: possession of it proves the caller's claim on this acquisition generation. A lease
     whose TTL already lapsed cannot be renewed — the call fails with `lease_expired` (the lease is
     gone; acquire again) — and an id that no longer names a live lease (released, expired, or taken
     over) is `not_found`.

    Args:
        id (str):
        body (RenewLeaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | RenewLeaseResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
