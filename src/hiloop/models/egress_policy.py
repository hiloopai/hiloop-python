from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.egress_policy_mode import EgressPolicyMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="EgressPolicy")


@_attrs_define
class EgressPolicy:
    """Provider-neutral outbound network policy for a sandbox. Omitted or EGRESS_MODE_UNSPECIFIED leaves
    outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
    runtime supports.

       Attributes:
           mode (EgressPolicyMode | Unset): Whether the lists below are an allowlist (deny mode) or a denylist (allow
               mode).
           domains (list[str] | Unset): Suffix-matched destination domains the policy applies to.
           cidrs (list[str] | Unset): Destination IP ranges, in CIDR notation, the policy applies to.
    """

    mode: EgressPolicyMode | Unset = UNSET
    domains: list[str] | Unset = UNSET
    cidrs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        domains: list[str] | Unset = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains

        cidrs: list[str] | Unset = UNSET
        if not isinstance(self.cidrs, Unset):
            cidrs = self.cidrs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if domains is not UNSET:
            field_dict["domains"] = domains
        if cidrs is not UNSET:
            field_dict["cidrs"] = cidrs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: EgressPolicyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = EgressPolicyMode(_mode)

        domains = cast(list[str], d.pop("domains", UNSET))

        cidrs = cast(list[str], d.pop("cidrs", UNSET))

        egress_policy = cls(
            mode=mode,
            domains=domains,
            cidrs=cidrs,
        )

        egress_policy.additional_properties = d
        return egress_policy

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
