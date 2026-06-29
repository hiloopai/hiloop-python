from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation_schema import AnnotationSchema


T = TypeVar("T", bound="ListAnnotationSchemasResponse")


@_attrs_define
class ListAnnotationSchemasResponse:
    """
    Attributes:
        schemas (list[AnnotationSchema] | Unset): The configs in the caller's tenant. By default the latest live version
            per name; with
             include_archived, every version, newest first.
    """

    schemas: list[AnnotationSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schemas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.schemas, Unset):
            schemas = []
            for schemas_item_data in self.schemas:
                schemas_item = schemas_item_data.to_dict()
                schemas.append(schemas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schemas is not UNSET:
            field_dict["schemas"] = schemas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.annotation_schema import AnnotationSchema

        d = dict(src_dict)
        _schemas = d.pop("schemas", UNSET)
        schemas: list[AnnotationSchema] | Unset = UNSET
        if _schemas is not UNSET:
            schemas = []
            for schemas_item_data in _schemas:
                schemas_item = AnnotationSchema.from_dict(schemas_item_data)

                schemas.append(schemas_item)

        list_annotation_schemas_response = cls(
            schemas=schemas,
        )

        list_annotation_schemas_response.additional_properties = d
        return list_annotation_schemas_response

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
