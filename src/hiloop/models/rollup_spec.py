from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RollupSpec")


@_attrs_define
class RollupSpec:
    """A Q4 rollup: columnar aggregation over the promoted token/cost/latency/status columns, grouped by
    gen_ai_model and a fixed-width wall-clock time bucket. Scoped to a single run when `run_id` is set,
    or across every run for the tenant when it is empty. Restricted to the `llm` signal so non-llm
    events never form a NULL-model group. The tenant is taken from request identity, never from this
    body.

       Attributes:
           run_id (str | Unset): The run (session) to roll up. Optional: present scopes the rollup to that run; absent
               (empty)
                rolls up across every run for the tenant. The forced tenant predicate is AND-ed in either way.
           bucket_ns (str | Unset): Time-bucket width in nanoseconds; each event is grouped into `ts_wall_ns / bucket_ns`.
               Required
                and must be > 0.
           model_filter (str | Unset): Optional exact gen_ai_model to restrict to (e.g. "gpt-4"); empty means all models.
           status_min (str | Unset): Optional minimum http_status_code (inclusive) to restrict to — the error-rate lever
                (e.g. 400 keeps only >= 400). 0 means no status floor.
    """

    run_id: str | Unset = UNSET
    bucket_ns: str | Unset = UNSET
    model_filter: str | Unset = UNSET
    status_min: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        bucket_ns = self.bucket_ns

        model_filter = self.model_filter

        status_min = self.status_min

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if bucket_ns is not UNSET:
            field_dict["bucketNs"] = bucket_ns
        if model_filter is not UNSET:
            field_dict["modelFilter"] = model_filter
        if status_min is not UNSET:
            field_dict["statusMin"] = status_min

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId", UNSET)

        bucket_ns = d.pop("bucketNs", UNSET)

        model_filter = d.pop("modelFilter", UNSET)

        status_min = d.pop("statusMin", UNSET)

        rollup_spec = cls(
            run_id=run_id,
            bucket_ns=bucket_ns,
            model_filter=model_filter,
            status_min=status_min,
        )

        rollup_spec.additional_properties = d
        return rollup_spec

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
