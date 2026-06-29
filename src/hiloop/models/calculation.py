from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calculation_op import CalculationOp
from ..types import UNSET, Unset

T = TypeVar("T", bound="Calculation")


@_attrs_define
class Calculation:
    """
    Attributes:
        op (CalculationOp | Unset):
        column (str | Unset): The column to aggregate. Required for every op except COUNT. A name starting with `$.` is
            a JSON
             path into the event's `attributes_json` (e.g. `$.gen_ai.usage.cost`); the extracted value is
             textual, so only COUNT/MIN/MAX apply to it (an arithmetic op over an extracted field is rejected).
    """

    op: CalculationOp | Unset = UNSET
    column: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        op: str | Unset = UNSET
        if not isinstance(self.op, Unset):
            op = self.op.value

        column = self.column

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if op is not UNSET:
            field_dict["op"] = op
        if column is not UNSET:
            field_dict["column"] = column

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _op = d.pop("op", UNSET)
        op: CalculationOp | Unset
        if isinstance(_op, Unset):
            op = UNSET
        else:
            op = CalculationOp(_op)

        column = d.pop("column", UNSET)

        calculation = cls(
            op=op,
            column=column,
        )

        calculation.additional_properties = d
        return calculation

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
