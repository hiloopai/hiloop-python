from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxStateCount")


@_attrs_define
class SandboxStateCount:
    """The count of active sandboxes in one observed lifecycle state.

    Attributes:
        observed_state (str | Unset): The sandbox observed state (e.g. running, ready, paused, provisioning).
        count (str | Unset): How many non-deleted sandboxes are in this state.
    """

    observed_state: str | Unset = UNSET
    count: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observed_state = self.observed_state

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if observed_state is not UNSET:
            field_dict["observed_state"] = observed_state
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        observed_state = d.pop("observed_state", UNSET)

        count = d.pop("count", UNSET)

        sandbox_state_count = cls(
            observed_state=observed_state,
            count=count,
        )

        sandbox_state_count.additional_properties = d
        return sandbox_state_count

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
