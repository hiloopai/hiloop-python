from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artifact import Artifact


T = TypeVar("T", bound="GetArtifactResponse")


@_attrs_define
class GetArtifactResponse:
    """
    Attributes:
        artifact (Artifact | Unset):
        bytes_ (str | Unset):
    """

    artifact: Artifact | Unset = UNSET
    bytes_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artifact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.artifact, Unset):
            artifact = self.artifact.to_dict()

        bytes_ = self.bytes_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifact is not UNSET:
            field_dict["artifact"] = artifact
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artifact import Artifact

        d = dict(src_dict)
        _artifact = d.pop("artifact", UNSET)
        artifact: Artifact | Unset
        if isinstance(_artifact, Unset):
            artifact = UNSET
        else:
            artifact = Artifact.from_dict(_artifact)

        bytes_ = d.pop("bytes", UNSET)

        get_artifact_response = cls(
            artifact=artifact,
            bytes_=bytes_,
        )

        get_artifact_response.additional_properties = d
        return get_artifact_response

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
