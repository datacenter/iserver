# LVM Storage Operator - Delete cluster instance

## Workflow

- delete lvm cluster instance
- if timeout waiting for no lvm cluster instance, delete metadata.finalizers and wait again
- delete lvm storage class
- wipe lvm from disks if requested

## Requirements

- No pvc or volume snapshots on lvm storage class

## Configurable options

```
# iserver delete ocp lvm --mode cluster
  --cluster TEXT                  Cluster Name
  --channel TEXT                  Operator channel  [default: __default__]
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver delete ocp lvm --cluster bm1 --mode cluster --wipe

OpenShift Workflow - LVM Operator - Delete Cluster
==================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "wipe": true,
    "confirmation": true,
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
LVM Cluster instance: openshift-storage/my-lvmcluster
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
- name: my-lvmcluster
- wait for no lvm cluster

Delete LVM Storage Class
------------------------
- already deleted

Devices to be wiped
-------------------
- node [ocp-bm1]: /dev/sda, /dev/sdb, /dev/sdd


Do you want to see linux lvm info first?. Continue [Y/N]? y

Collect linux level lvm state...
- ocp-bm1: collected [blks, lvs, vgs, pvs]

Block Devices [ocp-bm1]
-----------------------

+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| Path     | KName | Boot | Maj:Min | Size   | Model            | Serial                           | Group | FS Type |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| /dev/sda | sda   |      | 8:0     | 894.3G | Micron_5100_MTFD | xxxxxxxxxxx                      | disk  | ---     |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| /dev/sdb | sdb   |      | 8:16    | 894.3G | Micron_5100_MTFD | xxxxxxxxxxx                      | disk  | ---     |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| /dev/sdc | sdc   | ✓    | 8:32    | 1.1T   | UCSC-RAID12G-2GB | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | disk  | ---     | 
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| /dev/sdd | sdd   |      | 8:48    | 1.1T   | UCSC-RAID12G-2GB | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | disk  | ---     |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+

Physical Volume (LVM) [ocp-bm1]
-------------------------------

+----+----+-----+------+-------+-------+
| PV | VG | Fmt | Attr | PSize | PFree |
+----+----+-----+------+-------+-------+
+----+----+-----+------+-------+-------+

Volume Groups (LVM) [ocp-bm1]
-----------------------------

+----+-----+-----+------+-------+-------+
| VG | #PV | #LV | Attr | VSize | VFree |
+----+-----+-----+------+-------+-------+
+----+-----+-----+------+-------+-------+

Logical Volumes (LVM) [ocp-bm1]
-------------------------------

+---------+----+---------+-----+---------+-------+--------+------+------+
| LV Name | VG | LV Pool | Dev | LV Size | MSize | Layout | Role | Snap |
+---------+----+---------+-----+---------+-------+--------+------+------+
Continue [Y/N]? y

Collect linux level lvm state...

Node [ocp-bm1]
--------------

LVM wiped from servers

Collect linux level lvm state...
- ocp-bm1: collected [blks, lvs, vgs, pvs]

Block Devices [ocp-bm1]
-----------------------

+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| Path     | KName | Boot | Maj:Min | Size   | Model            | Serial                           | Group | FS Type |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| /dev/sda | sda   |      | 8:0     | 894.3G | Micron_5100_MTFD | xxxxxxxxxxx                      | disk  | ---     |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| /dev/sdb | sdb   |      | 8:16    | 894.3G | Micron_5100_MTFD | xxxxxxxxxxx                      | disk  | ---     |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| /dev/sdc | sdc   | ✓    | 8:32    | 1.1T   | UCSC-RAID12G-2GB | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | disk  | ---     |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+
| /dev/sdd | sdd   |      | 8:48    | 1.1T   | UCSC-RAID12G-2GB | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx | disk  | ---     |
+----------+-------+------+---------+--------+------------------+----------------------------------+-------+---------+

Physical Volume (LVM) [ocp-bm1]
-------------------------------

+----+----+-----+------+-------+-------+
| PV | VG | Fmt | Attr | PSize | PFree |
+----+----+-----+------+-------+-------+
+----+----+-----+------+-------+-------+

Volume Groups (LVM) [ocp-bm1]
-----------------------------

+----+-----+-----+------+-------+-------+
| VG | #PV | #LV | Attr | VSize | VFree |
+----+-----+-----+------+-------+-------+
+----+-----+-----+------+-------+-------+

Logical Volumes (LVM) [ocp-bm1]
-------------------------------

+---------+----+---------+-----+---------+-------+--------+------+------+
| LV Name | VG | LV Pool | Dev | LV Size | MSize | Layout | Role | Snap |
+---------+----+---------+-----+---------+-------+--------+------+------+

Completed tasks
- LVM Cluster instance deleted
- LVM storage class deleted
```

[[Back]](./README.md)