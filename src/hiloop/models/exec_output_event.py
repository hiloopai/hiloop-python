from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exec_exit import ExecExit


T = TypeVar("T", bound="ExecOutputEvent")


@_attrs_define
class ExecOutputEvent:
    """One framed event in an execution's combined output stream.

    Attributes:
        stdout_chunk (str | Unset): A chunk of standard output bytes.
        stderr_chunk (str | Unset): A chunk of standard error bytes.
        exit_ (ExecExit | Unset): Final disposition of an interactive execution.
    """

    stdout_chunk: str | Unset = UNSET
    stderr_chunk: str | Unset = UNSET
    exit_: ExecExit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stdout_chunk = self.stdout_chunk

        stderr_chunk = self.stderr_chunk

        exit_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exit_, Unset):
            exit_ = self.exit_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stdout_chunk is not UNSET:
            field_dict["stdoutChunk"] = stdout_chunk
        if stderr_chunk is not UNSET:
            field_dict["stderrChunk"] = stderr_chunk
        if exit_ is not UNSET:
            field_dict["exit"] = exit_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exec_exit import ExecExit

        d = dict(src_dict)
        stdout_chunk = d.pop("stdoutChunk", UNSET)

        stderr_chunk = d.pop("stderrChunk", UNSET)

        _exit_ = d.pop("exit", UNSET)
        exit_: ExecExit | Unset
        if isinstance(_exit_, Unset):
            exit_ = UNSET
        else:
            exit_ = ExecExit.from_dict(_exit_)

        exec_output_event = cls(
            stdout_chunk=stdout_chunk,
            stderr_chunk=stderr_chunk,
            exit_=exit_,
        )

        exec_output_event.additional_properties = d
        return exec_output_event

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
