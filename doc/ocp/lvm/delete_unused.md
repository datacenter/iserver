# LVM Storage - Delete unused pvs and snapshots

## Workflow

Unused := pvc not used by any pod and no associated volume snapshots

Workflow identifies and deletes the unused resources on Kubernetes level.

## Requirements

- LVM Cluster instance must exist although it may be in degraded state.

## Configurable options

```
# iserver delete ocp lvm --mode unused
  --cluster TEXT                  Cluster Name
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver delete ocp lvm --cluster bm1 --mode unused --no-confirm

OpenShift Workflow - LVM - Delete Unused PVC and Volume Snapshots
=================================================================

OpenShift Cluster: bm1

LVM Operator
------------

Operator
- subscription          : openshift-storage/lvms
- package               : openshift-marketplace/redhat-operators/lvms-operator
- channel               : stable-4.18
- install plan          : openshift-storage/install-2658c
- install plan approved : ✓
- installed csv         : lvms-operator.v4.18.4
- latest_csv            : ✓

LVM Operator [openshift-storage/lvms] with csv [lvms-operator.v4.18.4]
LVM Subscription resources deployed
LVM Cluster instance: openshift-storage/my-lvmcluster
LVM Cluster instance: ready
Storage class: lvms-vg1

Current Resources
-----------------

Perstistent Volume Claims

+----+---------+---------+------------+------+--------+---------------+-------+-----+------+
| ID | PVC     | Status  | Mode       | Size | Access | Storage Class | Usage | PV  | Age  |
+----+---------+---------+------------+------+--------+---------------+-------+-----+------+
| 1  | default | Pending | Filesystem | 1Gi  | RWO    | lvms-vg1      | ---   | --- | 2h5m | 
|    | lalala  |         |            |      |        |               |       |     |      | 
+----+---------+---------+------------+------+--------+---------------+-------+-----+------+

Volume Snapshots
None
- pvc [default/lalala] will be deleted
PVC deleted: [default/lalala]
- wait for no pvc...

Resources After Delete
----------------------

Perstistent Volume Claims

+----+-----+--------+------+------+--------+---------------+-------+----+-----+
| ID | PVC | Status | Mode | Size | Access | Storage Class | Usage | PV | Age |
+----+-----+--------+------+------+--------+---------------+-------+----+-----+
+----+-----+--------+------+------+--------+---------------+-------+----+-----+

Volume Snapshots
None

+----+---------+-------+---------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow      | Changes | Success | Duration [s] |
+----+---------+-------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | lvm   | delete unused | 1       | ✓       | 7            | 
+----+---------+-------+---------------+---------+---------+--------------+
```

[[Back]](./README.md)