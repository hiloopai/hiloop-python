from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workload_launch_acl_policy import WorkloadLaunchAclPolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workload_launcher import WorkloadLauncher


T = TypeVar("T", bound="WorkloadLaunchAcl")


@_attrs_define
class WorkloadLaunchAcl:
    """A per-workload launch ACL: which principals may launch a run or sandbox as the workload.

    Attributes:
        policy (WorkloadLaunchAclPolicy | Unset): The launch policy: open to all tenant members, or restricted to the
            listed launchers.
        launchers (list[WorkloadLauncher] | Unset): The principals allowed to launch as this workload. Meaningful only
            when the policy is
             WORKLOAD_LAUNCH_POLICY_RESTRICTED; empty otherwise.
    """

    policy: WorkloadLaunchAclPolicy | Unset = UNSET
    launchers: list[WorkloadLauncher] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: str | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.value

        launchers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.launchers, Unset):
            launchers = []
            for launchers_item_data in self.launchers:
                launchers_item = launchers_item_data.to_dict()
                launchers.append(launchers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy
        if launchers is not UNSET:
            field_dict["launchers"] = launchers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workload_launcher import WorkloadLauncher

        d = dict(src_dict)
        _policy = d.pop("policy", UNSET)
        policy: WorkloadLaunchAclPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = WorkloadLaunchAclPolicy(_policy)

        _launchers = d.pop("launchers", UNSET)
        launchers: list[WorkloadLauncher] | Unset = UNSET
        if _launchers is not UNSET:
            launchers = []
            for launchers_item_data in _launchers:
                launchers_item = WorkloadLauncher.from_dict(launchers_item_data)

                launchers.append(launchers_item)

        workload_launch_acl = cls(
            policy=policy,
            launchers=launchers,
        )

        workload_launch_acl.additional_properties = d
        return workload_launch_acl

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
