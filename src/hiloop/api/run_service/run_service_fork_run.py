from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fork_run_request import ForkRunRequest
from ...models.fork_run_response import ForkRunResponse
from ...types import Response


def _get_kwargs(
    parent_run_id: str,
    *,
    body: ForkRunRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/runs/{parent_run_id}:fork".format(
            parent_run_id=quote(str(parent_run_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ForkRunResponse | None:
    if response.status_code == 200:
        response_200 = ForkRunResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ForkRunResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    parent_run_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ForkRunRequest,
) -> Response[ForkRunResponse]:
    """Fork a run: mint a child run that branches from the parent at the given branch point.

    Args:
        parent_run_id (str):
        body (ForkRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForkRunResponse]
    """

    kwargs = _get_kwargs(
        parent_run_id=parent_run_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    parent_run_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ForkRunRequest,
) -> ForkRunResponse | None:
    """Fork a run: mint a child run that branches from the parent at the given branch point.

    Args:
        parent_run_id (str):
        body (ForkRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForkRunResponse
    """

    return sync_detailed(
        parent_run_id=parent_run_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    parent_run_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ForkRunRequest,
) -> Response[ForkRunResponse]:
    """Fork a run: mint a child run that branches from the parent at the given branch point.

    Args:
        parent_run_id (str):
        body (ForkRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForkRunResponse]
    """

    kwargs = _get_kwargs(
        parent_run_id=parent_run_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    parent_run_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ForkRunRequest,
) -> ForkRunResponse | None:
    """Fork a run: mint a child run that branches from the parent at the given branch point.

    Args:
        parent_run_id (str):
        body (ForkRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForkRunResponse
    """

    return (
        await asyncio_detailed(
            parent_run_id=parent_run_id,
            client=client,
            body=body,
        )
    ).parsed
