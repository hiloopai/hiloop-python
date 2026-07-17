from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.minted_port_exposure import MintedPortExposure


T = TypeVar("T", bound="ExposePortResponse")


@_attrs_define
class ExposePortResponse:
    """
    Attributes:
        exposure (MintedPortExposure | Unset): A newly activated exposure and its one-time credential.
    """

    exposure: MintedPortExposure | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exposure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exposure, Unset):
            exposure = self.exposure.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exposure is not UNSET:
            field_dict["exposure"] = exposure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.minted_port_exposure import MintedPortExposure

        d = dict(src_dict)
        _exposure = d.pop("exposure", UNSET)
        exposure: MintedPortExposure | Unset
        if isinstance(_exposure, Unset):
            exposure = UNSET
        else:
            exposure = MintedPortExposure.from_dict(_exposure)

        expose_port_response = cls(
            exposure=exposure,
        )

        expose_port_response.additional_properties = d
        return expose_port_response

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
