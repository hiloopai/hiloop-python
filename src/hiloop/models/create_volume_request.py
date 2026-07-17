from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateVolumeRequest")


@_attrs_define
class CreateVolumeRequest:
    """
    Attributes:
        project_id (str | Unset): The project the volume belongs to.
        name (str | Unset): The volume name — unique within the project (letters, digits, dots, dashes, underscores; at
             most 100 characters).
        description (str | Unset): An optional user-assigned free-text description (at most 4 KiB). Empty leaves the
            volume
             undescribed.
        quota_bytes (str | Unset): Storage quota in bytes (required). A quota, not an allocation; at most 2 TiB per
            volume.
    """

    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    quota_bytes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        name = self.name

        description = self.description

        quota_bytes = self.quota_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if quota_bytes is not UNSET:
            field_dict["quota_bytes"] = quota_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        quota_bytes = d.pop("quota_bytes", UNSET)

        create_volume_request = cls(
            project_id=project_id,
            name=name,
            description=description,
            quota_bytes=quota_bytes,
        )

        create_volume_request.additional_properties = d
        return create_volume_request

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
