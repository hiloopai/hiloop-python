from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_body import ErrorBody
from ...models.fork_run_request import ForkRunRequest
from ...models.fork_run_response import ForkRunResponse
from ...types import Response


def _get_kwargs(
    parent_run_id: str,
    *,
    body: ForkRunRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/runs/{parent_run_id}:fork".format(
            parent_run_id=quote(str(parent_run_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorBody | ForkRunResponse | None:
    if response.status_code == 200:
        response_200 = ForkRunResponse.from_dict(response.json())

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
) -> Response[ErrorBody | ForkRunResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    parent_run_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ForkRunRequest,
) -> Response[ErrorBody | ForkRunResponse]:
    """Fork a run: mint a child run that branches from the parent at the given branch point.

     Retries are safe with an `idempotency-key` header: repeating the request with the same key
     returns the original child run instead of minting a second one, and reusing a key with a
     different request fails with `idempotency_conflict`. Without a key, every call mints a fresh
     child run.

    Args:
        parent_run_id (str):
        body (ForkRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ForkRunResponse]
    """

    kwargs = _get_kwargs(
        parent_run_id=parent_run_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    parent_run_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ForkRunRequest,
) -> ErrorBody | ForkRunResponse | None:
    """Fork a run: mint a child run that branches from the parent at the given branch point.

     Retries are safe with an `idempotency-key` header: repeating the request with the same key
     returns the original child run instead of minting a second one, and reusing a key with a
     different request fails with `idempotency_conflict`. Without a key, every call mints a fresh
     child run.

    Args:
        parent_run_id (str):
        body (ForkRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ForkRunResponse
    """

    return sync_detailed(
        parent_run_id=parent_run_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    parent_run_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ForkRunRequest,
) -> Response[ErrorBody | ForkRunResponse]:
    """Fork a run: mint a child run that branches from the parent at the given branch point.

     Retries are safe with an `idempotency-key` header: repeating the request with the same key
     returns the original child run instead of minting a second one, and reusing a key with a
     different request fails with `idempotency_conflict`. Without a key, every call mints a fresh
     child run.

    Args:
        parent_run_id (str):
        body (ForkRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorBody | ForkRunResponse]
    """

    kwargs = _get_kwargs(
        parent_run_id=parent_run_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    parent_run_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ForkRunRequest,
) -> ErrorBody | ForkRunResponse | None:
    """Fork a run: mint a child run that branches from the parent at the given branch point.

     Retries are safe with an `idempotency-key` header: repeating the request with the same key
     returns the original child run instead of minting a second one, and reusing a key with a
     different request fails with `idempotency_conflict`. Without a key, every call mints a fresh
     child run.

    Args:
        parent_run_id (str):
        body (ForkRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorBody | ForkRunResponse
    """

    return (
        await asyncio_detailed(
            parent_run_id=parent_run_id,
            client=client,
            body=body,
        )
    ).parsed
