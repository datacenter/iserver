# Cilium

Add cilium cli on the cluster [management node](../Access.md)

## Workflow

- if --version value is not defined check helm version using https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt
- if --url value is not defined then url defaults to https://github.com/cilium/cilium-cli/releases/download/VERSION/cilium-linux-amd64.tar.gz
- download tarball
- upload tarball to cluster's management node 
- unpack and prepare binary in /usr/local/bin

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Expected outcome

```
$ ssh core@10.10.10.10                                  
[core@bm1 ~]$ which cilium
/usr/local/bin/cilium
[core@bm1 ~]$ $ cilium --help
CLI to install, manage, & troubleshooting Cilium clusters running Kubernetes.

Cilium is a CNI for Kubernetes to provide secure network connectivity and
load-balancing with excellent visibility using eBPF
...
```

## Configurable options

```
# iserver set ocp cli-cilium 
  --cluster TEXT  OCP cluster name
  --url TEXT      Cilium download url
  --version TEXT  Cilium version
```

## Example

```
# iserver set ocp cli-cilium --cluster bm1

OpenShift Workflow - Install cilium cli
=======================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "url": "https://github.com/cilium/cilium-cli/releases/download/v0.18.8/cilium-linux-amd64.tar.gz",
    "version": null,
    "confirmation": true,
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- management node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- cli cilium: not found

Downloading cilium binary from https://github.com/cilium/cilium-cli/releases/download/v0.18.8/cilium-linux-amd64.tar.gz
Uploading cilium binary to cluster management node
Unpack
Change file flags
Cilium binary ready to be used
cilium-cli: v0.18.8 compiled with go1.25.3 on linux/amd64
cilium image (default): v1.18.2
cilium image (stable): unknown
cilium image (running): unknown. Unable to obtain cilium version. Reason: release: not found
```

[[Back]](./README.md)