from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_annotations_response_annotations_item import ListAnnotationsResponseAnnotationsItem
    from ..models.skipped_annotation import SkippedAnnotation


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
             was event-bounded), and the schema-validated payload as a raw JSON object string under
             `payload_json` — the exact bytes that were annotated (the write-side `payload_json`), so
             payload values of every JSON type, including 64-bit integers, read back unchanged. Row fields
             are encoded canonically: snake_case keys, 64-bit integers as decimal strings, absent fields
             omitted.
        skipped (list[SkippedAnnotation] | Unset): Stored rows this listing could not decode (a legacy or corrupt
            storage shape), one entry per
             skipped row. The readable annotations above still serve in full; a listing that omits rows
             says so here rather than failing outright or dropping them silently. Empty on a healthy store.
        superseded_count (str | Unset): How many stored versions the default latest-wins view hid because a newer write
            shares their
             supersession key. Zero when nothing was superseded, and always zero with `history` (which
             returns every version). A non-zero count means acked writes are stored but not shown here —
             list with `history` to read them all.
    """

    annotations: list[ListAnnotationsResponseAnnotationsItem] | Unset = UNSET
    skipped: list[SkippedAnnotation] | Unset = UNSET
    superseded_count: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        skipped: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skipped, Unset):
            skipped = []
            for skipped_item_data in self.skipped:
                skipped_item = skipped_item_data.to_dict()
                skipped.append(skipped_item)

        superseded_count = self.superseded_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if superseded_count is not UNSET:
            field_dict["superseded_count"] = superseded_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_annotations_response_annotations_item import ListAnnotationsResponseAnnotationsItem
        from ..models.skipped_annotation import SkippedAnnotation

        d = dict(src_dict)
        _annotations = d.pop("annotations", UNSET)
        annotations: list[ListAnnotationsResponseAnnotationsItem] | Unset = UNSET
        if _annotations is not UNSET:
            annotations = []
            for annotations_item_data in _annotations:
                annotations_item = ListAnnotationsResponseAnnotationsItem.from_dict(annotations_item_data)

                annotations.append(annotations_item)

        _skipped = d.pop("skipped", UNSET)
        skipped: list[SkippedAnnotation] | Unset = UNSET
        if _skipped is not UNSET:
            skipped = []
            for skipped_item_data in _skipped:
                skipped_item = SkippedAnnotation.from_dict(skipped_item_data)

                skipped.append(skipped_item)

        superseded_count = d.pop("superseded_count", UNSET)

        list_annotations_response = cls(
            annotations=annotations,
            skipped=skipped,
            superseded_count=superseded_count,
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
