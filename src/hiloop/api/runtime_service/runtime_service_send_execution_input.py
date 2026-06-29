from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.send_execution_input_request import SendExecutionInputRequest
from ...models.send_execution_input_response import SendExecutionInputResponse
from ...types import Response


def _get_kwargs(
    execution_id: str,
    *,
    body: SendExecutionInputRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/executions/{execution_id}:input".format(
            execution_id=quote(str(execution_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SendExecutionInputResponse | None:
    if response.status_code == 200:
        response_200 = SendExecutionInputResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SendExecutionInputResponse]:
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
    body: SendExecutionInputRequest,
) -> Response[SendExecutionInputResponse]:
    """Send standard input or a control signal to a running execution.

    Args:
        execution_id (str):
        body (SendExecutionInputRequest): Deliver more input to a running execution: either
            standard input bytes or a control signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendExecutionInputResponse]
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
    body: SendExecutionInputRequest,
) -> SendExecutionInputResponse | None:
    """Send standard input or a control signal to a running execution.

    Args:
        execution_id (str):
        body (SendExecutionInputRequest): Deliver more input to a running execution: either
            standard input bytes or a control signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendExecutionInputResponse
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
    body: SendExecutionInputRequest,
) -> Response[SendExecutionInputResponse]:
    """Send standard input or a control signal to a running execution.

    Args:
        execution_id (str):
        body (SendExecutionInputRequest): Deliver more input to a running execution: either
            standard input bytes or a control signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendExecutionInputResponse]
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
    body: SendExecutionInputRequest,
) -> SendExecutionInputResponse | None:
    """Send standard input or a control signal to a running execution.

    Args:
        execution_id (str):
        body (SendExecutionInputRequest): Deliver more input to a running execution: either
            standard input bytes or a control signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendExecutionInputResponse
    """

    return (
        await asyncio_detailed(
            execution_id=execution_id,
            client=client,
            body=body,
        )
    ).parsed
