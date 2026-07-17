from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.command_spec_env import CommandSpecEnv


T = TypeVar("T", bound="CommandSpec")


@_attrs_define
class CommandSpec:
    """
    Attributes:
        program (str | Unset):
        args (list[str] | Unset):
        env (CommandSpecEnv | Unset):
        working_dir (str | Unset):
        timeout_secs (str | Unset): Zero uses the server default command timeout.
    """

    program: str | Unset = UNSET
    args: list[str] | Unset = UNSET
    env: CommandSpecEnv | Unset = UNSET
    working_dir: str | Unset = UNSET
    timeout_secs: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        program = self.program

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        working_dir = self.working_dir

        timeout_secs = self.timeout_secs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if program is not UNSET:
            field_dict["program"] = program
        if args is not UNSET:
            field_dict["args"] = args
        if env is not UNSET:
            field_dict["env"] = env
        if working_dir is not UNSET:
            field_dict["working_dir"] = working_dir
        if timeout_secs is not UNSET:
            field_dict["timeout_secs"] = timeout_secs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.command_spec_env import CommandSpecEnv

        d = dict(src_dict)
        program = d.pop("program", UNSET)

        args = cast(list[str], d.pop("args", UNSET))

        _env = d.pop("env", UNSET)
        env: CommandSpecEnv | Unset
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = CommandSpecEnv.from_dict(_env)

        working_dir = d.pop("working_dir", UNSET)

        timeout_secs = d.pop("timeout_secs", UNSET)

        command_spec = cls(
            program=program,
            args=args,
            env=env,
            working_dir=working_dir,
            timeout_secs=timeout_secs,
        )

        command_spec.additional_properties = d
        return command_spec

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
