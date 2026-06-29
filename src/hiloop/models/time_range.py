from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeRange")


@_attrs_define
class TimeRange:
    """Inclusive wall-clock window in nanoseconds (matches CanonicalEvent.ts_wall_ns).

    Attributes:
        start_ns (str | Unset):
        end_ns (str | Unset):
    """

    start_ns: str | Unset = UNSET
    end_ns: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_ns = self.start_ns

        end_ns = self.end_ns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_ns is not UNSET:
            field_dict["startNs"] = start_ns
        if end_ns is not UNSET:
            field_dict["endNs"] = end_ns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_ns = d.pop("startNs", UNSET)

        end_ns = d.pop("endNs", UNSET)

        time_range = cls(
            start_ns=start_ns,
            end_ns=end_ns,
        )

        time_range.additional_properties = d
        return time_range

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
