from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecExit")


@_attrs_define
class ExecExit:
    """Final disposition of an interactive execution.

    Attributes:
        exit_code (str | Unset): Process exit code. Meaningful only when the process exited normally.
        signal (int | Unset): Terminating signal number, or 0 when the process exited normally.
    """

    exit_code: str | Unset = UNSET
    signal: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exit_code = self.exit_code

        signal = self.signal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exit_code is not UNSET:
            field_dict["exitCode"] = exit_code
        if signal is not UNSET:
            field_dict["signal"] = signal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exit_code = d.pop("exitCode", UNSET)

        signal = d.pop("signal", UNSET)

        exec_exit = cls(
            exit_code=exit_code,
            signal=signal,
        )

        exec_exit.additional_properties = d
        return exec_exit

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
