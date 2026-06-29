from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exec_output_event import ExecOutputEvent
from ...types import Response


def _get_kwargs(
    execution_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/executions/{execution_id}:stream".format(
            execution_id=quote(str(execution_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExecOutputEvent | None:
    if response.status_code == 200:
        response_200 = ExecOutputEvent.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ExecOutputEvent]:
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
) -> Response[ExecOutputEvent]:
    """Stream an execution's combined stdout/stderr until it exits.

    Args:
        execution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecOutputEvent]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ExecOutputEvent | None:
    """Stream an execution's combined stdout/stderr until it exits.

    Args:
        execution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecOutputEvent
    """

    return sync_detailed(
        execution_id=execution_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExecOutputEvent]:
    """Stream an execution's combined stdout/stderr until it exits.

    Args:
        execution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecOutputEvent]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ExecOutputEvent | None:
    """Stream an execution's combined stdout/stderr until it exits.

    Args:
        execution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecOutputEvent
    """

    return (
        await asyncio_detailed(
            execution_id=execution_id,
            client=client,
        )
    ).parsed
