from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Run")


@_attrs_define
class Run:
    """A run record (the subset the API returns). Intentionally carries no cost or spend roll-up: the
    product is generic and does not surface cost by default.

       Attributes:
           id (str | Unset): The run id (a client-supplied ULID, shared with telemetry).
           tenant_id (str | Unset): The tenant the run belongs to (derived from the caller's scope, echoed for
               convenience).
           project_id (str | Unset): The project the run belongs to.
           label (str | Unset): An optional human-readable label.
           status (str | Unset): The run lifecycle status: pending, running, succeeded, failed, or canceled.
           created_by (str | Unset): The user that created the run, when recorded (empty otherwise).
           started_at (str | Unset): When the run started executing (RFC 3339), empty if it has not started.
           ended_at (str | Unset): When the run finished (RFC 3339), empty if it is still in flight.
           created_at (str | Unset): When the run record was created (RFC 3339).
           live_fork_count (str | Unset): The number of active (non-archived) fork nodes in the run's fork tree.
    """

    id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    label: str | Unset = UNSET
    status: str | Unset = UNSET
    created_by: str | Unset = UNSET
    started_at: str | Unset = UNSET
    ended_at: str | Unset = UNSET
    created_at: str | Unset = UNSET
    live_fork_count: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        project_id = self.project_id

        label = self.label

        status = self.status

        created_by = self.created_by

        started_at = self.started_at

        ended_at = self.ended_at

        created_at = self.created_at

        live_fork_count = self.live_fork_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if label is not UNSET:
            field_dict["label"] = label
        if status is not UNSET:
            field_dict["status"] = status
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if live_fork_count is not UNSET:
            field_dict["liveForkCount"] = live_fork_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        project_id = d.pop("projectId", UNSET)

        label = d.pop("label", UNSET)

        status = d.pop("status", UNSET)

        created_by = d.pop("createdBy", UNSET)

        started_at = d.pop("startedAt", UNSET)

        ended_at = d.pop("endedAt", UNSET)

        created_at = d.pop("createdAt", UNSET)

        live_fork_count = d.pop("liveForkCount", UNSET)

        run = cls(
            id=id,
            tenant_id=tenant_id,
            project_id=project_id,
            label=label,
            status=status,
            created_by=created_by,
            started_at=started_at,
            ended_at=ended_at,
            created_at=created_at,
            live_fork_count=live_fork_count,
        )

        run.additional_properties = d
        return run

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
