from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quota_limit import QuotaLimit
    from ..models.reserved_resources import ReservedResources
    from ..models.sandbox_state_count import SandboxStateCount


T = TypeVar("T", bound="UsageSnapshot")


@_attrs_define
class UsageSnapshot:
    """A point-in-time, tenant-scoped usage snapshot.

    Attributes:
        tenant_id (str | Unset): The tenant the snapshot covers (derived from the caller's scope, echoed for
            convenience).
        active_sandbox_count (str | Unset): The number of active (non-deleted, non-terminal) sandboxes.
        sandbox_state_counts (list[SandboxStateCount] | Unset): The per-observed-state breakdown of non-deleted
            sandboxes, including terminal states, so the
             caller can render the full distribution. Ordered by observed state.
        reserved (ReservedResources | Unset): Reserved resources summed over the active runtime instance of each in-use
            sandbox. These are the
             requested ("reserved") amounts the sandboxes asked for, not measured live utilization.
        limits (list[QuotaLimit] | Unset): The workspace's configured limits, one row per quota metric, each with the
            usage observed
             against it where the platform tracks an instantaneous value. Always covers every limited
             metric, whatever the current usage.
    """

    tenant_id: str | Unset = UNSET
    active_sandbox_count: str | Unset = UNSET
    sandbox_state_counts: list[SandboxStateCount] | Unset = UNSET
    reserved: ReservedResources | Unset = UNSET
    limits: list[QuotaLimit] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        active_sandbox_count = self.active_sandbox_count

        sandbox_state_counts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sandbox_state_counts, Unset):
            sandbox_state_counts = []
            for sandbox_state_counts_item_data in self.sandbox_state_counts:
                sandbox_state_counts_item = sandbox_state_counts_item_data.to_dict()
                sandbox_state_counts.append(sandbox_state_counts_item)

        reserved: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reserved, Unset):
            reserved = self.reserved.to_dict()

        limits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = []
            for limits_item_data in self.limits:
                limits_item = limits_item_data.to_dict()
                limits.append(limits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if active_sandbox_count is not UNSET:
            field_dict["active_sandbox_count"] = active_sandbox_count
        if sandbox_state_counts is not UNSET:
            field_dict["sandbox_state_counts"] = sandbox_state_counts
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quota_limit import QuotaLimit
        from ..models.reserved_resources import ReservedResources
        from ..models.sandbox_state_count import SandboxStateCount

        d = dict(src_dict)
        tenant_id = d.pop("tenant_id", UNSET)

        active_sandbox_count = d.pop("active_sandbox_count", UNSET)

        _sandbox_state_counts = d.pop("sandbox_state_counts", UNSET)
        sandbox_state_counts: list[SandboxStateCount] | Unset = UNSET
        if _sandbox_state_counts is not UNSET:
            sandbox_state_counts = []
            for sandbox_state_counts_item_data in _sandbox_state_counts:
                sandbox_state_counts_item = SandboxStateCount.from_dict(sandbox_state_counts_item_data)

                sandbox_state_counts.append(sandbox_state_counts_item)

        _reserved = d.pop("reserved", UNSET)
        reserved: ReservedResources | Unset
        if isinstance(_reserved, Unset):
            reserved = UNSET
        else:
            reserved = ReservedResources.from_dict(_reserved)

        _limits = d.pop("limits", UNSET)
        limits: list[QuotaLimit] | Unset = UNSET
        if _limits is not UNSET:
            limits = []
            for limits_item_data in _limits:
                limits_item = QuotaLimit.from_dict(limits_item_data)

                limits.append(limits_item)

        usage_snapshot = cls(
            tenant_id=tenant_id,
            active_sandbox_count=active_sandbox_count,
            sandbox_state_counts=sandbox_state_counts,
            reserved=reserved,
            limits=limits,
        )

        usage_snapshot.additional_properties = d
        return usage_snapshot

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
