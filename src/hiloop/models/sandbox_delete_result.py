from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxDeleteResult")


@_attrs_define
class SandboxDeleteResult:
    """Public-safe versioning evidence from deleting a sandbox backed by a versioned BranchFS
    workspace. Cell-local routes, prepared references, backend receipt IDs, nodes, paths, sockets,
    epochs, and writer fences never cross this boundary. Scratch-workspace deletes have no result.

       Attributes:
           versioned_workspace (bool | Unset): Always true for this result variant; allows additive clients to distinguish
               it explicitly.
           repository_id (str | Unset): Durable BranchFS repository whose writer epoch was sealed.
           base_change_id (str | Unset): Immutable change from which the deleted sandbox workspace began.
           sealed_change_id (str | Unset): Newly sealed immutable change containing the sandbox's terminal workspace
               contents.
           checkpoint_sequence (str | Unset): Exact acknowledged terminal workspace WAL sequence.
           checkpoint_prefix_hash (str | Unset): Lowercase-hex hash of the exact acknowledged terminal WAL prefix.
    """

    versioned_workspace: bool | Unset = UNSET
    repository_id: str | Unset = UNSET
    base_change_id: str | Unset = UNSET
    sealed_change_id: str | Unset = UNSET
    checkpoint_sequence: str | Unset = UNSET
    checkpoint_prefix_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        versioned_workspace = self.versioned_workspace

        repository_id = self.repository_id

        base_change_id = self.base_change_id

        sealed_change_id = self.sealed_change_id

        checkpoint_sequence = self.checkpoint_sequence

        checkpoint_prefix_hash = self.checkpoint_prefix_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if versioned_workspace is not UNSET:
            field_dict["versioned_workspace"] = versioned_workspace
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if base_change_id is not UNSET:
            field_dict["base_change_id"] = base_change_id
        if sealed_change_id is not UNSET:
            field_dict["sealed_change_id"] = sealed_change_id
        if checkpoint_sequence is not UNSET:
            field_dict["checkpoint_sequence"] = checkpoint_sequence
        if checkpoint_prefix_hash is not UNSET:
            field_dict["checkpoint_prefix_hash"] = checkpoint_prefix_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        versioned_workspace = d.pop("versioned_workspace", UNSET)

        repository_id = d.pop("repository_id", UNSET)

        base_change_id = d.pop("base_change_id", UNSET)

        sealed_change_id = d.pop("sealed_change_id", UNSET)

        checkpoint_sequence = d.pop("checkpoint_sequence", UNSET)

        checkpoint_prefix_hash = d.pop("checkpoint_prefix_hash", UNSET)

        sandbox_delete_result = cls(
            versioned_workspace=versioned_workspace,
            repository_id=repository_id,
            base_change_id=base_change_id,
            sealed_change_id=sealed_change_id,
            checkpoint_sequence=checkpoint_sequence,
            checkpoint_prefix_hash=checkpoint_prefix_hash,
        )

        sandbox_delete_result.additional_properties = d
        return sandbox_delete_result

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
