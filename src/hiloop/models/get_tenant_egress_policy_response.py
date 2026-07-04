from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tenant_egress_policy import TenantEgressPolicy


T = TypeVar("T", bound="GetTenantEgressPolicyResponse")


@_attrs_define
class GetTenantEgressPolicyResponse:
    """
    Attributes:
        policy (TenantEgressPolicy | Unset): A tenant's baseline egress policy — one per tenant.
    """

    policy: TenantEgressPolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_egress_policy import TenantEgressPolicy

        d = dict(src_dict)
        _policy = d.pop("policy", UNSET)
        policy: TenantEgressPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = TenantEgressPolicy.from_dict(_policy)

        get_tenant_egress_policy_response = cls(
            policy=policy,
        )

        get_tenant_egress_policy_response.additional_properties = d
        return get_tenant_egress_policy_response

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
