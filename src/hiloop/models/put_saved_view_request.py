from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutSavedViewRequest")


@_attrs_define
class PutSavedViewRequest:
    """Create or replace a saved view by name (upsert). The path `{name}` is authoritative.

    Attributes:
        name (str | Unset): The view name (per-tenant unique); supplied by the path.
        sql (str | Unset): The view's `SELECT` SQL.
    """

    name: str | Unset = UNSET
    sql: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        sql = self.sql

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if sql is not UNSET:
            field_dict["sql"] = sql

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        sql = d.pop("sql", UNSET)

        put_saved_view_request = cls(
            name=name,
            sql=sql,
        )

        put_saved_view_request.additional_properties = d
        return put_saved_view_request

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
