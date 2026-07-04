from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_project_response import DeleteProjectResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    cascade: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cascade"] = cascade

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/projects/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteProjectResponse | None:
    if response.status_code == 200:
        response_200 = DeleteProjectResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteProjectResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    cascade: bool | Unset = UNSET,
) -> Response[DeleteProjectResponse]:
    """Delete a project within the caller's tenant. By default a project that still has sandboxes, runs,
     or other resources cannot be deleted — remove those first — and the call returns a conflict. Set
     `cascade` to also delete the project's runs, snapshots, deleted sandboxes, and other resources
     (and reclaim the storage backing its artifacts) in one call. A cascade never tears down a live
     sandbox: every sandbox in the project must be deleted first, and while one is not the call
     returns a conflict with error code `sandboxes_not_deleted`. Deleting a project that does not
     exist in the caller's tenant is `not_found`.

    Args:
        id (str):
        cascade (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProjectResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        cascade=cascade,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    cascade: bool | Unset = UNSET,
) -> DeleteProjectResponse | None:
    """Delete a project within the caller's tenant. By default a project that still has sandboxes, runs,
     or other resources cannot be deleted — remove those first — and the call returns a conflict. Set
     `cascade` to also delete the project's runs, snapshots, deleted sandboxes, and other resources
     (and reclaim the storage backing its artifacts) in one call. A cascade never tears down a live
     sandbox: every sandbox in the project must be deleted first, and while one is not the call
     returns a conflict with error code `sandboxes_not_deleted`. Deleting a project that does not
     exist in the caller's tenant is `not_found`.

    Args:
        id (str):
        cascade (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProjectResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        cascade=cascade,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    cascade: bool | Unset = UNSET,
) -> Response[DeleteProjectResponse]:
    """Delete a project within the caller's tenant. By default a project that still has sandboxes, runs,
     or other resources cannot be deleted — remove those first — and the call returns a conflict. Set
     `cascade` to also delete the project's runs, snapshots, deleted sandboxes, and other resources
     (and reclaim the storage backing its artifacts) in one call. A cascade never tears down a live
     sandbox: every sandbox in the project must be deleted first, and while one is not the call
     returns a conflict with error code `sandboxes_not_deleted`. Deleting a project that does not
     exist in the caller's tenant is `not_found`.

    Args:
        id (str):
        cascade (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProjectResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        cascade=cascade,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    cascade: bool | Unset = UNSET,
) -> DeleteProjectResponse | None:
    """Delete a project within the caller's tenant. By default a project that still has sandboxes, runs,
     or other resources cannot be deleted — remove those first — and the call returns a conflict. Set
     `cascade` to also delete the project's runs, snapshots, deleted sandboxes, and other resources
     (and reclaim the storage backing its artifacts) in one call. A cascade never tears down a live
     sandbox: every sandbox in the project must be deleted first, and while one is not the call
     returns a conflict with error code `sandboxes_not_deleted`. Deleting a project that does not
     exist in the caller's tenant is `not_found`.

    Args:
        id (str):
        cascade (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProjectResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            cascade=cascade,
        )
    ).parsed
