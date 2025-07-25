// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Role extends pulumi.CustomResource {
    /**
     * Get an existing Role resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RoleState, opts?: pulumi.CustomResourceOptions): Role {
        return new Role(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'bytebase:index/role:Role';

    /**
     * Returns true if the given object is an instance of Role.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Role {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Role.__pulumiType;
    }

    /**
     * The role description.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The role full name in roles/{resource id} format.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The role permissions. Permissions should start with "bb." prefix. Check https://github.com/bytebase/bytebase/blob/main/backend/component/iam/permission.yaml for all permissions.
     */
    public readonly permissions!: pulumi.Output<string[]>;
    /**
     * The role unique resource id.
     */
    public readonly resourceId!: pulumi.Output<string>;
    /**
     * The role title.
     */
    public readonly title!: pulumi.Output<string>;
    /**
     * The role type.
     */
    public /*out*/ readonly type!: pulumi.Output<string>;

    /**
     * Create a Role resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RoleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RoleArgs | RoleState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as RoleState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["permissions"] = state ? state.permissions : undefined;
            resourceInputs["resourceId"] = state ? state.resourceId : undefined;
            resourceInputs["title"] = state ? state.title : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as RoleArgs | undefined;
            if ((!args || args.permissions === undefined) && !opts.urn) {
                throw new Error("Missing required property 'permissions'");
            }
            if ((!args || args.resourceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceId'");
            }
            if ((!args || args.title === undefined) && !opts.urn) {
                throw new Error("Missing required property 'title'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["permissions"] = args ? args.permissions : undefined;
            resourceInputs["resourceId"] = args ? args.resourceId : undefined;
            resourceInputs["title"] = args ? args.title : undefined;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Role.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Role resources.
 */
export interface RoleState {
    /**
     * The role description.
     */
    description?: pulumi.Input<string>;
    /**
     * The role full name in roles/{resource id} format.
     */
    name?: pulumi.Input<string>;
    /**
     * The role permissions. Permissions should start with "bb." prefix. Check https://github.com/bytebase/bytebase/blob/main/backend/component/iam/permission.yaml for all permissions.
     */
    permissions?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The role unique resource id.
     */
    resourceId?: pulumi.Input<string>;
    /**
     * The role title.
     */
    title?: pulumi.Input<string>;
    /**
     * The role type.
     */
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Role resource.
 */
export interface RoleArgs {
    /**
     * The role description.
     */
    description?: pulumi.Input<string>;
    /**
     * The role permissions. Permissions should start with "bb." prefix. Check https://github.com/bytebase/bytebase/blob/main/backend/component/iam/permission.yaml for all permissions.
     */
    permissions: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The role unique resource id.
     */
    resourceId: pulumi.Input<string>;
    /**
     * The role title.
     */
    title: pulumi.Input<string>;
}
