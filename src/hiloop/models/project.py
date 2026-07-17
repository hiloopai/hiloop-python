from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_display_rule import ProjectDisplayRule


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
        run_count (str | Unset): The total number of runs in the project, computed server-side across all of the
            project's runs (not just one page).
        last_run_at (str | Unset): When the most recent run in the project was created (RFC 3339), or empty when the
            project has no runs yet.
        description (str | Unset): User-assigned free-text description (at most 4 KiB). Empty when unset.
        created_by (str | Unset): Stable id of the principal that created the project — the API key (or user) that
            performed the
             create, recorded server-side, never client-supplied. Resolve it to a display name via the
             principals listing. Empty for projects created before attribution was recorded.
        updated_at (str | Unset): When the project was last updated (RFC 3339). Equal to created_at until the first
            update.
        display (list[ProjectDisplayRule] | Unset): The project's display configuration: for each annotation schema, the
            ordered fields that
             surfaces (run trees, consoles) show by default. Empty when unconfigured.
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    version: str | Unset = UNSET
    run_count: str | Unset = UNSET
    last_run_at: str | Unset = UNSET
    description: str | Unset = UNSET
    created_by: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    display: list[ProjectDisplayRule] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        slug = self.slug

        name = self.name

        created_at = self.created_at

        version = self.version

        run_count = self.run_count

        last_run_at = self.last_run_at

        description = self.description

        created_by = self.created_by

        updated_at = self.updated_at

        display: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.display, Unset):
            display = []
            for display_item_data in self.display:
                display_item = display_item_data.to_dict()
                display.append(display_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if version is not UNSET:
            field_dict["version"] = version
        if run_count is not UNSET:
            field_dict["run_count"] = run_count
        if last_run_at is not UNSET:
            field_dict["last_run_at"] = last_run_at
        if description is not UNSET:
            field_dict["description"] = description
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if display is not UNSET:
            field_dict["display"] = display

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_display_rule import ProjectDisplayRule

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        created_at = d.pop("created_at", UNSET)

        version = d.pop("version", UNSET)

        run_count = d.pop("run_count", UNSET)

        last_run_at = d.pop("last_run_at", UNSET)

        description = d.pop("description", UNSET)

        created_by = d.pop("created_by", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _display = d.pop("display", UNSET)
        display: list[ProjectDisplayRule] | Unset = UNSET
        if _display is not UNSET:
            display = []
            for display_item_data in _display:
                display_item = ProjectDisplayRule.from_dict(display_item_data)

                display.append(display_item)

        project = cls(
            id=id,
            tenant_id=tenant_id,
            slug=slug,
            name=name,
            created_at=created_at,
            version=version,
            run_count=run_count,
            last_run_at=last_run_at,
            description=description,
            created_by=created_by,
            updated_at=updated_at,
            display=display,
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
