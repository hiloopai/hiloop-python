from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.egress_policy_binding_enforcement import EgressPolicyBindingEnforcement
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egress_policy import EgressPolicy


T = TypeVar("T", bound="EgressPolicyBinding")


@_attrs_define
class EgressPolicyBinding:
    """An identity-bound egress policy binding: an egress policy attached to an identity selector, so a
    tenant can give a different outbound-network policy to a class of principals (e.g. autonomous
    workloads) than to others. A binding never widens the tenant baseline; it is one input the
    effective policy is resolved from.

       Attributes:
           selector (str | Unset): The identity selector this binding applies to. One of:
                  kind:workload | kind:user | kind:service_account   (an identity class)
                  role:owner | role:admin | role:member              (a membership role)
                  workload:NAME                                       (one registered workload, by name)
                  user:ID | key:ID                                    (one specific principal, by id)
           policy (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
               EGRESS_MODE_UNSPECIFIED leaves
                outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
                runtime supports.
           enforcement (EgressPolicyBindingEnforcement | Unset): The enforcement override for this class.
               EGRESS_ENFORCEMENT_UNSPECIFIED means no override — the
                tenant default applies; BLOCK or WARN overrides it for principals this selector matches.
           created_by (str | Unset): The user id that created the binding, when recorded. Empty for a service-credential
               caller.
           created_at (str | Unset): When the binding was created (RFC 3339).
           updated_at (str | Unset): When the binding was last set (RFC 3339).
    """

    selector: str | Unset = UNSET
    policy: EgressPolicy | Unset = UNSET
    enforcement: EgressPolicyBindingEnforcement | Unset = UNSET
    created_by: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        selector = self.selector

        policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        enforcement: str | Unset = UNSET
        if not isinstance(self.enforcement, Unset):
            enforcement = self.enforcement.value

        created_by = self.created_by

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selector is not UNSET:
            field_dict["selector"] = selector
        if policy is not UNSET:
            field_dict["policy"] = policy
        if enforcement is not UNSET:
            field_dict["enforcement"] = enforcement
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egress_policy import EgressPolicy

        d = dict(src_dict)
        selector = d.pop("selector", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: EgressPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = EgressPolicy.from_dict(_policy)

        _enforcement = d.pop("enforcement", UNSET)
        enforcement: EgressPolicyBindingEnforcement | Unset
        if isinstance(_enforcement, Unset):
            enforcement = UNSET
        else:
            enforcement = EgressPolicyBindingEnforcement(_enforcement)

        created_by = d.pop("created_by", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        egress_policy_binding = cls(
            selector=selector,
            policy=policy,
            enforcement=enforcement,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
        )

        egress_policy_binding.additional_properties = d
        return egress_policy_binding

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
