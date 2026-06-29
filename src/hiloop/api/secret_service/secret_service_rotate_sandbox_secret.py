from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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
) -> RotateSandboxSecretResponse | None:
    if response.status_code == 200:
        response_200 = RotateSandboxSecretResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RotateSandboxSecretResponse]:
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
) -> Response[RotateSandboxSecretResponse]:
    """Rotate a secret to a new value within the caller's tenant, storing it as a new version. The new
     value is not returned.

    Args:
        id (str):
        body (RotateSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RotateSandboxSecretResponse]
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
) -> RotateSandboxSecretResponse | None:
    """Rotate a secret to a new value within the caller's tenant, storing it as a new version. The new
     value is not returned.

    Args:
        id (str):
        body (RotateSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RotateSandboxSecretResponse
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
) -> Response[RotateSandboxSecretResponse]:
    """Rotate a secret to a new value within the caller's tenant, storing it as a new version. The new
     value is not returned.

    Args:
        id (str):
        body (RotateSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RotateSandboxSecretResponse]
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
) -> RotateSandboxSecretResponse | None:
    """Rotate a secret to a new value within the caller's tenant, storing it as a new version. The new
     value is not returned.

    Args:
        id (str):
        body (RotateSandboxSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RotateSandboxSecretResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
