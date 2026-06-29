from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """A project record (the subset the API returns).

    Attributes:
        id (str | Unset): The project id.
        tenant_id (str | Unset): The tenant the project belongs to (derived from the caller's scope, echoed for
            convenience).
        slug (str | Unset): The project slug — unique within the tenant.
        name (str | Unset): The human-readable project name.
        created_at (str | Unset): When the project was created (RFC 3339).
        version (str | Unset): Optimistic-concurrency version, bumped on every update. Echo it back as the `If-Match`
            request header to make a later update conditional — if the project changed meanwhile the server rejects the
            update with error code `precondition_failed` instead of overwriting.
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        slug = self.slug

        name = self.name

        created_at = self.created_at

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        created_at = d.pop("createdAt", UNSET)

        version = d.pop("version", UNSET)

        project = cls(
            id=id,
            tenant_id=tenant_id,
            slug=slug,
            name=name,
            created_at=created_at,
            version=version,
        )

        project.additional_properties = d
        return project

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
