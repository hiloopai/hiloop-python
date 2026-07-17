from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReservedResources")


@_attrs_define
class ReservedResources:
    """Reserved resources summed over the active runtime instance of each in-use sandbox. These are the
    requested ("reserved") amounts the sandboxes asked for, not measured live utilization.

       Attributes:
           cpus (str | Unset): Total reserved virtual CPUs.
           memory_mb (str | Unset): Total reserved memory in MiB.
           disk_mb (str | Unset): Total reserved root disk in MiB.
           gpus (str | Unset): Total reserved accelerators (e.g. GPUs). Best-effort: counted only for sandboxes whose spec
                requested an accelerator, so a tenant running no accelerator workloads reports zero.
    """

    cpus: str | Unset = UNSET
    memory_mb: str | Unset = UNSET
    disk_mb: str | Unset = UNSET
    gpus: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpus = self.cpus

        memory_mb = self.memory_mb

        disk_mb = self.disk_mb

        gpus = self.gpus

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if memory_mb is not UNSET:
            field_dict["memory_mb"] = memory_mb
        if disk_mb is not UNSET:
            field_dict["disk_mb"] = disk_mb
        if gpus is not UNSET:
            field_dict["gpus"] = gpus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpus = d.pop("cpus", UNSET)

        memory_mb = d.pop("memory_mb", UNSET)

        disk_mb = d.pop("disk_mb", UNSET)

        gpus = d.pop("gpus", UNSET)

        reserved_resources = cls(
            cpus=cpus,
            memory_mb=memory_mb,
            disk_mb=disk_mb,
            gpus=gpus,
        )

        reserved_resources.additional_properties = d
        return reserved_resources

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
