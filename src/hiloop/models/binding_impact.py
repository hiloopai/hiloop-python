from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egress_policy import EgressPolicy


T = TypeVar("T", bound="BindingImpact")


@_attrs_define
class BindingImpact:
    """One binding's effective-policy change under a proposed baseline. `before` is its effective policy
    under the current baseline; `after` is what it would become under the proposed one. `added`/
    `removed` are the destinations that would become reachable / unreachable for a principal matching
    the selector. The synthetic selector "baseline" reports the change to the default class (the
    principals that match no binding).

       Attributes:
           selector (str | Unset): The binding's selector, or "baseline" for the default class.
           before (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
               EGRESS_MODE_UNSPECIFIED leaves
                outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
                runtime supports.
           after (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
               EGRESS_MODE_UNSPECIFIED leaves
                outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
                runtime supports.
           added (list[str] | Unset): Destinations that become reachable for this selector under the proposed baseline.
           removed (list[str] | Unset): Destinations that become unreachable for this selector under the proposed baseline.
    """

    selector: str | Unset = UNSET
    before: EgressPolicy | Unset = UNSET
    after: EgressPolicy | Unset = UNSET
    added: list[str] | Unset = UNSET
    removed: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        selector = self.selector

        before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.before, Unset):
            before = self.before.to_dict()

        after: dict[str, Any] | Unset = UNSET
        if not isinstance(self.after, Unset):
            after = self.after.to_dict()

        added: list[str] | Unset = UNSET
        if not isinstance(self.added, Unset):
            added = self.added

        removed: list[str] | Unset = UNSET
        if not isinstance(self.removed, Unset):
            removed = self.removed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selector is not UNSET:
            field_dict["selector"] = selector
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after
        if added is not UNSET:
            field_dict["added"] = added
        if removed is not UNSET:
            field_dict["removed"] = removed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egress_policy import EgressPolicy

        d = dict(src_dict)
        selector = d.pop("selector", UNSET)

        _before = d.pop("before", UNSET)
        before: EgressPolicy | Unset
        if isinstance(_before, Unset):
            before = UNSET
        else:
            before = EgressPolicy.from_dict(_before)

        _after = d.pop("after", UNSET)
        after: EgressPolicy | Unset
        if isinstance(_after, Unset):
            after = UNSET
        else:
            after = EgressPolicy.from_dict(_after)

        added = cast(list[str], d.pop("added", UNSET))

        removed = cast(list[str], d.pop("removed", UNSET))

        binding_impact = cls(
            selector=selector,
            before=before,
            after=after,
            added=added,
            removed=removed,
        )

        binding_impact.additional_properties = d
        return binding_impact

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
