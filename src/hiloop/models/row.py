from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.row_columns import RowColumns


T = TypeVar("T", bound="Row")


@_attrs_define
class Row:
    """One result row: column name -> typed value. For aggregations the columns are the breakdown
    columns plus one per calculation (e.g. "p95_cost_usd").

       Attributes:
           columns (RowColumns | Unset):
    """

    columns: RowColumns | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        columns: dict[str, Any] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.row_columns import RowColumns

        d = dict(src_dict)
        _columns = d.pop("columns", UNSET)
        columns: RowColumns | Unset
        if isinstance(_columns, Unset):
            columns = UNSET
        else:
            columns = RowColumns.from_dict(_columns)

        row = cls(
            columns=columns,
        )

        row.additional_properties = d
        return row

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
