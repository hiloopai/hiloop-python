from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_runs_response import ListRunsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    root_run_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params["status"] = status

    params["createdBy"] = created_by

    params["createdAfter"] = created_after

    params["createdBefore"] = created_before

    params["rootRunId"] = root_run_id

    params["projectId"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/runs",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListRunsResponse | None:
    if response.status_code == 200:
        response_200 = ListRunsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListRunsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    root_run_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
) -> Response[ListRunsResponse]:
    """List the runs in the caller's tenant, newest first, with cursor pagination and optional
     status / creator / time / tree filters.

    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        status (str | Unset):
        created_by (str | Unset):
        created_after (str | Unset):
        created_before (str | Unset):
        root_run_id (str | Unset):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListRunsResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        status=status,
        created_by=created_by,
        created_after=created_after,
        created_before=created_before,
        root_run_id=root_run_id,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    root_run_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
) -> ListRunsResponse | None:
    """List the runs in the caller's tenant, newest first, with cursor pagination and optional
     status / creator / time / tree filters.

    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        status (str | Unset):
        created_by (str | Unset):
        created_after (str | Unset):
        created_before (str | Unset):
        root_run_id (str | Unset):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListRunsResponse
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page_token=page_token,
        status=status,
        created_by=created_by,
        created_after=created_after,
        created_before=created_before,
        root_run_id=root_run_id,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    root_run_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
) -> Response[ListRunsResponse]:
    """List the runs in the caller's tenant, newest first, with cursor pagination and optional
     status / creator / time / tree filters.

    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        status (str | Unset):
        created_by (str | Unset):
        created_after (str | Unset):
        created_before (str | Unset):
        root_run_id (str | Unset):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListRunsResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        status=status,
        created_by=created_by,
        created_after=created_after,
        created_before=created_before,
        root_run_id=root_run_id,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    root_run_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
) -> ListRunsResponse | None:
    """List the runs in the caller's tenant, newest first, with cursor pagination and optional
     status / creator / time / tree filters.

    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        status (str | Unset):
        created_by (str | Unset):
        created_after (str | Unset):
        created_before (str | Unset):
        root_run_id (str | Unset):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListRunsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page_token=page_token,
            status=status,
            created_by=created_by,
            created_after=created_after,
            created_before=created_before,
            root_run_id=root_run_id,
            project_id=project_id,
        )
    ).parsed
