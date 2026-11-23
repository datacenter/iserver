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
- reboot the node using 'sudo reboot' via ssh
- wait for node ssh access
- wait for k8s api
- wait for node ready
- if post-checks
    - mcp ready
    - all nodes ready
    - cluster operators available
    - if any of the condition above is not met, reload will not start

## Requirements

[SSH access](../Access.md) to cluster nodes

## Configurable options

- use --node multiple times in case you want to gracefully reload multiple nodes one after another
- use --no-pre if you want to skip pre-checks
- use --no-post if you want to skip post-checks
- use --no-confirm to proceed with reboot even if pod eviction fails

```
# iserver set ocp node reload
  --cluster TEXT  OCP cluster name
  --node TEXT     Node name
  --no-pre        Skip pre checks
  --no-post       Skip post checks
  --no-confirm    Confirmation mode in case of eviction problems
```

## Example

```
# iserver set ocp node reload --cluster bm1 --node bm1-3

OpenShift Workflow - Graceful node restart (reload)
===================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "node": [
        "bm1-3"
    ],
    "pre": true,
    "post": true,
    "confirmation": true,
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok
- cluster node [*****]: ok


+----+-------+-------+-------+--------+------+-----+-----+--------+-------------------+-----+
| ID | Node  | Ready | Taint | Memory | Disk | PID | MCP | Role   | IP                | Age |
+----+-------+-------+-------+--------+------+-----+-----+--------+-------------------+-----+
| 1  | bm1-3 | ✓     | ---   | ✓      | ✓    | ✓   | ✓   | Master | 10.10.10.10 (int) | 4d  | 
|    |       |       |       |        |      |     |     | Worker |                   |     | 
+----+-------+-------+-------+--------+------+-----+-----+--------+-------------------+-----+
Cordone node: bm1-3

~~~
spec:
  unschedulable: true

~~~
Node patched

Evict pods
- openshift-etcd/etcd-guard-bm1-3: success
- openshift-etcd/revision-pruner-10-bm1-3: success
- openshift-kube-apiserver/kube-apiserver-guard-bm1-3: success
- openshift-kube-apiserver/revision-pruner-11-bm1-3: success
- openshift-kube-controller-manager/kube-controller-manager-guard-bm1-3: success
- openshift-kube-scheduler/openshift-kube-scheduler-guard-bm1-3: success
- openshift-kube-scheduler/revision-pruner-6-bm1-3: success

Wait for pod evicted
- openshift-etcd/etcd-guard-bm1-3: success
- openshift-etcd/revision-pruner-10-bm1-3: success
- openshift-kube-apiserver/kube-apiserver-guard-bm1-3: success
- openshift-kube-apiserver/revision-pruner-11-bm1-3: success
- openshift-kube-controller-manager/kube-controller-manager-guard-bm1-3: success
- openshift-kube-scheduler/openshift-kube-scheduler-guard-bm1-3: success
- openshift-kube-scheduler/revision-pruner-6-bm1-3: success

Delete pods that are left

Wait for pod deleted

OpenShift Workflow - Node reboot
================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "node": [
        "bm1-3"
    ],
    "check-verbose": false,
    "wait": true,
    "sequential": true,
    "max-time": 600
}

Node [bm1-3] cli [sudo reboot]


Wait for node [bm1-3] up
- ssh
- k8s api
- node ready
Uncordon node: bm1-3

~~~
spec:
  unschedulable: null

~~~
Node patched

+----+-------+-------+------------+--------+------+-----+-----+--------+-------------------+-----+
| ID | Node  | Ready | Taint      | Memory | Disk | PID | MCP | Role   | IP                | Age |
+----+-------+-------+------------+--------+------+-----+-----+--------+-------------------+-----+
| 1  | bm1-3 | ✓     | NoSchedule | ✓      | ✓    | ✓   | ✓   | Master | 10.10.10.10 (int) | 4d  | 
|    |       |       | NoExecute  |        |      |     |     | Worker |                   |     | 
+----+-------+-------+------------+--------+------+-----+-----+--------+-------------------+-----+
Wait for mcp ready...
Wait for cluster operators available...
```

[[Back]](./README.md)