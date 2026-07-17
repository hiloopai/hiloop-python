from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GpuCapability")


@_attrs_define
class GpuCapability:
    """
    Attributes:
        models (list[str] | Unset): Product models the lane can serve, using the same vocabulary as GpuSpec.models.
        max_count (int | Unset): Maximum number of one model that the lane can allocate to one sandbox.
    """

    models: list[str] | Unset = UNSET
    max_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        models: list[str] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models

        max_count = self.max_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if models is not UNSET:
            field_dict["models"] = models
        if max_count is not UNSET:
            field_dict["max_count"] = max_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        models = cast(list[str], d.pop("models", UNSET))

        max_count = d.pop("max_count", UNSET)

        gpu_capability = cls(
            models=models,
            max_count=max_count,
        )

        gpu_capability.additional_properties = d
        return gpu_capability

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
