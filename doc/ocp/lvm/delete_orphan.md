# LVM Storage Operator - Delete orphan

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

Hint for test: sudo lvcreate -V 100M -T vg1/thin-pool-1 -n lalala

```
# iserver delete ocp lvm --mode orphan --no-confirm

OpenShift Workflow - LVM Operator - Delete Orphan Logical Volumes
=================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "ssh-required": true,
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
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok


LVM Operator
------------
LVM Operator [openshift-storage/lvms] with csv [lvms-operator.v4.18.3]
LVM Subscription resources deployed
LVM Cluster instance: openshift-storage/lvmcluster
LVM Cluster instance: ready
Storage class: lvms-vg1

Collect linux level lv state...

Logical Volumes (LVM) [ocp-bm1]
-------------------------------

+-------------+-----+-------------+-------+---------+-------+--------+---------+------+-----------+
| LV Name     | VG  | LV Pool     | Dev   | LV Size | MSize | Layout | Role    | Snap | K8s Usage |
+-------------+-----+-------------+-------+---------+-------+--------+---------+------+-----------+
| lalala      | vg1 | thin-pool-1 | 253:4 | 100.00m | 0.00% | thin   | public  | --   | --        |
|             |     |             |       |         |       | sparse |         |      |           |
+-------------+-----+-------------+-------+---------+-------+--------+---------+------+-----------+
| thin-pool-1 | vg1 |             | 253:2 | 1.57t   | 0.00% | thin   | private | --   | N/A       |
|             |     |             |       |         |       | pool   |         |      |           |
+-------------+-----+-------------+-------+---------+-------+--------+---------+------+-----------+

[WARNING] some logical volumes not backed with kube resources

Orphans to be deleted
- node [ocp-bm1] lv [/dev/vg1/lalala]

Delete orphans
- node [ocp-bm1] lv [/dev/vg1/lalala]
  Logical volume "lalala" successfully removed.


Completed tasks
- Linux logical volumes not backed by PVC/PV or Volume Snapshot (aka orphans) deleted
```

[[Back]](./README.md)