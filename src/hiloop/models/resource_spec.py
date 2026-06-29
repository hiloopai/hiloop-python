from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_spec_architecture import ResourceSpecArchitecture
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceSpec")


@_attrs_define
class ResourceSpec:
    """
    Attributes:
        cpus (int | Unset):
        memory_mb (str | Unset):
        disk_mb (str | Unset):
        architecture (ResourceSpecArchitecture | Unset):
    """

    cpus: int | Unset = UNSET
    memory_mb: str | Unset = UNSET
    disk_mb: str | Unset = UNSET
    architecture: ResourceSpecArchitecture | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpus = self.cpus

        memory_mb = self.memory_mb

        disk_mb = self.disk_mb

        architecture: str | Unset = UNSET
        if not isinstance(self.architecture, Unset):
            architecture = self.architecture.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if memory_mb is not UNSET:
            field_dict["memoryMb"] = memory_mb
        if disk_mb is not UNSET:
            field_dict["diskMb"] = disk_mb
        if architecture is not UNSET:
            field_dict["architecture"] = architecture

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpus = d.pop("cpus", UNSET)

        memory_mb = d.pop("memoryMb", UNSET)

        disk_mb = d.pop("diskMb", UNSET)

        _architecture = d.pop("architecture", UNSET)
        architecture: ResourceSpecArchitecture | Unset
        if isinstance(_architecture, Unset):
            architecture = UNSET
        else:
            architecture = ResourceSpecArchitecture(_architecture)

        resource_spec = cls(
            cpus=cpus,
            memory_mb=memory_mb,
            disk_mb=disk_mb,
            architecture=architecture,
        )

        resource_spec.additional_properties = d
        return resource_spec

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
