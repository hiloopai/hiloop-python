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
        enabled (bool | Unset): Compatibility capture toggle for existing clients. Omit this field, or omit the parent
             `capture` field, to use the default-enabled policy.
        policy (CaptureSpecPolicy | Unset): REST-safe capture policy. Use CAPTURE_POLICY_DISABLED to run the sandbox
            with no capture
             instrumentation; omitted or CAPTURE_POLICY_UNSPECIFIED defaults to enabled.
    """

    enabled: bool | Unset = UNSET
    policy: CaptureSpecPolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        policy: str | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: CaptureSpecPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = CaptureSpecPolicy(_policy)

        capture_spec = cls(
            enabled=enabled,
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
