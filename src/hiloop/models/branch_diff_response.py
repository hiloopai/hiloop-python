from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.branch_diff_response_rows_item import BranchDiffResponseRowsItem


T = TypeVar("T", bound="BranchDiffResponse")


@_attrs_define
class BranchDiffResponse:
    """
    Attributes:
        rows (list[BranchDiffResponseRowsItem] | Unset): Events present in run A but not in run B, projected to the diff
            key columns (one flat JSON
             object per row, same canonical row encoding as QueryResponse).
    """

    rows: list[BranchDiffResponseRowsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.branch_diff_response_rows_item import BranchDiffResponseRowsItem

        d = dict(src_dict)
        _rows = d.pop("rows", UNSET)
        rows: list[BranchDiffResponseRowsItem] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = BranchDiffResponseRowsItem.from_dict(rows_item_data)

                rows.append(rows_item)

        branch_diff_response = cls(
            rows=rows,
        )

        branch_diff_response.additional_properties = d
        return branch_diff_response

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
