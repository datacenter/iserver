# OpenShift Cluster with Cilium CNI

Tasks defined in [cluster](./uc2_cluster.md) input data.

Note: that you can control versions and binary sources if required

```
  "tasks": [
    {
        "cli": {
            "bashrc": true,
            "helm": true,
            "cilium": true,
            "hubble": true,
            "virtctl": true
        }
    }
```

As the outcome, .bashrc is configured with proxy and binary tools are ready on the cluster node

```
$ ls /usr/local/bin/
hubble
cilium
helm
virtctl
```

Checks logs below to get more insights on the execution workflow.

## bashrc

```
Task cli bashrc
---------------
{
    "enabled": true,
    "http_proxy": "http://proxy.domain.com:80",
    "https_proxy": "http://proxy.domain.com:80",
    "no_proxy": "domain.com"
}
Download /var/home/core/.bashrc

export HTTP_PROXY=http://proxy.domain.com:80
export HTTPS_PROXY=http://proxy.domain.com:80
export NO_PROXY=domain.com


Upload /var/home/core/.bashrc
.bashrc uploaded with proxy settings
```

## helm

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

## cilium

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

## hubble

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

## virtctl

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

[Back](./uc2.md)