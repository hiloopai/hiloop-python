from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnapshotResult")


@_attrs_define
class SnapshotResult:
    """Retired snapshot-compatibility result. Clean sandbox-cell deployments do not produce it.

    Attributes:
        snapshot_id (str | Unset):
        sandbox_id (str | Unset):
        state (str | Unset): The snapshot's lifecycle state at operation completion: pending, ready, or failed.
    """

    snapshot_id: str | Unset = UNSET
    sandbox_id: str | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_id = self.snapshot_id

        sandbox_id = self.sandbox_id

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snapshot_id is not UNSET:
            field_dict["snapshot_id"] = snapshot_id
        if sandbox_id is not UNSET:
            field_dict["sandbox_id"] = sandbox_id
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        snapshot_id = d.pop("snapshot_id", UNSET)

        sandbox_id = d.pop("sandbox_id", UNSET)

        state = d.pop("state", UNSET)

        snapshot_result = cls(
            snapshot_id=snapshot_id,
            sandbox_id=sandbox_id,
            state=state,
        )

        snapshot_result.additional_properties = d
        return snapshot_result

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
