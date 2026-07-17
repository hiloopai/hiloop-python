from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectDisplayRule")


@_attrs_define
class ProjectDisplayRule:
    """One project display rule: for annotations of one schema, the ordered fields that surfaces show by
    default (for example schema `experiment.v1` with fields `metrics.val_bpb`, `status`).

       Attributes:
           schema (str | Unset): The annotation-schema name the rule applies to. Never empty; a project's display
               configuration
                carries at most one rule per schema.
           fields (list[str] | Unset): The ordered annotation fields to display. Never empty; each entry is a non-blank
               field name.
    """

    schema: str | Unset = UNSET
    fields: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        fields: list[str] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schema is not UNSET:
            field_dict["schema"] = schema
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema = d.pop("schema", UNSET)

        fields = cast(list[str], d.pop("fields", UNSET))

        project_display_rule = cls(
            schema=schema,
            fields=fields,
        )

        project_display_rule.additional_properties = d
        return project_display_rule

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
