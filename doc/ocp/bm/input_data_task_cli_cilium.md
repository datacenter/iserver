# Task: cli cilium

## Input Data Model

Minimum intent definition (showing tasks.cli content only for brevity)

```
{
    "cilium": true
}
```

```
{
    "cilium": {}
}
```

```
{
    "cilium": {
        "enabled": true
    }
}
```

Complete input showing defaults

```
{
    "enabled": true,
    "version_url": "https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt",
    "version": "v0.18.5",
    "download_url": "https://github.com/cilium/cilium-cli/releases/download/v0.18.5/cilium-linux-amd64.tar.gz"
}
```

Configuration tips:
- change cilium:version to control the download_url version part
- change cilium:download_url for custom download url
- it is expected that binary is in tar.gz format and contains single file called 'cilium'

## Workflow

- check cluster:network_type, if not Cilium then disable cilium cli and exit
- download binary from cilium:download_url
- upload binary to cluster management node selected with kube:true
- unpack tarball content to /usr/local/bin
- make cilium executable (chmod a+x /usr/local/bin/cilium)
- check 'cilium version' output

## Output

Example

```
Task cli cilium
---------------
{
    "enabled": true,
    "version_url": "https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt",
    "version": "v0.18.5",
    "download_url": "https://github.com/cilium/cilium-cli/releases/download/v0.18.5/cilium-linux-amd64.tar.gz"
}
Downloading cilium binary from https://github.com/cilium/cilium-cli/releases/download/v0.18.5/cilium-linux-amd64.tar.gz
Uploading cilium binary to cluster management node
Unpack
Change file flags
Cilium binary ready to be used
cilium-cli: v0.18.5 compiled with go1.24.4 on linux/amd64
cilium image (default): v1.17.5
cilium image (stable): unknown
cilium image (running): unknown. Unable to obtain cilium version. Reason: release: not found
```

[Back](./input_data_tasks_cli.md)