from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StopResult")


@_attrs_define
class StopResult:
    """What a succeeded stop observed about the sandbox it brought to rest.

    Attributes:
        resumable (bool | Unset): Whether ResumeSandbox can preserve the sandbox filesystem through a sealed BranchFS
            revision.
             The clean cell path restores that revision under a fresh runtime generation; it never implies
             that process or memory state survived.
        warning (str | Unset): Human-readable continuity detail or recovery warning. A BranchFS teardown-stop uses this
            to
             state explicitly that filesystem bytes were sealed but process and memory state were not.
    """

    resumable: bool | Unset = UNSET
    warning: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resumable = self.resumable

        warning = self.warning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resumable is not UNSET:
            field_dict["resumable"] = resumable
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resumable = d.pop("resumable", UNSET)

        warning = d.pop("warning", UNSET)

        stop_result = cls(
            resumable=resumable,
            warning=warning,
        )

        stop_result.additional_properties = d
        return stop_result

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
