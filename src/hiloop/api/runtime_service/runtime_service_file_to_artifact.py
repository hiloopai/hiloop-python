from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_to_artifact_request import FileToArtifactRequest
from ...models.file_to_artifact_response import FileToArtifactResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sandbox_id: str,
    *,
    body: FileToArtifactRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sandboxes/{sandbox_id}/files:to-artifact".format(
            sandbox_id=quote(str(sandbox_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FileToArtifactResponse | None:
    if response.status_code == 200:
        response_200 = FileToArtifactResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FileToArtifactResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileToArtifactRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[FileToArtifactResponse]:
    """
    Args:
        sandbox_id (str):
        idempotency_key (str | Unset):
        body (FileToArtifactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileToArtifactResponse]
    """

    kwargs = _get_kwargs(
        sandbox_id=sandbox_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileToArtifactRequest,
    idempotency_key: str | Unset = UNSET,
) -> FileToArtifactResponse | None:
    """
    Args:
        sandbox_id (str):
        idempotency_key (str | Unset):
        body (FileToArtifactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileToArtifactResponse
    """

    return sync_detailed(
        sandbox_id=sandbox_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileToArtifactRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[FileToArtifactResponse]:
    """
    Args:
        sandbox_id (str):
        idempotency_key (str | Unset):
        body (FileToArtifactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileToArtifactResponse]
    """

    kwargs = _get_kwargs(
        sandbox_id=sandbox_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sandbox_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileToArtifactRequest,
    idempotency_key: str | Unset = UNSET,
) -> FileToArtifactResponse | None:
    """
    Args:
        sandbox_id (str):
        idempotency_key (str | Unset):
        body (FileToArtifactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileToArtifactResponse
    """

    return (
        await asyncio_detailed(
            sandbox_id=sandbox_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
