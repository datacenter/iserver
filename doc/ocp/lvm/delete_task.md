# LVM Storage Operator - Delete via Task

## Input

```
[
    {
        "lvm": {
            "operator": {},
            "cluster": {}
        }
    }
]
```

Notes:
- [operator](./delete_operator.md) and [cluster](./delete_cluster.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters may be silently ignored
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

## Requirements

None

## Configurable options

```
# iserver delete ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
# iserver delete ocp task --file C:\tmp\task.json          
OpenShift Cluster: bm1

Cluster: bm1 (type: ocp)

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - LVM Operator - Delete Cluster
==================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "ssh-required": false,
    "wipe": false,
    "check-verbose": true,
    "confirmation": true,
    "namespace": "openshift-storage",
    "name": "lvms-operator",
    "operator-group-name": "lvm-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok


LVM Operator
------------
LVM Operator [openshift-storage/lvms] with csv [lvms-operator.v4.18.3]
LVM Subscription resources deployed
LVM Cluster instance: openshift-storage/lvmcluster
LVM Cluster instance: ready
Storage class: lvms-vg1
Checking lvm cluster resources...

Current Resources
-----------------

Perstistent Volume Claims
None

Volume Snapshots
None

Delete LVM Cluster
------------------
- namespace: openshift-storage
- name: lvmcluster
- wait for no lvm cluster

Delete LVM Storage Class
------------------------
- already deleted

Completed tasks
- LVM Cluster instance deleted
- LVM storage class deleted

OpenShift Workflow - LVM Operator - Delete Operator
===================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-storage",
    "name": "lvms-operator",
    "operator-group-name": "lvm-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Delete Subscription
-------------------
- subscription: openshift-storage/lvms-operator
- checking cluster service version...
- csv found and will be deleted: openshift-storage/lvms-operator.v4.18.3
- wait for no subscription
- check cluster service version: openshift-storage/lvms-operator.v4.18.3
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-storage/lvms-operator
Wait for deamon sets deleted...
- openshift-storage/vg-manager

Delete Operator Group
---------------------
- namespace: openshift-storage
- name: openshift-storage-operatorgroup
- wait for no operator group

Delete Namespace
----------------
- name: openshift-storage

Namespace [openshift-storage] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)