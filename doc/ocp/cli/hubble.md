# Cilium

Add cilium cli on the cluster [management node](../Access.md)

## Workflow

- if --version value is not defined check helm version using https://raw.githubusercontent.com/cilium/hubble/main/stable.txt
- if --url value is not defined then url defaults to https://github.com/cilium/hubble/releases/download/VERSION/hubble-linux-amd64.tar.gz
- download tarball
- upload tarball to cluster's management node 
- unpack and prepare binary in /usr/local/bin

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Expected outcome

```
$ ssh core@10.10.10.10                                  
[core@bm1 ~]$ which hubble
/usr/local/bin/hubble
[core@bm1 ~]$ $ hubble --help
Hubble is a utility to observe and inspect recent Cilium routed traffic in a cluster.

Usage:
  hubble [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  config      Modify or view hubble config
  help        Help about any command
  list        List Hubble objects
  observe     Observe flows and events of a Hubble server
  status      Display status of Hubble server
  version     Display detailed version information
```

## Configurable options

```
# iserver set ocp cli-hubble 
  --cluster TEXT  OCP cluster name
  --url TEXT      Hubble download url
  --version TEXT  Hubble version
```

## Example

```
# iserver set ocp cli-hubble --cluster bm1


OpenShift Workflow - Install hubble cli
=======================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "url": "https://github.com/cilium/hubble/releases/download/v1.18.3/hubble-linux-amd64.tar.gz",
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
- cli hubble: not found

Downloading hubble binary from https://github.com/cilium/hubble/releases/download/v1.18.3/hubble-linux-amd64.tar.gz
Uploading hubble binary to cluster management node
Unpack
Change file flags
Hubble binary ready to be used
hubble v1.18.3@HEAD-c568539 compiled with go1.25.3 on linux/amd64
```

[[Back]](./README.md)