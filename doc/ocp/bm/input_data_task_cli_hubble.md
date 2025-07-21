# Task: cli hubble

## Input Data Model

Minimum intent definition (showing tasks.cli content only for brevity)

```
{
    "hubble": true
}
```

```
{
    "hubble": {}
}
```

```
{
    "hubble": {
        "enabled": true
    }
}
```

Complete input showing defaults

```
{
    "enabled": true,
    "version_url": "https://raw.githubusercontent.com/cilium/hubble/main/stable.txt",
    "version": "v1.17.5",
    "download_url": "https://github.com/cilium/hubble/releases/download/v1.17.5/hubble-linux-amd64.tar.gz"
}
```

Configuration tips:
- change hubble:version to control the download_url version part
- change hubble:download_url for custom download url
- it is expected that binary is in tar.gz format and contains single file called 'hubble'

## Workflow

- check cluster:network_type, if not Cilium then disable hubble cli and exit
- download binary from hubble:download_url
- upload binary to cluster management node selected with kube:true
- unpack tarball content to /usr/local/bin
- make hubble executable (chmod a+x /usr/local/bin/hubble)
- check 'hubble version' output

## Output

Example

```
Task cli hubble
---------------
{
    "enabled": true,
    "version_url": "https://raw.githubusercontent.com/cilium/hubble/main/stable.txt",
    "version": "v1.17.5",
    "download_url": "https://github.com/cilium/hubble/releases/download/v1.17.5/hubble-linux-amd64.tar.gz"
}
Downloading hubble binary from https://github.com/cilium/hubble/releases/download/v1.17.5/hubble-linux-amd64.tar.gz
Uploading hubble binary to cluster management node
Unpack
Change file flags
Hubble binary ready to be used
hubble v1.17.5@HEAD-13fb5dc compiled with go1.24.4 on linux/amd64
```

[Back](./input_data_tasks_cli.md)