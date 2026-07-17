from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_sandbox_request_network_mode import CreateSandboxRequestNetworkMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.capability_requirement import CapabilityRequirement
    from ..models.capture_spec import CaptureSpec
    from ..models.command_spec import CommandSpec
    from ..models.create_sandbox_request_labels import CreateSandboxRequestLabels
    from ..models.egress_policy import EgressPolicy
    from ..models.lifecycle_spec import LifecycleSpec
    from ..models.resource_spec import ResourceSpec
    from ..models.sandbox_image import SandboxImage
    from ..models.secret_binding import SecretBinding
    from ..models.volume_mount import VolumeMount
    from ..models.workspace_revision_mount import WorkspaceRevisionMount


T = TypeVar("T", bound="CreateSandboxRequest")


@_attrs_define
class CreateSandboxRequest:
    """
    Attributes:
        project_id (str | Unset):
        name (str | Unset): An optional display name for the sandbox. When empty the server generates one. Names are not
             unique; the id returned in the response is the canonical handle. The run created with the
             sandbox takes this name as its label, so naming the sandbox names its run tree's root.
        image (SandboxImage | Unset): Explicit immutable environment selection. A create must name a deployment profile
            or exact OCI
             environment; omitting the image does not select a provider default.
        resources (ResourceSpec | Unset):
        requested_capabilities (list[CapabilityRequirement] | Unset):
        labels (CreateSandboxRequestLabels | Unset):
        capture (CaptureSpec | Unset):
        egress (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
            EGRESS_MODE_UNSPECIFIED leaves
             outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
             runtime supports.
        secrets (list[SecretBinding] | Unset): Declared secret bindings. Non-empty requests require native injection and
            currently fail closed.
        lifecycle (LifecycleSpec | Unset): Sandbox lifecycle policy: two independent clocks, matching how the completion
            sweep and the
             lifetime reaper enforce them. This intentionally exposes only the two expiry controls needed by
             public callers; process defaults, environment, and user remain server-managed.
        description (str | Unset): User-assigned free-text description. Empty leaves the sandbox undescribed.
        command (CommandSpec | Unset):
        delete_on_exit (bool | Unset): One-shot mode only: delete the sandbox on command exit instead of stopping it.
            The run and
             execution records persist either way.
        execute_as_workload (str | Unset): Optional registered workload name to run the sandbox as. When set, the
            sandbox is
             workload-classed: its work is attributed to that workload, its managed credential is bound to the
             workload on the caller's behalf, and any identity-bound egress policy for that workload applies
             (the caller must hold launch rights on it and the name must be registered). When empty, the
             sandbox executes as the caller's own identity. The executing identity is always declared here,
             never inferred.
        volume_mounts (list[VolumeMount] | Unset): Retired volume-compatibility field. Clean sandbox-cell deployments
            reject non-empty volume
             mounts; attach an exact BranchFS workspace revision instead.
        network_mode (CreateSandboxRequestNetworkMode | Unset): Network dataplane mode for the sandbox. Omitted or
            NETWORK_MODE_UNSPECIFIED keeps the
             default (NETWORK_MODE_NONE).
        workspace (WorkspaceRevisionMount | Unset): One writable, copy-on-write BranchFS workspace mounted into a
            sandbox. The tenant comes only
             from the authenticated request scope and is never caller-supplied. Node paths, sockets, writer
             fences, and backend handles remain internal to the selected cell.
    """

    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    image: SandboxImage | Unset = UNSET
    resources: ResourceSpec | Unset = UNSET
    requested_capabilities: list[CapabilityRequirement] | Unset = UNSET
    labels: CreateSandboxRequestLabels | Unset = UNSET
    capture: CaptureSpec | Unset = UNSET
    egress: EgressPolicy | Unset = UNSET
    secrets: list[SecretBinding] | Unset = UNSET
    lifecycle: LifecycleSpec | Unset = UNSET
    description: str | Unset = UNSET
    command: CommandSpec | Unset = UNSET
    delete_on_exit: bool | Unset = UNSET
    execute_as_workload: str | Unset = UNSET
    volume_mounts: list[VolumeMount] | Unset = UNSET
    network_mode: CreateSandboxRequestNetworkMode | Unset = UNSET
    workspace: WorkspaceRevisionMount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        name = self.name

        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        requested_capabilities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requested_capabilities, Unset):
            requested_capabilities = []
            for requested_capabilities_item_data in self.requested_capabilities:
                requested_capabilities_item = requested_capabilities_item_data.to_dict()
                requested_capabilities.append(requested_capabilities_item)

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        capture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capture, Unset):
            capture = self.capture.to_dict()

        egress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.egress, Unset):
            egress = self.egress.to_dict()

        secrets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()
                secrets.append(secrets_item)

        lifecycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lifecycle, Unset):
            lifecycle = self.lifecycle.to_dict()

        description = self.description

        command: dict[str, Any] | Unset = UNSET
        if not isinstance(self.command, Unset):
            command = self.command.to_dict()

        delete_on_exit = self.delete_on_exit

        execute_as_workload = self.execute_as_workload

        volume_mounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.volume_mounts, Unset):
            volume_mounts = []
            for volume_mounts_item_data in self.volume_mounts:
                volume_mounts_item = volume_mounts_item_data.to_dict()
                volume_mounts.append(volume_mounts_item)

        network_mode: str | Unset = UNSET
        if not isinstance(self.network_mode, Unset):
            network_mode = self.network_mode.value

        workspace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if image is not UNSET:
            field_dict["image"] = image
        if resources is not UNSET:
            field_dict["resources"] = resources
        if requested_capabilities is not UNSET:
            field_dict["requested_capabilities"] = requested_capabilities
        if labels is not UNSET:
            field_dict["labels"] = labels
        if capture is not UNSET:
            field_dict["capture"] = capture
        if egress is not UNSET:
            field_dict["egress"] = egress
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if description is not UNSET:
            field_dict["description"] = description
        if command is not UNSET:
            field_dict["command"] = command
        if delete_on_exit is not UNSET:
            field_dict["delete_on_exit"] = delete_on_exit
        if execute_as_workload is not UNSET:
            field_dict["execute_as_workload"] = execute_as_workload
        if volume_mounts is not UNSET:
            field_dict["volume_mounts"] = volume_mounts
        if network_mode is not UNSET:
            field_dict["network_mode"] = network_mode
        if workspace is not UNSET:
            field_dict["workspace"] = workspace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capability_requirement import CapabilityRequirement
        from ..models.capture_spec import CaptureSpec
        from ..models.command_spec import CommandSpec
        from ..models.create_sandbox_request_labels import CreateSandboxRequestLabels
        from ..models.egress_policy import EgressPolicy
        from ..models.lifecycle_spec import LifecycleSpec
        from ..models.resource_spec import ResourceSpec
        from ..models.sandbox_image import SandboxImage
        from ..models.secret_binding import SecretBinding
        from ..models.volume_mount import VolumeMount
        from ..models.workspace_revision_mount import WorkspaceRevisionMount

        d = dict(src_dict)
        project_id = d.pop("project_id", UNSET)

        name = d.pop("name", UNSET)

        _image = d.pop("image", UNSET)
        image: SandboxImage | Unset
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = SandboxImage.from_dict(_image)

        _resources = d.pop("resources", UNSET)
        resources: ResourceSpec | Unset
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = ResourceSpec.from_dict(_resources)

        _requested_capabilities = d.pop("requested_capabilities", UNSET)
        requested_capabilities: list[CapabilityRequirement] | Unset = UNSET
        if _requested_capabilities is not UNSET:
            requested_capabilities = []
            for requested_capabilities_item_data in _requested_capabilities:
                requested_capabilities_item = CapabilityRequirement.from_dict(requested_capabilities_item_data)

                requested_capabilities.append(requested_capabilities_item)

        _labels = d.pop("labels", UNSET)
        labels: CreateSandboxRequestLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = CreateSandboxRequestLabels.from_dict(_labels)

        _capture = d.pop("capture", UNSET)
        capture: CaptureSpec | Unset
        if isinstance(_capture, Unset):
            capture = UNSET
        else:
            capture = CaptureSpec.from_dict(_capture)

        _egress = d.pop("egress", UNSET)
        egress: EgressPolicy | Unset
        if isinstance(_egress, Unset):
            egress = UNSET
        else:
            egress = EgressPolicy.from_dict(_egress)

        _secrets = d.pop("secrets", UNSET)
        secrets: list[SecretBinding] | Unset = UNSET
        if _secrets is not UNSET:
            secrets = []
            for secrets_item_data in _secrets:
                secrets_item = SecretBinding.from_dict(secrets_item_data)

                secrets.append(secrets_item)

        _lifecycle = d.pop("lifecycle", UNSET)
        lifecycle: LifecycleSpec | Unset
        if isinstance(_lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = LifecycleSpec.from_dict(_lifecycle)

        description = d.pop("description", UNSET)

        _command = d.pop("command", UNSET)
        command: CommandSpec | Unset
        if isinstance(_command, Unset):
            command = UNSET
        else:
            command = CommandSpec.from_dict(_command)

        delete_on_exit = d.pop("delete_on_exit", UNSET)

        execute_as_workload = d.pop("execute_as_workload", UNSET)

        _volume_mounts = d.pop("volume_mounts", UNSET)
        volume_mounts: list[VolumeMount] | Unset = UNSET
        if _volume_mounts is not UNSET:
            volume_mounts = []
            for volume_mounts_item_data in _volume_mounts:
                volume_mounts_item = VolumeMount.from_dict(volume_mounts_item_data)

                volume_mounts.append(volume_mounts_item)

        _network_mode = d.pop("network_mode", UNSET)
        network_mode: CreateSandboxRequestNetworkMode | Unset
        if isinstance(_network_mode, Unset):
            network_mode = UNSET
        else:
            network_mode = CreateSandboxRequestNetworkMode(_network_mode)

        _workspace = d.pop("workspace", UNSET)
        workspace: WorkspaceRevisionMount | Unset
        if isinstance(_workspace, Unset):
            workspace = UNSET
        else:
            workspace = WorkspaceRevisionMount.from_dict(_workspace)

        create_sandbox_request = cls(
            project_id=project_id,
            name=name,
            image=image,
            resources=resources,
            requested_capabilities=requested_capabilities,
            labels=labels,
            capture=capture,
            egress=egress,
            secrets=secrets,
            lifecycle=lifecycle,
            description=description,
            command=command,
            delete_on_exit=delete_on_exit,
            execute_as_workload=execute_as_workload,
            volume_mounts=volume_mounts,
            network_mode=network_mode,
            workspace=workspace,
        )

        create_sandbox_request.additional_properties = d
        return create_sandbox_request

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
