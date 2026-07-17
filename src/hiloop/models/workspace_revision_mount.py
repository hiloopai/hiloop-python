from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceRevisionMount")


@_attrs_define
class WorkspaceRevisionMount:
    """One writable, copy-on-write BranchFS workspace mounted into a sandbox. The tenant comes only
    from the authenticated request scope and is never caller-supplied. Node paths, sockets, writer
    fences, and backend handles remain internal to the selected cell.

       Attributes:
           revision_ref (str | Unset): Exact immutable base: branchfs:v1:REPOSITORY_HEX:CHANGE_HEX, with respectively 32
               and 64
                lowercase hexadecimal characters. Mutable names, branches, latest aliases, paths, URLs, and
                all-zero identities are rejected.
           target_path (str | Unset): Absolute in-sandbox mount path. It must match the selected immutable runtime plan's
               workspace
                path (the standard CPU/GPU plans use /workspace).
    """

    revision_ref: str | Unset = UNSET
    target_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revision_ref = self.revision_ref

        target_path = self.target_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if revision_ref is not UNSET:
            field_dict["revision_ref"] = revision_ref
        if target_path is not UNSET:
            field_dict["target_path"] = target_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revision_ref = d.pop("revision_ref", UNSET)

        target_path = d.pop("target_path", UNSET)

        workspace_revision_mount = cls(
            revision_ref=revision_ref,
            target_path=target_path,
        )

        workspace_revision_mount.additional_properties = d
        return workspace_revision_mount

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
