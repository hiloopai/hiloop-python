from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calculation import Calculation
    from ..models.filter_ import Filter
    from ..models.order import Order
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="QuerySpec")


@_attrs_define
class QuerySpec:
    """A structured, server-validated query. The set of addressable columns is fixed by the canonical
    event schema; unknown columns are rejected.

       Attributes:
           run_id (str | Unset): The run (session) to query. Optional: present scopes the query to that run; absent (empty)
               makes
                the query tenant-scoped across every run — the forced tenant predicate is unchanged either way,
                so tenant isolation always holds. A saved/reusable data view that spans runs leaves this empty.
           fork_path (str | Unset): Subtree anchor: the fork-node path to scope to. Empty means the whole run.
           calculations (list[Calculation] | Unset): Aggregations to compute. Empty means return matching rows (subject to
               `limit`).
           breakdowns (list[str] | Unset): Group-by columns for the calculations. Each is a column name or a `$.`-prefixed
               JSON path into
                `attributes_json` (e.g. `$.gen_ai.request.temperature`), so a breakdown can target an arbitrary
                SDK-emitted attribute, not just a promoted column.
           filters (list[Filter] | Unset): Conjunctive (AND-ed) typed predicates.
           time_range (TimeRange | Unset): Inclusive wall-clock window in nanoseconds (matches CanonicalEvent.ts_wall_ns).
           orders (list[Order] | Unset):
           limit (int | Unset): Row cap; clamped server-side to a maximum.
    """

    run_id: str | Unset = UNSET
    fork_path: str | Unset = UNSET
    calculations: list[Calculation] | Unset = UNSET
    breakdowns: list[str] | Unset = UNSET
    filters: list[Filter] | Unset = UNSET
    time_range: TimeRange | Unset = UNSET
    orders: list[Order] | Unset = UNSET
    limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        fork_path = self.fork_path

        calculations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.calculations, Unset):
            calculations = []
            for calculations_item_data in self.calculations:
                calculations_item = calculations_item_data.to_dict()
                calculations.append(calculations_item)

        breakdowns: list[str] | Unset = UNSET
        if not isinstance(self.breakdowns, Unset):
            breakdowns = self.breakdowns

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if fork_path is not UNSET:
            field_dict["forkPath"] = fork_path
        if calculations is not UNSET:
            field_dict["calculations"] = calculations
        if breakdowns is not UNSET:
            field_dict["breakdowns"] = breakdowns
        if filters is not UNSET:
            field_dict["filters"] = filters
        if time_range is not UNSET:
            field_dict["timeRange"] = time_range
        if orders is not UNSET:
            field_dict["orders"] = orders
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calculation import Calculation
        from ..models.filter_ import Filter
        from ..models.order import Order
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        run_id = d.pop("runId", UNSET)

        fork_path = d.pop("forkPath", UNSET)

        _calculations = d.pop("calculations", UNSET)
        calculations: list[Calculation] | Unset = UNSET
        if _calculations is not UNSET:
            calculations = []
            for calculations_item_data in _calculations:
                calculations_item = Calculation.from_dict(calculations_item_data)

                calculations.append(calculations_item)

        breakdowns = cast(list[str], d.pop("breakdowns", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: list[Filter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = Filter.from_dict(filters_item_data)

                filters.append(filters_item)

        _time_range = d.pop("timeRange", UNSET)
        time_range: TimeRange | Unset
        if isinstance(_time_range, Unset):
            time_range = UNSET
        else:
            time_range = TimeRange.from_dict(_time_range)

        _orders = d.pop("orders", UNSET)
        orders: list[Order] | Unset = UNSET
        if _orders is not UNSET:
            orders = []
            for orders_item_data in _orders:
                orders_item = Order.from_dict(orders_item_data)

                orders.append(orders_item)

        limit = d.pop("limit", UNSET)

        query_spec = cls(
            run_id=run_id,
            fork_path=fork_path,
            calculations=calculations,
            breakdowns=breakdowns,
            filters=filters,
            time_range=time_range,
            orders=orders,
            limit=limit,
        )

        query_spec.additional_properties = d
        return query_spec

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
