from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egress_policy_binding import EgressPolicyBinding


T = TypeVar("T", bound="ListEgressPolicyBindingsResponse")


@_attrs_define
class ListEgressPolicyBindingsResponse:
    """
    Attributes:
        bindings (list[EgressPolicyBinding] | Unset): The tenant's egress-policy bindings, by selector.
    """

    bindings: list[EgressPolicyBinding] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bindings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bindings, Unset):
            bindings = []
            for bindings_item_data in self.bindings:
                bindings_item = bindings_item_data.to_dict()
                bindings.append(bindings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bindings is not UNSET:
            field_dict["bindings"] = bindings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egress_policy_binding import EgressPolicyBinding

        d = dict(src_dict)
        _bindings = d.pop("bindings", UNSET)
        bindings: list[EgressPolicyBinding] | Unset = UNSET
        if _bindings is not UNSET:
            bindings = []
            for bindings_item_data in _bindings:
                bindings_item = EgressPolicyBinding.from_dict(bindings_item_data)

                bindings.append(bindings_item)

        list_egress_policy_bindings_response = cls(
            bindings=bindings,
        )

        list_egress_policy_bindings_response.additional_properties = d
        return list_egress_policy_bindings_response

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
