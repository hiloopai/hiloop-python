from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenewLeaseRequest")


@_attrs_define
class RenewLeaseRequest:
    """
    Attributes:
        id (str | Unset): The lease id to renew (from the acquire response).
        ttl_secs (str | Unset): The new time-to-live in seconds (1 to 86400), measured from now — not added to the
            previous
             expiry.
    """

    id: str | Unset = UNSET
    ttl_secs: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ttl_secs = self.ttl_secs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ttl_secs is not UNSET:
            field_dict["ttl_secs"] = ttl_secs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        ttl_secs = d.pop("ttl_secs", UNSET)

        renew_lease_request = cls(
            id=id,
            ttl_secs=ttl_secs,
        )

        renew_lease_request.additional_properties = d
        return renew_lease_request

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
