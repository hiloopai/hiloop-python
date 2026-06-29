from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForkNode")


@_attrs_define
class ForkNode:
    """A fork-tree node: one position in a run's fork lineage, shared with telemetry.

    Attributes:
        id (str | Unset): The fork node id (a client-supplied ULID, shared with telemetry).
        run_id (str | Unset): The run this fork node belongs to.
        fork_path (str | Unset): The gap-free fork path as a dotted ltree label (e.g. "1.2.1").
        parent_fork_node_id (str | Unset): The parent fork node id, empty for a root node.
        status (str | Unset): The fork node status: active or archived.
        created_at (str | Unset): When the fork node was created (RFC 3339).
    """

    id: str | Unset = UNSET
    run_id: str | Unset = UNSET
    fork_path: str | Unset = UNSET
    parent_fork_node_id: str | Unset = UNSET
    status: str | Unset = UNSET
    created_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        run_id = self.run_id

        fork_path = self.fork_path

        parent_fork_node_id = self.parent_fork_node_id

        status = self.status

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if fork_path is not UNSET:
            field_dict["forkPath"] = fork_path
        if parent_fork_node_id is not UNSET:
            field_dict["parentForkNodeId"] = parent_fork_node_id
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        run_id = d.pop("runId", UNSET)

        fork_path = d.pop("forkPath", UNSET)

        parent_fork_node_id = d.pop("parentForkNodeId", UNSET)

        status = d.pop("status", UNSET)

        created_at = d.pop("createdAt", UNSET)

        fork_node = cls(
            id=id,
            run_id=run_id,
            fork_path=fork_path,
            parent_fork_node_id=parent_fork_node_id,
            status=status,
            created_at=created_at,
        )

        fork_node.additional_properties = d
        return fork_node

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
