# LVM Storage Operator - Delete unused pvs and snapshots

## Workflow

Unused := pvc not used by any pod and associated volume snapshots

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
# iserver delete ocp lvm --mode unused

OpenShift Workflow - LVM Operator - Delete Unused PVC and Volume Snapshots
==========================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": true,
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


LVM Operator
------------
LVM Operator [openshift-storage/lvms] with csv [lvms-operator.v4.18.3]
LVM Subscription resources deployed
LVM Cluster instance: openshift-storage/lvmcluster
LVM Cluster instance: ready
Storage class: lvms-vg1

Current Resources
-----------------

Perstistent Volume Claims

+-----------+----------+---------+--------+------+-------------+---------------+-------+-------+------+
| Namespace | Name     | Status  | Volume | Size | Access Mode | Storage Class | Usage | Owner | Age  |
+-----------+----------+---------+--------+------+-------------+---------------+-------+-------+------+
| default   | test-pvc | Pending | None   |      |             | lvms-vg1      | --    | --    | 2h0m |
+-----------+----------+---------+--------+------+-------------+---------------+-------+-------+------+

Volume Snapshots
None
- pvc [default/test-pvc] will be deleted


Continue [Y/N]? y
PVC deleted: [default/test-pvc]
- wait for no pvc...

Resources After Delete
----------------------

Perstistent Volume Claims
None

Volume Snapshots
None
```

Test pvc example

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-pvc
  namespace: default
spec:
  storageClassName: lvms-vg1
  accessModes:
  - ReadWriteOnce
  volumeMode: Block
  resources:
    requests:
      storage: 1Gi
    limits:
      storage: 2Gi
```

[[Back]](./README.md)