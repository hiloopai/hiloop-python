from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution import Execution
    from ..models.operation import Operation


T = TypeVar("T", bound="ExecuteSandboxResponse")


@_attrs_define
class ExecuteSandboxResponse:
    """
    Attributes:
        execution (Execution | Unset):
        operation (Operation | Unset):
    """

    execution: Execution | Unset = UNSET
    operation: Operation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution, Unset):
            execution = self.execution.to_dict()

        operation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution is not UNSET:
            field_dict["execution"] = execution
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution import Execution
        from ..models.operation import Operation

        d = dict(src_dict)
        _execution = d.pop("execution", UNSET)
        execution: Execution | Unset
        if isinstance(_execution, Unset):
            execution = UNSET
        else:
            execution = Execution.from_dict(_execution)

        _operation = d.pop("operation", UNSET)
        operation: Operation | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = Operation.from_dict(_operation)

        execute_sandbox_response = cls(
            execution=execution,
            operation=operation,
        )

        execute_sandbox_response.additional_properties = d
        return execute_sandbox_response

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
