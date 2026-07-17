from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Volume")


@_attrs_define
class Volume:
    """A volume record (the subset the API returns).

    Attributes:
        id (str | Unset): The volume id.
        tenant_id (str | Unset): The tenant the volume belongs to (derived from the caller's scope, echoed for
            convenience).
        project_id (str | Unset): The project the volume belongs to.
        name (str | Unset): The volume name — unique within its project. Sandboxes attach a volume by this name, so it
            is
             limited to letters, digits, dots, dashes, and underscores (at most 100 characters).
        description (str | Unset): User-assigned free-text description (at most 4 KiB). Empty when unset.
        quota_bytes (str | Unset): Storage quota in bytes: the cap on the volume's total committed size. A quota, not an
             allocation — an empty volume consumes no storage.
        current_version_digest (str | Unset): Digest of the volume's current (latest committed) version. Empty until the
            first push
             publishes a version.
        created_by (str | Unset): Stable id of the principal that created the volume — the API key (or user) that
            performed the
             create, recorded server-side. Resolve it to a display name via the principals listing.
        created_at (str | Unset): When the volume was created (RFC 3339).
        updated_at (str | Unset): When the volume record was last updated (RFC 3339). Equal to created_at until the
            first
             update.
        used_bytes (str | Unset): Committed storage in bytes: the total size of the distinct content blobs referenced by
            the
             volume's versions. Content is stored deduplicated, so a blob shared by several versions
             counts once — this is what the volume's committed content occupies, not the sum of its
             versions' sizes. Zero for a volume with no committed versions.
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    quota_bytes: str | Unset = UNSET
    current_version_digest: str | Unset = UNSET
    created_by: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    used_bytes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        project_id = self.project_id

        name = self.name

        description = self.description

        quota_bytes = self.quota_bytes

        current_version_digest = self.current_version_digest

        created_by = self.created_by

        created_at = self.created_at

        updated_at = self.updated_at

        used_bytes = self.used_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if quota_bytes is not UNSET:
            field_dict["quota_bytes"] = quota_bytes
        if current_version_digest is not UNSET:
            field_dict["current_version_digest"] = current_version_digest
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if used_bytes is not UNSET:
            field_dict["used_bytes"] = used_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        project_id = d.pop("project_id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        quota_bytes = d.pop("quota_bytes", UNSET)

        current_version_digest = d.pop("current_version_digest", UNSET)

        created_by = d.pop("created_by", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        used_bytes = d.pop("used_bytes", UNSET)

        volume = cls(
            id=id,
            tenant_id=tenant_id,
            project_id=project_id,
            name=name,
            description=description,
            quota_bytes=quota_bytes,
            current_version_digest=current_version_digest,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            used_bytes=used_bytes,
        )

        volume.additional_properties = d
        return volume

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
