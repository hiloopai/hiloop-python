from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_execution_input_request_signal import SendExecutionInputRequestSignal
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendExecutionInputRequest")


@_attrs_define
class SendExecutionInputRequest:
    """Deliver more input to a running execution: either standard input bytes or a control signal.

    Attributes:
        execution_id (str | Unset):
        stdin (str | Unset): Bytes appended to the process's standard input.
        signal (SendExecutionInputRequestSignal | Unset): A control signal delivered to the process.
    """

    execution_id: str | Unset = UNSET
    stdin: str | Unset = UNSET
    signal: SendExecutionInputRequestSignal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        stdin = self.stdin

        signal: str | Unset = UNSET
        if not isinstance(self.signal, Unset):
            signal = self.signal.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if stdin is not UNSET:
            field_dict["stdin"] = stdin
        if signal is not UNSET:
            field_dict["signal"] = signal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("executionId", UNSET)

        stdin = d.pop("stdin", UNSET)

        _signal = d.pop("signal", UNSET)
        signal: SendExecutionInputRequestSignal | Unset
        if isinstance(_signal, Unset):
            signal = UNSET
        else:
            signal = SendExecutionInputRequestSignal(_signal)

        send_execution_input_request = cls(
            execution_id=execution_id,
            stdin=stdin,
            signal=signal,
        )

        send_execution_input_request.additional_properties = d
        return send_execution_input_request

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
