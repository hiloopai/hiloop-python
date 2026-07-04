from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LifecycleSpec")


@_attrs_define
class LifecycleSpec:
    """Runtime lease policy. Omitted, or lease_secs=0, uses the server default. This intentionally exposes
    only the expiry control needed by public callers; process defaults, mounts, environment, and user
    remain server-managed in the first runtime slice.

       Attributes:
           lease_secs (str | Unset): Max runtime duration in seconds. Nonzero values must be between 60 and 86400
               inclusive;
                zero/omitted uses the server default.
    """

    lease_secs: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lease_secs = self.lease_secs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lease_secs is not UNSET:
            field_dict["leaseSecs"] = lease_secs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lease_secs = d.pop("leaseSecs", UNSET)

        lifecycle_spec = cls(
            lease_secs=lease_secs,
        )

        lifecycle_spec.additional_properties = d
        return lifecycle_spec

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
