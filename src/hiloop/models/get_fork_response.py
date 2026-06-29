from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fork import Fork


T = TypeVar("T", bound="GetForkResponse")


@_attrs_define
class GetForkResponse:
    """
    Attributes:
        fork (Fork | Unset):
    """

    fork: Fork | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fork: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fork, Unset):
            fork = self.fork.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fork is not UNSET:
            field_dict["fork"] = fork

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fork import Fork

        d = dict(src_dict)
        _fork = d.pop("fork", UNSET)
        fork: Fork | Unset
        if isinstance(_fork, Unset):
            fork = UNSET
        else:
            fork = Fork.from_dict(_fork)

        get_fork_response = cls(
            fork=fork,
        )

        get_fork_response.additional_properties = d
        return get_fork_response

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
