from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Artifact")


@_attrs_define
class Artifact:
    """
    Attributes:
        id (str | Unset):
        tenant_id (str | Unset):
        kind (str | Unset):
        media_type (str | Unset):
        size_bytes (str | Unset):
        digest_algorithm (str | Unset):
        digest (str | Unset):
        created_at (str | Unset): When the artifact was created (RFC 3339).
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    kind: str | Unset = UNSET
    media_type: str | Unset = UNSET
    size_bytes: str | Unset = UNSET
    digest_algorithm: str | Unset = UNSET
    digest: str | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        kind = self.kind

        media_type = self.media_type

        size_bytes = self.size_bytes

        digest_algorithm = self.digest_algorithm

        digest = self.digest

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if media_type is not UNSET:
            field_dict["media_type"] = media_type
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if digest_algorithm is not UNSET:
            field_dict["digest_algorithm"] = digest_algorithm
        if digest is not UNSET:
            field_dict["digest"] = digest
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        kind = d.pop("kind", UNSET)

        media_type = d.pop("media_type", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        digest_algorithm = d.pop("digest_algorithm", UNSET)

        digest = d.pop("digest", UNSET)

        created_at = d.pop("created_at", UNSET)

        artifact = cls(
            id=id,
            tenant_id=tenant_id,
            kind=kind,
            media_type=media_type,
            size_bytes=size_bytes,
            digest_algorithm=digest_algorithm,
            digest=digest,
            created_at=created_at,
        )

        artifact.additional_properties = d
        return artifact

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
