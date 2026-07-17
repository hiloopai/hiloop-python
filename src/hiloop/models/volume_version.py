from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VolumeVersion")


@_attrs_define
class VolumeVersion:
    """One immutable, committed volume version. The digest of the version's manifest (the canonical
    file listing) is the version's identity: identical content under the same parent always yields
    the same digest, and a version can never change after it is published.

       Attributes:
           volume_id (str | Unset): The volume this version belongs to.
           version_digest (str | Unset): The version's identity: the digest of its manifest (`blake3:<hex>`).
           parent_version_digest (str | Unset): The digest of the version this one was published on top of. Empty for a
               volume's first
                version.
           size_bytes (str | Unset): Total content size in bytes across all files in the version.
           file_count (str | Unset): Number of files in the version.
           created_by (str | Unset): Stable id of the principal that published the version, recorded server-side.
           created_at (str | Unset): When the version was published (RFC 3339).
    """

    volume_id: str | Unset = UNSET
    version_digest: str | Unset = UNSET
    parent_version_digest: str | Unset = UNSET
    size_bytes: str | Unset = UNSET
    file_count: str | Unset = UNSET
    created_by: str | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume_id = self.volume_id

        version_digest = self.version_digest

        parent_version_digest = self.parent_version_digest

        size_bytes = self.size_bytes

        file_count = self.file_count

        created_by = self.created_by

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if volume_id is not UNSET:
            field_dict["volume_id"] = volume_id
        if version_digest is not UNSET:
            field_dict["version_digest"] = version_digest
        if parent_version_digest is not UNSET:
            field_dict["parent_version_digest"] = parent_version_digest
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if file_count is not UNSET:
            field_dict["file_count"] = file_count
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        volume_id = d.pop("volume_id", UNSET)

        version_digest = d.pop("version_digest", UNSET)

        parent_version_digest = d.pop("parent_version_digest", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        file_count = d.pop("file_count", UNSET)

        created_by = d.pop("created_by", UNSET)

        created_at = d.pop("created_at", UNSET)

        volume_version = cls(
            volume_id=volume_id,
            version_digest=version_digest,
            parent_version_digest=parent_version_digest,
            size_bytes=size_bytes,
            file_count=file_count,
            created_by=created_by,
            created_at=created_at,
        )

        volume_version.additional_properties = d
        return volume_version

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
