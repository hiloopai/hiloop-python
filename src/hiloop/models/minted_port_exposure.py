from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_exposure import PortExposure


T = TypeVar("T", bound="MintedPortExposure")


@_attrs_define
class MintedPortExposure:
    """A newly activated exposure and its one-time credential.

    Attributes:
        exposure (PortExposure | Unset): Public-safe metadata for one exposed sandbox port. Tokens and their stored
            digests never appear
             on list/read surfaces.
        token (str | Unset): Returned only by the call that minted this token. Empty on an identity-idempotent replay
            and
             never returned by list.
        created (bool | Unset): True when this call activated the exposure; false when it found the same identity
            active.
    """

    exposure: PortExposure | Unset = UNSET
    token: str | Unset = UNSET
    created: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exposure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exposure, Unset):
            exposure = self.exposure.to_dict()

        token = self.token

        created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exposure is not UNSET:
            field_dict["exposure"] = exposure
        if token is not UNSET:
            field_dict["token"] = token
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.port_exposure import PortExposure

        d = dict(src_dict)
        _exposure = d.pop("exposure", UNSET)
        exposure: PortExposure | Unset
        if isinstance(_exposure, Unset):
            exposure = UNSET
        else:
            exposure = PortExposure.from_dict(_exposure)

        token = d.pop("token", UNSET)

        created = d.pop("created", UNSET)

        minted_port_exposure = cls(
            exposure=exposure,
            token=token,
            created=created,
        )

        minted_port_exposure.additional_properties = d
        return minted_port_exposure

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
