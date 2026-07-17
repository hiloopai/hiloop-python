from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_egress_policy_binding_request_enforcement import SetEgressPolicyBindingRequestEnforcement
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egress_policy import EgressPolicy


T = TypeVar("T", bound="SetEgressPolicyBindingRequest")


@_attrs_define
class SetEgressPolicyBindingRequest:
    """
    Attributes:
        selector (str | Unset): The identity selector to bind (see EgressPolicyBinding.selector for the grammar).
            Rejected as
             INVALID_ARGUMENT if it is not a well-formed selector.
        policy (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
            EGRESS_MODE_UNSPECIFIED leaves
             outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
             runtime supports.
        enforcement (SetEgressPolicyBindingRequestEnforcement | Unset): The enforcement override to set for this class,
            or EGRESS_ENFORCEMENT_UNSPECIFIED for no
             override (the tenant default applies).
    """

    selector: str | Unset = UNSET
    policy: EgressPolicy | Unset = UNSET
    enforcement: SetEgressPolicyBindingRequestEnforcement | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        selector = self.selector

        policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        enforcement: str | Unset = UNSET
        if not isinstance(self.enforcement, Unset):
            enforcement = self.enforcement.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selector is not UNSET:
            field_dict["selector"] = selector
        if policy is not UNSET:
            field_dict["policy"] = policy
        if enforcement is not UNSET:
            field_dict["enforcement"] = enforcement

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
        enforcement: SetEgressPolicyBindingRequestEnforcement | Unset
        if isinstance(_enforcement, Unset):
            enforcement = UNSET
        else:
            enforcement = SetEgressPolicyBindingRequestEnforcement(_enforcement)

        set_egress_policy_binding_request = cls(
            selector=selector,
            policy=policy,
            enforcement=enforcement,
        )

        set_egress_policy_binding_request.additional_properties = d
        return set_egress_policy_binding_request

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
