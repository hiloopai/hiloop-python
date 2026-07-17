from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchDiffSpec")


@_attrs_define
class BranchDiffSpec:
    """A branch-diff (Q3): the events unique to run A that are absent from run B, across two runs sharing
    a tree. This is the differentiated tree-native query — each run's lineage subtree is resolved
    server-side and the two are set-differenced on a semantic key (signal, name, attributes). The
    tenant is taken from request identity, never from this body.

       Attributes:
           signal (str | Unset): Optional signal to restrict the diff to (e.g. "llm"); empty means all signals.
           run_id_a (str | Unset): The run whose unique events to return (the "A" branch). Required.
           run_id_b (str | Unset): The run to subtract (the "B" branch). Required.
    """

    signal: str | Unset = UNSET
    run_id_a: str | Unset = UNSET
    run_id_b: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signal = self.signal

        run_id_a = self.run_id_a

        run_id_b = self.run_id_b

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signal is not UNSET:
            field_dict["signal"] = signal
        if run_id_a is not UNSET:
            field_dict["run_id_a"] = run_id_a
        if run_id_b is not UNSET:
            field_dict["run_id_b"] = run_id_b

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        signal = d.pop("signal", UNSET)

        run_id_a = d.pop("run_id_a", UNSET)

        run_id_b = d.pop("run_id_b", UNSET)

        branch_diff_spec = cls(
            signal=signal,
            run_id_a=run_id_a,
            run_id_b=run_id_b,
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
