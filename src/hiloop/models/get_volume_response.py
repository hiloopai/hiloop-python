from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volume import Volume


T = TypeVar("T", bound="GetVolumeResponse")


@_attrs_define
class GetVolumeResponse:
    """
    Attributes:
        volume (Volume | Unset): A volume record (the subset the API returns).
    """

    volume: Volume | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume: dict[str, Any] | Unset = UNSET
        if not isinstance(self.volume, Unset):
            volume = self.volume.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volume import Volume

        d = dict(src_dict)
        _volume = d.pop("volume", UNSET)
        volume: Volume | Unset
        if isinstance(_volume, Unset):
            volume = UNSET
        else:
            volume = Volume.from_dict(_volume)

        get_volume_response = cls(
            volume=volume,
        )

        get_volume_response.additional_properties = d
        return get_volume_response

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
