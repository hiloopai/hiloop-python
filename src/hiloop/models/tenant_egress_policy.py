from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tenant_egress_policy_enforcement import TenantEgressPolicyEnforcement
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egress_policy import EgressPolicy


T = TypeVar("T", bound="TenantEgressPolicy")


@_attrs_define
class TenantEgressPolicy:
    """A tenant's baseline egress policy — one per tenant.

    Attributes:
        policy (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
            EGRESS_MODE_UNSPECIFIED leaves
             outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
             runtime supports.
        enforcement (TenantEgressPolicyEnforcement | Unset): The default enforcement disposition for the tenant.
        updated_at (str | Unset): When the policy was last set (RFC 3339). Empty when the tenant has never set a policy
            (the
             implicit default baseline applies).
    """

    policy: EgressPolicy | Unset = UNSET
    enforcement: TenantEgressPolicyEnforcement | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        enforcement: str | Unset = UNSET
        if not isinstance(self.enforcement, Unset):
            enforcement = self.enforcement.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy
        if enforcement is not UNSET:
            field_dict["enforcement"] = enforcement
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

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
        enforcement: TenantEgressPolicyEnforcement | Unset
        if isinstance(_enforcement, Unset):
            enforcement = UNSET
        else:
            enforcement = TenantEgressPolicyEnforcement(_enforcement)

        updated_at = d.pop("updatedAt", UNSET)

        tenant_egress_policy = cls(
            policy=policy,
            enforcement=enforcement,
            updated_at=updated_at,
        )

        tenant_egress_policy.additional_properties = d
        return tenant_egress_policy

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
