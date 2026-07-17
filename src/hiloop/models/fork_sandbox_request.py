from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.capability_requirement import CapabilityRequirement
    from ..models.capture_spec import CaptureSpec
    from ..models.egress_policy import EgressPolicy
    from ..models.fork_sandbox_request_labels import ForkSandboxRequestLabels
    from ..models.lifecycle_spec import LifecycleSpec
    from ..models.resource_spec import ResourceSpec
    from ..models.sandbox_image import SandboxImage
    from ..models.secret_binding import SecretBinding


T = TypeVar("T", bound="ForkSandboxRequest")


@_attrs_define
class ForkSandboxRequest:
    """Retired fork compatibility request. Clean sandbox-cell deployments return unsupported.

    Attributes:
        source_sandbox_id (str | Unset):
        project_id (str | Unset):
        name (str | Unset): An optional display name for the child sandbox. When empty the server names it: a labeled
            fork
             of a named source gets `<source-name>-<label>`, anything else gets a generated name. Names are
             not unique; the child id in the response is the canonical handle.
        image (SandboxImage | Unset): Explicit immutable environment selection. A create must name a deployment profile
            or exact OCI
             environment; omitting the image does not select a provider default.
        resources (ResourceSpec | Unset):
        requested_capabilities (list[CapabilityRequirement] | Unset):
        labels (ForkSandboxRequestLabels | Unset):
        continuity (str | Unset):
        allow_fallback (bool | Unset):
        capture (CaptureSpec | Unset):
        egress (EgressPolicy | Unset): Provider-neutral outbound network policy for a sandbox. Omitted or
            EGRESS_MODE_UNSPECIFIED leaves
             outbound traffic unbounded (the default-allow behavior). Enforced at the strongest layer the
             runtime supports.
        secrets (list[SecretBinding] | Unset): Secret bindings for the child sandbox, merged by name into the bindings
            inherited from the
             source sandbox: an entry with a new name is added, an entry whose name matches an inherited
             binding replaces it. With inherit_secrets set to false this list is the child's entire binding
             set. Secret values are resolved per child at request time; they are never carried in the fork.
        parent_run_id (str | Unset): The run being forked from. The fork mints a child run beneath it.
        branch_event_id (str | Unset): The parent event id the child forks at — the divergence point on the parent's
            timeline. Empty
             forks at the parent's current head.
        branch_hlc_wall_ns (str | Unset): The parent branch-point wall-clock time in nanoseconds that pairs with
            branch_event_id. Zero
             when forking at the head.
        branch_hlc_logical (str | Unset): The parent branch-point logical tiebreak that pairs with branch_hlc_wall_ns.
        label (str | Unset): An optional human-readable label for the child run the fork mints. When empty, the server
             assigns a friendly fallback name.
        lifecycle (LifecycleSpec | Unset): Sandbox lifecycle policy: two independent clocks, matching how the completion
            sweep and the
             lifetime reaper enforce them. This intentionally exposes only the two expiry controls needed by
             public callers; process defaults, environment, and user remain server-managed.
        execute_as_workload (str | Unset): Optional registered workload name to narrow the fork to. A fork otherwise
            inherits the parent's
             executing identity — a workload's whole subtree stays workload-classed and cannot shed its class
             by forking. Declaring a workload here may only narrow a non-workload-classed parent (the caller
             must hold launch rights and the name must be registered); declaring one on an
             already-workload-classed fork is rejected. Empty inherits the parent's executing identity.
        inherit_secrets (bool | Unset): Whether the child inherits the source sandbox's secret bindings. Defaults to
            true: the child
             starts with every binding the source has, with any secrets entries merged in by name. Set
             false to give the child exactly the secrets list — possibly none.
    """

    source_sandbox_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    image: SandboxImage | Unset = UNSET
    resources: ResourceSpec | Unset = UNSET
    requested_capabilities: list[CapabilityRequirement] | Unset = UNSET
    labels: ForkSandboxRequestLabels | Unset = UNSET
    continuity: str | Unset = UNSET
    allow_fallback: bool | Unset = UNSET
    capture: CaptureSpec | Unset = UNSET
    egress: EgressPolicy | Unset = UNSET
    secrets: list[SecretBinding] | Unset = UNSET
    parent_run_id: str | Unset = UNSET
    branch_event_id: str | Unset = UNSET
    branch_hlc_wall_ns: str | Unset = UNSET
    branch_hlc_logical: str | Unset = UNSET
    label: str | Unset = UNSET
    lifecycle: LifecycleSpec | Unset = UNSET
    execute_as_workload: str | Unset = UNSET
    inherit_secrets: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_sandbox_id = self.source_sandbox_id

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

        continuity = self.continuity

        allow_fallback = self.allow_fallback

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

        parent_run_id = self.parent_run_id

        branch_event_id = self.branch_event_id

        branch_hlc_wall_ns = self.branch_hlc_wall_ns

        branch_hlc_logical = self.branch_hlc_logical

        label = self.label

        lifecycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lifecycle, Unset):
            lifecycle = self.lifecycle.to_dict()

        execute_as_workload = self.execute_as_workload

        inherit_secrets = self.inherit_secrets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_sandbox_id is not UNSET:
            field_dict["source_sandbox_id"] = source_sandbox_id
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
        if continuity is not UNSET:
            field_dict["continuity"] = continuity
        if allow_fallback is not UNSET:
            field_dict["allow_fallback"] = allow_fallback
        if capture is not UNSET:
            field_dict["capture"] = capture
        if egress is not UNSET:
            field_dict["egress"] = egress
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if parent_run_id is not UNSET:
            field_dict["parent_run_id"] = parent_run_id
        if branch_event_id is not UNSET:
            field_dict["branch_event_id"] = branch_event_id
        if branch_hlc_wall_ns is not UNSET:
            field_dict["branch_hlc_wall_ns"] = branch_hlc_wall_ns
        if branch_hlc_logical is not UNSET:
            field_dict["branch_hlc_logical"] = branch_hlc_logical
        if label is not UNSET:
            field_dict["label"] = label
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if execute_as_workload is not UNSET:
            field_dict["execute_as_workload"] = execute_as_workload
        if inherit_secrets is not UNSET:
            field_dict["inherit_secrets"] = inherit_secrets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capability_requirement import CapabilityRequirement
        from ..models.capture_spec import CaptureSpec
        from ..models.egress_policy import EgressPolicy
        from ..models.fork_sandbox_request_labels import ForkSandboxRequestLabels
        from ..models.lifecycle_spec import LifecycleSpec
        from ..models.resource_spec import ResourceSpec
        from ..models.sandbox_image import SandboxImage
        from ..models.secret_binding import SecretBinding

        d = dict(src_dict)
        source_sandbox_id = d.pop("source_sandbox_id", UNSET)

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
        labels: ForkSandboxRequestLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ForkSandboxRequestLabels.from_dict(_labels)

        continuity = d.pop("continuity", UNSET)

        allow_fallback = d.pop("allow_fallback", UNSET)

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

        parent_run_id = d.pop("parent_run_id", UNSET)

        branch_event_id = d.pop("branch_event_id", UNSET)

        branch_hlc_wall_ns = d.pop("branch_hlc_wall_ns", UNSET)

        branch_hlc_logical = d.pop("branch_hlc_logical", UNSET)

        label = d.pop("label", UNSET)

        _lifecycle = d.pop("lifecycle", UNSET)
        lifecycle: LifecycleSpec | Unset
        if isinstance(_lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = LifecycleSpec.from_dict(_lifecycle)

        execute_as_workload = d.pop("execute_as_workload", UNSET)

        inherit_secrets = d.pop("inherit_secrets", UNSET)

        fork_sandbox_request = cls(
            source_sandbox_id=source_sandbox_id,
            project_id=project_id,
            name=name,
            image=image,
            resources=resources,
            requested_capabilities=requested_capabilities,
            labels=labels,
            continuity=continuity,
            allow_fallback=allow_fallback,
            capture=capture,
            egress=egress,
            secrets=secrets,
            parent_run_id=parent_run_id,
            branch_event_id=branch_event_id,
            branch_hlc_wall_ns=branch_hlc_wall_ns,
            branch_hlc_logical=branch_hlc_logical,
            label=label,
            lifecycle=lifecycle,
            execute_as_workload=execute_as_workload,
            inherit_secrets=inherit_secrets,
        )

        fork_sandbox_request.additional_properties = d
        return fork_sandbox_request

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
