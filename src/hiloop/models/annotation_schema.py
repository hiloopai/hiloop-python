from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.promoted_field import PromotedField


T = TypeVar("T", bound="AnnotationSchema")


@_attrs_define
class AnnotationSchema:
    """One registered annotation-schema config: a single immutable, versioned row of the registry.

    Attributes:
        id (str | Unset): The config id.
        tenant_id (str | Unset): The tenant the config belongs to (derived from the caller's scope, echoed for
            convenience).
        name (str | Unset): The schema name — unique per tenant across versions (the registered name an annotation
            names).
        version (str | Unset): The monotonic version within (tenant, name). The first registration is 1.
        description (str | Unset): An optional human-readable description.
        json_schema (str | Unset): The JSON Schema document (draft 2020-12) as a JSON string.
        archived_at (str | Unset): When the config was archived (RFC 3339), or empty if it is still live.
        created_at (str | Unset): When the config version was created (RFC 3339).
        promoted_fields (list[PromotedField] | Unset): The fields this schema promotes from the payload into typed
            columns, each with its server-assigned
             slot. Empty when the schema promotes nothing.
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    name: str | Unset = UNSET
    version: str | Unset = UNSET
    description: str | Unset = UNSET
    json_schema: str | Unset = UNSET
    archived_at: str | Unset = UNSET
    created_at: str | Unset = UNSET
    promoted_fields: list[PromotedField] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        name = self.name

        version = self.version

        description = self.description

        json_schema = self.json_schema

        archived_at = self.archived_at

        created_at = self.created_at

        promoted_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.promoted_fields, Unset):
            promoted_fields = []
            for promoted_fields_item_data in self.promoted_fields:
                promoted_fields_item = promoted_fields_item_data.to_dict()
                promoted_fields.append(promoted_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if description is not UNSET:
            field_dict["description"] = description
        if json_schema is not UNSET:
            field_dict["json_schema"] = json_schema
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if promoted_fields is not UNSET:
            field_dict["promoted_fields"] = promoted_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promoted_field import PromotedField

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        description = d.pop("description", UNSET)

        json_schema = d.pop("json_schema", UNSET)

        archived_at = d.pop("archived_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        _promoted_fields = d.pop("promoted_fields", UNSET)
        promoted_fields: list[PromotedField] | Unset = UNSET
        if _promoted_fields is not UNSET:
            promoted_fields = []
            for promoted_fields_item_data in _promoted_fields:
                promoted_fields_item = PromotedField.from_dict(promoted_fields_item_data)

                promoted_fields.append(promoted_fields_item)

        annotation_schema = cls(
            id=id,
            tenant_id=tenant_id,
            name=name,
            version=version,
            description=description,
            json_schema=json_schema,
            archived_at=archived_at,
            created_at=created_at,
            promoted_fields=promoted_fields,
        )

        annotation_schema.additional_properties = d
        return annotation_schema

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
