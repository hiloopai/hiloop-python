from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnotateRequest")


@_attrs_define
class AnnotateRequest:
    """One annotation: run-scoped (optionally targeting a single event within the run) or
    project-scoped (no run — durable cross-run knowledge that outlives any sandbox).

       Attributes:
           run_id (str | Unset): The run (session) the annotation belongs to. Exactly one of `run_id` or `project_id` is
               set.
           schema_name (str | Unset): The registered annotation-schema name the payload validates against (the event
               `name`).
           target_event_id (str | Unset): The `event_id` of the single event this annotation is about. Only valid with
               `run_id`; empty
                annotates the run (or project) itself.
           payload_json (str | Unset): The annotation payload as a JSON object string; validated against `schema_name`'s
               registered
                JSON Schema at ingest. Reserved `hiloop.annotation.*` keys are platform-owned and excluded.
           project_id (str | Unset): The project a run-less annotation belongs to. Exactly one of `run_id` or `project_id`
               is set;
                a project-scoped annotation carries no run lineage and no target event.
    """

    run_id: str | Unset = UNSET
    schema_name: str | Unset = UNSET
    target_event_id: str | Unset = UNSET
    payload_json: str | Unset = UNSET
    project_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        schema_name = self.schema_name

        target_event_id = self.target_event_id

        payload_json = self.payload_json

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if schema_name is not UNSET:
            field_dict["schemaName"] = schema_name
        if target_event_id is not UNSET:
            field_dict["targetEventId"] = target_event_id
        if payload_json is not UNSET:
            field_dict["payloadJson"] = payload_json
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId", UNSET)

        schema_name = d.pop("schemaName", UNSET)

        target_event_id = d.pop("targetEventId", UNSET)

        payload_json = d.pop("payloadJson", UNSET)

        project_id = d.pop("projectId", UNSET)

        annotate_request = cls(
            run_id=run_id,
            schema_name=schema_name,
            target_event_id=target_event_id,
            payload_json=payload_json,
            project_id=project_id,
        )

        annotate_request.additional_properties = d
        return annotate_request

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
