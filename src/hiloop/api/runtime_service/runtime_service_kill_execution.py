from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.kill_execution_request import KillExecutionRequest
from ...models.kill_execution_response import KillExecutionResponse
from ...types import Response


def _get_kwargs(
    execution_id: str,
    *,
    body: KillExecutionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/executions/{execution_id}:kill".format(
            execution_id=quote(str(execution_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | KillExecutionResponse | None:
    if response.status_code == 200:
        response_200 = KillExecutionResponse.from_dict(response.json())

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
) -> Response[ErrorBody | KillExecutionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KillExecutionRequest,
) -> Response[ErrorBody | KillExecutionResponse]:
    """Retired provider-interactive compatibility RPC. Clean sandbox-cell deployments return
     unsupported.

    Args:
        execution_id (str):
        body (KillExecutionRequest): Retired provider-interactive compatibility request. Clean
            sandbox-cell deployments return
             unsupported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | KillExecutionResponse]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KillExecutionRequest,
) -> ErrorBody | KillExecutionResponse | None:
    """Retired provider-interactive compatibility RPC. Clean sandbox-cell deployments return
     unsupported.

    Args:
        execution_id (str):
        body (KillExecutionRequest): Retired provider-interactive compatibility request. Clean
            sandbox-cell deployments return
             unsupported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | KillExecutionResponse
    """

    return sync_detailed(
        execution_id=execution_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KillExecutionRequest,
) -> Response[ErrorBody | KillExecutionResponse]:
    """Retired provider-interactive compatibility RPC. Clean sandbox-cell deployments return
     unsupported.

    Args:
        execution_id (str):
        body (KillExecutionRequest): Retired provider-interactive compatibility request. Clean
            sandbox-cell deployments return
             unsupported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | KillExecutionResponse]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KillExecutionRequest,
) -> ErrorBody | KillExecutionResponse | None:
    """Retired provider-interactive compatibility RPC. Clean sandbox-cell deployments return
     unsupported.

    Args:
        execution_id (str):
        body (KillExecutionRequest): Retired provider-interactive compatibility request. Clean
            sandbox-cell deployments return
             unsupported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | KillExecutionResponse
    """

    return (
        await asyncio_detailed(
            execution_id=execution_id,
            client=client,
            body=body,
        )
    ).parsed
