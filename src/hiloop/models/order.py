from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Order")


@_attrs_define
class Order:
    """
    Attributes:
        column (str | Unset): A column name, a `$.`-prefixed JSON path into `attributes_json`, or a calculation alias
            (for an
             aggregate query).
        descending (bool | Unset):
    """

    column: str | Unset = UNSET
    descending: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column = self.column

        descending = self.descending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if column is not UNSET:
            field_dict["column"] = column
        if descending is not UNSET:
            field_dict["descending"] = descending

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column = d.pop("column", UNSET)

        descending = d.pop("descending", UNSET)

        order = cls(
            column=column,
            descending=descending,
        )

        order.additional_properties = d
        return order

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
