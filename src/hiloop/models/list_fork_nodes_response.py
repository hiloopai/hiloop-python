from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fork_node import ForkNode


T = TypeVar("T", bound="ListForkNodesResponse")


@_attrs_define
class ListForkNodesResponse:
    """
    Attributes:
        fork_nodes (list[ForkNode] | Unset): The fork tree, ordered by fork path (breadth-first within each level).
    """

    fork_nodes: list[ForkNode] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fork_nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fork_nodes, Unset):
            fork_nodes = []
            for fork_nodes_item_data in self.fork_nodes:
                fork_nodes_item = fork_nodes_item_data.to_dict()
                fork_nodes.append(fork_nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fork_nodes is not UNSET:
            field_dict["forkNodes"] = fork_nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fork_node import ForkNode

        d = dict(src_dict)
        _fork_nodes = d.pop("forkNodes", UNSET)
        fork_nodes: list[ForkNode] | Unset = UNSET
        if _fork_nodes is not UNSET:
            fork_nodes = []
            for fork_nodes_item_data in _fork_nodes:
                fork_nodes_item = ForkNode.from_dict(fork_nodes_item_data)

                fork_nodes.append(fork_nodes_item)

        list_fork_nodes_response = cls(
            fork_nodes=fork_nodes,
        )

        list_fork_nodes_response.additional_properties = d
        return list_fork_nodes_response

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
