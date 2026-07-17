from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quota_details import QuotaDetails


T = TypeVar("T", bound="ErrorDetails")


@_attrs_define
class ErrorDetails:
    """Structured detail payloads an error may carry — one member per detail family, so clients can branch without parsing
    the message.

        Attributes:
            quota (QuotaDetails | Unset): The named limit behind a quota or rate-limit rejection: which metric rejected the
                request, its configured limit, and where the caller stands against it.
    """

    quota: QuotaDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quota: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quota, Unset):
            quota = self.quota.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quota is not UNSET:
            field_dict["quota"] = quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quota_details import QuotaDetails

        d = dict(src_dict)
        _quota = d.pop("quota", UNSET)
        quota: QuotaDetails | Unset
        if isinstance(_quota, Unset):
            quota = UNSET
        else:
            quota = QuotaDetails.from_dict(_quota)

        error_details = cls(
            quota=quota,
        )

        error_details.additional_properties = d
        return error_details

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
