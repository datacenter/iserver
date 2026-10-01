# LVM Storage - Delete cluster

[[Back]](./README.md)

## Workflow

- delete lvm cluster instance
- if timeout waiting for no lvm cluster instance, delete metadata.finalizers and wait again
- delete lvm storage class
- [wipe](../disk/delete_lvm.md) lvm from disks 
- [zap](../disk/zap.md) disks with lvm filesystem

## Requirements

- No pvc or volume snapshots on lvm storage class

## Configurable options

```
# iserver delete ocp lvm --mode cluster
  --cluster TEXT                  Cluster Name
  --no-wipe                       Wipe lvm from disks
  --no-zap                        Wipe filesystem from lvm disks
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver delete ocp lvm --cluster bm1 --mode cluster --wipe

OpenShift Workflow - LVM - Delete Cluster
=========================================

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
LVM Cluster instance: openshift-storage/lvmcluster
LVM Cluster instance: ready
Storage class: lvms-vg1
Checking lvm cluster resources...

Current Resources
-----------------

Perstistent Volume Claims

+----+-----+--------+------+------+--------+---------------+-------+----+-----+
| ID | PVC | Status | Mode | Size | Access | Storage Class | Usage | PV | Age |
+----+-----+--------+------+------+--------+---------------+-------+----+-----+
+----+-----+--------+------+------+--------+---------------+-------+----+-----+

Volume Snapshots
None

Delete LVM Cluster
------------------
- namespace: openshift-storage
- name: lvmcluster
- wait for no lvm cluster
LVM Cluster instance still there... checking finalizers...

Replace LVMCluster
------------------
- namespace: openshift-storage
- name: lvmcluster

~~~
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
...
~~~
LVMCluster [openshift-storage/lvmcluster] replaced
Finalizers removed
Wait for no lvm cluster [timeout:60s]...

Delete LVM Storage Class
------------------------
- name: lvms-vg1
- wait for no storage class

Completed tasks
- LVM Cluster instance deleted
- LVM storage class deleted

+----+---------+-------+----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow       | Changes | Success | Duration [s] |
+----+---------+-------+----------------+---------+---------+--------------+
| 1  | ocp:bm1 | lvm   | delete cluster | 3       | ✓       | 68           | 
+----+---------+-------+----------------+---------+---------+--------------+
```

[[Back]](./README.md)