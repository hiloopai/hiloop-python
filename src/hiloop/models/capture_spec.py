from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.capture_spec_policy import CaptureSpecPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptureSpec")


@_attrs_define
class CaptureSpec:
    """
    Attributes:
        policy (CaptureSpecPolicy | Unset): REST-safe capture policy. Omitted or CAPTURE_POLICY_UNSPECIFIED defaults to
            disabled. Enabling
             capture requires a runtime lane with native capture support.
    """

    policy: CaptureSpecPolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: str | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _policy = d.pop("policy", UNSET)
        policy: CaptureSpecPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = CaptureSpecPolicy(_policy)

        capture_spec = cls(
            policy=policy,
        )

        capture_spec.additional_properties = d
        return capture_spec

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
