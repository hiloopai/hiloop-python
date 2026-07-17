from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox import Sandbox


T = TypeVar("T", bound="ListSandboxesResponse")


@_attrs_define
class ListSandboxesResponse:
    """
    Attributes:
        sandboxes (list[Sandbox] | Unset): The sandboxes on this page, newest first.
        next_page_token (str | Unset): The token to pass as page_token to fetch the next page. Empty when there are no
            more results.
    """

    sandboxes: list[Sandbox] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandboxes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sandboxes, Unset):
            sandboxes = []
            for sandboxes_item_data in self.sandboxes:
                sandboxes_item = sandboxes_item_data.to_dict()
                sandboxes.append(sandboxes_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sandboxes is not UNSET:
            field_dict["sandboxes"] = sandboxes
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox import Sandbox

        d = dict(src_dict)
        _sandboxes = d.pop("sandboxes", UNSET)
        sandboxes: list[Sandbox] | Unset = UNSET
        if _sandboxes is not UNSET:
            sandboxes = []
            for sandboxes_item_data in _sandboxes:
                sandboxes_item = Sandbox.from_dict(sandboxes_item_data)

                sandboxes.append(sandboxes_item)

        next_page_token = d.pop("next_page_token", UNSET)

        list_sandboxes_response = cls(
            sandboxes=sandboxes,
            next_page_token=next_page_token,
        )

        list_sandboxes_response.additional_properties = d
        return list_sandboxes_response

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
