from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_spec_architecture import ResourceSpecArchitecture
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gpu_spec import GpuSpec


T = TypeVar("T", bound="ResourceSpec")


@_attrs_define
class ResourceSpec:
    """
    Attributes:
        cpus (int | Unset): Virtual CPU count. Unset resolves to the deployment default.
        memory_mb (str | Unset): Memory in MiB. Unset resolves to the deployment default.
        disk_mb (str | Unset): Root disk in MiB. Unset resolves to the deployment default.
        architecture (ResourceSpecArchitecture | Unset):
        gpus (GpuSpec | Unset): Requested sandbox resources. A sizing field left unset (or 0) resolves to the
            deployment's
             default sizing for the selected image or runtime profile. An explicitly-set value is honored as
             requested, or the create fails when no node can satisfy it — it is never silently resized.
    """

    cpus: int | Unset = UNSET
    memory_mb: str | Unset = UNSET
    disk_mb: str | Unset = UNSET
    architecture: ResourceSpecArchitecture | Unset = UNSET
    gpus: GpuSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpus = self.cpus

        memory_mb = self.memory_mb

        disk_mb = self.disk_mb

        architecture: str | Unset = UNSET
        if not isinstance(self.architecture, Unset):
            architecture = self.architecture.value

        gpus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpus, Unset):
            gpus = self.gpus.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if memory_mb is not UNSET:
            field_dict["memory_mb"] = memory_mb
        if disk_mb is not UNSET:
            field_dict["disk_mb"] = disk_mb
        if architecture is not UNSET:
            field_dict["architecture"] = architecture
        if gpus is not UNSET:
            field_dict["gpus"] = gpus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gpu_spec import GpuSpec

        d = dict(src_dict)
        cpus = d.pop("cpus", UNSET)

        memory_mb = d.pop("memory_mb", UNSET)

        disk_mb = d.pop("disk_mb", UNSET)

        _architecture = d.pop("architecture", UNSET)
        architecture: ResourceSpecArchitecture | Unset
        if isinstance(_architecture, Unset):
            architecture = UNSET
        else:
            architecture = ResourceSpecArchitecture(_architecture)

        _gpus = d.pop("gpus", UNSET)
        gpus: GpuSpec | Unset
        if isinstance(_gpus, Unset):
            gpus = UNSET
        else:
            gpus = GpuSpec.from_dict(_gpus)

        resource_spec = cls(
            cpus=cpus,
            memory_mb=memory_mb,
            disk_mb=disk_mb,
            architecture=architecture,
            gpus=gpus,
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
