from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VolumeAttachment")


@_attrs_define
class VolumeAttachment:
    """A live volume attachment: a volume mounted into a sandbox at a path, pinned to the version the
    attach resolved. The record is the handle a later detach names.

       Attributes:
           id (str | Unset): The attachment id — the handle DetachVolume takes.
           volume_id (str | Unset): The attached volume.
           sandbox_id (str | Unset): The sandbox the volume is mounted into.
           version_digest (str | Unset): The version pinned at attach time (`blake3:<hex>`). A later publish never moves
               it.
           target_path (str | Unset): The absolute path the volume is mounted at inside the sandbox.
           created_at (str | Unset): When the attachment was admitted (RFC 3339).
    """

    id: str | Unset = UNSET
    volume_id: str | Unset = UNSET
    sandbox_id: str | Unset = UNSET
    version_digest: str | Unset = UNSET
    target_path: str | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        volume_id = self.volume_id

        sandbox_id = self.sandbox_id

        version_digest = self.version_digest

        target_path = self.target_path

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if volume_id is not UNSET:
            field_dict["volume_id"] = volume_id
        if sandbox_id is not UNSET:
            field_dict["sandbox_id"] = sandbox_id
        if version_digest is not UNSET:
            field_dict["version_digest"] = version_digest
        if target_path is not UNSET:
            field_dict["target_path"] = target_path
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        volume_id = d.pop("volume_id", UNSET)

        sandbox_id = d.pop("sandbox_id", UNSET)

        version_digest = d.pop("version_digest", UNSET)

        target_path = d.pop("target_path", UNSET)

        created_at = d.pop("created_at", UNSET)

        volume_attachment = cls(
            id=id,
            volume_id=volume_id,
            sandbox_id=sandbox_id,
            version_digest=version_digest,
            target_path=target_path,
            created_at=created_at,
        )

        volume_attachment.additional_properties = d
        return volume_attachment

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
