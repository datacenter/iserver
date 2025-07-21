# Task: cli helm

## Input Data Model

Minimum intent definition (showing tasks.cli content only for brevity)

```
{
    "helm": true
}
```

```
{
    "helm": {}
}
```

```
{
    "helm": {
        "enabled": true
    }
}
```

Complete input showing defaults

```
{
    "enabled": true,
    "version_url": "https://get.helm.sh/helm-latest-version",
    "version": "v3.18.4",
    "download_url": "https://get.helm.sh/helm-v3.18.4-linux-amd64.tar.gz"
}
```

Configuration tips:
- change helm:version to control the download_url version part
- change helm:download_url for custom download url
- it is expected that binary is in tar.gz format and contains file called 'helm'

## Workflow

- download binary from helm:download_url
- upload binary to cluster management node selected with kube:true
- unpack tarball content locally and move helm binary to /usr/local/bin
- make helm executable (chmod a+x /usr/local/bin/helm)
- delete local unpack directory
- check 'helm version' output

## Output

Example

```
Task cli helm
-------------
{
    "enabled": true,
    "version_url": "https://get.helm.sh/helm-latest-version",
    "version": "v3.18.4",
    "download_url": "https://get.helm.sh/helm-v3.18.4-linux-amd64.tar.gz"
}
Downloading helm binary from https://get.helm.sh/helm-v3.18.4-linux-amd64.tar.gz
Uploading helm binary to cluster management node
Unpack
Copy helm to /usr/local/bin
Remove local files
Change file flags
Helm binary ready to be used
version.BuildInfo{Version:"v3.18.4", GitCommit:"d80839cf37d860c8aa9a0503fe463278f26cd5e2", GitTreeState:"clean", GoVersion:"go1.24.4"}
```

[Back](./input_data_tasks_cli.md)