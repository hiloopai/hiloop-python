from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clamped_entry import ClampedEntry
    from ..models.egress_policy_binding import EgressPolicyBinding


T = TypeVar("T", bound="SetEgressPolicyBindingResponse")


@_attrs_define
class SetEgressPolicyBindingResponse:
    """
    Attributes:
        binding (EgressPolicyBinding | Unset): An identity-bound egress policy binding: an egress policy attached to an
            identity selector, so a
             tenant can give a different outbound-network policy to a class of principals (e.g. autonomous
             workloads) than to others. A binding never widens the tenant baseline; it is one input the
             effective policy is resolved from.
        clamped (list[ClampedEntry] | Unset): Destinations the stored binding names that the tenant baseline ceiling
            removes from its
             effective policy. The binding is stored verbatim, but a clamped destination never takes
             effect, so it is reported in the write response itself — no separate resolve read is needed
             to learn that an entry cannot take effect. Empty when every entry survives the baseline.
    """

    binding: EgressPolicyBinding | Unset = UNSET
    clamped: list[ClampedEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        binding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.binding, Unset):
            binding = self.binding.to_dict()

        clamped: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clamped, Unset):
            clamped = []
            for clamped_item_data in self.clamped:
                clamped_item = clamped_item_data.to_dict()
                clamped.append(clamped_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if binding is not UNSET:
            field_dict["binding"] = binding
        if clamped is not UNSET:
            field_dict["clamped"] = clamped

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clamped_entry import ClampedEntry
        from ..models.egress_policy_binding import EgressPolicyBinding

        d = dict(src_dict)
        _binding = d.pop("binding", UNSET)
        binding: EgressPolicyBinding | Unset
        if isinstance(_binding, Unset):
            binding = UNSET
        else:
            binding = EgressPolicyBinding.from_dict(_binding)

        _clamped = d.pop("clamped", UNSET)
        clamped: list[ClampedEntry] | Unset = UNSET
        if _clamped is not UNSET:
            clamped = []
            for clamped_item_data in _clamped:
                clamped_item = ClampedEntry.from_dict(clamped_item_data)

                clamped.append(clamped_item)

        set_egress_policy_binding_response = cls(
            binding=binding,
            clamped=clamped,
        )

        set_egress_policy_binding_response.additional_properties = d
        return set_egress_policy_binding_response

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
