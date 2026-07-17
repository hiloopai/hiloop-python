from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_egress_policy_binding_response import DeleteEgressPolicyBindingResponse
from ...models.error_body import ErrorBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    selector: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["selector"] = selector

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/tenant/egress-policy/bindings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteEgressPolicyBindingResponse | ErrorBody | None:
    if response.status_code == 200:
        response_200 = DeleteEgressPolicyBindingResponse.from_dict(response.json())

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
) -> Response[DeleteEgressPolicyBindingResponse | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    selector: str | Unset = UNSET,
) -> Response[DeleteEgressPolicyBindingResponse | ErrorBody]:
    """Delete an identity-bound egress policy binding by selector. Requires an owner or admin.

    Args:
        selector (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEgressPolicyBindingResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        selector=selector,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    selector: str | Unset = UNSET,
) -> DeleteEgressPolicyBindingResponse | ErrorBody | None:
    """Delete an identity-bound egress policy binding by selector. Requires an owner or admin.

    Args:
        selector (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEgressPolicyBindingResponse | ErrorBody
    """

    return sync_detailed(
        client=client,
        selector=selector,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    selector: str | Unset = UNSET,
) -> Response[DeleteEgressPolicyBindingResponse | ErrorBody]:
    """Delete an identity-bound egress policy binding by selector. Requires an owner or admin.

    Args:
        selector (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEgressPolicyBindingResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        selector=selector,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    selector: str | Unset = UNSET,
) -> DeleteEgressPolicyBindingResponse | ErrorBody | None:
    """Delete an identity-bound egress policy binding by selector. Requires an owner or admin.

    Args:
        selector (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEgressPolicyBindingResponse | ErrorBody
    """

    return (
        await asyncio_detailed(
            client=client,
            selector=selector,
        )
    ).parsed
