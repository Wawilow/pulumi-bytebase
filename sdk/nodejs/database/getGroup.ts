// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The database group data source.
 */
export function getGroup(args: GetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetGroupResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("bytebase:Database/getGroup:getGroup", {
        "project": args.project,
        "resourceId": args.resourceId,
    }, opts);
}

/**
 * A collection of arguments for invoking getGroup.
 */
export interface GetGroupArgs {
    /**
     * The project fullname in projects/{id} format.
     */
    project: string;
    /**
     * The database group unique resource id.
     */
    resourceId: string;
}

/**
 * A collection of values returned by getGroup.
 */
export interface GetGroupResult {
    /**
     * The database group condition.
     */
    readonly condition: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The matched databases in the group.
     */
    readonly matchedDatabases: string[];
    /**
     * The project fullname in projects/{id} format.
     */
    readonly project: string;
    /**
     * The database group unique resource id.
     */
    readonly resourceId: string;
    /**
     * The database group title.
     */
    readonly title: string;
}
/**
 * The database group data source.
 */
export function getGroupOutput(args: GetGroupOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetGroupResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("bytebase:Database/getGroup:getGroup", {
        "project": args.project,
        "resourceId": args.resourceId,
    }, opts);
}

/**
 * A collection of arguments for invoking getGroup.
 */
export interface GetGroupOutputArgs {
    /**
     * The project fullname in projects/{id} format.
     */
    project: pulumi.Input<string>;
    /**
     * The database group unique resource id.
     */
    resourceId: pulumi.Input<string>;
}
