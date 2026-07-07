from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_snapshots_response import ListSnapshotsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: str,
    sandbox_id: str | Unset = UNSET,
    run_id: str | Unset = UNSET,
    origin: str | Unset = UNSET,
    state: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params["sandboxId"] = sandbox_id

    params["runId"] = run_id

    params["origin"] = origin

    params["state"] = state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/snapshots",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListSnapshotsResponse | None:
    if response.status_code == 200:
        response_200 = ListSnapshotsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListSnapshotsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    sandbox_id: str | Unset = UNSET,
    run_id: str | Unset = UNSET,
    origin: str | Unset = UNSET,
    state: str | Unset = UNSET,
) -> Response[ListSnapshotsResponse]:
    """
    Args:
        project_id (str):
        sandbox_id (str | Unset):
        run_id (str | Unset):
        origin (str | Unset):
        state (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSnapshotsResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        sandbox_id=sandbox_id,
        run_id=run_id,
        origin=origin,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    sandbox_id: str | Unset = UNSET,
    run_id: str | Unset = UNSET,
    origin: str | Unset = UNSET,
    state: str | Unset = UNSET,
) -> ListSnapshotsResponse | None:
    """
    Args:
        project_id (str):
        sandbox_id (str | Unset):
        run_id (str | Unset):
        origin (str | Unset):
        state (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSnapshotsResponse
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        sandbox_id=sandbox_id,
        run_id=run_id,
        origin=origin,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    sandbox_id: str | Unset = UNSET,
    run_id: str | Unset = UNSET,
    origin: str | Unset = UNSET,
    state: str | Unset = UNSET,
) -> Response[ListSnapshotsResponse]:
    """
    Args:
        project_id (str):
        sandbox_id (str | Unset):
        run_id (str | Unset):
        origin (str | Unset):
        state (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSnapshotsResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        sandbox_id=sandbox_id,
        run_id=run_id,
        origin=origin,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    sandbox_id: str | Unset = UNSET,
    run_id: str | Unset = UNSET,
    origin: str | Unset = UNSET,
    state: str | Unset = UNSET,
) -> ListSnapshotsResponse | None:
    """
    Args:
        project_id (str):
        sandbox_id (str | Unset):
        run_id (str | Unset):
        origin (str | Unset):
        state (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSnapshotsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            sandbox_id=sandbox_id,
            run_id=run_id,
            origin=origin,
            state=state,
        )
    ).parsed
