from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_sandboxes_response import ListSandboxesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    observed_state: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params["projectId"] = project_id

    params["observedState"] = observed_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sandboxes",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListSandboxesResponse | None:
    if response.status_code == 200:
        response_200 = ListSandboxesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListSandboxesResponse]:
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
    project_id: str | Unset = UNSET,
    observed_state: str | Unset = UNSET,
) -> Response[ListSandboxesResponse]:
    """
    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        project_id (str | Unset):
        observed_state (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSandboxesResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        project_id=project_id,
        observed_state=observed_state,
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
    project_id: str | Unset = UNSET,
    observed_state: str | Unset = UNSET,
) -> ListSandboxesResponse | None:
    """
    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        project_id (str | Unset):
        observed_state (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSandboxesResponse
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page_token=page_token,
        project_id=project_id,
        observed_state=observed_state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    observed_state: str | Unset = UNSET,
) -> Response[ListSandboxesResponse]:
    """
    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        project_id (str | Unset):
        observed_state (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSandboxesResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        project_id=project_id,
        observed_state=observed_state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    observed_state: str | Unset = UNSET,
) -> ListSandboxesResponse | None:
    """
    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        project_id (str | Unset):
        observed_state (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSandboxesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page_token=page_token,
            project_id=project_id,
            observed_state=observed_state,
        )
    ).parsed
