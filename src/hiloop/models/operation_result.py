from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_result import ExecuteResult
    from ..models.file_from_artifact_result import FileFromArtifactResult
    from ..models.file_to_artifact_result import FileToArtifactResult
    from ..models.fork_result import ForkResult
    from ..models.restore_result import RestoreResult
    from ..models.resume_result import ResumeResult
    from ..models.sandbox_delete_result import SandboxDeleteResult
    from ..models.snapshot_delete_result import SnapshotDeleteResult
    from ..models.snapshot_result import SnapshotResult
    from ..models.stop_result import StopResult


T = TypeVar("T", bound="OperationResult")


@_attrs_define
class OperationResult:
    """The typed report of a succeeded operation. The set variant matches the operation's kind; kinds
    whose success carries no report (for example a sandbox create or scratch-workspace delete)
    settle with no result.

       Attributes:
           stop (StopResult | Unset): What a succeeded stop observed about the sandbox it brought to rest.
           resume (ResumeResult | Unset): What a succeeded resume observed about the sandbox it brought back.
           execute (ExecuteResult | Unset): The report of a succeeded command execution.
           snapshot (SnapshotResult | Unset): Retired snapshot-compatibility result. Clean sandbox-cell deployments do not
               produce it.
           snapshot_delete (SnapshotDeleteResult | Unset): Retired snapshot-delete compatibility result. Clean sandbox-cell
               deployments do not produce it.
           restore (RestoreResult | Unset): Retired snapshot-restore compatibility result. Clean sandbox-cell deployments
               do not produce it.
           fork (ForkResult | Unset): Retired fork-compatibility result. Clean sandbox-cell deployments do not produce it.
           file_to_artifact (FileToArtifactResult | Unset): The report of a succeeded file-to-artifact export.
           file_from_artifact (FileFromArtifactResult | Unset): The report of a succeeded file-from-artifact import.
           sandbox_delete (SandboxDeleteResult | Unset): Public-safe versioning evidence from deleting a sandbox backed by
               a versioned BranchFS
                workspace. Cell-local routes, prepared references, backend receipt IDs, nodes, paths, sockets,
                epochs, and writer fences never cross this boundary. Scratch-workspace deletes have no result.
    """

    stop: StopResult | Unset = UNSET
    resume: ResumeResult | Unset = UNSET
    execute: ExecuteResult | Unset = UNSET
    snapshot: SnapshotResult | Unset = UNSET
    snapshot_delete: SnapshotDeleteResult | Unset = UNSET
    restore: RestoreResult | Unset = UNSET
    fork: ForkResult | Unset = UNSET
    file_to_artifact: FileToArtifactResult | Unset = UNSET
    file_from_artifact: FileFromArtifactResult | Unset = UNSET
    sandbox_delete: SandboxDeleteResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop, Unset):
            stop = self.stop.to_dict()

        resume: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resume, Unset):
            resume = self.resume.to_dict()

        execute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execute, Unset):
            execute = self.execute.to_dict()

        snapshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot, Unset):
            snapshot = self.snapshot.to_dict()

        snapshot_delete: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot_delete, Unset):
            snapshot_delete = self.snapshot_delete.to_dict()

        restore: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restore, Unset):
            restore = self.restore.to_dict()

        fork: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fork, Unset):
            fork = self.fork.to_dict()

        file_to_artifact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_to_artifact, Unset):
            file_to_artifact = self.file_to_artifact.to_dict()

        file_from_artifact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_from_artifact, Unset):
            file_from_artifact = self.file_from_artifact.to_dict()

        sandbox_delete: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sandbox_delete, Unset):
            sandbox_delete = self.sandbox_delete.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stop is not UNSET:
            field_dict["stop"] = stop
        if resume is not UNSET:
            field_dict["resume"] = resume
        if execute is not UNSET:
            field_dict["execute"] = execute
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot
        if snapshot_delete is not UNSET:
            field_dict["snapshot_delete"] = snapshot_delete
        if restore is not UNSET:
            field_dict["restore"] = restore
        if fork is not UNSET:
            field_dict["fork"] = fork
        if file_to_artifact is not UNSET:
            field_dict["file_to_artifact"] = file_to_artifact
        if file_from_artifact is not UNSET:
            field_dict["file_from_artifact"] = file_from_artifact
        if sandbox_delete is not UNSET:
            field_dict["sandbox_delete"] = sandbox_delete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_result import ExecuteResult
        from ..models.file_from_artifact_result import FileFromArtifactResult
        from ..models.file_to_artifact_result import FileToArtifactResult
        from ..models.fork_result import ForkResult
        from ..models.restore_result import RestoreResult
        from ..models.resume_result import ResumeResult
        from ..models.sandbox_delete_result import SandboxDeleteResult
        from ..models.snapshot_delete_result import SnapshotDeleteResult
        from ..models.snapshot_result import SnapshotResult
        from ..models.stop_result import StopResult

        d = dict(src_dict)
        _stop = d.pop("stop", UNSET)
        stop: StopResult | Unset
        if isinstance(_stop, Unset):
            stop = UNSET
        else:
            stop = StopResult.from_dict(_stop)

        _resume = d.pop("resume", UNSET)
        resume: ResumeResult | Unset
        if isinstance(_resume, Unset):
            resume = UNSET
        else:
            resume = ResumeResult.from_dict(_resume)

        _execute = d.pop("execute", UNSET)
        execute: ExecuteResult | Unset
        if isinstance(_execute, Unset):
            execute = UNSET
        else:
            execute = ExecuteResult.from_dict(_execute)

        _snapshot = d.pop("snapshot", UNSET)
        snapshot: SnapshotResult | Unset
        if isinstance(_snapshot, Unset):
            snapshot = UNSET
        else:
            snapshot = SnapshotResult.from_dict(_snapshot)

        _snapshot_delete = d.pop("snapshot_delete", UNSET)
        snapshot_delete: SnapshotDeleteResult | Unset
        if isinstance(_snapshot_delete, Unset):
            snapshot_delete = UNSET
        else:
            snapshot_delete = SnapshotDeleteResult.from_dict(_snapshot_delete)

        _restore = d.pop("restore", UNSET)
        restore: RestoreResult | Unset
        if isinstance(_restore, Unset):
            restore = UNSET
        else:
            restore = RestoreResult.from_dict(_restore)

        _fork = d.pop("fork", UNSET)
        fork: ForkResult | Unset
        if isinstance(_fork, Unset):
            fork = UNSET
        else:
            fork = ForkResult.from_dict(_fork)

        _file_to_artifact = d.pop("file_to_artifact", UNSET)
        file_to_artifact: FileToArtifactResult | Unset
        if isinstance(_file_to_artifact, Unset):
            file_to_artifact = UNSET
        else:
            file_to_artifact = FileToArtifactResult.from_dict(_file_to_artifact)

        _file_from_artifact = d.pop("file_from_artifact", UNSET)
        file_from_artifact: FileFromArtifactResult | Unset
        if isinstance(_file_from_artifact, Unset):
            file_from_artifact = UNSET
        else:
            file_from_artifact = FileFromArtifactResult.from_dict(_file_from_artifact)

        _sandbox_delete = d.pop("sandbox_delete", UNSET)
        sandbox_delete: SandboxDeleteResult | Unset
        if isinstance(_sandbox_delete, Unset):
            sandbox_delete = UNSET
        else:
            sandbox_delete = SandboxDeleteResult.from_dict(_sandbox_delete)

        operation_result = cls(
            stop=stop,
            resume=resume,
            execute=execute,
            snapshot=snapshot,
            snapshot_delete=snapshot_delete,
            restore=restore,
            fork=fork,
            file_to_artifact=file_to_artifact,
            file_from_artifact=file_from_artifact,
            sandbox_delete=sandbox_delete,
        )

        operation_result.additional_properties = d
        return operation_result

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
