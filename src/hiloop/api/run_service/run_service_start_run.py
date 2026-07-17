from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.start_run_request import StartRunRequest
from ...models.start_run_response import StartRunResponse
from ...types import Response


def _get_kwargs(
    *,
    body: StartRunRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/runs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorBody | StartRunResponse | None:
    if response.status_code == 200:
        response_200 = StartRunResponse.from_dict(response.json())

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
) -> Response[ErrorBody | StartRunResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartRunRequest,
) -> Response[ErrorBody | StartRunResponse]:
    """Start a new run: a new tree root, or a run that continues an existing tree when parent_run_id
     is set. The run begins executing immediately (status running, started_at stamped); record its
     outcome with CompleteRun.

     Retries are safe with an `idempotency-key` header: repeating the request with the same key
     returns the original run (in whatever state it has reached) instead of starting a second one,
     and reusing a key with a different request fails with `idempotency_conflict`. Without a key,
     every call starts a fresh run.

    Args:
        body (StartRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | StartRunResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: StartRunRequest,
) -> ErrorBody | StartRunResponse | None:
    """Start a new run: a new tree root, or a run that continues an existing tree when parent_run_id
     is set. The run begins executing immediately (status running, started_at stamped); record its
     outcome with CompleteRun.

     Retries are safe with an `idempotency-key` header: repeating the request with the same key
     returns the original run (in whatever state it has reached) instead of starting a second one,
     and reusing a key with a different request fails with `idempotency_conflict`. Without a key,
     every call starts a fresh run.

    Args:
        body (StartRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | StartRunResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartRunRequest,
) -> Response[ErrorBody | StartRunResponse]:
    """Start a new run: a new tree root, or a run that continues an existing tree when parent_run_id
     is set. The run begins executing immediately (status running, started_at stamped); record its
     outcome with CompleteRun.

     Retries are safe with an `idempotency-key` header: repeating the request with the same key
     returns the original run (in whatever state it has reached) instead of starting a second one,
     and reusing a key with a different request fails with `idempotency_conflict`. Without a key,
     every call starts a fresh run.

    Args:
        body (StartRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | StartRunResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StartRunRequest,
) -> ErrorBody | StartRunResponse | None:
    """Start a new run: a new tree root, or a run that continues an existing tree when parent_run_id
     is set. The run begins executing immediately (status running, started_at stamped); record its
     outcome with CompleteRun.

     Retries are safe with an `idempotency-key` header: repeating the request with the same key
     returns the original run (in whatever state it has reached) instead of starting a second one,
     and reusing a key with a different request fails with `idempotency_conflict`. Without a key,
     every call starts a fresh run.

    Args:
        body (StartRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | StartRunResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
