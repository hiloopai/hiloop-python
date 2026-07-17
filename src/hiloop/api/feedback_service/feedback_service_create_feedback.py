from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_feedback_request import CreateFeedbackRequest
from ...models.create_feedback_response import CreateFeedbackResponse
from ...models.error_body import ErrorBody
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFeedbackRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/feedback",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateFeedbackResponse | ErrorBody | None:
    if response.status_code == 200:
        response_200 = CreateFeedbackResponse.from_dict(response.json())

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
) -> Response[CreateFeedbackResponse | ErrorBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFeedbackRequest,
) -> Response[CreateFeedbackResponse | ErrorBody]:
    """Submit a bug report or product feedback. The report is persisted first and then surfaced to
     the hiloop team; a delivery problem on the surfacing side never fails the request. Repeat
     submissions with the same fingerprint (supplied, or content-derived when omitted) return the
     original report instead of storing a duplicate, so retries are safe.

    Args:
        body (CreateFeedbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFeedbackResponse | ErrorBody]
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
    body: CreateFeedbackRequest,
) -> CreateFeedbackResponse | ErrorBody | None:
    """Submit a bug report or product feedback. The report is persisted first and then surfaced to
     the hiloop team; a delivery problem on the surfacing side never fails the request. Repeat
     submissions with the same fingerprint (supplied, or content-derived when omitted) return the
     original report instead of storing a duplicate, so retries are safe.

    Args:
        body (CreateFeedbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFeedbackResponse | ErrorBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFeedbackRequest,
) -> Response[CreateFeedbackResponse | ErrorBody]:
    """Submit a bug report or product feedback. The report is persisted first and then surfaced to
     the hiloop team; a delivery problem on the surfacing side never fails the request. Repeat
     submissions with the same fingerprint (supplied, or content-derived when omitted) return the
     original report instead of storing a duplicate, so retries are safe.

    Args:
        body (CreateFeedbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFeedbackResponse | ErrorBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFeedbackRequest,
) -> CreateFeedbackResponse | ErrorBody | None:
    """Submit a bug report or product feedback. The report is persisted first and then surfaced to
     the hiloop team; a delivery problem on the surfacing side never fails the request. Repeat
     submissions with the same fingerprint (supplied, or content-derived when omitted) return the
     original report instead of storing a duplicate, so retries are safe.

    Args:
        body (CreateFeedbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFeedbackResponse | ErrorBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
