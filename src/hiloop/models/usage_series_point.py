from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageSeriesPoint")


@_attrs_define
class UsageSeriesPoint:
    """One time bucket of a tenant's reserved-resource usage, for the usage-over-time charts. Reserved
    amounts are the time-weighted average over the bucket (rounded).

       Attributes:
           bucket_start (str | Unset): Bucket start (RFC 3339, UTC). Buckets are contiguous and `bucket_seconds` wide.
           reserved_cpus (str | Unset): Time-weighted average reserved virtual CPUs during the bucket.
           reserved_memory_mb (str | Unset): Time-weighted average reserved memory (MiB) during the bucket.
           reserved_gpus (str | Unset): Time-weighted average reserved accelerators during the bucket.
           reserved_disk_mb (str | Unset): Time-weighted average reserved root disk (MiB) during the bucket.
    """

    bucket_start: str | Unset = UNSET
    reserved_cpus: str | Unset = UNSET
    reserved_memory_mb: str | Unset = UNSET
    reserved_gpus: str | Unset = UNSET
    reserved_disk_mb: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_start = self.bucket_start

        reserved_cpus = self.reserved_cpus

        reserved_memory_mb = self.reserved_memory_mb

        reserved_gpus = self.reserved_gpus

        reserved_disk_mb = self.reserved_disk_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_start is not UNSET:
            field_dict["bucketStart"] = bucket_start
        if reserved_cpus is not UNSET:
            field_dict["reservedCpus"] = reserved_cpus
        if reserved_memory_mb is not UNSET:
            field_dict["reservedMemoryMb"] = reserved_memory_mb
        if reserved_gpus is not UNSET:
            field_dict["reservedGpus"] = reserved_gpus
        if reserved_disk_mb is not UNSET:
            field_dict["reservedDiskMb"] = reserved_disk_mb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket_start = d.pop("bucketStart", UNSET)

        reserved_cpus = d.pop("reservedCpus", UNSET)

        reserved_memory_mb = d.pop("reservedMemoryMb", UNSET)

        reserved_gpus = d.pop("reservedGpus", UNSET)

        reserved_disk_mb = d.pop("reservedDiskMb", UNSET)

        usage_series_point = cls(
            bucket_start=bucket_start,
            reserved_cpus=reserved_cpus,
            reserved_memory_mb=reserved_memory_mb,
            reserved_gpus=reserved_gpus,
            reserved_disk_mb=reserved_disk_mb,
        )

        usage_series_point.additional_properties = d
        return usage_series_point

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
