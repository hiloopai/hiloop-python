from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishVolumeVersionRequest")


@_attrs_define
class PublishVolumeVersionRequest:
    """
    Attributes:
        volume_id (str | Unset): The volume to publish the version on.
        push_id (str | Unset): The push handle from StartVolumePush, naming the uploaded manifest.
    """

    volume_id: str | Unset = UNSET
    push_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume_id = self.volume_id

        push_id = self.push_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if volume_id is not UNSET:
            field_dict["volume_id"] = volume_id
        if push_id is not UNSET:
            field_dict["push_id"] = push_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        volume_id = d.pop("volume_id", UNSET)

        push_id = d.pop("push_id", UNSET)

        publish_volume_version_request = cls(
            volume_id=volume_id,
            push_id=push_id,
        )

        publish_volume_version_request.additional_properties = d
        return publish_volume_version_request

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
