from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnotateRangeRequest")


@_attrs_define
class AnnotateRangeRequest:
    """A range annotation spanning a window within a run (rather than a single target event). The window
    is either a pair of wall-clock nanosecond bounds or a pair of event ids whose recorded timestamps
    become the bounds — supply exactly one form.

       Attributes:
           run_id (str | Unset): The run (session) the annotation belongs to.
           schema_name (str | Unset): The registered annotation-schema name the payload validates against (the event
               `name`).
           range_start_ns (str | Unset): Inclusive start of the annotated window, in wall-clock nanoseconds. Mutually
               exclusive with the
                event-pair form.
           range_end_ns (str | Unset): Inclusive end of the annotated window, in wall-clock nanoseconds. Mutually exclusive
               with the
                event-pair form.
           payload_json (str | Unset): The annotation payload as a JSON object string; validated against `schema_name`'s
               registered
                JSON Schema at ingest. Reserved `hiloop.annotation.*` keys are platform-owned and excluded.
           range_start_event_id (str | Unset): The `event_id` whose recorded timestamp starts the annotated window. Both
               event endpoints must
                exist in `run_id`; the window bounds are materialized from their timestamps. Set together with
                `range_end_event_id`, and not alongside the nanosecond bounds.
           range_end_event_id (str | Unset): The `event_id` whose recorded timestamp ends the annotated window. Set
               together with
                `range_start_event_id`, and not alongside the nanosecond bounds.
    """

    run_id: str | Unset = UNSET
    schema_name: str | Unset = UNSET
    range_start_ns: str | Unset = UNSET
    range_end_ns: str | Unset = UNSET
    payload_json: str | Unset = UNSET
    range_start_event_id: str | Unset = UNSET
    range_end_event_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        schema_name = self.schema_name

        range_start_ns = self.range_start_ns

        range_end_ns = self.range_end_ns

        payload_json = self.payload_json

        range_start_event_id = self.range_start_event_id

        range_end_event_id = self.range_end_event_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if schema_name is not UNSET:
            field_dict["schemaName"] = schema_name
        if range_start_ns is not UNSET:
            field_dict["rangeStartNs"] = range_start_ns
        if range_end_ns is not UNSET:
            field_dict["rangeEndNs"] = range_end_ns
        if payload_json is not UNSET:
            field_dict["payloadJson"] = payload_json
        if range_start_event_id is not UNSET:
            field_dict["rangeStartEventId"] = range_start_event_id
        if range_end_event_id is not UNSET:
            field_dict["rangeEndEventId"] = range_end_event_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId", UNSET)

        schema_name = d.pop("schemaName", UNSET)

        range_start_ns = d.pop("rangeStartNs", UNSET)

        range_end_ns = d.pop("rangeEndNs", UNSET)

        payload_json = d.pop("payloadJson", UNSET)

        range_start_event_id = d.pop("rangeStartEventId", UNSET)

        range_end_event_id = d.pop("rangeEndEventId", UNSET)

        annotate_range_request = cls(
            run_id=run_id,
            schema_name=schema_name,
            range_start_ns=range_start_ns,
            range_end_ns=range_end_ns,
            payload_json=payload_json,
            range_start_event_id=range_start_event_id,
            range_end_event_id=range_end_event_id,
        )

        annotate_range_request.additional_properties = d
        return annotate_range_request

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
