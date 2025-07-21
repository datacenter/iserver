# Task: cli virtctl

## Input Data Model

Minimum intent definition (showing tasks.cli content only for brevity)

```
{
    "virtctl": true
}
```

```
{
    "virtctl": {}
}
```

```
{
    "virtctl": {
        "enabled": true
    }
}
```

Complete input showing defaults

```
{
    "enabled": true,
    "download_url": "https://hyperconverged-cluster-cli-download-openshift-cnv.apps.bm.ocp.domain.com/amd64/linux/virtctl.tar.gz"
}
```

Configuration tips:
- change virtctl:download_url for custom download url
- it is expected that binary is in tar.gz format and contains single file called 'virtctl'

## Workflow

- download binary from virtctl:download_url
- upload binary to cluster management node selected with kube:true
- unpack tarball content to /usr/local/bin
- make virtctl executable (chmod a+x /usr/local/bin/virtctl)
- check 'virtctl version' output

## Output

Example

```
Task cli virtctl
----------------
{
    "enabled": true,
    "download_url": "https://hyperconverged-cluster-cli-download-openshift-cnv.apps.bm.ocp.domain.com/amd64/linux/virtctl.tar.gz"
}
Check for cluster endpoint to download virtctl binary from...
Wait for endpoint openshift-cnv/hyperconverged-cluster-cli-download...
Downloading virtctl binary from https://hyperconverged-cluster-cli-download-openshift-cnv.apps.bm.ocp.domain.com/amd64/linux/virtctl.tar.gz
Uploading virtctl binary to cluster management node
Unpack
Change file flags
Virtctl binary ready to be used
Client Version: version.Info{GitVersion:"v1.4.1-21-g146cc65682", GitCommit:"146cc65682210b17688d9b1c6d93d17d3443dd6c", GitTreeState:"clean", BuildDate:"2025-06-13T04:49:58Z", GoVersion:"go1.22.12 (Red Hat 1.22.12-2.el9_5) X:strictfipsruntime", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{GitVersion:"v1.4.1-21-g146cc65682", GitCommit:"146cc65682210b17688d9b1c6d93d17d3443dd6c", GitTreeState:"clean", BuildDate:"2025-06-12T04:56:24Z", GoVersion:"go1.22.12 (Red Hat 1.22.12-2.el9_5) X:strictfipsruntime", Compiler:"gc", Platform:"linux/amd64"}
```

[Back](./input_data_tasks_cli.md)