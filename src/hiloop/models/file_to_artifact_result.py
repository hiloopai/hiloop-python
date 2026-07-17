from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileToArtifactResult")


@_attrs_define
class FileToArtifactResult:
    """The report of a succeeded file-to-artifact export.

    Attributes:
        artifact_id (str | Unset): The artifact the file's bytes were archived into.
        path (str | Unset): The sandbox path that was exported.
        media_type (str | Unset):
        size_bytes (str | Unset):
    """

    artifact_id: str | Unset = UNSET
    path: str | Unset = UNSET
    media_type: str | Unset = UNSET
    size_bytes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artifact_id = self.artifact_id

        path = self.path

        media_type = self.media_type

        size_bytes = self.size_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifact_id is not UNSET:
            field_dict["artifact_id"] = artifact_id
        if path is not UNSET:
            field_dict["path"] = path
        if media_type is not UNSET:
            field_dict["media_type"] = media_type
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        artifact_id = d.pop("artifact_id", UNSET)

        path = d.pop("path", UNSET)

        media_type = d.pop("media_type", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        file_to_artifact_result = cls(
            artifact_id=artifact_id,
            path=path,
            media_type=media_type,
            size_bytes=size_bytes,
        )

        file_to_artifact_result.additional_properties = d
        return file_to_artifact_result

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
