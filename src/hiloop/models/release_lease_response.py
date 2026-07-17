from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lease import Lease


T = TypeVar("T", bound="ReleaseLeaseResponse")


@_attrs_define
class ReleaseLeaseResponse:
    """
    Attributes:
        lease (Lease | Unset): One acquisition generation of a project-scoped lease.
    """

    lease: Lease | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lease: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lease, Unset):
            lease = self.lease.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lease is not UNSET:
            field_dict["lease"] = lease

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lease import Lease

        d = dict(src_dict)
        _lease = d.pop("lease", UNSET)
        lease: Lease | Unset
        if isinstance(_lease, Unset):
            lease = UNSET
        else:
            lease = Lease.from_dict(_lease)

        release_lease_response = cls(
            lease=lease,
        )

        release_lease_response.additional_properties = d
        return release_lease_response

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
