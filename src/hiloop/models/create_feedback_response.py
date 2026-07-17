from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFeedbackResponse")


@_attrs_define
class CreateFeedbackResponse:
    """
    Attributes:
        id (str | Unset): The stored report's id.
        relayed (bool | Unset): Whether the report was surfaced to the team's review channel. The report is stored
            either way,
             so a `false` here never means the feedback was lost.
    """

    id: str | Unset = UNSET
    relayed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        relayed = self.relayed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if relayed is not UNSET:
            field_dict["relayed"] = relayed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        relayed = d.pop("relayed", UNSET)

        create_feedback_response = cls(
            id=id,
            relayed=relayed,
        )

        create_feedback_response.additional_properties = d
        return create_feedback_response

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
