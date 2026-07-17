from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.set_workload_launch_acl_request import SetWorkloadLaunchAclRequest
from ...models.set_workload_launch_acl_response import SetWorkloadLaunchAclResponse
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: SetWorkloadLaunchAclRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/workloads/{name}/launch-acl".format(
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | SetWorkloadLaunchAclResponse | None:
    if response.status_code == 200:
        response_200 = SetWorkloadLaunchAclResponse.from_dict(response.json())

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
) -> Response[ErrorBody | SetWorkloadLaunchAclResponse]:
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
    body: SetWorkloadLaunchAclRequest,
) -> Response[ErrorBody | SetWorkloadLaunchAclResponse]:
    """Replace a workload's launch ACL. Requires an owner or admin in the tenant.

    Args:
        name (str):
        body (SetWorkloadLaunchAclRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SetWorkloadLaunchAclResponse]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetWorkloadLaunchAclRequest,
) -> ErrorBody | SetWorkloadLaunchAclResponse | None:
    """Replace a workload's launch ACL. Requires an owner or admin in the tenant.

    Args:
        name (str):
        body (SetWorkloadLaunchAclRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SetWorkloadLaunchAclResponse
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetWorkloadLaunchAclRequest,
) -> Response[ErrorBody | SetWorkloadLaunchAclResponse]:
    """Replace a workload's launch ACL. Requires an owner or admin in the tenant.

    Args:
        name (str):
        body (SetWorkloadLaunchAclRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | SetWorkloadLaunchAclResponse]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetWorkloadLaunchAclRequest,
) -> ErrorBody | SetWorkloadLaunchAclResponse | None:
    """Replace a workload's launch ACL. Requires an owner or admin in the tenant.

    Args:
        name (str):
        body (SetWorkloadLaunchAclRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | SetWorkloadLaunchAclResponse
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
