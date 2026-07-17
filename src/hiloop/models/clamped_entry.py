from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClampedEntry")


@_attrs_define
class ClampedEntry:
    """One destination the tenant baseline ceiling removed from a matched binding. A binding may only
    narrow the baseline, so any destination it names that the baseline forbids is dropped from the
    effective policy — surfaced here so an operator can see what a binding asked for but could not get.

       Attributes:
           entry (str | Unset): The destination (a domain or a CIDR) that was removed.
           reason (str | Unset): Why it was removed (e.g. it is outside the baseline allowlist, or the baseline denies it).
    """

    entry: str | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry = self.entry

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry is not UNSET:
            field_dict["entry"] = entry
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entry = d.pop("entry", UNSET)

        reason = d.pop("reason", UNSET)

        clamped_entry = cls(
            entry=entry,
            reason=reason,
        )

        clamped_entry.additional_properties = d
        return clamped_entry

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
