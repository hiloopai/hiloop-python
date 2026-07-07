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
           created_by (str | Unset): The stable id of the principal that created the run — the API key (or user) that
               performed the
                start or fork, recorded server-side. Empty when unrecorded.
           started_at (str | Unset): When the run started executing (RFC 3339), empty if it has not started.
           ended_at (str | Unset): When the run finished (RFC 3339), empty if it is still in flight.
           created_at (str | Unset): When the run record was created (RFC 3339).
           parent_run_id (str | Unset): The run this run forked from. Empty for a tree root.
           root_run_id (str | Unset): The root of this run's tree (equal to id for a root). Lets the whole tree resolve in
               one
                indexed lookup.
           lineage_path (str | Unset): The materialized path of run ids from the root to this run, as a dotted label (e.g.
                "root_ulid.child_ulid"). Sorts in creation order and addresses the subtree by prefix.
           branch_event_id (str | Unset): The parent event id this run forked at — the divergence point on the parent's
               timeline. Empty
                for a tree root or a manually started new tree.
           branch_hlc_wall_ns (str | Unset): The parent branch-point wall-clock time in nanoseconds (the cursor coordinate
               the timeline
                uses). Zero when there is no branch point.
           branch_hlc_logical (str | Unset): The parent branch-point logical tiebreak that pairs with branch_hlc_wall_ns.
               Zero when there is
                no branch point.
           sandbox_id (str | Unset): The sandbox executing (or last to execute) this run, when the run is sandbox-backed.
               Empty for
                a run with no sandbox (e.g. a local wrapped run).
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
    parent_run_id: str | Unset = UNSET
    root_run_id: str | Unset = UNSET
    lineage_path: str | Unset = UNSET
    branch_event_id: str | Unset = UNSET
    branch_hlc_wall_ns: str | Unset = UNSET
    branch_hlc_logical: str | Unset = UNSET
    sandbox_id: str | Unset = UNSET
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

        parent_run_id = self.parent_run_id

        root_run_id = self.root_run_id

        lineage_path = self.lineage_path

        branch_event_id = self.branch_event_id

        branch_hlc_wall_ns = self.branch_hlc_wall_ns

        branch_hlc_logical = self.branch_hlc_logical

        sandbox_id = self.sandbox_id

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
        if parent_run_id is not UNSET:
            field_dict["parentRunId"] = parent_run_id
        if root_run_id is not UNSET:
            field_dict["rootRunId"] = root_run_id
        if lineage_path is not UNSET:
            field_dict["lineagePath"] = lineage_path
        if branch_event_id is not UNSET:
            field_dict["branchEventId"] = branch_event_id
        if branch_hlc_wall_ns is not UNSET:
            field_dict["branchHlcWallNs"] = branch_hlc_wall_ns
        if branch_hlc_logical is not UNSET:
            field_dict["branchHlcLogical"] = branch_hlc_logical
        if sandbox_id is not UNSET:
            field_dict["sandboxId"] = sandbox_id

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

        parent_run_id = d.pop("parentRunId", UNSET)

        root_run_id = d.pop("rootRunId", UNSET)

        lineage_path = d.pop("lineagePath", UNSET)

        branch_event_id = d.pop("branchEventId", UNSET)

        branch_hlc_wall_ns = d.pop("branchHlcWallNs", UNSET)

        branch_hlc_logical = d.pop("branchHlcLogical", UNSET)

        sandbox_id = d.pop("sandboxId", UNSET)

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
            parent_run_id=parent_run_id,
            root_run_id=root_run_id,
            lineage_path=lineage_path,
            branch_event_id=branch_event_id,
            branch_hlc_wall_ns=branch_hlc_wall_ns,
            branch_hlc_logical=branch_hlc_logical,
            sandbox_id=sandbox_id,
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
