---
title: Bytebase Installation & Configuration
meta_desc: Information on how to install the Bytebase provider.
layout: installation
---

## Installation

The Pulumi Bytebase provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@wawilow/pulumi-bytebase`](https://www.npmjs.com/package/@wawilow/pulumi-bytebase)
* Python: [`pulumi-bytebase`](https://pypi.org/project/pulumi-bytebase/)
* Go: [`github.com/wawilow/pulumi-bytebase/sdk/go/bytebase`](https://github.com/pulumi/pulumi-aws/tree/master/sdk/go/bytebase)

[//]: # (* .NET: [`pulumi-bytebase.Bytebase`]&#40;https://www.nuget.org/packages/pulumi-bytebase.Bytebase&#41;)


## Configuration

> Note:
> hiii, I'll finish all docs later

### Provider Binary

The Bytebase provider binary is a third party binary. It can be installed using the `pulumi plugin` command.

```bash
pulumi plugin install resource bytebase <version>
```

Replace the version string `<version>` with your desired version.
