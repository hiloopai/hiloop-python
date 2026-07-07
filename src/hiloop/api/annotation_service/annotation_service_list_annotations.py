from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_annotations_response import ListAnnotationsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    run_id: str | Unset = UNSET,
    subtree: bool | Unset = UNSET,
    schema_name: str | Unset = UNSET,
    history: bool | Unset = UNSET,
    project_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["runId"] = run_id

    params["subtree"] = subtree

    params["schemaName"] = schema_name

    params["history"] = history

    params["projectId"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/telemetry/annotations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListAnnotationsResponse | None:
    if response.status_code == 200:
        response_200 = ListAnnotationsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListAnnotationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    run_id: str | Unset = UNSET,
    subtree: bool | Unset = UNSET,
    schema_name: str | Unset = UNSET,
    history: bool | Unset = UNSET,
    project_id: str | Unset = UNSET,
) -> Response[ListAnnotationsResponse]:
    """List a run's (or project's) annotations: the current latest-wins set by default, every stored
     version with `history`, optionally widened to the run's lineage subtree.

    Args:
        run_id (str | Unset):
        subtree (bool | Unset):
        schema_name (str | Unset):
        history (bool | Unset):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAnnotationsResponse]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        subtree=subtree,
        schema_name=schema_name,
        history=history,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    run_id: str | Unset = UNSET,
    subtree: bool | Unset = UNSET,
    schema_name: str | Unset = UNSET,
    history: bool | Unset = UNSET,
    project_id: str | Unset = UNSET,
) -> ListAnnotationsResponse | None:
    """List a run's (or project's) annotations: the current latest-wins set by default, every stored
     version with `history`, optionally widened to the run's lineage subtree.

    Args:
        run_id (str | Unset):
        subtree (bool | Unset):
        schema_name (str | Unset):
        history (bool | Unset):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAnnotationsResponse
    """

    return sync_detailed(
        client=client,
        run_id=run_id,
        subtree=subtree,
        schema_name=schema_name,
        history=history,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    run_id: str | Unset = UNSET,
    subtree: bool | Unset = UNSET,
    schema_name: str | Unset = UNSET,
    history: bool | Unset = UNSET,
    project_id: str | Unset = UNSET,
) -> Response[ListAnnotationsResponse]:
    """List a run's (or project's) annotations: the current latest-wins set by default, every stored
     version with `history`, optionally widened to the run's lineage subtree.

    Args:
        run_id (str | Unset):
        subtree (bool | Unset):
        schema_name (str | Unset):
        history (bool | Unset):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAnnotationsResponse]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        subtree=subtree,
        schema_name=schema_name,
        history=history,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    run_id: str | Unset = UNSET,
    subtree: bool | Unset = UNSET,
    schema_name: str | Unset = UNSET,
    history: bool | Unset = UNSET,
    project_id: str | Unset = UNSET,
) -> ListAnnotationsResponse | None:
    """List a run's (or project's) annotations: the current latest-wins set by default, every stored
     version with `history`, optionally widened to the run's lineage subtree.

    Args:
        run_id (str | Unset):
        subtree (bool | Unset):
        schema_name (str | Unset):
        history (bool | Unset):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAnnotationsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            run_id=run_id,
            subtree=subtree,
            schema_name=schema_name,
            history=history,
            project_id=project_id,
        )
    ).parsed
