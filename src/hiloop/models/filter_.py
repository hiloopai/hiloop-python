from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_op import FilterOp
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute_value import AttributeValue


T = TypeVar("T", bound="Filter")


@_attrs_define
class Filter:
    """
    Attributes:
        column (str | Unset): A column name, or a `$.`-prefixed JSON path into `attributes_json` (e.g.
             `$.gen_ai.request.temperature`). Extracted JSON values are textual: EQ/NE/CONTAINS/EXISTS apply.
        op (FilterOp | Unset):
        value (AttributeValue | Unset): A typed scalar attribute value (mirrors the Event v1 narrow value model).
    """

    column: str | Unset = UNSET
    op: FilterOp | Unset = UNSET
    value: AttributeValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column = self.column

        op: str | Unset = UNSET
        if not isinstance(self.op, Unset):
            op = self.op.value

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if column is not UNSET:
            field_dict["column"] = column
        if op is not UNSET:
            field_dict["op"] = op
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_value import AttributeValue

        d = dict(src_dict)
        column = d.pop("column", UNSET)

        _op = d.pop("op", UNSET)
        op: FilterOp | Unset
        if isinstance(_op, Unset):
            op = UNSET
        else:
            op = FilterOp(_op)

        _value = d.pop("value", UNSET)
        value: AttributeValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = AttributeValue.from_dict(_value)

        filter_ = cls(
            column=column,
            op=op,
            value=value,
        )

        filter_.additional_properties = d
        return filter_

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
