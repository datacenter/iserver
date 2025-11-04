# Local Storage Operator - Delete via Task

## Input

```
[
    {
        "lso": {
            "operator": {},
            "volume": {}
        }
    }
]
```

Notes:
- [volume](./delete_volume.md) and [operator](./delete_operator.md) trigger workflow execution
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
# iserver delete ocp task --cluster bm1 --file C:\tmp\task.json          
OpenShift Cluster: bm1

Cluster: bm1 (type: ocp)

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Local Storage Operator - Delete Local Volume
=================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-local-storage",
    "name": "local-storage-operator",
    "operator-group-name": "local-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

Local Storage Operator
----------------------
- namespace: openshift-local-storage/local-storage-operator
- package: local-storage-operator
- csv: local-storage-operator.v4.18.0-202509240837

Collect cluster state and validate input values
-----------------------------------------------
- get kubernetes node names
- get local volume discovery
- get local volume sets
- get local volumes

Delete local volumes
--------------------

Local Volume [#2]
-----------------

+-------------------------+--------------------------+-------+------------------------+---------------+-------+
| Namespace               | Name                     | Node  | Device                 | Storage Class | Mode  |
+-------------------------+--------------------------+-------+------------------------+---------------+-------+
| openshift-local-storage | local-disks-20b59c6289fd | bm1-1 | wwn-0x500a075118ef25c1 | local-sc      | Block |
| openshift-local-storage | local-disks-3e6f21e12e8d | bm1-2 | wwn-0x500a075118ef266c | local-sc      | Block |
+-------------------------+--------------------------+-------+------------------------+---------------+-------+

Associated Persistent Volumes
-----------------------------


+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+------+
| Name              | Status    | Mode  | SC       | Size  | Access Mode   | CSI Driver  | CSI Handle               | Device                         | PVC | Age  |
+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+------+
| local-pv-bf5ba6b4 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-20b59c6289fd | wwn-0x500a075118ef25c1 [bm1-1] | --  | 2h1m |
| local-pv-c6bf5067 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-3e6f21e12e8d | wwn-0x500a075118ef266c [bm1-2] | --  | 2h1m |
+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+------+
- openshift-local-storage/local-disks-20b59c6289fd
        REST API successful
        Wait for no local volume [timeout:60]...
- openshift-local-storage/local-disks-3e6f21e12e8d
        REST API successful
        Wait for no local volume [timeout:60]...

Delete local volume sets
------------------------
No local volume set found

Delete local volume discovieries
--------------------------------
No local volume discover found

Unlabel Storage Nodes
---------------------
- node label: cluster.ocs.openshift.io/openshift-storage=""
- node: bm1-1
- node: bm1-2
- node: bm1-3

Completed tasks
- Volumes deleted
- Node labels removed

OpenShift Workflow - Local Storage Operator - Delete Operator
=============================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-local-storage",
    "name": "local-storage-operator",
    "operator-group-name": "local-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Check Local Storage Operator Resources
--------------------------------------
- checking local volume...
- checking local volume set...
- checking local volume discovery...

Delete Subscription
-------------------
- subscription: openshift-local-storage/local-storage-operator
- checking cluster service version...
- csv found and will be deleted: openshift-local-storage/local-storage-operator.v4.18.0-202509240837
- wait for no subscription
- check cluster service version: openshift-local-storage/local-storage-operator.v4.18.0-202509240837
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-local-storage/local-storage-operator

Delete Operator Group
---------------------
- namespace: openshift-local-storage
- name: local-operator-group
- wait for no operator group

Delete Namespace
----------------
- name: openshift-local-storage

Namespace [openshift-local-storage] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- No volumes checked
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)