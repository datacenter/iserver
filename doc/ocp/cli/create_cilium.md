# Cilium

Add cilium cli on the cluster [management node](../ManagementServer.md)

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

OpenShift Workflow - CLI - Add cilium
=====================================

OpenShift Cluster: bm1
Uploading file to cluster management node: /tmp/0dfa09a1-d393-4902-bb35-868b7b259fc8
Unpack: sudo tar xzvfC /tmp/0dfa09a1-d393-4902-bb35-868b7b259fc8 /tmp/
Copy file: sudo sudo mv /tmp/cilium /usr/local/bin/cilium
Change file flags: sudo chmod a+x /usr/local/bin/cilium
Test: cilium version

~~~
cilium-cli: v0.19.2 compiled with go1.25.5 on linux/amd64
cilium image (default): v1.19.1
cilium image (stable): unknown
cilium image (running): unknown. Unable to obtain cilium version. Reason: release: not found
~~~

Completed tasks
- cilium installed

+----+---------+-------+---------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow      | Changes | Success | Duration [s] |
+----+---------+-------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | create cilium | 0       | V       | 124          | 
+----+---------+-------+---------------+---------+---------+--------------+
```

[[Back]](./README.md)