from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchHlc")


@_attrs_define
class BranchHlc:
    """A hybrid logical clock coordinate on an event timeline.

    Attributes:
        wall_ns (str | Unset): Wall-clock component in nanoseconds since the Unix epoch.
        logical (int | Unset): Logical tiebreak for events sharing a wall-clock reading.
    """

    wall_ns: str | Unset = UNSET
    logical: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wall_ns = self.wall_ns

        logical = self.logical

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wall_ns is not UNSET:
            field_dict["wall_ns"] = wall_ns
        if logical is not UNSET:
            field_dict["logical"] = logical

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wall_ns = d.pop("wall_ns", UNSET)

        logical = d.pop("logical", UNSET)

        branch_hlc = cls(
            wall_ns=wall_ns,
            logical=logical,
        )

        branch_hlc.additional_properties = d
        return branch_hlc

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
