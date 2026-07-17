from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Lease")


@_attrs_define
class Lease:
    """One acquisition generation of a project-scoped lease.

    Attributes:
        id (str | Unset): The lease id — minted fresh on every successful acquire. Renew and release address this id, so
             it acts as the holder's handle for the current acquisition generation.
        project_id (str | Unset): The project the lease belongs to.
        name (str | Unset): The lease name — unique within the project among live leases.
        holder (str | Unset): Stable id of the principal that acquired the lease — the API key (or user) that performed
            the
             acquire, recorded server-side, never client-supplied. Resolve it to a display name via the
             principals listing.
        acquired_at (str | Unset): When the lease was acquired (RFC 3339).
        renewed_at (str | Unset): When the lease was last renewed (RFC 3339), or empty if it has never been renewed.
        expires_at (str | Unset): When the lease expires (RFC 3339). Renewing extends this; once it lapses the lease is
            expired
             and the name is free to acquire.
    """

    id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    holder: str | Unset = UNSET
    acquired_at: str | Unset = UNSET
    renewed_at: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_id = self.project_id

        name = self.name

        holder = self.holder

        acquired_at = self.acquired_at

        renewed_at = self.renewed_at

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if holder is not UNSET:
            field_dict["holder"] = holder
        if acquired_at is not UNSET:
            field_dict["acquired_at"] = acquired_at
        if renewed_at is not UNSET:
            field_dict["renewed_at"] = renewed_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        project_id = d.pop("project_id", UNSET)

        name = d.pop("name", UNSET)

        holder = d.pop("holder", UNSET)

        acquired_at = d.pop("acquired_at", UNSET)

        renewed_at = d.pop("renewed_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        lease = cls(
            id=id,
            project_id=project_id,
            name=name,
            holder=holder,
            acquired_at=acquired_at,
            renewed_at=renewed_at,
            expires_at=expires_at,
        )

        lease.additional_properties = d
        return lease

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
