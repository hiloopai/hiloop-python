from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox import Sandbox
    from ..models.sandbox_describe import SandboxDescribe


T = TypeVar("T", bound="GetSandboxResponse")


@_attrs_define
class GetSandboxResponse:
    """
    Attributes:
        sandbox (Sandbox | Unset):
        describe (SandboxDescribe | Unset): Describe-altitude detail for one sandbox: what it runs, what it asked for,
            where it is in its
             lifecycle, and what recently happened to it. Returned only by GetSandbox; list rows stay lean.
    """

    sandbox: Sandbox | Unset = UNSET
    describe: SandboxDescribe | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sandbox, Unset):
            sandbox = self.sandbox.to_dict()

        describe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.describe, Unset):
            describe = self.describe.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sandbox is not UNSET:
            field_dict["sandbox"] = sandbox
        if describe is not UNSET:
            field_dict["describe"] = describe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox import Sandbox
        from ..models.sandbox_describe import SandboxDescribe

        d = dict(src_dict)
        _sandbox = d.pop("sandbox", UNSET)
        sandbox: Sandbox | Unset
        if isinstance(_sandbox, Unset):
            sandbox = UNSET
        else:
            sandbox = Sandbox.from_dict(_sandbox)

        _describe = d.pop("describe", UNSET)
        describe: SandboxDescribe | Unset
        if isinstance(_describe, Unset):
            describe = UNSET
        else:
            describe = SandboxDescribe.from_dict(_describe)

        get_sandbox_response = cls(
            sandbox=sandbox,
            describe=describe,
        )

        get_sandbox_response.additional_properties = d
        return get_sandbox_response

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
