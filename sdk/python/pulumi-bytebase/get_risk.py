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

__all__ = [
    'GetRiskResult',
    'AwaitableGetRiskResult',
    'get_risk',
    'get_risk_output',
]

@pulumi.output_type
class GetRiskResult:
    """
    A collection of values returned by getRisk.
    """
    def __init__(__self__, active=None, condition=None, id=None, level=None, name=None, source=None, title=None):
        if active and not isinstance(active, bool):
            raise TypeError("Expected argument 'active' to be a bool")
        pulumi.set(__self__, "active", active)
        if condition and not isinstance(condition, str):
            raise TypeError("Expected argument 'condition' to be a str")
        pulumi.set(__self__, "condition", condition)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if level and not isinstance(level, int):
            raise TypeError("Expected argument 'level' to be a int")
        pulumi.set(__self__, "level", level)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)

    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        """
        The risk active.
        """
        return pulumi.get(self, "active")

    @_builtins.property
    @pulumi.getter
    def condition(self) -> _builtins.str:
        """
        The risk condition.
        """
        return pulumi.get(self, "condition")

    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @_builtins.property
    @pulumi.getter
    def level(self) -> _builtins.int:
        """
        The risk level.
        """
        return pulumi.get(self, "level")

    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        """
        The risk full name in risks/{uid} format.
        """
        return pulumi.get(self, "name")

    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        """
        The risk source.
        """
        return pulumi.get(self, "source")

    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        """
        The risk title.
        """
        return pulumi.get(self, "title")


class AwaitableGetRiskResult(GetRiskResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRiskResult(
            active=self.active,
            condition=self.condition,
            id=self.id,
            level=self.level,
            name=self.name,
            source=self.source,
            title=self.title)


def get_risk(name: Optional[_builtins.str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRiskResult:
    """
    The risk data source.


    :param _builtins.str name: The risk full name in risks/{uid} format.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('bytebase:index/getRisk:getRisk', __args__, opts=opts, typ=GetRiskResult).value

    return AwaitableGetRiskResult(
        active=pulumi.get(__ret__, 'active'),
        condition=pulumi.get(__ret__, 'condition'),
        id=pulumi.get(__ret__, 'id'),
        level=pulumi.get(__ret__, 'level'),
        name=pulumi.get(__ret__, 'name'),
        source=pulumi.get(__ret__, 'source'),
        title=pulumi.get(__ret__, 'title'))
def get_risk_output(name: Optional[pulumi.Input[_builtins.str]] = None,
                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetRiskResult]:
    """
    The risk data source.


    :param _builtins.str name: The risk full name in risks/{uid} format.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('bytebase:index/getRisk:getRisk', __args__, opts=opts, typ=GetRiskResult)
    return __ret__.apply(lambda __response__: GetRiskResult(
        active=pulumi.get(__response__, 'active'),
        condition=pulumi.get(__response__, 'condition'),
        id=pulumi.get(__response__, 'id'),
        level=pulumi.get(__response__, 'level'),
        name=pulumi.get(__response__, 'name'),
        source=pulumi.get(__response__, 'source'),
        title=pulumi.get(__response__, 'title')))
