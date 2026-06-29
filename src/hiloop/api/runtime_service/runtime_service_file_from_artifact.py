from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_from_artifact_request import FileFromArtifactRequest
from ...models.file_from_artifact_response import FileFromArtifactResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sandbox_id: str,
    *,
    body: FileFromArtifactRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/sandboxes/{sandbox_id}/files:from-artifact".format(
            sandbox_id=quote(str(sandbox_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileFromArtifactResponse | None:
    if response.status_code == 200:
        response_200 = FileFromArtifactResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FileFromArtifactResponse]:
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
    body: FileFromArtifactRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[FileFromArtifactResponse]:
    """
    Args:
        sandbox_id (str):
        idempotency_key (str | Unset):
        body (FileFromArtifactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileFromArtifactResponse]
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
    body: FileFromArtifactRequest,
    idempotency_key: str | Unset = UNSET,
) -> FileFromArtifactResponse | None:
    """
    Args:
        sandbox_id (str):
        idempotency_key (str | Unset):
        body (FileFromArtifactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileFromArtifactResponse
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
    body: FileFromArtifactRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[FileFromArtifactResponse]:
    """
    Args:
        sandbox_id (str):
        idempotency_key (str | Unset):
        body (FileFromArtifactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileFromArtifactResponse]
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
    body: FileFromArtifactRequest,
    idempotency_key: str | Unset = UNSET,
) -> FileFromArtifactResponse | None:
    """
    Args:
        sandbox_id (str):
        idempotency_key (str | Unset):
        body (FileFromArtifactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileFromArtifactResponse
    """

    return (
        await asyncio_detailed(
            sandbox_id=sandbox_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
