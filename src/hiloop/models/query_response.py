from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_response_rows_item import QueryResponseRowsItem


T = TypeVar("T", bound="QueryResponse")


@_attrs_define
class QueryResponse:
    """
    Attributes:
        rows (list[QueryResponseRowsItem] | Unset): One flat JSON object per result row: column name -> bare scalar
            value, nulls omitted, 64-bit
             integers as decimal strings. For aggregate surfaces the columns are the grouping columns plus
             one per aggregate metric (e.g. "sum_input_tokens"). Reused by the view service.
        columns (list[str] | Unset): The result set's declared column names, in projection order. Present even when a
            column is
             NULL in every row (per-row nulls are omitted), so a selected-but-empty column stays visible.
    """

    rows: list[QueryResponseRowsItem] | Unset = UNSET
    columns: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        columns: list[str] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rows is not UNSET:
            field_dict["rows"] = rows
        if columns is not UNSET:
            field_dict["columns"] = columns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_response_rows_item import QueryResponseRowsItem

        d = dict(src_dict)
        _rows = d.pop("rows", UNSET)
        rows: list[QueryResponseRowsItem] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = QueryResponseRowsItem.from_dict(rows_item_data)

                rows.append(rows_item)

        columns = cast(list[str], d.pop("columns", UNSET))

        query_response = cls(
            rows=rows,
            columns=columns,
        )

        query_response.additional_properties = d
        return query_response

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
