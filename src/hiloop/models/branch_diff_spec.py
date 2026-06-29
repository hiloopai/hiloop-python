from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchDiffSpec")


@_attrs_define
class BranchDiffSpec:
    """A branch-diff (Q3): the events under subtree `path_a` that are absent under subtree `path_b`,
    within one run. This is the differentiated tree-native query — two anchored `fork_path` prefix
    scans, set-differenced on a semantic key (signal, name, attributes). The tenant is taken from
    request identity, never from this body.

       Attributes:
           run_id (str | Unset): The run (session) both branches belong to. Required.
           path_a (str | Unset): The subtree whose unique events to return (the "A" branch). Required; anchored by
               `fork_path`
                prefix (the node plus its descendants).
           path_b (str | Unset): The subtree to subtract (the "B" branch). Required.
           signal (str | Unset): Optional signal to restrict the diff to (e.g. "llm"); empty means all signals.
    """

    run_id: str | Unset = UNSET
    path_a: str | Unset = UNSET
    path_b: str | Unset = UNSET
    signal: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        path_a = self.path_a

        path_b = self.path_b

        signal = self.signal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if path_a is not UNSET:
            field_dict["pathA"] = path_a
        if path_b is not UNSET:
            field_dict["pathB"] = path_b
        if signal is not UNSET:
            field_dict["signal"] = signal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId", UNSET)

        path_a = d.pop("pathA", UNSET)

        path_b = d.pop("pathB", UNSET)

        signal = d.pop("signal", UNSET)

        branch_diff_spec = cls(
            run_id=run_id,
            path_a=path_a,
            path_b=path_b,
            signal=signal,
        )

        branch_diff_spec.additional_properties = d
        return branch_diff_spec

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
