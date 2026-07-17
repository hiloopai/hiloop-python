from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecuteResult")


@_attrs_define
class ExecuteResult:
    """The report of a succeeded command execution.

    Attributes:
        execution_id (str | Unset): The execution row the command ran as.
        exit_code (str | Unset): The command's observed exit code.
        stdout_artifact_id (str | Unset):
        stderr_artifact_id (str | Unset):
        stdout_truncated (bool | Unset): Whether the captured stream was truncated at the runtime output limit.
        stderr_truncated (bool | Unset):
    """

    execution_id: str | Unset = UNSET
    exit_code: str | Unset = UNSET
    stdout_artifact_id: str | Unset = UNSET
    stderr_artifact_id: str | Unset = UNSET
    stdout_truncated: bool | Unset = UNSET
    stderr_truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        exit_code = self.exit_code

        stdout_artifact_id = self.stdout_artifact_id

        stderr_artifact_id = self.stderr_artifact_id

        stdout_truncated = self.stdout_truncated

        stderr_truncated = self.stderr_truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_id is not UNSET:
            field_dict["execution_id"] = execution_id
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if stdout_artifact_id is not UNSET:
            field_dict["stdout_artifact_id"] = stdout_artifact_id
        if stderr_artifact_id is not UNSET:
            field_dict["stderr_artifact_id"] = stderr_artifact_id
        if stdout_truncated is not UNSET:
            field_dict["stdout_truncated"] = stdout_truncated
        if stderr_truncated is not UNSET:
            field_dict["stderr_truncated"] = stderr_truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("execution_id", UNSET)

        exit_code = d.pop("exit_code", UNSET)

        stdout_artifact_id = d.pop("stdout_artifact_id", UNSET)

        stderr_artifact_id = d.pop("stderr_artifact_id", UNSET)

        stdout_truncated = d.pop("stdout_truncated", UNSET)

        stderr_truncated = d.pop("stderr_truncated", UNSET)

        execute_result = cls(
            execution_id=execution_id,
            exit_code=exit_code,
            stdout_artifact_id=stdout_artifact_id,
            stderr_artifact_id=stderr_artifact_id,
            stdout_truncated=stdout_truncated,
            stderr_truncated=stderr_truncated,
        )

        execute_result.additional_properties = d
        return execute_result

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
