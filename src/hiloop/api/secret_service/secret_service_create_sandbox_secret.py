from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_sandbox_secret_request import CreateSandboxSecretRequest
from ...models.create_sandbox_secret_response import CreateSandboxSecretResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateSandboxSecretRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/secrets",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateSandboxSecretResponse | None:
    if response.status_code == 200:
        response_200 = CreateSandboxSecretResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateSandboxSecretResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSandboxSecretRequest,
) -> Response[CreateSandboxSecretResponse]:
    """Create a secret in the caller's tenant, storing the value encrypted. A duplicate name within the
     tenant is a conflict. The value is not returned.

    Args:
        body (CreateSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSandboxSecretResponse]
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
    body: CreateSandboxSecretRequest,
) -> CreateSandboxSecretResponse | None:
    """Create a secret in the caller's tenant, storing the value encrypted. A duplicate name within the
     tenant is a conflict. The value is not returned.

    Args:
        body (CreateSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSandboxSecretResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSandboxSecretRequest,
) -> Response[CreateSandboxSecretResponse]:
    """Create a secret in the caller's tenant, storing the value encrypted. A duplicate name within the
     tenant is a conflict. The value is not returned.

    Args:
        body (CreateSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSandboxSecretResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSandboxSecretRequest,
) -> CreateSandboxSecretResponse | None:
    """Create a secret in the caller's tenant, storing the value encrypted. A duplicate name within the
     tenant is a conflict. The value is not returned.

    Args:
        body (CreateSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSandboxSecretResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
