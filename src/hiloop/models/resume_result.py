from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResumeResult")


@_attrs_define
class ResumeResult:
    """What a succeeded resume observed about the sandbox it brought back.

    Attributes:
        fresh_workspace (bool | Unset): True when the resume provisioned a fresh, empty workspace under a new generation
            (the
             explicit fresh_workspace opt-in) instead of restoring a sealed BranchFS filesystem.
        generation (str | Unset): The sandbox generation serving the resumed workload. Present when resume materialized
            a new
             runtime, whether from fresh scratch storage or an exact sealed BranchFS revision.
        observed_state (str | Unset): The sandbox's observed state once the resume settled. A non-fresh resume may still
            report a
             new generation when it restored an exact sealed filesystem; process and memory state are not
             implied by this result.
    """

    fresh_workspace: bool | Unset = UNSET
    generation: str | Unset = UNSET
    observed_state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fresh_workspace = self.fresh_workspace

        generation = self.generation

        observed_state = self.observed_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fresh_workspace is not UNSET:
            field_dict["fresh_workspace"] = fresh_workspace
        if generation is not UNSET:
            field_dict["generation"] = generation
        if observed_state is not UNSET:
            field_dict["observed_state"] = observed_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fresh_workspace = d.pop("fresh_workspace", UNSET)

        generation = d.pop("generation", UNSET)

        observed_state = d.pop("observed_state", UNSET)

        resume_result = cls(
            fresh_workspace=fresh_workspace,
            generation=generation,
            observed_state=observed_state,
        )

        resume_result.additional_properties = d
        return resume_result

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
