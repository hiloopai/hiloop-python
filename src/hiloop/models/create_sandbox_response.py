from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation import Operation
    from ..models.sandbox import Sandbox


T = TypeVar("T", bound="CreateSandboxResponse")


@_attrs_define
class CreateSandboxResponse:
    """
    Attributes:
        sandbox (Sandbox | Unset):
        operation (Operation | Unset):
    """

    sandbox: Sandbox | Unset = UNSET
    operation: Operation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sandbox, Unset):
            sandbox = self.sandbox.to_dict()

        operation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sandbox is not UNSET:
            field_dict["sandbox"] = sandbox
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.operation import Operation
        from ..models.sandbox import Sandbox

        d = dict(src_dict)
        _sandbox = d.pop("sandbox", UNSET)
        sandbox: Sandbox | Unset
        if isinstance(_sandbox, Unset):
            sandbox = UNSET
        else:
            sandbox = Sandbox.from_dict(_sandbox)

        _operation = d.pop("operation", UNSET)
        operation: Operation | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = Operation.from_dict(_operation)

        create_sandbox_response = cls(
            sandbox=sandbox,
            operation=operation,
        )

        create_sandbox_response.additional_properties = d
        return create_sandbox_response

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
