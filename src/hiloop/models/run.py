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
           last_activity_at (str | Unset): When the run last showed a liveness signal (RFC 3339): the time of its most
               recent telemetry
                event, or started_at for a run that has emitted no events yet. Derived at read time, and only
                for a `running` run that no sandbox executes — the runs whose liveness the platform cannot
                attest. Empty for every other run, and empty when the signal is temporarily unavailable.
           stale (bool | Unset): True when last_activity_at is older than the staleness window (15 minutes): the run still
                reads `running` — no terminal state is ever recorded on the creator's behalf — but its creator
                has gone quiet, so readers should render it as `running (stale)`. Always false when
                last_activity_at is empty.
           executing_principal (str | Unset): The stable id of the identity this run executes AS: the registered workload's
               id when the
                launch declared one, otherwise the launcher's own principal id (matching created_by). Forks
                inherit it from their parent. Empty on runs that predate executing-identity recording.
           executing_kind (str | Unset): The executing identity's kind: `user`, `service_account`, or `workload`. Empty on
               runs that
                predate executing-identity recording.
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
    last_activity_at: str | Unset = UNSET
    stale: bool | Unset = UNSET
    executing_principal: str | Unset = UNSET
    executing_kind: str | Unset = UNSET
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

        last_activity_at = self.last_activity_at

        stale = self.stale

        executing_principal = self.executing_principal

        executing_kind = self.executing_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if label is not UNSET:
            field_dict["label"] = label
        if status is not UNSET:
            field_dict["status"] = status
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if parent_run_id is not UNSET:
            field_dict["parent_run_id"] = parent_run_id
        if root_run_id is not UNSET:
            field_dict["root_run_id"] = root_run_id
        if lineage_path is not UNSET:
            field_dict["lineage_path"] = lineage_path
        if branch_event_id is not UNSET:
            field_dict["branch_event_id"] = branch_event_id
        if branch_hlc_wall_ns is not UNSET:
            field_dict["branch_hlc_wall_ns"] = branch_hlc_wall_ns
        if branch_hlc_logical is not UNSET:
            field_dict["branch_hlc_logical"] = branch_hlc_logical
        if sandbox_id is not UNSET:
            field_dict["sandbox_id"] = sandbox_id
        if last_activity_at is not UNSET:
            field_dict["last_activity_at"] = last_activity_at
        if stale is not UNSET:
            field_dict["stale"] = stale
        if executing_principal is not UNSET:
            field_dict["executing_principal"] = executing_principal
        if executing_kind is not UNSET:
            field_dict["executing_kind"] = executing_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        project_id = d.pop("project_id", UNSET)

        label = d.pop("label", UNSET)

        status = d.pop("status", UNSET)

        created_by = d.pop("created_by", UNSET)

        started_at = d.pop("started_at", UNSET)

        ended_at = d.pop("ended_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        parent_run_id = d.pop("parent_run_id", UNSET)

        root_run_id = d.pop("root_run_id", UNSET)

        lineage_path = d.pop("lineage_path", UNSET)

        branch_event_id = d.pop("branch_event_id", UNSET)

        branch_hlc_wall_ns = d.pop("branch_hlc_wall_ns", UNSET)

        branch_hlc_logical = d.pop("branch_hlc_logical", UNSET)

        sandbox_id = d.pop("sandbox_id", UNSET)

        last_activity_at = d.pop("last_activity_at", UNSET)

        stale = d.pop("stale", UNSET)

        executing_principal = d.pop("executing_principal", UNSET)

        executing_kind = d.pop("executing_kind", UNSET)

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
            last_activity_at=last_activity_at,
            stale=stale,
            executing_principal=executing_principal,
            executing_kind=executing_kind,
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
