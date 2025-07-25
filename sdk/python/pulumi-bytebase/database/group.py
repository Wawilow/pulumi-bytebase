# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins as _builtins
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

__all__ = ['GroupArgs', 'Group']

@pulumi.input_type
class GroupArgs:
    def __init__(__self__, *,
                 condition: pulumi.Input[_builtins.str],
                 project: pulumi.Input[_builtins.str],
                 resource_id: pulumi.Input[_builtins.str],
                 title: pulumi.Input[_builtins.str]):
        """
        The set of arguments for constructing a Group resource.
        :param pulumi.Input[_builtins.str] condition: The database group condition. Check the proto message https://github.com/bytebase/bytebase/blob/main/proto/v1/v1/database*group*service.proto#L185 for details.
        :param pulumi.Input[_builtins.str] project: The project fullname in projects/{id} format.
        :param pulumi.Input[_builtins.str] resource_id: The database group unique resource id.
        :param pulumi.Input[_builtins.str] title: The database group title.
        """
        pulumi.set(__self__, "condition", condition)
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "title", title)

    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Input[_builtins.str]:
        """
        The database group condition. Check the proto message https://github.com/bytebase/bytebase/blob/main/proto/v1/v1/database*group*service.proto#L185 for details.
        """
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "condition", value)

    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]:
        """
        The project fullname in projects/{id} format.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "project", value)

    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]:
        """
        The database group unique resource id.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "resource_id", value)

    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        """
        The database group title.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "title", value)


@pulumi.input_type
class _GroupState:
    def __init__(__self__, *,
                 condition: Optional[pulumi.Input[_builtins.str]] = None,
                 matched_databases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
                 project: Optional[pulumi.Input[_builtins.str]] = None,
                 resource_id: Optional[pulumi.Input[_builtins.str]] = None,
                 title: Optional[pulumi.Input[_builtins.str]] = None):
        """
        Input properties used for looking up and filtering Group resources.
        :param pulumi.Input[_builtins.str] condition: The database group condition. Check the proto message https://github.com/bytebase/bytebase/blob/main/proto/v1/v1/database*group*service.proto#L185 for details.
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] matched_databases: The matched databases in the group.
        :param pulumi.Input[_builtins.str] project: The project fullname in projects/{id} format.
        :param pulumi.Input[_builtins.str] resource_id: The database group unique resource id.
        :param pulumi.Input[_builtins.str] title: The database group title.
        """
        if condition is not None:
            pulumi.set(__self__, "condition", condition)
        if matched_databases is not None:
            pulumi.set(__self__, "matched_databases", matched_databases)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The database group condition. Check the proto message https://github.com/bytebase/bytebase/blob/main/proto/v1/v1/database*group*service.proto#L185 for details.
        """
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "condition", value)

    @_builtins.property
    @pulumi.getter(name="matchedDatabases")
    def matched_databases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        """
        The matched databases in the group.
        """
        return pulumi.get(self, "matched_databases")

    @matched_databases.setter
    def matched_databases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]):
        pulumi.set(self, "matched_databases", value)

    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The project fullname in projects/{id} format.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "project", value)

    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The database group unique resource id.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "resource_id", value)

    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The database group title.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "title", value)


@pulumi.type_token("bytebase:Database/group:Group")
class Group(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 condition: Optional[pulumi.Input[_builtins.str]] = None,
                 project: Optional[pulumi.Input[_builtins.str]] = None,
                 resource_id: Optional[pulumi.Input[_builtins.str]] = None,
                 title: Optional[pulumi.Input[_builtins.str]] = None,
                 __props__=None):
        """
        The database group resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[_builtins.str] condition: The database group condition. Check the proto message https://github.com/bytebase/bytebase/blob/main/proto/v1/v1/database*group*service.proto#L185 for details.
        :param pulumi.Input[_builtins.str] project: The project fullname in projects/{id} format.
        :param pulumi.Input[_builtins.str] resource_id: The database group unique resource id.
        :param pulumi.Input[_builtins.str] title: The database group title.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The database group resource.

        :param str resource_name: The name of the resource.
        :param GroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 condition: Optional[pulumi.Input[_builtins.str]] = None,
                 project: Optional[pulumi.Input[_builtins.str]] = None,
                 resource_id: Optional[pulumi.Input[_builtins.str]] = None,
                 title: Optional[pulumi.Input[_builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupArgs.__new__(GroupArgs)

            if condition is None and not opts.urn:
                raise TypeError("Missing required property 'condition'")
            __props__.__dict__["condition"] = condition
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            __props__.__dict__["matched_databases"] = None
        super(Group, __self__).__init__(
            'bytebase:Database/group:Group',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            condition: Optional[pulumi.Input[_builtins.str]] = None,
            matched_databases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
            project: Optional[pulumi.Input[_builtins.str]] = None,
            resource_id: Optional[pulumi.Input[_builtins.str]] = None,
            title: Optional[pulumi.Input[_builtins.str]] = None) -> 'Group':
        """
        Get an existing Group resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[_builtins.str] condition: The database group condition. Check the proto message https://github.com/bytebase/bytebase/blob/main/proto/v1/v1/database*group*service.proto#L185 for details.
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] matched_databases: The matched databases in the group.
        :param pulumi.Input[_builtins.str] project: The project fullname in projects/{id} format.
        :param pulumi.Input[_builtins.str] resource_id: The database group unique resource id.
        :param pulumi.Input[_builtins.str] title: The database group title.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupState.__new__(_GroupState)

        __props__.__dict__["condition"] = condition
        __props__.__dict__["matched_databases"] = matched_databases
        __props__.__dict__["project"] = project
        __props__.__dict__["resource_id"] = resource_id
        __props__.__dict__["title"] = title
        return Group(resource_name, opts=opts, __props__=__props__)

    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Output[_builtins.str]:
        """
        The database group condition. Check the proto message https://github.com/bytebase/bytebase/blob/main/proto/v1/v1/database*group*service.proto#L185 for details.
        """
        return pulumi.get(self, "condition")

    @_builtins.property
    @pulumi.getter(name="matchedDatabases")
    def matched_databases(self) -> pulumi.Output[Sequence[_builtins.str]]:
        """
        The matched databases in the group.
        """
        return pulumi.get(self, "matched_databases")

    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        """
        The project fullname in projects/{id} format.
        """
        return pulumi.get(self, "project")

    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[_builtins.str]:
        """
        The database group unique resource id.
        """
        return pulumi.get(self, "resource_id")

    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[_builtins.str]:
        """
        The database group title.
        """
        return pulumi.get(self, "title")

