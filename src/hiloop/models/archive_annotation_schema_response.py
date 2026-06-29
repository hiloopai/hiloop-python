from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation_schema import AnnotationSchema


T = TypeVar("T", bound="ArchiveAnnotationSchemaResponse")


@_attrs_define
class ArchiveAnnotationSchemaResponse:
    """
    Attributes:
        schema (AnnotationSchema | Unset): One registered annotation-schema config: a single immutable, versioned row of
            the registry.
    """

    schema: AnnotationSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.annotation_schema import AnnotationSchema

        d = dict(src_dict)
        _schema = d.pop("schema", UNSET)
        schema: AnnotationSchema | Unset
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = AnnotationSchema.from_dict(_schema)

        archive_annotation_schema_response = cls(
            schema=schema,
        )

        archive_annotation_schema_response.additional_properties = d
        return archive_annotation_schema_response

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
