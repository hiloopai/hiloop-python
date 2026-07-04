from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_tenant_egress_policy_request_enforcement import SetTenantEgressPolicyRequestEnforcement
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egress_policy import EgressPolicy


T = TypeVar("T", bound="SetTenantEgressPolicyRequest")


@_attrs_define
class SetTenantEgressPolicyRequest:
    """
    Attributes:
        policy (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
            EGRESS_MODE_UNSPECIFIED leaves
             outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
             runtime supports.
        enforcement (SetTenantEgressPolicyRequestEnforcement | Unset): The default enforcement disposition to set for
            the tenant.
    """

    policy: EgressPolicy | Unset = UNSET
    enforcement: SetTenantEgressPolicyRequestEnforcement | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        enforcement: str | Unset = UNSET
        if not isinstance(self.enforcement, Unset):
            enforcement = self.enforcement.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy
        if enforcement is not UNSET:
            field_dict["enforcement"] = enforcement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egress_policy import EgressPolicy

        d = dict(src_dict)
        _policy = d.pop("policy", UNSET)
        policy: EgressPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = EgressPolicy.from_dict(_policy)

        _enforcement = d.pop("enforcement", UNSET)
        enforcement: SetTenantEgressPolicyRequestEnforcement | Unset
        if isinstance(_enforcement, Unset):
            enforcement = UNSET
        else:
            enforcement = SetTenantEgressPolicyRequestEnforcement(_enforcement)

        set_tenant_egress_policy_request = cls(
            policy=policy,
            enforcement=enforcement,
        )

        set_tenant_egress_policy_request.additional_properties = d
        return set_tenant_egress_policy_request

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
