# Node - Graceful reload

[[Back]](./README.md)

Follows [Rebooting a node gracefully](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/nodes/working-with-nodes#nodes-nodes-rebooting-gracefully_nodes-nodes-rebooting) OpenShift documentation.

## Workflow

- run steps below for every selected node
- if pre-checks
    - mcp ready
    - all nodes ready
    - cluster operators available
    - if any of the condition above is not met, reload will not start
- evict all pods that are not owned by DaemonSet, ReplicaSet or Node
- shutdown the node using 'sudo shutdown -h now' via ssh

## Requirements

[SSH access](../Access.md) to cluster nodes

## Configurable options

- use --node multiple times in case you want to gracefully reload multiple nodes one after another
- use --no-checks if you want to skip pre-checks
- use --no-confirm to proceed with reboot even if pod eviction fails

```
# iserver set ocp node shutdown
  --cluster TEXT  OCP cluster name
  --node TEXT     Node name
  --no-checks     Skip checks
  --no-confirm    Confirmation mode in case of eviction problems
```

## Example

```
# iserver set ocp node shutdown --cluster bm1 --node bm1-1


OpenShift Workflow - Graceful node shutdown
===========================================

OpenShift Cluster: bm1

OpenShift Workflow - Cluster readiness check
============================================

OpenShift Cluster: bm1
Checking machine config pool
All updated
Checking nodes
All ready
Checking cluster operators
All available

+----+-------+-------+-------+--------+------+-----+-----+--------+-------------------+-----+
| ID | Node  | Ready | Taint | Memory | Disk | PID | MCP | Role   | IP                | Age |
+----+-------+-------+-------+--------+------+-----+-----+--------+-------------------+-----+
| 1  | bm1-1 | V     | ---   | V      | V    | V   | V   | Master | 10.10.10.10 (int) | 18d | 
|    |       |       |       |        |      |     |     | Worker |                   |     | 
+----+-------+-------+-------+--------+------+-----+-----+--------+-------------------+-----+
Cordone node: bm1-1

~~~
spec:
  unschedulable: true

~~~
Node patched

Evict pods
- openshift-etcd/etcd-guard-bm1-1: failed
- openshift-kube-apiserver/kube-apiserver-guard-bm1-1: failed
- openshift-kube-controller-manager/kube-controller-manager-guard-bm1-1: failed
- openshift-kube-controller-manager/revision-pruner-11-bm1-1: failed
- openshift-kube-scheduler/openshift-kube-scheduler-guard-bm1-1: failed

Wait for pod evicted

Delete pods that are left
- openshift-etcd/etcd-guard-bm1-1: success
- openshift-kube-apiserver/kube-apiserver-guard-bm1-1: success
- openshift-kube-controller-manager/kube-controller-manager-guard-bm1-1: success
- openshift-kube-controller-manager/revision-pruner-11-bm1-1: success
- openshift-kube-scheduler/openshift-kube-scheduler-guard-bm1-1: success

Wait for pod deleted
- openshift-etcd/etcd-guard-bm1-1: success
- openshift-kube-apiserver/kube-apiserver-guard-bm1-1: success
- openshift-kube-controller-manager/kube-controller-manager-guard-bm1-1: success
- openshift-kube-controller-manager/revision-pruner-11-bm1-1: success
- openshift-kube-scheduler/openshift-kube-scheduler-guard-bm1-1: success
Node [bm1-1] cli [sudo shutdown -h now]

Completed tasks
- Node shut down gracefully
```

[[Back]](./README.md)