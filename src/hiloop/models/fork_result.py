from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForkResult")


@_attrs_define
class ForkResult:
    """Retired fork-compatibility result. Clean sandbox-cell deployments do not produce it.

    Attributes:
        fork_id (str | Unset):
        source_sandbox_id (str | Unset):
        child_sandbox_id (str | Unset):
        child_run_id (str | Unset): The child run the fork minted.
        implementation (str | Unset): The continuity implementation that served the fork, in the public vocabulary.
        filesystem_continuity (bool | Unset): Which dimensions of the source's state the child actually continued.
        memory_continuity (bool | Unset):
        process_continuity (bool | Unset):
        observed_state (str | Unset):
        readiness (str | Unset):
        warnings (list[str] | Unset): Human-readable degradation notes recorded by the fork (for example a fallback the
            request
             allowed).
    """

    fork_id: str | Unset = UNSET
    source_sandbox_id: str | Unset = UNSET
    child_sandbox_id: str | Unset = UNSET
    child_run_id: str | Unset = UNSET
    implementation: str | Unset = UNSET
    filesystem_continuity: bool | Unset = UNSET
    memory_continuity: bool | Unset = UNSET
    process_continuity: bool | Unset = UNSET
    observed_state: str | Unset = UNSET
    readiness: str | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fork_id = self.fork_id

        source_sandbox_id = self.source_sandbox_id

        child_sandbox_id = self.child_sandbox_id

        child_run_id = self.child_run_id

        implementation = self.implementation

        filesystem_continuity = self.filesystem_continuity

        memory_continuity = self.memory_continuity

        process_continuity = self.process_continuity

        observed_state = self.observed_state

        readiness = self.readiness

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fork_id is not UNSET:
            field_dict["fork_id"] = fork_id
        if source_sandbox_id is not UNSET:
            field_dict["source_sandbox_id"] = source_sandbox_id
        if child_sandbox_id is not UNSET:
            field_dict["child_sandbox_id"] = child_sandbox_id
        if child_run_id is not UNSET:
            field_dict["child_run_id"] = child_run_id
        if implementation is not UNSET:
            field_dict["implementation"] = implementation
        if filesystem_continuity is not UNSET:
            field_dict["filesystem_continuity"] = filesystem_continuity
        if memory_continuity is not UNSET:
            field_dict["memory_continuity"] = memory_continuity
        if process_continuity is not UNSET:
            field_dict["process_continuity"] = process_continuity
        if observed_state is not UNSET:
            field_dict["observed_state"] = observed_state
        if readiness is not UNSET:
            field_dict["readiness"] = readiness
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fork_id = d.pop("fork_id", UNSET)

        source_sandbox_id = d.pop("source_sandbox_id", UNSET)

        child_sandbox_id = d.pop("child_sandbox_id", UNSET)

        child_run_id = d.pop("child_run_id", UNSET)

        implementation = d.pop("implementation", UNSET)

        filesystem_continuity = d.pop("filesystem_continuity", UNSET)

        memory_continuity = d.pop("memory_continuity", UNSET)

        process_continuity = d.pop("process_continuity", UNSET)

        observed_state = d.pop("observed_state", UNSET)

        readiness = d.pop("readiness", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        fork_result = cls(
            fork_id=fork_id,
            source_sandbox_id=source_sandbox_id,
            child_sandbox_id=child_sandbox_id,
            child_run_id=child_run_id,
            implementation=implementation,
            filesystem_continuity=filesystem_continuity,
            memory_continuity=memory_continuity,
            process_continuity=process_continuity,
            observed_state=observed_state,
            readiness=readiness,
            warnings=warnings,
        )

        fork_result.additional_properties = d
        return fork_result

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
