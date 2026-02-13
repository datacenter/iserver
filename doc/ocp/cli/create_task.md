# CLI Tools - Create via Task

## Input

```
[
  {
    "cli": {
      "butane": {},
      "cilium": {},
      "helm": {},
      "hubble": {},
      "virtctl": {},
      "web": {
        "operator": {}
      }
    }
  }
]
```

Notes:
- [butane](./butane.md), [cilium](./cilium.md), [helm](./helm.md), [hubble](./hubble.md), [virtctl](./virtctl.md) and [web](../web-terminal/README.md) trigger workflow execution with optional input parameters

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Expected outcome

CLI tool installed

## Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - CLI Tools Installation
===========================================

Workflow Parameters
-------------------
{
    "helm": {
        "enabled": true,
        "cluster": "bm1",
        "confirmation": false,
        "version_url": "https://get.helm.sh/helm-latest-version",
        "version": "v3.19.0",
        "download_url": "https://get.helm.sh/helm-v3.19.0-linux-amd64.tar.gz"
    },
    "cluster": "bm1",
    "exec": [],
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok


OpenShift Workflow - Install helm cli
=====================================

Workflow Parameters
-------------------
{
    "enabled": true,
    "cluster": "bm1",
    "confirmation": false,
    "version_url": "https://get.helm.sh/helm-latest-version",
    "version": "v3.19.0",
    "download_url": "https://get.helm.sh/helm-v3.19.0-linux-amd64.tar.gz",
    "url": "https://get.helm.sh/helm-v3.19.0-linux-amd64.tar.gz",
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok
- cluster node [*****]: ok
- management node [*****]: ok
- cli helm: ok

Downloading helm binary from https://get.helm.sh/helm-v3.19.0-linux-amd64.tar.gz
Uploading helm binary to cluster management node
Unpack
Copy helm to /usr/local/bin
Remove local files
Change file flags

OpenShift Workflow - .bashrc proxy settings
===========================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "inherit": true,
    "http_proxy": null,
    "https_proxy": null,
    "no_proxy": null,
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok
- cluster node [*****]: ok
- management node [*****]: ok

Proxy settings inherited from cluster proxy
...

Completed tasks
- helm installed
- proxy settings configured
- helm ready to use
version.BuildInfo{Version:"v3.19.0", GitCommit:"3d8990f0836691f0229297773f3524598f46bda6", GitTreeState:"clean", GoVersion:"go1.24.7"}
```

[[Back]](./README.md)