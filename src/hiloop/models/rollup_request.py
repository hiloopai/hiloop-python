from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rollup_spec import RollupSpec


T = TypeVar("T", bound="RollupRequest")


@_attrs_define
class RollupRequest:
    """
    Attributes:
        spec (RollupSpec | Unset): A Q4 rollup: columnar aggregation over the promoted token/cost/latency/status
            columns, grouped by
             gen_ai_model and a fixed-width wall-clock time bucket. Scoped to a single run when `run_id` is set,
             or across every run for the tenant when it is empty. Restricted to the `llm` signal so non-llm
             events never form a NULL-model group. The tenant is taken from request identity, never from this
             body.
    """

    spec: RollupSpec | Unset = UNSET
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
        from ..models.rollup_spec import RollupSpec

        d = dict(src_dict)
        _spec = d.pop("spec", UNSET)
        spec: RollupSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = RollupSpec.from_dict(_spec)

        rollup_request = cls(
            spec=spec,
        )

        rollup_request.additional_properties = d
        return rollup_request

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
