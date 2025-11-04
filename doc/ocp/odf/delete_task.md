# OpenShift Data Foundation (ODF) Operator - Create via Task

## Input

```
[
    {
        "odf": {
            "operator": {},
            "cluster": {
                "replica": 3,
                "count": 2,
                "nfs": true,
                "default_sc": true,
                "flexible": true
            }
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


OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Delete Cluster
==============================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-storage",
    "name": "odf-operator",
    "cluster-name": "odf-cluster",
    "operator-group-name": "openshift-storage-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok


Delete storage cluster
----------------------
- rest api successful
- wait for no storage cluster resources...
- wait for no storage cluster crd [timeout:60]...

Wipe rook filesystem
--------------------
- bm1-1
- bm1-2
- bm1-3

Completed tasks
- Cluster deleted

OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Delete Operator
===============================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-storage",
    "name": "odf-operator",
    "cluster-name": "odf-cluster",
    "operator-group-name": "openshift-storage-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Check OpenShift Data Foundation (ODF) Operator Resources
--------------------------------------------------------
- checking storage cluster...

Check Subscription
------------------
- subscription found and will be deleted: odf-operator
- csv found and will be deleted: openshift-storage/odf-operator.v4.18.11-rhodf
- subscription deleted: openshift-storage/odf-operator
- wait for no subscription
- csv deleted: openshift-storage/odf-operator.v4.18.11-rhodf
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-storage/ceph-csi-controller-manager
- openshift-storage/csi-addons-controller-manager
- openshift-storage/noobaa-operator
- openshift-storage/ocs-client-operator-console
- openshift-storage/ocs-client-operator-controller-manager
- openshift-storage/ocs-operator
- openshift-storage/odf-console
- openshift-storage/odf-operator-controller-manager
- openshift-storage/prometheus-operator
- openshift-storage/rook-ceph-operator
- openshift-storage/ux-backend-server

Check Operator Group
--------------------
- operator group deleted: openshift-storage/openshift-storage-operator-group
- wait for no operator group

Delete namespaced jobs
----------------------
- namespace: openshift-storage

Delete namespaced services
--------------------------
- namespace: openshift-storage
- ux-backend-proxy

Delete PODs
-----------

Object filter
- namespace:openshift-storage

Delete
- csi-nfsplugin-c25cd
[ERROR] REST API failed
- csi-nfsplugin-lpt5b
[ERROR] REST API failed
- csi-nfsplugin-nt94h
[ERROR] REST API failed
- csi-nfsplugin-provisioner-5f5b996867-bbptj
- wait for no pod...
- csi-nfsplugin-provisioner-5f5b996867-tv2vx
[ERROR] REST API failed
- ocs-operator-565775cfb8-5tpll
[ERROR] REST API failed

Delete odf storage systems
--------------------------
- namespace: openshift-storage
- odf-cluster-storagesystem
- wait for no storage system...
[ERROR] Timed out
Remove finalizers

Delete odf ocs initialization
-----------------------------
- namespace: openshift-storage
- ocsinit

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
- ODF resources checked
- Subscription and csv deleted
- Operator Group deleted
- Resources deleted
- Namespace deleted
```

[[Back]](./README.md)