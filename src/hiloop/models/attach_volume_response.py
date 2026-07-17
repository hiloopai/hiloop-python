from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volume_attachment import VolumeAttachment


T = TypeVar("T", bound="AttachVolumeResponse")


@_attrs_define
class AttachVolumeResponse:
    """
    Attributes:
        attachment (VolumeAttachment | Unset): A live volume attachment: a volume mounted into a sandbox at a path,
            pinned to the version the
             attach resolved. The record is the handle a later detach names.
    """

    attachment: VolumeAttachment | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attachment, Unset):
            attachment = self.attachment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachment is not UNSET:
            field_dict["attachment"] = attachment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volume_attachment import VolumeAttachment

        d = dict(src_dict)
        _attachment = d.pop("attachment", UNSET)
        attachment: VolumeAttachment | Unset
        if isinstance(_attachment, Unset):
            attachment = UNSET
        else:
            attachment = VolumeAttachment.from_dict(_attachment)

        attach_volume_response = cls(
            attachment=attachment,
        )

        attach_volume_response.additional_properties = d
        return attach_volume_response

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
