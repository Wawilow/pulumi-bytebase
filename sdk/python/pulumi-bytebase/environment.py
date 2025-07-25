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
from . import _utilities

__all__ = ['EnvironmentArgs', 'Environment']

@pulumi.input_type
class EnvironmentArgs:
    def __init__(__self__, *,
                 resource_id: pulumi.Input[_builtins.str],
                 title: pulumi.Input[_builtins.str],
                 color: Optional[pulumi.Input[_builtins.str]] = None,
                 order: Optional[pulumi.Input[_builtins.int]] = None,
                 protected: Optional[pulumi.Input[_builtins.bool]] = None):
        """
        The set of arguments for constructing a Environment resource.
        :param pulumi.Input[_builtins.str] resource_id: The environment unique id.
        :param pulumi.Input[_builtins.str] title: The environment display name.
        :param pulumi.Input[_builtins.str] color: The environment color.
        :param pulumi.Input[_builtins.int] order: The environment sorting order.
        :param pulumi.Input[_builtins.bool] protected: The environment is protected or not.
        """
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "title", title)
        if color is not None:
            pulumi.set(__self__, "color", color)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if protected is not None:
            pulumi.set(__self__, "protected", protected)

    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]:
        """
        The environment unique id.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "resource_id", value)

    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        """
        The environment display name.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "title", value)

    @_builtins.property
    @pulumi.getter
    def color(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The environment color.
        """
        return pulumi.get(self, "color")

    @color.setter
    def color(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "color", value)

    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.int]]:
        """
        The environment sorting order.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.int]]):
        pulumi.set(self, "order", value)

    @_builtins.property
    @pulumi.getter
    def protected(self) -> Optional[pulumi.Input[_builtins.bool]]:
        """
        The environment is protected or not.
        """
        return pulumi.get(self, "protected")

    @protected.setter
    def protected(self, value: Optional[pulumi.Input[_builtins.bool]]):
        pulumi.set(self, "protected", value)


@pulumi.input_type
class _EnvironmentState:
    def __init__(__self__, *,
                 color: Optional[pulumi.Input[_builtins.str]] = None,
                 name: Optional[pulumi.Input[_builtins.str]] = None,
                 order: Optional[pulumi.Input[_builtins.int]] = None,
                 protected: Optional[pulumi.Input[_builtins.bool]] = None,
                 resource_id: Optional[pulumi.Input[_builtins.str]] = None,
                 title: Optional[pulumi.Input[_builtins.str]] = None):
        """
        Input properties used for looking up and filtering Environment resources.
        :param pulumi.Input[_builtins.str] color: The environment color.
        :param pulumi.Input[_builtins.str] name: The environment readonly name in environments/{id} format.
        :param pulumi.Input[_builtins.int] order: The environment sorting order.
        :param pulumi.Input[_builtins.bool] protected: The environment is protected or not.
        :param pulumi.Input[_builtins.str] resource_id: The environment unique id.
        :param pulumi.Input[_builtins.str] title: The environment display name.
        """
        if color is not None:
            pulumi.set(__self__, "color", color)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if protected is not None:
            pulumi.set(__self__, "protected", protected)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @_builtins.property
    @pulumi.getter
    def color(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The environment color.
        """
        return pulumi.get(self, "color")

    @color.setter
    def color(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "color", value)

    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The environment readonly name in environments/{id} format.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "name", value)

    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.int]]:
        """
        The environment sorting order.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.int]]):
        pulumi.set(self, "order", value)

    @_builtins.property
    @pulumi.getter
    def protected(self) -> Optional[pulumi.Input[_builtins.bool]]:
        """
        The environment is protected or not.
        """
        return pulumi.get(self, "protected")

    @protected.setter
    def protected(self, value: Optional[pulumi.Input[_builtins.bool]]):
        pulumi.set(self, "protected", value)

    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The environment unique id.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "resource_id", value)

    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The environment display name.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "title", value)


@pulumi.type_token("bytebase:index/environment:Environment")
class Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color: Optional[pulumi.Input[_builtins.str]] = None,
                 order: Optional[pulumi.Input[_builtins.int]] = None,
                 protected: Optional[pulumi.Input[_builtins.bool]] = None,
                 resource_id: Optional[pulumi.Input[_builtins.str]] = None,
                 title: Optional[pulumi.Input[_builtins.str]] = None,
                 __props__=None):
        """
        The environment resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[_builtins.str] color: The environment color.
        :param pulumi.Input[_builtins.int] order: The environment sorting order.
        :param pulumi.Input[_builtins.bool] protected: The environment is protected or not.
        :param pulumi.Input[_builtins.str] resource_id: The environment unique id.
        :param pulumi.Input[_builtins.str] title: The environment display name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The environment resource.

        :param str resource_name: The name of the resource.
        :param EnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color: Optional[pulumi.Input[_builtins.str]] = None,
                 order: Optional[pulumi.Input[_builtins.int]] = None,
                 protected: Optional[pulumi.Input[_builtins.bool]] = None,
                 resource_id: Optional[pulumi.Input[_builtins.str]] = None,
                 title: Optional[pulumi.Input[_builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

            __props__.__dict__["color"] = color
            __props__.__dict__["order"] = order
            __props__.__dict__["protected"] = protected
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            __props__.__dict__["name"] = None
        super(Environment, __self__).__init__(
            'bytebase:index/environment:Environment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            color: Optional[pulumi.Input[_builtins.str]] = None,
            name: Optional[pulumi.Input[_builtins.str]] = None,
            order: Optional[pulumi.Input[_builtins.int]] = None,
            protected: Optional[pulumi.Input[_builtins.bool]] = None,
            resource_id: Optional[pulumi.Input[_builtins.str]] = None,
            title: Optional[pulumi.Input[_builtins.str]] = None) -> 'Environment':
        """
        Get an existing Environment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[_builtins.str] color: The environment color.
        :param pulumi.Input[_builtins.str] name: The environment readonly name in environments/{id} format.
        :param pulumi.Input[_builtins.int] order: The environment sorting order.
        :param pulumi.Input[_builtins.bool] protected: The environment is protected or not.
        :param pulumi.Input[_builtins.str] resource_id: The environment unique id.
        :param pulumi.Input[_builtins.str] title: The environment display name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EnvironmentState.__new__(_EnvironmentState)

        __props__.__dict__["color"] = color
        __props__.__dict__["name"] = name
        __props__.__dict__["order"] = order
        __props__.__dict__["protected"] = protected
        __props__.__dict__["resource_id"] = resource_id
        __props__.__dict__["title"] = title
        return Environment(resource_name, opts=opts, __props__=__props__)

    @_builtins.property
    @pulumi.getter
    def color(self) -> pulumi.Output[Optional[_builtins.str]]:
        """
        The environment color.
        """
        return pulumi.get(self, "color")

    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        """
        The environment readonly name in environments/{id} format.
        """
        return pulumi.get(self, "name")

    @_builtins.property
    @pulumi.getter
    def order(self) -> pulumi.Output[Optional[_builtins.int]]:
        """
        The environment sorting order.
        """
        return pulumi.get(self, "order")

    @_builtins.property
    @pulumi.getter
    def protected(self) -> pulumi.Output[Optional[_builtins.bool]]:
        """
        The environment is protected or not.
        """
        return pulumi.get(self, "protected")

    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[_builtins.str]:
        """
        The environment unique id.
        """
        return pulumi.get(self, "resource_id")

    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[_builtins.str]:
        """
        The environment display name.
        """
        return pulumi.get(self, "title")

