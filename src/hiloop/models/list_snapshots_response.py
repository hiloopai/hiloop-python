from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snapshot import Snapshot


T = TypeVar("T", bound="ListSnapshotsResponse")


@_attrs_define
class ListSnapshotsResponse:
    """
    Attributes:
        snapshots (list[Snapshot] | Unset):
    """

    snapshots: list[Snapshot] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshots: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.snapshots, Unset):
            snapshots = []
            for snapshots_item_data in self.snapshots:
                snapshots_item = snapshots_item_data.to_dict()
                snapshots.append(snapshots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snapshots is not UNSET:
            field_dict["snapshots"] = snapshots

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snapshot import Snapshot

        d = dict(src_dict)
        _snapshots = d.pop("snapshots", UNSET)
        snapshots: list[Snapshot] | Unset = UNSET
        if _snapshots is not UNSET:
            snapshots = []
            for snapshots_item_data in _snapshots:
                snapshots_item = Snapshot.from_dict(snapshots_item_data)

                snapshots.append(snapshots_item)

        list_snapshots_response = cls(
            snapshots=snapshots,
        )

        list_snapshots_response.additional_properties = d
        return list_snapshots_response

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
