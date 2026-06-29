from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_snapshot import UsageSnapshot


T = TypeVar("T", bound="GetUsageSnapshotResponse")


@_attrs_define
class GetUsageSnapshotResponse:
    """
    Attributes:
        snapshot (UsageSnapshot | Unset): A point-in-time, tenant-scoped usage snapshot.
    """

    snapshot: UsageSnapshot | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot, Unset):
            snapshot = self.snapshot.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_snapshot import UsageSnapshot

        d = dict(src_dict)
        _snapshot = d.pop("snapshot", UNSET)
        snapshot: UsageSnapshot | Unset
        if isinstance(_snapshot, Unset):
            snapshot = UNSET
        else:
            snapshot = UsageSnapshot.from_dict(_snapshot)

        get_usage_snapshot_response = cls(
            snapshot=snapshot,
        )

        get_usage_snapshot_response.additional_properties = d
        return get_usage_snapshot_response

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
