from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForkRunRequest")


@_attrs_define
class ForkRunRequest:
    """
    Attributes:
        parent_run_id (str | Unset): The run to fork from. Required.
        branch_event_id (str | Unset): The parent event id to fork at — the divergence point on the parent's timeline.
            Empty forks at
             the parent's current head.
        branch_hlc_wall_ns (str | Unset): The parent branch-point wall-clock time in nanoseconds that pairs with
            branch_event_id. Zero
             when forking at the head.
        branch_hlc_logical (str | Unset): The parent branch-point logical tiebreak that pairs with branch_hlc_wall_ns.
        label (str | Unset): An optional human-readable label for the child run.
    """

    parent_run_id: str | Unset = UNSET
    branch_event_id: str | Unset = UNSET
    branch_hlc_wall_ns: str | Unset = UNSET
    branch_hlc_logical: str | Unset = UNSET
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_run_id = self.parent_run_id

        branch_event_id = self.branch_event_id

        branch_hlc_wall_ns = self.branch_hlc_wall_ns

        branch_hlc_logical = self.branch_hlc_logical

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_run_id is not UNSET:
            field_dict["parent_run_id"] = parent_run_id
        if branch_event_id is not UNSET:
            field_dict["branch_event_id"] = branch_event_id
        if branch_hlc_wall_ns is not UNSET:
            field_dict["branch_hlc_wall_ns"] = branch_hlc_wall_ns
        if branch_hlc_logical is not UNSET:
            field_dict["branch_hlc_logical"] = branch_hlc_logical
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_run_id = d.pop("parent_run_id", UNSET)

        branch_event_id = d.pop("branch_event_id", UNSET)

        branch_hlc_wall_ns = d.pop("branch_hlc_wall_ns", UNSET)

        branch_hlc_logical = d.pop("branch_hlc_logical", UNSET)

        label = d.pop("label", UNSET)

        fork_run_request = cls(
            parent_run_id=parent_run_id,
            branch_event_id=branch_event_id,
            branch_hlc_wall_ns=branch_hlc_wall_ns,
            branch_hlc_logical=branch_hlc_logical,
            label=label,
        )

        fork_run_request.additional_properties = d
        return fork_run_request

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
