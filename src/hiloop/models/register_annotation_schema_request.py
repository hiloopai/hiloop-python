from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisterAnnotationSchemaRequest")


@_attrs_define
class RegisterAnnotationSchemaRequest:
    """
    Attributes:
        name (str | Unset): The schema name — unique per tenant across versions. A new registration of an existing name
             creates the next version; an unseen name starts at version 1.
        json_schema (str | Unset): The JSON Schema document (draft 2020-12) as a JSON string. Must be a JSON object.
        description (str | Unset): An optional human-readable description for this version.
    """

    name: str | Unset = UNSET
    json_schema: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        json_schema = self.json_schema

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if json_schema is not UNSET:
            field_dict["jsonSchema"] = json_schema
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        json_schema = d.pop("jsonSchema", UNSET)

        description = d.pop("description", UNSET)

        register_annotation_schema_request = cls(
            name=name,
            json_schema=json_schema,
            description=description,
        )

        register_annotation_schema_request.additional_properties = d
        return register_annotation_schema_request

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
