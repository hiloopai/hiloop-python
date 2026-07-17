from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestoreResult")


@_attrs_define
class RestoreResult:
    """Retired snapshot-restore compatibility result. Clean sandbox-cell deployments do not produce it.

    Attributes:
        sandbox_id (str | Unset): The new sandbox the restore created.
        snapshot_id (str | Unset):
        generation (str | Unset):
        observed_state (str | Unset):
        readiness (str | Unset):
    """

    sandbox_id: str | Unset = UNSET
    snapshot_id: str | Unset = UNSET
    generation: str | Unset = UNSET
    observed_state: str | Unset = UNSET
    readiness: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        snapshot_id = self.snapshot_id

        generation = self.generation

        observed_state = self.observed_state

        readiness = self.readiness

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sandbox_id is not UNSET:
            field_dict["sandbox_id"] = sandbox_id
        if snapshot_id is not UNSET:
            field_dict["snapshot_id"] = snapshot_id
        if generation is not UNSET:
            field_dict["generation"] = generation
        if observed_state is not UNSET:
            field_dict["observed_state"] = observed_state
        if readiness is not UNSET:
            field_dict["readiness"] = readiness

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id", UNSET)

        snapshot_id = d.pop("snapshot_id", UNSET)

        generation = d.pop("generation", UNSET)

        observed_state = d.pop("observed_state", UNSET)

        readiness = d.pop("readiness", UNSET)

        restore_result = cls(
            sandbox_id=sandbox_id,
            snapshot_id=snapshot_id,
            generation=generation,
            observed_state=observed_state,
            readiness=readiness,
        )

        restore_result.additional_properties = d
        return restore_result

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
