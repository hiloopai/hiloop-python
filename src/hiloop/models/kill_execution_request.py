from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kill_execution_request_signal import KillExecutionRequestSignal
from ..types import UNSET, Unset

T = TypeVar("T", bound="KillExecutionRequest")


@_attrs_define
class KillExecutionRequest:
    """Retired provider-interactive compatibility request. Clean sandbox-cell deployments return
    unsupported.

       Attributes:
           execution_id (str | Unset):
           signal (KillExecutionRequestSignal | Unset): Signal to deliver. TERMINATE is used when unspecified.
    """

    execution_id: str | Unset = UNSET
    signal: KillExecutionRequestSignal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        signal: str | Unset = UNSET
        if not isinstance(self.signal, Unset):
            signal = self.signal.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_id is not UNSET:
            field_dict["execution_id"] = execution_id
        if signal is not UNSET:
            field_dict["signal"] = signal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("execution_id", UNSET)

        _signal = d.pop("signal", UNSET)
        signal: KillExecutionRequestSignal | Unset
        if isinstance(_signal, Unset):
            signal = UNSET
        else:
            signal = KillExecutionRequestSignal(_signal)

        kill_execution_request = cls(
            execution_id=execution_id,
            signal=signal,
        )

        kill_execution_request.additional_properties = d
        return kill_execution_request

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
