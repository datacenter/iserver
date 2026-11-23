# Migration Toolkit for Virtualization - Delete Storage Map

## Workflow

- delete selected|all storage maps
- skip maps associated with migration plans

## Requirements

mtv operator [installed](./create_operator.md)

## Configurable options

```
# iserver delete ocp mtv --mode smap
  --cluster TEXT                  Cluster Name
  --namespace TEXT                Filter by namespace
  --name TEXT                     Filter by name
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver delete ocp mtv --cluster bm1 --mode smap

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Storage Map
=======================================================================================

OpenShift Cluster: bm3

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

+----+---------------+-------+--------+------------+-------------+----------+--------+------+
| ID | Storage Map   | Owner | Source | Storage    | Destination | Storage  | Status | Plan |
+----+---------------+-------+--------+------------+-------------+----------+--------+------+
| 1  | openshift-mtv | Plan  | vc     | My-NAS     | host        | lvms-vg1 | Ready  | mtv1 | 
|    | mtv1-vc-ds    | mtv1  |        |            |             |          |        |      |
+----+---------------+-------+--------+------------+-------------+----------+--------+------+
| 2  | openshift-mtv | ---   | vc     | My-NAS     | host        | lvms-vg1 | Ready  | ---  |
|    | vc-ds         |       |        |            |             |          |        |      |
+----+---------------+-------+--------+------------+-------------+----------+--------+------+
Continue [Y/N]? y

Storage maps being used and not to be deleted
- openshift-mtv/mtv1-vc-ds


Delete Storage Map
------------------
- namespace: openshift-mtv
- name: vc-ds

Storage map deleted

Wait for no storage map...

Completed tasks
- selected storage maps deleted
- storage maps used by migration plans not deleted
```

[[Back]](./README.md)