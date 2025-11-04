# Local Storage Operator - Delete volume

## Workflow

- delete local volume, local volume set and local volume discovery resources
- unlabel storage nodes

## Requirements

None

## Configurable options

```
# iserver delete ocp lso --mode volume
  --cluster TEXT                  Cluster Name
```

## Example (volumes created in discovery-node mode)

```
# iserver delete ocp lso --mode volume

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
No local volumes found

Delete local volume sets
------------------------

LocalVolumeSet [#1]
-------------------

+-------------------------+----------------+---------------+-------------+-----------+------------+---------+
| Namespace               | Name           | Storage Class | Volume Mode | Available | Disk Maker | Devices |
+-------------------------+----------------+---------------+-------------+-----------+------------+---------+
| openshift-local-storage | my-local-disks | local-sc      | Block       | ✓         | ✓          | 4       |
+-------------------------+----------------+---------------+-------------+-----------+------------+---------+
- openshift-local-storage/my-local-disks
        REST API successful
        Wait for no local volume set [timeout:60]...

Delete local volume discovieries
--------------------------------

Local Volume Discovery [#1]
---------------------------

+-------------------------+-----------------------+-----------+-------------+
| Namespace               | Name                  | Available | Phase       |
+-------------------------+-----------------------+-----------+-------------+
| openshift-local-storage | auto-discover-devices | ✓         | Discovering |
+-------------------------+-----------------------+-----------+-------------+
- openshift-local-storage/auto-discover-devices
        REST API successful
        Wait for no local volume discovery [timeout:60]...

Unlabel Storage Nodes
---------------------
- node label: cluster.ocs.openshift.io/openshift-storage=""
- node: bm1-1
- node: bm1-2
- node: bm1-3

Completed tasks
- Volumes deleted
- Node labels removed
```

## Example (volumes created in explicit mode)

```
# iserver delete ocp lso --mode volume

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
| openshift-local-storage | local-disks-5fb3cf004057 | bm1-2 | wwn-0x500a075118ef266c | local-sc      | Block |
| openshift-local-storage | local-disks-f3e4a3a77a00 | bm1-1 | wwn-0x500a075118ef25c1 | local-sc      | Block |
+-------------------------+--------------------------+-------+------------------------+---------------+-------+

Associated Persistent Volumes
-----------------------------


+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+------+
| Name              | Status    | Mode  | SC       | Size  | Access Mode   | CSI Driver  | CSI Handle               | Device                         | PVC | Age  |
+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+------+
| local-pv-c6bf5067 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-5fb3cf004057 | wwn-0x500a075118ef266c [bm1-2] | --  | 2h1m | 
| local-pv-bf5ba6b4 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-f3e4a3a77a00 | wwn-0x500a075118ef25c1 [bm1-1] | --  | 2h1m |
+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+------+
- openshift-local-storage/local-disks-5fb3cf004057
        REST API successful
        Wait for no local volume [timeout:60]...
- openshift-local-storage/local-disks-f3e4a3a77a00
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
```

[[Back]](./README.md)