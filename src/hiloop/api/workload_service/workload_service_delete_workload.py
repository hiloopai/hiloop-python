from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_workload_response import DeleteWorkloadResponse
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/workloads/{name}".format(
            name=quote(str(name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteWorkloadResponse | ErrorBody | None:
    if response.status_code == 200:
        response_200 = DeleteWorkloadResponse.from_dict(response.json())

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
) -> Response[DeleteWorkloadResponse | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteWorkloadResponse | ErrorBody]:
    """Delete a registered workload and its launch ACL. Requires an owner or admin in the tenant.
     A workload with live sandboxes still operating under its identity is a conflict — stop them
     first. Past runs attributed to the workload keep their recorded principal id; once the name is
     gone that id renders raw, so prefer keeping workloads that own meaningful history.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWorkloadResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteWorkloadResponse | ErrorBody | None:
    """Delete a registered workload and its launch ACL. Requires an owner or admin in the tenant.
     A workload with live sandboxes still operating under its identity is a conflict — stop them
     first. Past runs attributed to the workload keep their recorded principal id; once the name is
     gone that id renders raw, so prefer keeping workloads that own meaningful history.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWorkloadResponse | ErrorBody
    """

    return sync_detailed(
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteWorkloadResponse | ErrorBody]:
    """Delete a registered workload and its launch ACL. Requires an owner or admin in the tenant.
     A workload with live sandboxes still operating under its identity is a conflict — stop them
     first. Past runs attributed to the workload keep their recorded principal id; once the name is
     gone that id renders raw, so prefer keeping workloads that own meaningful history.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWorkloadResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteWorkloadResponse | ErrorBody | None:
    """Delete a registered workload and its launch ACL. Requires an owner or admin in the tenant.
     A workload with live sandboxes still operating under its identity is a conflict — stop them
     first. Past runs attributed to the workload keep their recorded principal id; once the name is
     gone that id renders raw, so prefer keeping workloads that own meaningful history.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWorkloadResponse | ErrorBody
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
        )
    ).parsed
