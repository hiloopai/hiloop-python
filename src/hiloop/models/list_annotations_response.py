from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_annotations_response_annotations_item import ListAnnotationsResponseAnnotationsItem


T = TypeVar("T", bound="ListAnnotationsResponse")


@_attrs_define
class ListAnnotationsResponse:
    """
    Attributes:
        annotations (list[ListAnnotationsResponseAnnotationsItem] | Unset): One annotation per row, newest first. Each
            row carries the annotation's identity and anchor
             (`event_id`, `run_id` — absent on project-scoped rows — `project_id`, `lineage_path`, the
             schema `name`, `ts_wall_ns`, `principal`), its target (`target_event_id`, or the range bounds
             `range_start_ns`/`range_end_ns` plus `range_start_event_id`/`range_end_event_id` when the range
             was event-bounded), and the schema-validated payload under `payload`. Encoded canonically:
             snake_case keys, 64-bit integers as decimal strings, absent fields omitted.
    """

    annotations: list[ListAnnotationsResponseAnnotationsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_annotations_response_annotations_item import ListAnnotationsResponseAnnotationsItem

        d = dict(src_dict)
        _annotations = d.pop("annotations", UNSET)
        annotations: list[ListAnnotationsResponseAnnotationsItem] | Unset = UNSET
        if _annotations is not UNSET:
            annotations = []
            for annotations_item_data in _annotations:
                annotations_item = ListAnnotationsResponseAnnotationsItem.from_dict(annotations_item_data)

                annotations.append(annotations_item)

        list_annotations_response = cls(
            annotations=annotations,
        )

        list_annotations_response.additional_properties = d
        return list_annotations_response

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
