from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proposed_egress_policy import ProposedEgressPolicy


T = TypeVar("T", bound="ResolveEffectiveEgressRequest")


@_attrs_define
class ResolveEffectiveEgressRequest:
    """
    Attributes:
        selector (str | Unset): The identity selector to resolve (see EgressPolicyBinding.selector for the grammar).
            Rejected as
             INVALID_ARGUMENT if it is not a well-formed selector.
        proposed (ProposedEgressPolicy | Unset): A proposed (unsaved) binding policy to preview at a selector's tier,
            for the rule editor's live
             "if I save this rule, what's the effective result?" preview. It is an EgressPolicy plus an optional
             enforcement override, matching a stored binding.
    """

    selector: str | Unset = UNSET
    proposed: ProposedEgressPolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        selector = self.selector

        proposed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.proposed, Unset):
            proposed = self.proposed.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selector is not UNSET:
            field_dict["selector"] = selector
        if proposed is not UNSET:
            field_dict["proposed"] = proposed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposed_egress_policy import ProposedEgressPolicy

        d = dict(src_dict)
        selector = d.pop("selector", UNSET)

        _proposed = d.pop("proposed", UNSET)
        proposed: ProposedEgressPolicy | Unset
        if isinstance(_proposed, Unset):
            proposed = UNSET
        else:
            proposed = ProposedEgressPolicy.from_dict(_proposed)

        resolve_effective_egress_request = cls(
            selector=selector,
            proposed=proposed,
        )

        resolve_effective_egress_request.additional_properties = d
        return resolve_effective_egress_request

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
