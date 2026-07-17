from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.get_usage_series_response import GetUsageSeriesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    bucket_seconds: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["project_id"] = project_id

    params["start_time"] = start_time

    params["end_time"] = end_time

    params["bucket_seconds"] = bucket_seconds

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/usage/series",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorBody | GetUsageSeriesResponse | None:
    if response.status_code == 200:
        response_200 = GetUsageSeriesResponse.from_dict(response.json())

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
) -> Response[ErrorBody | GetUsageSeriesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    bucket_seconds: str | Unset = UNSET,
) -> Response[ErrorBody | GetUsageSeriesResponse]:
    """Get reserved-resource usage over time for the caller's tenant, bucketed for the usage dashboard's
     over-time charts.

    Args:
        project_id (str | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        bucket_seconds (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetUsageSeriesResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        start_time=start_time,
        end_time=end_time,
        bucket_seconds=bucket_seconds,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    bucket_seconds: str | Unset = UNSET,
) -> ErrorBody | GetUsageSeriesResponse | None:
    """Get reserved-resource usage over time for the caller's tenant, bucketed for the usage dashboard's
     over-time charts.

    Args:
        project_id (str | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        bucket_seconds (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetUsageSeriesResponse
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        start_time=start_time,
        end_time=end_time,
        bucket_seconds=bucket_seconds,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    bucket_seconds: str | Unset = UNSET,
) -> Response[ErrorBody | GetUsageSeriesResponse]:
    """Get reserved-resource usage over time for the caller's tenant, bucketed for the usage dashboard's
     over-time charts.

    Args:
        project_id (str | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        bucket_seconds (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | GetUsageSeriesResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        start_time=start_time,
        end_time=end_time,
        bucket_seconds=bucket_seconds,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    bucket_seconds: str | Unset = UNSET,
) -> ErrorBody | GetUsageSeriesResponse | None:
    """Get reserved-resource usage over time for the caller's tenant, bucketed for the usage dashboard's
     over-time charts.

    Args:
        project_id (str | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        bucket_seconds (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | GetUsageSeriesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            start_time=start_time,
            end_time=end_time,
            bucket_seconds=bucket_seconds,
        )
    ).parsed
