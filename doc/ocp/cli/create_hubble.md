# Hubble

Add hubble cli on the cluster [management node](../ManagementServer.md)

## Workflow

>[!CAUTION]
>In some cases it may be required to use the hubble-cli version matching your cilium cni version rather that taking the latest stable

- `--version` value based on available [releases](https://github.com/cilium/hubble/releases) e.g., v1.18.6
- if `--version` value is not defined check helm version using https://raw.githubusercontent.com/cilium/hubble/main/stable.txt
- if `--url` value is not defined then url defaults to https://github.com/cilium/hubble/releases/download/VERSION/hubble-linux-amd64.tar.gz
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
  --overwrite     Overwrite if exists
```

## Example

```
# iserver set ocp cli-hubble --cluster bm1

OpenShift Workflow - CLI - Add hubble
=====================================

OpenShift Cluster: bm1
Download: https://github.com/cilium/hubble/releases/download/v1.19.3/hubble-linux-amd64.tar.gz
Uploading file to cluster management node: /tmp/fa174554-e350-478f-b157-963e90824744
Unpack: sudo tar xzvfC /tmp/fa174554-e350-478f-b157-963e90824744 /tmp/
Copy file: sudo sudo mv /tmp/hubble /usr/local/bin/hubble
Change file flags: sudo chmod a+x /usr/local/bin/hubble
Test: hubble version

~~~
hubble v1.19.3@HEAD-400168b compiled with go1.26.2 on linux/amd64
~~~

Completed tasks
- hubble installed

+----+---------+-------+---------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow      | Changes | Success | Duration [s] |
+----+---------+-------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | create hubble | 0       | V       | 38           | 
+----+---------+-------+---------------+---------+---------+--------------+
```

[[Back]](./README.md)