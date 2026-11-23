# Persistent Volume Claim - Delete

## Workflow

- get pvc selected by namespace, name, unused or all
- if pvc has associated data volume, delete data volume instead
- skip if pvc has associated pod, cron, virtual machine or snapshot
- delete pvcs one-by-one

## Requirements

None

## Configurable options

```
# iserver delete k8s pvc 
  --cluster TEXT    Cluster Name
  --namespace TEXT  Filter by namespace
  --name TEXT       Filter by name
  --unused          Select unused claims
  --no-confirm      No confirmation mode
```

## Example

```
# iserver delete k8s pvc --cluster bm1 --namespace default

OpenShift Workflow - PVC - Delete
=================================

OpenShift Cluster: bm1

+----+-----------------------------+---------+-------+------+--------+---------------+---------------------------------------------------------------+------+
| ID | PVC                         | Status  | Mode  | Size | Access | Storage Class | Usage                                                         | Age  |
+----+-----------------------------+---------+-------+------+--------+---------------+---------------------------------------------------------------+------+
| 1  | default                     | Bound   | Block | 30Gi | RWO    | lvms-vg1      | [dv] fedora-apricot-chickadee-80                              | 16d  |
|    | fedora-apricot-chickadee-80 |         |       |      |        |               | [pod] default/virt-launcher-fedora-apricot-chickadee-80-ldstf |      |
|    |                             |         |       |      |        |               | [vmi] default/fedora-apricot-chickadee-80                     |      |
|    |                             |         |       |      |        |               | [pv] pvc-0940bbb7-d735-4930-bd66-f21c33bfc4d7                 |      |
+----+-----------------------------+---------+-------+------+--------+---------------+---------------------------------------------------------------+------+
| 2  | default                     | Bound   | Block | 8Gi  | RWO    | lvms-vg1      | [dv] mtv1-vm-61951-nrh7j                                      | 1d   |
|    | mtv1-vm-61951-nrh7j         |         |       |      |        |               | [pv] pvc-2b9645ed-4574-4fc1-8b1b-3c127fc12e16                 |      |
+----+-----------------------------+---------+-------+------+--------+---------------+---------------------------------------------------------------+------+
| 3  | default                     | Pending | Block | 1Gi  | RWO    | lvms-vg1      | ---                                                           | 1h7m |
|    | test                        |         |       |      |        |               |                                                               |      |
+----+-----------------------------+---------+-------+------+--------+---------------+---------------------------------------------------------------+------+
Continue [Y/N]? y

Delete pvc
- default/fedora-apricot-chickadee-80 (skipping used)
- dv default/mtv1-vm-61951-nrh7j (success)
- pvc default/test (success)

Used pvcs not deleted
```

[[Back]](./README.md)