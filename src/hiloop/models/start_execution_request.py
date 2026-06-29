from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.command_spec import CommandSpec


T = TypeVar("T", bound="StartExecutionRequest")


@_attrs_define
class StartExecutionRequest:
    """Start an interactive command execution that can be streamed and driven over time.

    Attributes:
        sandbox_id (str | Unset):
        command (CommandSpec | Unset):
        stdin (str | Unset): Optional bytes written to the process's standard input at start.
        pty (bool | Unset): Allocate a pseudo-terminal for the execution.
    """

    sandbox_id: str | Unset = UNSET
    command: CommandSpec | Unset = UNSET
    stdin: str | Unset = UNSET
    pty: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        command: dict[str, Any] | Unset = UNSET
        if not isinstance(self.command, Unset):
            command = self.command.to_dict()

        stdin = self.stdin

        pty = self.pty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sandbox_id is not UNSET:
            field_dict["sandboxId"] = sandbox_id
        if command is not UNSET:
            field_dict["command"] = command
        if stdin is not UNSET:
            field_dict["stdin"] = stdin
        if pty is not UNSET:
            field_dict["pty"] = pty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.command_spec import CommandSpec

        d = dict(src_dict)
        sandbox_id = d.pop("sandboxId", UNSET)

        _command = d.pop("command", UNSET)
        command: CommandSpec | Unset
        if isinstance(_command, Unset):
            command = UNSET
        else:
            command = CommandSpec.from_dict(_command)

        stdin = d.pop("stdin", UNSET)

        pty = d.pop("pty", UNSET)

        start_execution_request = cls(
            sandbox_id=sandbox_id,
            command=command,
            stdin=stdin,
            pty=pty,
        )

        start_execution_request.additional_properties = d
        return start_execution_request

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
