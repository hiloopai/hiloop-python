from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proposed_egress_policy_enforcement import ProposedEgressPolicyEnforcement
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egress_policy import EgressPolicy


T = TypeVar("T", bound="ProposedEgressPolicy")


@_attrs_define
class ProposedEgressPolicy:
    """A proposed (unsaved) binding policy to preview at a selector's tier, for the rule editor's live
    "if I save this rule, what's the effective result?" preview. It is an EgressPolicy plus an optional
    enforcement override, matching a stored binding.

       Attributes:
           policy (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
               EGRESS_MODE_UNSPECIFIED leaves
                outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
                runtime supports.
           enforcement (ProposedEgressPolicyEnforcement | Unset): The proposed enforcement override.
               EGRESS_ENFORCEMENT_UNSPECIFIED inherits the tenant default,
                exactly as a stored binding's optional override does.
    """

    policy: EgressPolicy | Unset = UNSET
    enforcement: ProposedEgressPolicyEnforcement | Unset = UNSET
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
        enforcement: ProposedEgressPolicyEnforcement | Unset
        if isinstance(_enforcement, Unset):
            enforcement = UNSET
        else:
            enforcement = ProposedEgressPolicyEnforcement(_enforcement)

        proposed_egress_policy = cls(
            policy=policy,
            enforcement=enforcement,
        )

        proposed_egress_policy.additional_properties = d
        return proposed_egress_policy

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
