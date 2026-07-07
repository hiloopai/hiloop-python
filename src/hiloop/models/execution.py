from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_error import ExecutionError


T = TypeVar("T", bound="Execution")


@_attrs_define
class Execution:
    """
    Attributes:
        id (str | Unset):
        tenant_id (str | Unset):
        sandbox_id (str | Unset):
        state (str | Unset):
        exit_code (str | Unset): Process exit code. Absent until the process exit is observed; a failed execution whose
            exit was
             never seen carries no exit code.
        stdout_artifact_id (str | Unset):
        stderr_artifact_id (str | Unset):
        error (ExecutionError | Unset): Why an execution failed, when it did.
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    sandbox_id: str | Unset = UNSET
    state: str | Unset = UNSET
    exit_code: str | Unset = UNSET
    stdout_artifact_id: str | Unset = UNSET
    stderr_artifact_id: str | Unset = UNSET
    error: ExecutionError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        sandbox_id = self.sandbox_id

        state = self.state

        exit_code = self.exit_code

        stdout_artifact_id = self.stdout_artifact_id

        stderr_artifact_id = self.stderr_artifact_id

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if sandbox_id is not UNSET:
            field_dict["sandboxId"] = sandbox_id
        if state is not UNSET:
            field_dict["state"] = state
        if exit_code is not UNSET:
            field_dict["exitCode"] = exit_code
        if stdout_artifact_id is not UNSET:
            field_dict["stdoutArtifactId"] = stdout_artifact_id
        if stderr_artifact_id is not UNSET:
            field_dict["stderrArtifactId"] = stderr_artifact_id
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_error import ExecutionError

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        sandbox_id = d.pop("sandboxId", UNSET)

        state = d.pop("state", UNSET)

        exit_code = d.pop("exitCode", UNSET)

        stdout_artifact_id = d.pop("stdoutArtifactId", UNSET)

        stderr_artifact_id = d.pop("stderrArtifactId", UNSET)

        _error = d.pop("error", UNSET)
        error: ExecutionError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ExecutionError.from_dict(_error)

        execution = cls(
            id=id,
            tenant_id=tenant_id,
            sandbox_id=sandbox_id,
            state=state,
            exit_code=exit_code,
            stdout_artifact_id=stdout_artifact_id,
            stderr_artifact_id=stderr_artifact_id,
            error=error,
        )

        execution.additional_properties = d
        return execution

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
