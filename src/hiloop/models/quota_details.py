from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuotaDetails")


@_attrs_define
class QuotaDetails:
    """The named limit behind a quota or rate-limit rejection: which metric rejected the request, its configured limit, and
    where the caller stands against it.

        Attributes:
            metric (str): Stable name of the limit that rejected the request (for example sandboxes.active or
                sandbox.create.rate).
            limit (int): The configured limit that rejected the request.
            current (int | Unset): The usage observed against the limit, when the metric counts occupancy. Omitted for rate
                limits, which have no meaningful instantaneous count.
            reserved (int | Unset): Capacity already reserved by accepted but not-yet-settled work. Omitted when the quota
                has no reservation phase or the service cannot distinguish it from committed usage.
            retry_after_seconds (int | Unset): How long to wait before retrying, when the rejection is time-bounded (rate
                limits). Also rendered as a Retry-After header.
    """

    metric: str
    limit: int
    current: int | Unset = UNSET
    reserved: int | Unset = UNSET
    retry_after_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        limit = self.limit

        current = self.current

        reserved = self.reserved

        retry_after_seconds = self.retry_after_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric": metric,
                "limit": limit,
            }
        )
        if current is not UNSET:
            field_dict["current"] = current
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if retry_after_seconds is not UNSET:
            field_dict["retry_after_seconds"] = retry_after_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metric = d.pop("metric")

        limit = d.pop("limit")

        current = d.pop("current", UNSET)

        reserved = d.pop("reserved", UNSET)

        retry_after_seconds = d.pop("retry_after_seconds", UNSET)

        quota_details = cls(
            metric=metric,
            limit=limit,
            current=current,
            reserved=reserved,
            retry_after_seconds=retry_after_seconds,
        )

        quota_details.additional_properties = d
        return quota_details

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
