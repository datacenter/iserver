# LVM Storage - Delete orphan

## Workflow

Orphan := logical volume on Linux LVM level that is not backed by pvc/pv or volume snapshot on OpenShift level

Workflow identifies and deletes the orpans on Linux LVM level.

## Requirements

- LVM Cluster instance must exist although it may be in degraded state.
- ssh access to cluster

## Configurable options

```
# iserver delete ocp lvm --mode operator
  --cluster TEXT                  Cluster Name
  --no-confirm                    Confirmation mode
```

## Example

Hint for test: `sudo lvcreate -V 100M -T vg1/thin-pool-1 -n lalala`

```
# iserver delete ocp lvm --cluster bm1 --mode orphan --no-confirm

OpenShift Workflow - LVM - Delete Orphan Logical Volumes
========================================================

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

Collect linux level lv state...

Logical Volumes (LVM) [bm1-1]
-----------------------------

+-------------+-----+-------------+-------+---------+-------+--------+---------+------+-----------+
| LV Name     | VG  | LV Pool     | Dev   | LV Size | MSize | Layout | Role    | Snap | K8s Usage |
+-------------+-----+-------------+-------+---------+-------+--------+---------+------+-----------+
| lalala      | vg1 | thin-pool-1 | 253:4 | 100.00m | 0.00% | thin   | public  | --   | --        | 
|             |     |             |       |         |       | sparse |         |      |           | 
+-------------+-----+-------------+-------+---------+-------+--------+---------+------+-----------+
| thin-pool-1 | vg1 |             | 253:2 | <8.64t  | 0.00% | thin   | private | --   | N/A       | 
|             |     |             |       |         |       | pool   |         |      |           | 
+-------------+-----+-------------+-------+---------+-------+--------+---------+------+-----------+

[WARNING] some logical volumes not backed with kube resources

Logical Volumes (LVM) [bm1-2]
-----------------------------

+-------------+-----+---------+-------+---------+-------+--------+---------+------+-----------+
| LV Name     | VG  | LV Pool | Dev   | LV Size | MSize | Layout | Role    | Snap | K8s Usage |
+-------------+-----+---------+-------+---------+-------+--------+---------+------+-----------+
| thin-pool-1 | vg1 |         | 253:2 | <8.64t  | 0.00% | thin   | private | --   | N/A       | 
|             |     |         |       |         |       | pool   |         |      |           | 
+-------------+-----+---------+-------+---------+-------+--------+---------+------+-----------+

Logical Volumes (LVM) [bm1-3]
-----------------------------

+-------------+-----+---------+-------+---------+-------+--------+---------+------+-----------+
| LV Name     | VG  | LV Pool | Dev   | LV Size | MSize | Layout | Role    | Snap | K8s Usage |
+-------------+-----+---------+-------+---------+-------+--------+---------+------+-----------+
| thin-pool-1 | vg1 |         | 253:2 | <8.64t  | 0.00% | thin   | private | --   | N/A       | 
|             |     |         |       |         |       | pool   |         |      |           | 
+-------------+-----+---------+-------+---------+-------+--------+---------+------+-----------+

Orphans to be deleted
- node [bm1-1] lv [/dev/vg1/lalala]

Delete orphans
- node [bm1-1] lv [/dev/vg1/lalala]
  Logical volume "lalala" successfully removed.


Completed tasks
- Linux logical volumes not backed by PVC/PV or Volume Snapshot (aka orphans) deleted

+----+---------+-------+---------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow      | Changes | Success | Duration [s] |
+----+---------+-------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | lvm   | delete orphan | 0       | ✓       | 9            | 
+----+---------+-------+---------------+---------+---------+--------------+
```

[[Back]](./README.md)