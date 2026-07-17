from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
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

    params["project_id"] = project_id

    params["sandbox_id"] = sandbox_id

    params["run_id"] = run_id

    params["origin"] = origin

    params["state"] = state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/snapshots",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | ListSnapshotsResponse | None:
    if response.status_code == 200:
        response_200 = ListSnapshotsResponse.from_dict(response.json())

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
) -> Response[ErrorBody | ListSnapshotsResponse]:
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
) -> Response[ErrorBody | ListSnapshotsResponse]:
    """Retired snapshot compatibility RPC. Clean sandbox-cell deployments return unsupported.

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
        Response[ErrorBody | ListSnapshotsResponse]
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
) -> ErrorBody | ListSnapshotsResponse | None:
    """Retired snapshot compatibility RPC. Clean sandbox-cell deployments return unsupported.

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
        ErrorBody | ListSnapshotsResponse
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
) -> Response[ErrorBody | ListSnapshotsResponse]:
    """Retired snapshot compatibility RPC. Clean sandbox-cell deployments return unsupported.

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
        Response[ErrorBody | ListSnapshotsResponse]
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
) -> ErrorBody | ListSnapshotsResponse | None:
    """Retired snapshot compatibility RPC. Clean sandbox-cell deployments return unsupported.

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
        ErrorBody | ListSnapshotsResponse
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
