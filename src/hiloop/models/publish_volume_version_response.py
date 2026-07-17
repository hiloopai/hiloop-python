from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volume_version import VolumeVersion


T = TypeVar("T", bound="PublishVolumeVersionResponse")


@_attrs_define
class PublishVolumeVersionResponse:
    """
    Attributes:
        version (VolumeVersion | Unset): One immutable, committed volume version. The digest of the version's manifest
            (the canonical
             file listing) is the version's identity: identical content under the same parent always yields
             the same digest, and a version can never change after it is published.
    """

    version: VolumeVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volume_version import VolumeVersion

        d = dict(src_dict)
        _version = d.pop("version", UNSET)
        version: VolumeVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = VolumeVersion.from_dict(_version)

        publish_volume_version_response = cls(
            version=version,
        )

        publish_volume_version_response.additional_properties = d
        return publish_volume_version_response

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
