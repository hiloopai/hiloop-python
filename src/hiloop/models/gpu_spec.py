from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GpuSpec")


@_attrs_define
class GpuSpec:
    """Requested sandbox resources. A sizing field left unset (or 0) resolves to the deployment's
    default sizing for the selected image or runtime profile. An explicitly-set value is honored as
    requested, or the create fails when no node can satisfy it — it is never silently resized.

       Attributes:
           count (int | Unset): Number of accelerators. Zero means no accelerator request.
           models (list[str] | Unset): Acceptable product models in preference order. Empty accepts any advertised model.
    """

    count: int | Unset = UNSET
    models: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        models: list[str] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if models is not UNSET:
            field_dict["models"] = models

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        models = cast(list[str], d.pop("models", UNSET))

        gpu_spec = cls(
            count=count,
            models=models,
        )

        gpu_spec.additional_properties = d
        return gpu_spec

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
