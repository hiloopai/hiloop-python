from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteProjectResponse")


@_attrs_define
class DeleteProjectResponse:
    """The delete's effect report: how many of each dependent resource the call actually removed. All
    counts are zero for a non-cascading delete (it only ever removes a project with no dependents).

       Attributes:
           runs_deleted (str | Unset): The number of runs deleted.
           sandboxes_deleted (str | Unset): The number of sandboxes whose records were removed (each had already been
               deleted, so no
                compute was torn down by this call).
           snapshots_deleted (str | Unset): The number of snapshots deleted.
           volumes_deleted (str | Unset): The number of volumes deleted.
           executions_deleted (str | Unset): The number of command executions deleted.
           secrets_deleted (str | Unset): The number of project-scoped secrets deleted.
           api_keys_deleted (str | Unset): The number of project-scoped API keys deleted (keys scoped to the whole tenant
               are untouched).
    """

    runs_deleted: str | Unset = UNSET
    sandboxes_deleted: str | Unset = UNSET
    snapshots_deleted: str | Unset = UNSET
    volumes_deleted: str | Unset = UNSET
    executions_deleted: str | Unset = UNSET
    secrets_deleted: str | Unset = UNSET
    api_keys_deleted: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runs_deleted = self.runs_deleted

        sandboxes_deleted = self.sandboxes_deleted

        snapshots_deleted = self.snapshots_deleted

        volumes_deleted = self.volumes_deleted

        executions_deleted = self.executions_deleted

        secrets_deleted = self.secrets_deleted

        api_keys_deleted = self.api_keys_deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if runs_deleted is not UNSET:
            field_dict["runs_deleted"] = runs_deleted
        if sandboxes_deleted is not UNSET:
            field_dict["sandboxes_deleted"] = sandboxes_deleted
        if snapshots_deleted is not UNSET:
            field_dict["snapshots_deleted"] = snapshots_deleted
        if volumes_deleted is not UNSET:
            field_dict["volumes_deleted"] = volumes_deleted
        if executions_deleted is not UNSET:
            field_dict["executions_deleted"] = executions_deleted
        if secrets_deleted is not UNSET:
            field_dict["secrets_deleted"] = secrets_deleted
        if api_keys_deleted is not UNSET:
            field_dict["api_keys_deleted"] = api_keys_deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        runs_deleted = d.pop("runs_deleted", UNSET)

        sandboxes_deleted = d.pop("sandboxes_deleted", UNSET)

        snapshots_deleted = d.pop("snapshots_deleted", UNSET)

        volumes_deleted = d.pop("volumes_deleted", UNSET)

        executions_deleted = d.pop("executions_deleted", UNSET)

        secrets_deleted = d.pop("secrets_deleted", UNSET)

        api_keys_deleted = d.pop("api_keys_deleted", UNSET)

        delete_project_response = cls(
            runs_deleted=runs_deleted,
            sandboxes_deleted=sandboxes_deleted,
            snapshots_deleted=snapshots_deleted,
            volumes_deleted=volumes_deleted,
            executions_deleted=executions_deleted,
            secrets_deleted=secrets_deleted,
            api_keys_deleted=api_keys_deleted,
        )

        delete_project_response.additional_properties = d
        return delete_project_response

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
