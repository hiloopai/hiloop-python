from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkloadLauncher")


@_attrs_define
class WorkloadLauncher:
    """One launch-ACL entry: a principal allowed to launch as the workload.

    Attributes:
        kind (str | Unset): The kind of principal this entry names: `user` (a tenant member, named by user id — also the
             meaning of an unset kind) or `service_account` (a service-account API key, named by key id).
             Any other value is rejected.
        principal_id (str | Unset): The principal's stable id: a user id for `user`, a service-account key id for
             `service_account`.
    """

    kind: str | Unset = UNSET
    principal_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        principal_id = self.principal_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if principal_id is not UNSET:
            field_dict["principal_id"] = principal_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        principal_id = d.pop("principal_id", UNSET)

        workload_launcher = cls(
            kind=kind,
            principal_id=principal_id,
        )

        workload_launcher.additional_properties = d
        return workload_launcher

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
