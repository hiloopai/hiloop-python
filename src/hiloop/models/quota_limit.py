from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuotaLimit")


@_attrs_define
class QuotaLimit:
    """One workspace limit: the stable metric name, the configured cap, and — where the platform tracks
    an instantaneous value — the usage observed against it right now.

       Attributes:
           metric (str | Unset): The stable limit name (e.g. `sandboxes.active`, `snapshots.bytes`) — the same vocabulary a
                limit rejection carries in its error `details.quota.metric`.
           limit (str | Unset): The configured cap for this workspace.
           current (str | Unset): The usage observed against the cap right now. Omitted for per-minute rate limits, which
               have
                no instantaneous occupancy.
           reserved (str | Unset): Capacity reserved by accepted but not-yet-settled work. Omitted for metrics without a
                reservation phase.
    """

    metric: str | Unset = UNSET
    limit: str | Unset = UNSET
    current: str | Unset = UNSET
    reserved: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        limit = self.limit

        current = self.current

        reserved = self.reserved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metric is not UNSET:
            field_dict["metric"] = metric
        if limit is not UNSET:
            field_dict["limit"] = limit
        if current is not UNSET:
            field_dict["current"] = current
        if reserved is not UNSET:
            field_dict["reserved"] = reserved

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metric = d.pop("metric", UNSET)

        limit = d.pop("limit", UNSET)

        current = d.pop("current", UNSET)

        reserved = d.pop("reserved", UNSET)

        quota_limit = cls(
            metric=metric,
            limit=limit,
            current=current,
            reserved=reserved,
        )

        quota_limit.additional_properties = d
        return quota_limit

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
