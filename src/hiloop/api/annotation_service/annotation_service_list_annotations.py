from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
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

    params["run_id"] = run_id

    params["subtree"] = subtree

    params["schema_name"] = schema_name

    params["history"] = history

    params["project_id"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/telemetry/annotations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | ListAnnotationsResponse | None:
    if response.status_code == 200:
        response_200 = ListAnnotationsResponse.from_dict(response.json())

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
) -> Response[ErrorBody | ListAnnotationsResponse]:
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
) -> Response[ErrorBody | ListAnnotationsResponse]:
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
        Response[ErrorBody | ListAnnotationsResponse]
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
) -> ErrorBody | ListAnnotationsResponse | None:
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
        ErrorBody | ListAnnotationsResponse
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
) -> Response[ErrorBody | ListAnnotationsResponse]:
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
        Response[ErrorBody | ListAnnotationsResponse]
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
) -> ErrorBody | ListAnnotationsResponse | None:
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
        ErrorBody | ListAnnotationsResponse
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
