from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSnapshotRequest")


@_attrs_define
class CreateSnapshotRequest:
    """Retired snapshot compatibility request. Clean sandbox-cell deployments return unsupported; use
    a BranchFS workspace plus stop/resume for filesystem continuity.

       Attributes:
           sandbox_id (str | Unset):
           contents (str | Unset): Requested snapshot semantics. Omitted requests the `filesystem` baseline capture.
           allow_fallback (bool | Unset):
           retention_class (str | Unset):
           ttl_secs (str | Unset):
           legal_hold (bool | Unset):
           verification_probe_path (str | Unset): Optional path to a stable file whose bytes should be recorded at capture
               time and verified after
                every restore of this snapshot. Callers should quiesce writes to this path before requesting the
                snapshot.
           name (str | Unset): Optional user-assigned snapshot name. Names are not enforced unique; where a name is unique
                within its project, the snapshot is addressable by it wherever a snapshot id is accepted.
           description (str | Unset): Optional user-assigned free-text description.
    """

    sandbox_id: str | Unset = UNSET
    contents: str | Unset = UNSET
    allow_fallback: bool | Unset = UNSET
    retention_class: str | Unset = UNSET
    ttl_secs: str | Unset = UNSET
    legal_hold: bool | Unset = UNSET
    verification_probe_path: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        contents = self.contents

        allow_fallback = self.allow_fallback

        retention_class = self.retention_class

        ttl_secs = self.ttl_secs

        legal_hold = self.legal_hold

        verification_probe_path = self.verification_probe_path

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sandbox_id is not UNSET:
            field_dict["sandbox_id"] = sandbox_id
        if contents is not UNSET:
            field_dict["contents"] = contents
        if allow_fallback is not UNSET:
            field_dict["allow_fallback"] = allow_fallback
        if retention_class is not UNSET:
            field_dict["retention_class"] = retention_class
        if ttl_secs is not UNSET:
            field_dict["ttl_secs"] = ttl_secs
        if legal_hold is not UNSET:
            field_dict["legal_hold"] = legal_hold
        if verification_probe_path is not UNSET:
            field_dict["verification_probe_path"] = verification_probe_path
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id", UNSET)

        contents = d.pop("contents", UNSET)

        allow_fallback = d.pop("allow_fallback", UNSET)

        retention_class = d.pop("retention_class", UNSET)

        ttl_secs = d.pop("ttl_secs", UNSET)

        legal_hold = d.pop("legal_hold", UNSET)

        verification_probe_path = d.pop("verification_probe_path", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        create_snapshot_request = cls(
            sandbox_id=sandbox_id,
            contents=contents,
            allow_fallback=allow_fallback,
            retention_class=retention_class,
            ttl_secs=ttl_secs,
            legal_hold=legal_hold,
            verification_probe_path=verification_probe_path,
            name=name,
            description=description,
        )

        create_snapshot_request.additional_properties = d
        return create_snapshot_request

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
