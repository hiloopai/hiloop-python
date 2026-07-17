from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SkippedAnnotation")


@_attrs_define
class SkippedAnnotation:
    """A stored annotation row a listing skipped because it could not be decoded, with the row's stored
    event id and the decode failure. Skipped rows are surfaced, never silently dropped: the listing
    stays available while naming exactly what it could not serve.

       Attributes:
           event_id (str | Unset): The stored `event_id` of the row that failed to decode.
           reason (str | Unset): Why the row could not be decoded.
    """

    event_id: str | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_id = d.pop("event_id", UNSET)

        reason = d.pop("reason", UNSET)

        skipped_annotation = cls(
            event_id=event_id,
            reason=reason,
        )

        skipped_annotation.additional_properties = d
        return skipped_annotation

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
