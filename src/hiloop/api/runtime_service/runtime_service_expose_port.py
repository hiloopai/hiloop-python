from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.expose_port_request import ExposePortRequest
from ...models.expose_port_response import ExposePortResponse
from ...types import Response


def _get_kwargs(
    sandbox_id: str,
    *,
    body: ExposePortRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sandboxes/{sandbox_id}:expose".format(
            sandbox_id=quote(str(sandbox_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | ExposePortResponse | None:
    if response.status_code == 200:
        response_200 = ExposePortResponse.from_dict(response.json())

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
) -> Response[ErrorBody | ExposePortResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExposePortRequest,
) -> Response[ErrorBody | ExposePortResponse]:
    """Expose one guest port through the deployment's preview edge. Identity is `(sandbox_id, port)`:
     repeating an active identity succeeds without rotating or returning its token. Rotate explicitly
     with UnexposePort followed by ExposePort.

    Args:
        sandbox_id (str):
        body (ExposePortRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ExposePortResponse]
    """

    kwargs = _get_kwargs(
        sandbox_id=sandbox_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExposePortRequest,
) -> ErrorBody | ExposePortResponse | None:
    """Expose one guest port through the deployment's preview edge. Identity is `(sandbox_id, port)`:
     repeating an active identity succeeds without rotating or returning its token. Rotate explicitly
     with UnexposePort followed by ExposePort.

    Args:
        sandbox_id (str):
        body (ExposePortRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ExposePortResponse
    """

    return sync_detailed(
        sandbox_id=sandbox_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExposePortRequest,
) -> Response[ErrorBody | ExposePortResponse]:
    """Expose one guest port through the deployment's preview edge. Identity is `(sandbox_id, port)`:
     repeating an active identity succeeds without rotating or returning its token. Rotate explicitly
     with UnexposePort followed by ExposePort.

    Args:
        sandbox_id (str):
        body (ExposePortRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ExposePortResponse]
    """

    kwargs = _get_kwargs(
        sandbox_id=sandbox_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExposePortRequest,
) -> ErrorBody | ExposePortResponse | None:
    """Expose one guest port through the deployment's preview edge. Identity is `(sandbox_id, port)`:
     repeating an active identity succeeds without rotating or returning its token. Rotate explicitly
     with UnexposePort followed by ExposePort.

    Args:
        sandbox_id (str):
        body (ExposePortRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ExposePortResponse
    """

    return (
        await asyncio_detailed(
            sandbox_id=sandbox_id,
            client=client,
            body=body,
        )
    ).parsed
