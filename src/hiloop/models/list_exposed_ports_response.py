from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_exposure import PortExposure


T = TypeVar("T", bound="ListExposedPortsResponse")


@_attrs_define
class ListExposedPortsResponse:
    """
    Attributes:
        exposures (list[PortExposure] | Unset):
    """

    exposures: list[PortExposure] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exposures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exposures, Unset):
            exposures = []
            for exposures_item_data in self.exposures:
                exposures_item = exposures_item_data.to_dict()
                exposures.append(exposures_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exposures is not UNSET:
            field_dict["exposures"] = exposures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.port_exposure import PortExposure

        d = dict(src_dict)
        _exposures = d.pop("exposures", UNSET)
        exposures: list[PortExposure] | Unset = UNSET
        if _exposures is not UNSET:
            exposures = []
            for exposures_item_data in _exposures:
                exposures_item = PortExposure.from_dict(exposures_item_data)

                exposures.append(exposures_item)

        list_exposed_ports_response = cls(
            exposures=exposures,
        )

        list_exposed_ports_response.additional_properties = d
        return list_exposed_ports_response

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
