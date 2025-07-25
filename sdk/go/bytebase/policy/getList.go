// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package policy

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/wawilow/pulumi-bytebase/sdk/go/bytebase/internal"
)

// The policy data source list.
func GetList(ctx *pulumi.Context, args *GetListArgs, opts ...pulumi.InvokeOption) (*GetListResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetListResult
	err := ctx.Invoke("bytebase:Policy/getList:getList", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getList.
type GetListArgs struct {
	// The policy parent name for the policy, support projects/{resource id}, environments/{resource id}, instances/{resource id}, or instances/{resource id}/databases/{database name}
	Parent *string `pulumi:"parent"`
}

// A collection of values returned by getList.
type GetListResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The policy parent name for the policy, support projects/{resource id}, environments/{resource id}, instances/{resource id}, or instances/{resource id}/databases/{database name}
	Parent   *string         `pulumi:"parent"`
	Policies []GetListPolicy `pulumi:"policies"`
}

func GetListOutput(ctx *pulumi.Context, args GetListOutputArgs, opts ...pulumi.InvokeOption) GetListResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetListResultOutput, error) {
			args := v.(GetListArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("bytebase:Policy/getList:getList", args, GetListResultOutput{}, options).(GetListResultOutput), nil
		}).(GetListResultOutput)
}

// A collection of arguments for invoking getList.
type GetListOutputArgs struct {
	// The policy parent name for the policy, support projects/{resource id}, environments/{resource id}, instances/{resource id}, or instances/{resource id}/databases/{database name}
	Parent pulumi.StringPtrInput `pulumi:"parent"`
}

func (GetListOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetListArgs)(nil)).Elem()
}

// A collection of values returned by getList.
type GetListResultOutput struct{ *pulumi.OutputState }

func (GetListResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetListResult)(nil)).Elem()
}

func (o GetListResultOutput) ToGetListResultOutput() GetListResultOutput {
	return o
}

func (o GetListResultOutput) ToGetListResultOutputWithContext(ctx context.Context) GetListResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetListResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetListResult) string { return v.Id }).(pulumi.StringOutput)
}

// The policy parent name for the policy, support projects/{resource id}, environments/{resource id}, instances/{resource id}, or instances/{resource id}/databases/{database name}
func (o GetListResultOutput) Parent() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetListResult) *string { return v.Parent }).(pulumi.StringPtrOutput)
}

func (o GetListResultOutput) Policies() GetListPolicyArrayOutput {
	return o.ApplyT(func(v GetListResult) []GetListPolicy { return v.Policies }).(GetListPolicyArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetListResultOutput{})
}
