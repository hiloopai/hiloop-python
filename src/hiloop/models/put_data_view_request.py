from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_data_view_request_spec import PutDataViewRequestSpec


T = TypeVar("T", bound="PutDataViewRequest")


@_attrs_define
class PutDataViewRequest:
    """Create or replace a data view by name (upsert). The path `{name}` is authoritative; a `name` inside
    the body is ignored.

       Attributes:
           name (str | Unset): The view name (per-tenant unique); supplied by the path.
           description (str | Unset): An optional human description.
           spec (PutDataViewRequestSpec | Unset): The data-view spec (opaque JSON, the engine's tagged `DataViewSpec`).
               Compile-validated before
                store.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    spec: PutDataViewRequestSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_data_view_request_spec import PutDataViewRequestSpec

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _spec = d.pop("spec", UNSET)
        spec: PutDataViewRequestSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = PutDataViewRequestSpec.from_dict(_spec)

        put_data_view_request = cls(
            name=name,
            description=description,
            spec=spec,
        )

        put_data_view_request.additional_properties = d
        return put_data_view_request

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
