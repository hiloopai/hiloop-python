from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartRunRequest")


@_attrs_define
class StartRunRequest:
    """
    Attributes:
        project_id (str | Unset): The project the new run belongs to.
        parent_run_id (str | Unset): Optional parent run to continue the tree from. Empty starts a new tree root.
        label (str | Unset): An optional human-readable label.
        execute_as_workload (str | Unset): Optional registered workload name to run as. When set, the run is attributed
            to that workload
             (the caller must hold launch rights on it and the name must be registered); when empty, the run
             executes as the caller's own identity. The executing identity is always declared here, never
             inferred from the command.
    """

    project_id: str | Unset = UNSET
    parent_run_id: str | Unset = UNSET
    label: str | Unset = UNSET
    execute_as_workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        parent_run_id = self.parent_run_id

        label = self.label

        execute_as_workload = self.execute_as_workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if parent_run_id is not UNSET:
            field_dict["parent_run_id"] = parent_run_id
        if label is not UNSET:
            field_dict["label"] = label
        if execute_as_workload is not UNSET:
            field_dict["execute_as_workload"] = execute_as_workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id", UNSET)

        parent_run_id = d.pop("parent_run_id", UNSET)

        label = d.pop("label", UNSET)

        execute_as_workload = d.pop("execute_as_workload", UNSET)

        start_run_request = cls(
            project_id=project_id,
            parent_run_id=parent_run_id,
            label=label,
            execute_as_workload=execute_as_workload,
        )

        start_run_request.additional_properties = d
        return start_run_request

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
