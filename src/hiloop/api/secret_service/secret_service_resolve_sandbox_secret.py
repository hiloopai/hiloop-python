from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resolve_sandbox_secret_request import ResolveSandboxSecretRequest
from ...models.resolve_sandbox_secret_response import ResolveSandboxSecretResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ResolveSandboxSecretRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/secrets/resolve",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ResolveSandboxSecretResponse | None:
    if response.status_code == 200:
        response_200 = ResolveSandboxSecretResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResolveSandboxSecretResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ResolveSandboxSecretRequest,
) -> Response[ResolveSandboxSecretResponse]:
    """Resolve a secret's plaintext value by name within the caller's tenant. Called by the in-sandbox
     proxy with the per-sandbox credential to fetch a value to inject into an outbound request; this is
     the only RPC that returns the value.

    Args:
        body (ResolveSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResolveSandboxSecretResponse]
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
    body: ResolveSandboxSecretRequest,
) -> ResolveSandboxSecretResponse | None:
    """Resolve a secret's plaintext value by name within the caller's tenant. Called by the in-sandbox
     proxy with the per-sandbox credential to fetch a value to inject into an outbound request; this is
     the only RPC that returns the value.

    Args:
        body (ResolveSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResolveSandboxSecretResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ResolveSandboxSecretRequest,
) -> Response[ResolveSandboxSecretResponse]:
    """Resolve a secret's plaintext value by name within the caller's tenant. Called by the in-sandbox
     proxy with the per-sandbox credential to fetch a value to inject into an outbound request; this is
     the only RPC that returns the value.

    Args:
        body (ResolveSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResolveSandboxSecretResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ResolveSandboxSecretRequest,
) -> ResolveSandboxSecretResponse | None:
    """Resolve a secret's plaintext value by name within the caller's tenant. Called by the in-sandbox
     proxy with the per-sandbox credential to fetch a value to inject into an outbound request; this is
     the only RPC that returns the value.

    Args:
        body (ResolveSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResolveSandboxSecretResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
