from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttributeValue")


@_attrs_define
class AttributeValue:
    """A typed scalar attribute value (mirrors the Event v1 narrow value model).

    Attributes:
        string_value (str | Unset):
        int_value (str | Unset):
        double_value (float | Unset):
        bool_value (bool | Unset):
    """

    string_value: str | Unset = UNSET
    int_value: str | Unset = UNSET
    double_value: float | Unset = UNSET
    bool_value: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        string_value = self.string_value

        int_value = self.int_value

        double_value = self.double_value

        bool_value = self.bool_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value
        if int_value is not UNSET:
            field_dict["intValue"] = int_value
        if double_value is not UNSET:
            field_dict["doubleValue"] = double_value
        if bool_value is not UNSET:
            field_dict["boolValue"] = bool_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        string_value = d.pop("stringValue", UNSET)

        int_value = d.pop("intValue", UNSET)

        double_value = d.pop("doubleValue", UNSET)

        bool_value = d.pop("boolValue", UNSET)

        attribute_value = cls(
            string_value=string_value,
            int_value=int_value,
            double_value=double_value,
            bool_value=bool_value,
        )

        attribute_value.additional_properties = d
        return attribute_value

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
