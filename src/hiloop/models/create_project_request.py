from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_display_rule import ProjectDisplayRule


T = TypeVar("T", bound="CreateProjectRequest")


@_attrs_define
class CreateProjectRequest:
    """
    Attributes:
        slug (str | Unset): The project slug — unique within the caller's tenant.
        name (str | Unset): The human-readable project name.
        description (str | Unset): An optional user-assigned free-text description (at most 4 KiB). Empty leaves the
            project
             undescribed.
        display (list[ProjectDisplayRule] | Unset): An optional display configuration (at most one rule per schema).
            Empty leaves the project
             unconfigured.
    """

    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    display: list[ProjectDisplayRule] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        description = self.description

        display: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.display, Unset):
            display = []
            for display_item_data in self.display:
                display_item = display_item_data.to_dict()
                display.append(display_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if display is not UNSET:
            field_dict["display"] = display

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_display_rule import ProjectDisplayRule

        d = dict(src_dict)
        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _display = d.pop("display", UNSET)
        display: list[ProjectDisplayRule] | Unset = UNSET
        if _display is not UNSET:
            display = []
            for display_item_data in _display:
                display_item = ProjectDisplayRule.from_dict(display_item_data)

                display.append(display_item)

        create_project_request = cls(
            slug=slug,
            name=name,
            description=description,
            display=display,
        )

        create_project_request.additional_properties = d
        return create_project_request

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
