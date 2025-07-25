// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package project

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/wawilow/pulumi-bytebase/sdk/go/bytebase/internal"
)

// The project data source list.
func GetList(ctx *pulumi.Context, args *GetListArgs, opts ...pulumi.InvokeOption) (*GetListResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetListResult
	err := ctx.Invoke("bytebase:Project/getList:getList", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getList.
type GetListArgs struct {
	// If not include the default project in the response.
	ExcludeDefault *bool `pulumi:"excludeDefault"`
	// Filter projects by name or resource id with wildcard.
	Query *string `pulumi:"query"`
	// Filter projects by state. Default ACTIVE.
	State *string `pulumi:"state"`
}

// A collection of values returned by getList.
type GetListResult struct {
	// If not include the default project in the response.
	ExcludeDefault *bool `pulumi:"excludeDefault"`
	// The provider-assigned unique ID for this managed resource.
	Id       string           `pulumi:"id"`
	Projects []GetListProject `pulumi:"projects"`
	// Filter projects by name or resource id with wildcard.
	Query *string `pulumi:"query"`
	// Filter projects by state. Default ACTIVE.
	State *string `pulumi:"state"`
}

func GetListOutput(ctx *pulumi.Context, args GetListOutputArgs, opts ...pulumi.InvokeOption) GetListResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetListResultOutput, error) {
			args := v.(GetListArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("bytebase:Project/getList:getList", args, GetListResultOutput{}, options).(GetListResultOutput), nil
		}).(GetListResultOutput)
}

// A collection of arguments for invoking getList.
type GetListOutputArgs struct {
	// If not include the default project in the response.
	ExcludeDefault pulumi.BoolPtrInput `pulumi:"excludeDefault"`
	// Filter projects by name or resource id with wildcard.
	Query pulumi.StringPtrInput `pulumi:"query"`
	// Filter projects by state. Default ACTIVE.
	State pulumi.StringPtrInput `pulumi:"state"`
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

// If not include the default project in the response.
func (o GetListResultOutput) ExcludeDefault() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v GetListResult) *bool { return v.ExcludeDefault }).(pulumi.BoolPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetListResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetListResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetListResultOutput) Projects() GetListProjectArrayOutput {
	return o.ApplyT(func(v GetListResult) []GetListProject { return v.Projects }).(GetListProjectArrayOutput)
}

// Filter projects by name or resource id with wildcard.
func (o GetListResultOutput) Query() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetListResult) *string { return v.Query }).(pulumi.StringPtrOutput)
}

// Filter projects by state. Default ACTIVE.
func (o GetListResultOutput) State() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetListResult) *string { return v.State }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetListResultOutput{})
}
