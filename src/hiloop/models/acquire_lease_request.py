from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcquireLeaseRequest")


@_attrs_define
class AcquireLeaseRequest:
    """
    Attributes:
        project_id (str | Unset): The project to acquire the lease in.
        name (str | Unset): The lease name to acquire — at most 100 characters after trimming.
        ttl_secs (str | Unset): How long the lease is held before it expires, in seconds (1 to 86400). Renew before
            expiry to
             keep holding it.
    """

    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    ttl_secs: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        name = self.name

        ttl_secs = self.ttl_secs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if ttl_secs is not UNSET:
            field_dict["ttl_secs"] = ttl_secs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id", UNSET)

        name = d.pop("name", UNSET)

        ttl_secs = d.pop("ttl_secs", UNSET)

        acquire_lease_request = cls(
            project_id=project_id,
            name=name,
            ttl_secs=ttl_secs,
        )

        acquire_lease_request.additional_properties = d
        return acquire_lease_request

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
