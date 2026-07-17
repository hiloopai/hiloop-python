from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxSecret")


@_attrs_define
class SandboxSecret:
    """A sandbox-secret record — metadata only, never the value.

    Attributes:
        id (str | Unset): The secret id.
        name (str | Unset): The human-readable secret name — unique within the tenant. The sandbox spec references it by
            name.
        kind (str | Unset): What kind of credential the secret holds for future cell-owned injection: `api_key`,
            `bearer`,
             `basic`, or `custom`.
        dest_host (str | Unset): Intended outbound host for future native injection (empty for an unbound secret).
        dest_header (str | Unset): Intended header for future native injection (empty when the kind implies it).
        scheme (str | Unset): The auth scheme prefix (e.g. `Bearer`), when applicable.
        current_version (str | Unset): The current version number. Incremented on each rotation; 0 before the first
            value is set.
        created_at (str | Unset): When the secret was created (RFC 3339).
        rotated_at (str | Unset): When the secret was last rotated, if ever (RFC 3339).
        expires_at (str | Unset): When the secret expires, if an expiry is set (RFC 3339).
        revoked_at (str | Unset): When the secret was revoked, if it has been (RFC 3339). A revoked secret resolves to
            nothing.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    kind: str | Unset = UNSET
    dest_host: str | Unset = UNSET
    dest_header: str | Unset = UNSET
    scheme: str | Unset = UNSET
    current_version: str | Unset = UNSET
    created_at: str | Unset = UNSET
    rotated_at: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    revoked_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        kind = self.kind

        dest_host = self.dest_host

        dest_header = self.dest_header

        scheme = self.scheme

        current_version = self.current_version

        created_at = self.created_at

        rotated_at = self.rotated_at

        expires_at = self.expires_at

        revoked_at = self.revoked_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if dest_host is not UNSET:
            field_dict["dest_host"] = dest_host
        if dest_header is not UNSET:
            field_dict["dest_header"] = dest_header
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if current_version is not UNSET:
            field_dict["current_version"] = current_version
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if rotated_at is not UNSET:
            field_dict["rotated_at"] = rotated_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        kind = d.pop("kind", UNSET)

        dest_host = d.pop("dest_host", UNSET)

        dest_header = d.pop("dest_header", UNSET)

        scheme = d.pop("scheme", UNSET)

        current_version = d.pop("current_version", UNSET)

        created_at = d.pop("created_at", UNSET)

        rotated_at = d.pop("rotated_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        revoked_at = d.pop("revoked_at", UNSET)

        sandbox_secret = cls(
            id=id,
            name=name,
            kind=kind,
            dest_host=dest_host,
            dest_header=dest_header,
            scheme=scheme,
            current_version=current_version,
            created_at=created_at,
            rotated_at=rotated_at,
            expires_at=expires_at,
            revoked_at=revoked_at,
        )

        sandbox_secret.additional_properties = d
        return sandbox_secret

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
