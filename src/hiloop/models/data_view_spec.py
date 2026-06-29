from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DataViewSpec")


@_attrs_define
class DataViewSpec:
    """The structured spec as opaque JSON — the engine's tagged `DataViewSpec` shape (a Query or Rollup
    view: scope + calculations + breakdowns + filters + orders + limit + opaque render config). Carried
    as a Struct so the spec schema lives in ONE place (the engine's serde types); the service never
    re-models it. Re-validated against the current column allowlist on store and on every run, so a
    view referencing a dropped column fails closed with INVALID_ARGUMENT rather than serving a stale
    result.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_view_spec = cls()

        data_view_spec.additional_properties = d
        return data_view_spec

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
