# Developing with a Terraform Bridge Provider

This document describes the procedures for developing and maintaining a Pulumi
provider based on the Pulumi Terraform Bridge.

- [Developing with a Terraform Bridge Provider](#developing-with-a-terraform-bridge-provider)
  - [Creating a Pulumi Terraform Bridge Provider](#creating-a-pulumi-terraform-bridge-provider)
    - [Prerequisites](#prerequisites)
    - [Publishing checklist](#publishing-checklist)
    - [Composing the Provider Code - Prerequisites](#composing-the-provider-code---prerequisites)
  - [Adding Mappings, Building the Provider and SDKs](#adding-mappings-building-the-provider-and-sdks)
    - [Autogeneration of mappings](#autogeneration-of-mappings)
    - [Manually add mappings](#manually-add-mappings)
    - [Building the provider and SDKs](#building-the-provider-and-sdks)
  - [Sample Program](#sample-program)
  - [Add End-to-end Testing](#add-end-to-end-testing)
  - [CI/CD with GitHub Actions](#cicd-with-github-actions)

## Creating a Pulumi Terraform Bridge Provider

The following instructions cover:

- providers maintained by Pulumi (denoted with a "Pulumi Official" checkmark on the Pulumi registry)
- providers published and maintained by the Pulumi community, referred to as "third-party" providers

We showcase a Pulumi-owned provider based on an upstream provider named
`terraform-provider-bytebase`.  Substitute
appropriate values below for your use case.

> Note: If the name of the desired Pulumi provider differs from the name of the
> Terraform provider, you will need to carefully distinguish between the
> references - see <https://github.com/pulumi/pulumi-azure> for an example.

### Prerequisites

Ensure the following tools are installed and present in your `$PATH`:

* [`pulumictl`](https://github.com/pulumi/pulumictl#installation)
* [Go 1.17](https://golang.org/dl/) or 1.latest
* [NodeJS](https://nodejs.org/en/) 16.x. We recommend using [nvm](https://github.com/nvm-sh/nvm) to manage NodeJS installations.
* [Yarn](https://yarnpkg.com/)
* [TypeScript](https://www.typescriptlang.org/)
* [Python](https://www.python.org/downloads/) (called as `python3`). For recent
  versions of MacOS, the system-installed version is fine.
* [.NET](https://dotnet.microsoft.com/download)

### Publishing checklist

When publishing a new release, the following points should be observed to ensure
that the publishing process is successful:


- [ ] Before creating a new realease, build the SDKs locally `make build_sdks`
  using the `main`branch of the repository and check with `git status` for
  changes of workspace. If any changes are created, create a pull qreuest to
  sync the SDK changes to the `main` branch.
- [ ] Ensure that the local GO version used to compile the provider match the
  version used in the GitHub Release Workflow `release.yaml`
- [ ] Check for messages of `tfgen` containing `no-resource plugin` and add
  missing Pulumi resource plugins to the `install_plugins` target in `Makefile`
- [ ] Ensure that the `dotnet` version required by the `*.csproj`-file in
  in the `<TargetFramework>` element is configured in the `release.yaml` file
- [ ] Ensure you registered the provider in the
  `community-packages/package-list.json` in the [Pulumi Registry](https://github.com/pulumi/registry) repo

### Composing the Provider Code - Prerequisites

Pulumi provider repositories have the following general structure:

* `examples/` contains sample code which may optionally be included as
  integration tests to be run as part of a CI/CD pipeline.
* `provider/` contains the Go code used to create the provider as well as
  generate the SDKs in the various languages that Pulumi supports.
  * `provider/cmd/pulumi-tfgen-bytebase`
    generates the Pulumi resource schema (`schema.json`), based on the Terraform
    provider's resources.
  * `provider/cmd/pulumi-resource-bytebase`
    generates the SDKs in all supported languages from the schema, placing them
    in the `sdk/` folder.
  * `provider/pkg/resources.go` is the location where we will define the
    Terraform-to-Pulumi mappings for resources.
* `sdk/` contains the generated SDK code for each of the language platforms that
  Pulumi supports, with each supported platform in a separate subfolder.

1. In `provider/go.mod`, add a reference to the upstream Terraform provider in the `require` section, e.g.

    ```go
    github.com/foo/terraform-provider-bytebase v0.4.0
    ```

1. In `provider/resources.go`, ensure the reference in the `import` section uses the correct Go module path, e.g.:

    ```go
    github.com/foo/terraform-provider-bytebase/bytebase
    ```

1. Download the dependencies:

    ```bash
    cd provider && go mod tidy && cd -
    ```

1. Create the schema by running the following command:

    ```bash
    make tfgen
    ```

    Note warnings about unmapped resources and data sources in the command's output.  We map these in the next section, e.g.:

    ```text
    warning: resource bytebase_something not found in provider map; skipping
    warning: resource bytebase_something_else not found in provider map; skipping
    warning: data source bytebase_something not found in provider map; skipping
    warning: data source bytebase_something_else not found in provider map; skipping
    ```

## Adding Mappings, Building the Provider and SDKs

In this section we will add the mappings that allow the interoperation between
the Pulumi provider and the Terraform provider. Terraform resources map to an
identically named concept in Pulumi. Terraform data sources map to plain old
functions in your supported programming language of choice. Pulumi also allows
provider functions and resources to be grouped into _namespaces_ to improve the
cohesion of a provider's code, thereby making it easier for developers to use.
If your provider has a large number of resources, consider using namespaces to
improve usability.

### Autogeneration of mappings

The repository utilizes the autodiscovery mechanism of Pulumi Terraform Bridge
which automatically maps resources and data sources from the upstream Terraform
provider to Pulumi resources and functions.

However, it is still possible to configure resources and data sources manually
via the `Resources` and `DataSources` properties of the struct
`tfbridge.ProviderInfo`. These manual configurations have a higher precedence than
the configurations of the autodiscovery mechanism.

### Manually add mappings
The following instructions all pertain to `provider/resources.go`, in the
section of the code where we construct a `tfbridge.ProviderInfo` object:

1. **Add resource mappings:** For each resource in the provider, add an entry in
   the `Resources` property of the `tfbridge.ProviderInfo`, e.g.:


    ```go
    // Most providers will have all resources (and data sources) in the main module.
    // Note the mapping from snake_case HCL naming conventions to UpperCamelCase Pulumi SDK naming conventions.
    // The name of the provider is omitted from the mapped name due to the presence of namespaces in all supported Pulumi languages.
    "bytebase_something":      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Something")},
    "bytebase_something_else": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SomethingElse")},
    ```

1. **Add CSharpName (if necessary):** Dotnet does not allow for fields named the
    same as the enclosing type, which sometimes results in errors during the
    dotnet SDK build. If you see something like
    ```text
    error CS0542: 'ApiKey': member names cannot be the same as their enclosing type [/Users/guin/go/src/github.com/pulumi/pulumi-artifactory/sdk/dotnet/Pulumi.Artifactory.csproj]
    ```
    you'll want to give your Resource a CSharpName, which can have any value that makes sense:

    ```go
    "bytebase_something_dotnet": {
        Tok: tfbridge.MakeResource(mainPkg, mainMod, "SomethingDotnet"),
        Fields: map[string]*tfbridge.SchemaInfo{
            "something_dotnet": {
                CSharpName: "SpecialName",
            },
        },
    },
    ```

   [See the underlying terraform-bridge code here.](https://github.com/pulumi/pulumi-terraform-bridge/blob/master/pkg/tfbridge/info.go#L168)

1. **Add data source mappings:** For each data source in the provider, add an entry in the `DataSources` property of the `tfbridge.ProviderInfo`, e.g.:

    ```go
    // Note the 'get' prefix for data sources
    "bytebase_something":      {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getSomething")},
    "bytebase_something_else": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getSomethingElse")},
    ```

1. **Add documentation mapping (sometimes needed):**  If the upstream provider's
   repo is not a part of the `terraform-providers` GitHub organization, specify
   the `GitHubOrg` property of `tfbridge.ProviderInfo` to ensure that
   documentation is picked up by the codegen process, and that attribution for
   the upstream provider is correct, e.g.:


    ```go
    GitHubOrg: "wawilow",
    ```

1. **Add provider configuration overrides (not typically needed):** Pulumi's
   Terraform bridge automatically detects configuration options for the upstream
   provider.  However, in rare cases these settings may need to be overridden,
   e.g. if we want to change an environment variable default from `API_KEY` to
   `bytebase_API_KEY`.  Examples of common
   uses cases:


    ```go
    "additional_required_parameter": {},
    "additional_optional_string_parameter": {
        Default: &tfbridge.DefaultInfo{
            Value: "default_value",
        },
    "additional_optional_boolean_parameter": {
        Default: &tfbridge.DefaultInfo{
            Value: true,
        },
    // Renamed environment variables can be accounted for like so:
    "apikey": {
        Default: &tfbridge.DefaultInfo{
            EnvVars: []string{"bytebase_API_KEY"},
        },
    ```

### Building the provider and SDKs

1. Build the provider binary and ensure there are no warnings about unmapped
   resources and no warnings about unmapped data sources:

    ```bash
    make provider
    ```

    You may see warnings about documentation and examples, including "unexpected
    code snippets".  These can be safely ignored for now.  Pulumi will add
    additional documentation on mapping docs in a future revision of this guide.

1. Build the SDKs in the various languages Pulumi supports:

    ```bash
    make build_sdks
    ```

1. Ensure the Golang SDK is a proper go module:

    ```bash
    cd sdk && go mod tidy && cd -
    ```

    This will pull in the correct dependencies in `sdk/go.mod` as well as setting the dependency tree in `sdk/go.sum`.

1. Finally, ensure the provider code conforms to Go standards:

    ```bash
    make lint_provider
    ```

    Fix any issues found by the linter.

**Note:** If you make revisions to code in `resources.go`, you must re-run the `make tfgen` target to regenerate the schema.
The `make tfgen` target will take the file `schema.json` and serialize it to a byte array so that it can be included in the build output.
(This is a holdover from Go 1.16, which does not have the ability to directly embed text files. We are working on removing the need for this step.)

## Sample Program

In this section, we will create a Pulumi program in TypeScript that utilizes the
provider we created to ensure everything is working properly.

1. Create an account with the provider's service and generate any necessary credentials, e.g. API keys.

    * Email: bot@pulumi.com
    * Password: (Create a random password in 1Password with the  maximum length and complexity allowed by the provider.)
    * Ensure all secrets (passwords, generated API keys) are stored in Pulumi's 1Password vault.

1. Copy the `pulumi-resource-bytebase` binary
   generated by `make provider` and place it in your `$PATH` (`$GOPATH/bin` is a
   convenient choice), e.g.:

    ```bash
    cp bin/pulumi-resource-bytebase $GOPATH/bin
    ```

1. Tell Yarn to use your local copy of the SDK:

    ```bash
    make install_nodejs_sdk
    ```

1. Create a new Pulumi program in the `examples/` directory, e.g.:

    ```bash
    mkdir examples/my-example/ts # Change "my-example" to something more meaningful.
    cd examples/my-example/ts
    pulumi new typescript
    # (Go through the prompts with the default values)
    npm install
    yarn link @wawilow/pulumi-bytebase
    ```

1. Create a minimal program for the provider, i.e. one that creates the
   smallest-footprint resource.  Place this code in `index.ts`.

1. Configure any necessary environment variables for authentication, e.g
   `$FOO_USERNAME`, `$FOO_TOKEN`, in your local environment.

1. Ensure the program runs successfully via `pulumi up`.

1. Once the program completes successfully, verify the resource was created in
   the provider's UI.

1. Destroy any resources created by the program via `pulumi destroy`.

Optionally, you may create additional examples for SDKs in other languages
supported by Pulumi:

1. Python:

    ```bash
    mkdir examples/my-example/py
    cd examples/my-example/py
    pulumi new python
    # (Go through the prompts with the default values)
    source venv/bin/activate # use the virtual Python env that Pulumi sets up for you
    pip install pulumi_bytebase
    ```

1. Follow the steps above to verify the program runs successfully.

## Add End-to-end Testing

We can run integration tests on our examples using the `*_test.go` files in the
`examples/` folder.

1. Add code to `examples_nodejs_test.go` to call the example you created, e.g.:

    ```go
    // Swap out MyExample and "my-example" below with the name of your integration test.
    func TestAccMyExampleTs(t *testing.T) {
        test := getJSBaseOptions(t).
            With(integration.ProgramTestOptions{
                Dir: filepath.Join(getCwd(t), "my-example", "ts"),
            })
        integration.ProgramTest(t, &test)
    }
    ```

1. Add a similar function for each example that you want to run in an
   integration test.  For examples written in other languages, create similar
   files for `examples_${LANGUAGE}_test.go`.

1. You can run these tests locally via Make:

    ```bash
    make test
    ```

    You can also run each test file separately via test tags:

    ```bash
    cd examples && go test -v -tags=nodejs
    ```

## CI/CD with GitHub Actions

The repository contains two GitHub workflows for publishing new releases and
performing build validation for pull requests:

- Release workflow: `.github/workflows/release.yml`
- Pull Request validation: `.github/workflows/pull-request.yml`

The GitHub release workflow requires the following GitHub secrets (variables) to
be configured in the workflow envinronment. Refer to the [GitHub documentation](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
how to configure secrets and variables for workflows for any details.

- `GITHUB_TOKEN`: The GitHhub is required to push a new release of the provider
      to GitHub. Thus the GitHub token must include the permission `contents:
      write`
- `NPM_TOKEN`: The token is used to authenticate towards NPMJS.com to push the NodeJS SDK
- `NUGET_PUBLISH_KEY`: The token is required to publish the dotnet SDK to nuget.org
- `PYPI_PASSWORD`: The token is used to publish the Python SDK on PyPi.org

> **Note:**
> The release workflow will be triggred when a new version tag (format: `v*`) is
> pushed to the repository.

Now you are ready to use the provider, cut releases, and have some well-deserved :ice_cream:!
