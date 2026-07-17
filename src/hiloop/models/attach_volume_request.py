from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachVolumeRequest")


@_attrs_define
class AttachVolumeRequest:
    """
    Attributes:
        volume_id (str | Unset): The volume to attach, by id, within the caller's tenant.
        sandbox_id (str | Unset): The sandbox to mount the volume into. It must share the volume's project.
        target_path (str | Unset): The absolute path inside the sandbox to mount the volume at.
    """

    volume_id: str | Unset = UNSET
    sandbox_id: str | Unset = UNSET
    target_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume_id = self.volume_id

        sandbox_id = self.sandbox_id

        target_path = self.target_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if volume_id is not UNSET:
            field_dict["volume_id"] = volume_id
        if sandbox_id is not UNSET:
            field_dict["sandbox_id"] = sandbox_id
        if target_path is not UNSET:
            field_dict["target_path"] = target_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        volume_id = d.pop("volume_id", UNSET)

        sandbox_id = d.pop("sandbox_id", UNSET)

        target_path = d.pop("target_path", UNSET)

        attach_volume_request = cls(
            volume_id=volume_id,
            sandbox_id=sandbox_id,
            target_path=target_path,
        )

        attach_volume_request.additional_properties = d
        return attach_volume_request

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
