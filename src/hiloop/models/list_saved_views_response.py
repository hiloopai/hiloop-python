from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.saved_view import SavedView


T = TypeVar("T", bound="ListSavedViewsResponse")


@_attrs_define
class ListSavedViewsResponse:
    """
    Attributes:
        views (list[SavedView] | Unset): The tenant's saved views, in a stable order (by name).
    """

    views: list[SavedView] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        views: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.views, Unset):
            views = []
            for views_item_data in self.views:
                views_item = views_item_data.to_dict()
                views.append(views_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.saved_view import SavedView

        d = dict(src_dict)
        _views = d.pop("views", UNSET)
        views: list[SavedView] | Unset = UNSET
        if _views is not UNSET:
            views = []
            for views_item_data in _views:
                views_item = SavedView.from_dict(views_item_data)

                views.append(views_item)

        list_saved_views_response = cls(
            views=views,
        )

        list_saved_views_response.additional_properties = d
        return list_saved_views_response

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
