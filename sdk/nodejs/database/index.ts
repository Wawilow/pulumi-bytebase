// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { GetGroupArgs, GetGroupResult, GetGroupOutputArgs } from "./getGroup";
export const getGroup: typeof import("./getGroup").getGroup = null as any;
export const getGroupOutput: typeof import("./getGroup").getGroupOutput = null as any;
utilities.lazyLoad(exports, ["getGroup","getGroupOutput"], () => require("./getGroup"));

export { GetListArgs, GetListResult, GetListOutputArgs } from "./getList";
export const getList: typeof import("./getList").getList = null as any;
export const getListOutput: typeof import("./getList").getListOutput = null as any;
utilities.lazyLoad(exports, ["getList","getListOutput"], () => require("./getList"));

export { GroupArgs, GroupState } from "./group";
export type Group = import("./group").Group;
export const Group: typeof import("./group").Group = null as any;
utilities.lazyLoad(exports, ["Group"], () => require("./group"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "bytebase:Database/group:Group":
                return new Group(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("bytebase", "Database/group", _module)
