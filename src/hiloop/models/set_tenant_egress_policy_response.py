from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.binding_impact import BindingImpact
    from ..models.tenant_egress_policy import TenantEgressPolicy


T = TypeVar("T", bound="SetTenantEgressPolicyResponse")


@_attrs_define
class SetTenantEgressPolicyResponse:
    """
    Attributes:
        policy (TenantEgressPolicy | Unset): A tenant's baseline egress policy — one per tenant.
        changes (list[BindingImpact] | Unset): How the new baseline changed the effective policy of the default class
            and every existing
             binding, relative to the baseline it replaced — one entry per selector whose effective policy
             changed (the same report PreviewBaselineImpact computes for a proposal). A baseline write
             silently re-clamps every existing binding, so the change it caused is reported in the write
             response itself. Empty when the new baseline changes no effective policy.
    """

    policy: TenantEgressPolicy | Unset = UNSET
    changes: list[BindingImpact] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        changes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = []
            for changes_item_data in self.changes:
                changes_item = changes_item_data.to_dict()
                changes.append(changes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.binding_impact import BindingImpact
        from ..models.tenant_egress_policy import TenantEgressPolicy

        d = dict(src_dict)
        _policy = d.pop("policy", UNSET)
        policy: TenantEgressPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = TenantEgressPolicy.from_dict(_policy)

        _changes = d.pop("changes", UNSET)
        changes: list[BindingImpact] | Unset = UNSET
        if _changes is not UNSET:
            changes = []
            for changes_item_data in _changes:
                changes_item = BindingImpact.from_dict(changes_item_data)

                changes.append(changes_item)

        set_tenant_egress_policy_response = cls(
            policy=policy,
            changes=changes,
        )

        set_tenant_egress_policy_response.additional_properties = d
        return set_tenant_egress_policy_response

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
