from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workload_launch_acl import WorkloadLaunchAcl


T = TypeVar("T", bound="SetWorkloadLaunchAclRequest")


@_attrs_define
class SetWorkloadLaunchAclRequest:
    """
    Attributes:
        name (str | Unset): The registered workload name.
        acl (WorkloadLaunchAcl | Unset): A per-workload launch ACL: which principals may launch a run or sandbox as the
            workload.
    """

    name: str | Unset = UNSET
    acl: WorkloadLaunchAcl | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        acl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.acl, Unset):
            acl = self.acl.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if acl is not UNSET:
            field_dict["acl"] = acl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workload_launch_acl import WorkloadLaunchAcl

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _acl = d.pop("acl", UNSET)
        acl: WorkloadLaunchAcl | Unset
        if isinstance(_acl, Unset):
            acl = UNSET
        else:
            acl = WorkloadLaunchAcl.from_dict(_acl)

        set_workload_launch_acl_request = cls(
            name=name,
            acl=acl,
        )

        set_workload_launch_acl_request.additional_properties = d
        return set_workload_launch_acl_request

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
