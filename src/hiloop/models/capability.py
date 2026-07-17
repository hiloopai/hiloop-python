from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gpu_capability import GpuCapability


T = TypeVar("T", bound="Capability")


@_attrs_define
class Capability:
    """
    Attributes:
        key (str | Unset):
        support (str | Unset):
        maturity (str | Unset):
        gpu (GpuCapability | Unset):
    """

    key: str | Unset = UNSET
    support: str | Unset = UNSET
    maturity: str | Unset = UNSET
    gpu: GpuCapability | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        support = self.support

        maturity = self.maturity

        gpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpu, Unset):
            gpu = self.gpu.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if support is not UNSET:
            field_dict["support"] = support
        if maturity is not UNSET:
            field_dict["maturity"] = maturity
        if gpu is not UNSET:
            field_dict["gpu"] = gpu

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gpu_capability import GpuCapability

        d = dict(src_dict)
        key = d.pop("key", UNSET)

        support = d.pop("support", UNSET)

        maturity = d.pop("maturity", UNSET)

        _gpu = d.pop("gpu", UNSET)
        gpu: GpuCapability | Unset
        if isinstance(_gpu, Unset):
            gpu = UNSET
        else:
            gpu = GpuCapability.from_dict(_gpu)

        capability = cls(
            key=key,
            support=support,
            maturity=maturity,
            gpu=gpu,
        )

        capability.additional_properties = d
        return capability

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
