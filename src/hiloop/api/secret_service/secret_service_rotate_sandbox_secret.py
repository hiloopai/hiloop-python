from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.rotate_sandbox_secret_request import RotateSandboxSecretRequest
from ...models.rotate_sandbox_secret_response import RotateSandboxSecretResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: RotateSandboxSecretRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/secrets/{id}/rotate".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | RotateSandboxSecretResponse | None:
    if response.status_code == 200:
        response_200 = RotateSandboxSecretResponse.from_dict(response.json())

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
) -> Response[ErrorBody | RotateSandboxSecretResponse]:
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
    body: RotateSandboxSecretRequest,
) -> Response[ErrorBody | RotateSandboxSecretResponse]:
    """Rotate a secret to a new value within the caller's tenant, storing it as a new version. The new
     value is not returned.

     Retries are safe with an `idempotency-key` header: repeating the request with the same key and
     the same value returns the secret's current metadata instead of rotating a second time, and
     reusing a key with a different value (or another secret) fails with `idempotency_conflict`.
     Without a key, every call mints a new version.

    Args:
        id (str):
        body (RotateSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | RotateSandboxSecretResponse]
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
    body: RotateSandboxSecretRequest,
) -> ErrorBody | RotateSandboxSecretResponse | None:
    """Rotate a secret to a new value within the caller's tenant, storing it as a new version. The new
     value is not returned.

     Retries are safe with an `idempotency-key` header: repeating the request with the same key and
     the same value returns the secret's current metadata instead of rotating a second time, and
     reusing a key with a different value (or another secret) fails with `idempotency_conflict`.
     Without a key, every call mints a new version.

    Args:
        id (str):
        body (RotateSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | RotateSandboxSecretResponse
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
    body: RotateSandboxSecretRequest,
) -> Response[ErrorBody | RotateSandboxSecretResponse]:
    """Rotate a secret to a new value within the caller's tenant, storing it as a new version. The new
     value is not returned.

     Retries are safe with an `idempotency-key` header: repeating the request with the same key and
     the same value returns the secret's current metadata instead of rotating a second time, and
     reusing a key with a different value (or another secret) fails with `idempotency_conflict`.
     Without a key, every call mints a new version.

    Args:
        id (str):
        body (RotateSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | RotateSandboxSecretResponse]
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
    body: RotateSandboxSecretRequest,
) -> ErrorBody | RotateSandboxSecretResponse | None:
    """Rotate a secret to a new value within the caller's tenant, storing it as a new version. The new
     value is not returned.

     Retries are safe with an `idempotency-key` header: repeating the request with the same key and
     the same value returns the secret's current metadata instead of rotating a second time, and
     reusing a key with a different value (or another secret) fails with `idempotency_conflict`.
     Without a key, every call mints a new version.

    Args:
        id (str):
        body (RotateSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | RotateSandboxSecretResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
