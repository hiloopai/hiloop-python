from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.binding_impact import BindingImpact


T = TypeVar("T", bound="PreviewBaselineImpactResponse")


@_attrs_define
class PreviewBaselineImpactResponse:
    """
    Attributes:
        changes (list[BindingImpact] | Unset): One entry per selector whose effective policy would change under the
            proposed baseline (selectors
             with no change are omitted). Empty when the proposed baseline changes nothing.
    """

    changes: list[BindingImpact] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = []
            for changes_item_data in self.changes:
                changes_item = changes_item_data.to_dict()
                changes.append(changes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.binding_impact import BindingImpact

        d = dict(src_dict)
        _changes = d.pop("changes", UNSET)
        changes: list[BindingImpact] | Unset = UNSET
        if _changes is not UNSET:
            changes = []
            for changes_item_data in _changes:
                changes_item = BindingImpact.from_dict(changes_item_data)

                changes.append(changes_item)

        preview_baseline_impact_response = cls(
            changes=changes,
        )

        preview_baseline_impact_response.additional_properties = d
        return preview_baseline_impact_response

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
