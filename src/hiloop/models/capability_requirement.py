from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CapabilityRequirement")


@_attrs_define
class CapabilityRequirement:
    """
    Attributes:
        key (str | Unset):
        minimum_support (str | Unset):
        minimum_maturity (str | Unset):
    """

    key: str | Unset = UNSET
    minimum_support: str | Unset = UNSET
    minimum_maturity: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        minimum_support = self.minimum_support

        minimum_maturity = self.minimum_maturity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if minimum_support is not UNSET:
            field_dict["minimum_support"] = minimum_support
        if minimum_maturity is not UNSET:
            field_dict["minimum_maturity"] = minimum_maturity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        minimum_support = d.pop("minimum_support", UNSET)

        minimum_maturity = d.pop("minimum_maturity", UNSET)

        capability_requirement = cls(
            key=key,
            minimum_support=minimum_support,
            minimum_maturity=minimum_maturity,
        )

        capability_requirement.additional_properties = d
        return capability_requirement

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
