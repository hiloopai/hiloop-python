from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrefetchVolumeRequest")


@_attrs_define
class PrefetchVolumeRequest:
    """
    Attributes:
        volume_id (str | Unset): The volume whose content to pre-warm, by id, within the caller's tenant.
        version_digest (str | Unset): The version to pre-warm (`blake3:<hex>`). Empty pre-warms the volume's current
            (latest
             committed) version.
    """

    volume_id: str | Unset = UNSET
    version_digest: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume_id = self.volume_id

        version_digest = self.version_digest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if volume_id is not UNSET:
            field_dict["volume_id"] = volume_id
        if version_digest is not UNSET:
            field_dict["version_digest"] = version_digest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        volume_id = d.pop("volume_id", UNSET)

        version_digest = d.pop("version_digest", UNSET)

        prefetch_volume_request = cls(
            volume_id=volume_id,
            version_digest=version_digest,
        )

        prefetch_volume_request.additional_properties = d
        return prefetch_volume_request

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
