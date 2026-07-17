from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
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

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["project_id"] = project_id

    params["observed_state"] = observed_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sandboxes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | ListSandboxesResponse | None:
    if response.status_code == 200:
        response_200 = ListSandboxesResponse.from_dict(response.json())

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
) -> Response[ErrorBody | ListSandboxesResponse]:
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
) -> Response[ErrorBody | ListSandboxesResponse]:
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
        Response[ErrorBody | ListSandboxesResponse]
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
) -> ErrorBody | ListSandboxesResponse | None:
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
        ErrorBody | ListSandboxesResponse
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
) -> Response[ErrorBody | ListSandboxesResponse]:
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
        Response[ErrorBody | ListSandboxesResponse]
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
) -> ErrorBody | ListSandboxesResponse | None:
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
        ErrorBody | ListSandboxesResponse
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
