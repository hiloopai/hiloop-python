from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_view_spec import DataViewSpec


T = TypeVar("T", bound="DataView")


@_attrs_define
class DataView:
    """A structured data view: a named, versioned spec that compiles 1:1 to a safe query.

    Attributes:
        name (str | Unset): The view name, unique within a tenant among non-deleted views.
        description (str | Unset): A human description, surfaced in the console switcher.
        spec (DataViewSpec | Unset): The structured spec as opaque JSON — the engine's tagged `DataViewSpec` shape (a
            Query or Rollup
             view: scope + calculations + breakdowns + filters + orders + limit + opaque render config). Carried
             as a Struct so the spec schema lives in ONE place (the engine's serde types); the service never
             re-models it. Re-validated against the current column allowlist on store and on every run, so a
             view referencing a dropped column fails closed with INVALID_ARGUMENT rather than serving a stale
             result.
        spec_version (str | Unset): Monotonic per-edit version; the store bumps it on each upsert.
        is_builtin (bool | Unset): A seeded starter view (read-only; clone-on-edit per tenant). Customer-authored views
            are false.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    spec: DataViewSpec | Unset = UNSET
    spec_version: str | Unset = UNSET
    is_builtin: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        spec_version = self.spec_version

        is_builtin = self.is_builtin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if spec is not UNSET:
            field_dict["spec"] = spec
        if spec_version is not UNSET:
            field_dict["specVersion"] = spec_version
        if is_builtin is not UNSET:
            field_dict["isBuiltin"] = is_builtin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_view_spec import DataViewSpec

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _spec = d.pop("spec", UNSET)
        spec: DataViewSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = DataViewSpec.from_dict(_spec)

        spec_version = d.pop("specVersion", UNSET)

        is_builtin = d.pop("isBuiltin", UNSET)

        data_view = cls(
            name=name,
            description=description,
            spec=spec,
            spec_version=spec_version,
            is_builtin=is_builtin,
        )

        data_view.additional_properties = d
        return data_view

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
