from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_tenant_egress_policy_request import SetTenantEgressPolicyRequest
from ...models.set_tenant_egress_policy_response import SetTenantEgressPolicyResponse
from ...types import Response


def _get_kwargs(
    *,
    body: SetTenantEgressPolicyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/tenant/egress-policy",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SetTenantEgressPolicyResponse | None:
    if response.status_code == 200:
        response_200 = SetTenantEgressPolicyResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SetTenantEgressPolicyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SetTenantEgressPolicyRequest,
) -> Response[SetTenantEgressPolicyResponse]:
    """Set the caller's tenant baseline egress policy. Requires an owner or admin in the tenant.

    Args:
        body (SetTenantEgressPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetTenantEgressPolicyResponse]
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
    body: SetTenantEgressPolicyRequest,
) -> SetTenantEgressPolicyResponse | None:
    """Set the caller's tenant baseline egress policy. Requires an owner or admin in the tenant.

    Args:
        body (SetTenantEgressPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetTenantEgressPolicyResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SetTenantEgressPolicyRequest,
) -> Response[SetTenantEgressPolicyResponse]:
    """Set the caller's tenant baseline egress policy. Requires an owner or admin in the tenant.

    Args:
        body (SetTenantEgressPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetTenantEgressPolicyResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SetTenantEgressPolicyRequest,
) -> SetTenantEgressPolicyResponse | None:
    """Set the caller's tenant baseline egress policy. Requires an owner or admin in the tenant.

    Args:
        body (SetTenantEgressPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetTenantEgressPolicyResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
