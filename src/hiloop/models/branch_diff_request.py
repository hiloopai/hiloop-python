from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.branch_diff_spec import BranchDiffSpec


T = TypeVar("T", bound="BranchDiffRequest")


@_attrs_define
class BranchDiffRequest:
    """
    Attributes:
        spec (BranchDiffSpec | Unset): A branch-diff (Q3): the events unique to run A that are absent from run B, across
            two runs sharing
             a tree. This is the differentiated tree-native query — each run's lineage subtree is resolved
             server-side and the two are set-differenced on a semantic key (signal, name, attributes). The
             tenant is taken from request identity, never from this body.
    """

    spec: BranchDiffSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.branch_diff_spec import BranchDiffSpec

        d = dict(src_dict)
        _spec = d.pop("spec", UNSET)
        spec: BranchDiffSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = BranchDiffSpec.from_dict(_spec)

        branch_diff_request = cls(
            spec=spec,
        )

        branch_diff_request.additional_properties = d
        return branch_diff_request

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
