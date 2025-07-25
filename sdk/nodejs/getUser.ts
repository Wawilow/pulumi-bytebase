// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The user data source.
 */
export function getUser(args: GetUserArgs, opts?: pulumi.InvokeOptions): Promise<GetUserResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("bytebase:index/getUser:getUser", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getUser.
 */
export interface GetUserArgs {
    /**
     * The user name in users/{user id or email} format.
     */
    name: string;
}

/**
 * A collection of values returned by getUser.
 */
export interface GetUserResult {
    /**
     * The user email.
     */
    readonly email: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The user last change password time.
     */
    readonly lastChangePasswordTime: string;
    /**
     * The user last login time.
     */
    readonly lastLoginTime: string;
    /**
     * The mfaEnabled flag means if the user has enabled MFA.
     */
    readonly mfaEnabled: boolean;
    /**
     * The user name in users/{user id or email} format.
     */
    readonly name: string;
    /**
     * The user phone.
     */
    readonly phone: string;
    /**
     * Source means where the user comes from. For now we support Entra ID SCIM sync, so the source could be Entra ID.
     */
    readonly source: string;
    /**
     * The user is deleted or not.
     */
    readonly state: string;
    /**
     * The user title.
     */
    readonly title: string;
    /**
     * The user type.
     */
    readonly type: string;
}
/**
 * The user data source.
 */
export function getUserOutput(args: GetUserOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetUserResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("bytebase:index/getUser:getUser", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getUser.
 */
export interface GetUserOutputArgs {
    /**
     * The user name in users/{user id or email} format.
     */
    name: pulumi.Input<string>;
}
