from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
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
) -> ErrorBody | ResolveSandboxSecretResponse | None:
    if response.status_code == 200:
        response_200 = ResolveSandboxSecretResponse.from_dict(response.json())

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
) -> Response[ErrorBody | ResolveSandboxSecretResponse]:
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
) -> Response[ErrorBody | ResolveSandboxSecretResponse]:
    """Resolve a secret's plaintext value by name within the caller's tenant. Called by the in-sandbox
     proxy with the per-sandbox credential to fetch a value to inject into an outbound request; this is
     the only RPC that returns the value.

    Args:
        body (ResolveSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ResolveSandboxSecretResponse]
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
) -> ErrorBody | ResolveSandboxSecretResponse | None:
    """Resolve a secret's plaintext value by name within the caller's tenant. Called by the in-sandbox
     proxy with the per-sandbox credential to fetch a value to inject into an outbound request; this is
     the only RPC that returns the value.

    Args:
        body (ResolveSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ResolveSandboxSecretResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ResolveSandboxSecretRequest,
) -> Response[ErrorBody | ResolveSandboxSecretResponse]:
    """Resolve a secret's plaintext value by name within the caller's tenant. Called by the in-sandbox
     proxy with the per-sandbox credential to fetch a value to inject into an outbound request; this is
     the only RPC that returns the value.

    Args:
        body (ResolveSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ResolveSandboxSecretResponse]
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
) -> ErrorBody | ResolveSandboxSecretResponse | None:
    """Resolve a secret's plaintext value by name within the caller's tenant. Called by the in-sandbox
     proxy with the per-sandbox credential to fetch a value to inject into an outbound request; this is
     the only RPC that returns the value.

    Args:
        body (ResolveSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ResolveSandboxSecretResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
