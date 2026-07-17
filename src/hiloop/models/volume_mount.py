from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.volume_mount_mode import VolumeMountMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="VolumeMount")


@_attrs_define
class VolumeMount:
    """Retained wire type for the retired volume-attachment compatibility field. Clean sandbox-cell
    deployments reject it; use WorkspaceRevisionMount.

       Attributes:
           volume (str | Unset): The volume to attach: its name within the sandbox's project, or its id. Required.
           target_path (str | Unset): The absolute path inside the sandbox to mount the volume at. Required.
           mode (VolumeMountMode | Unset): The access mode. Defaults to VOLUME_MODE_RO when unspecified. VOLUME_MODE_RW is
               reserved and
                not yet accepted.
    """

    volume: str | Unset = UNSET
    target_path: str | Unset = UNSET
    mode: VolumeMountMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume = self.volume

        target_path = self.target_path

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if volume is not UNSET:
            field_dict["volume"] = volume
        if target_path is not UNSET:
            field_dict["target_path"] = target_path
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        volume = d.pop("volume", UNSET)

        target_path = d.pop("target_path", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: VolumeMountMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = VolumeMountMode(_mode)

        volume_mount = cls(
            volume=volume,
            target_path=target_path,
            mode=mode,
        )

        volume_mount.additional_properties = d
        return volume_mount

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
