# Migration Toolkit for Virtualization - Delete Network Map

## Workflow

- delete selected|all network maps
- skip maps associated with migration plans

## Requirements

mtv operator [installed](./create_operator.md)

## Configurable options

```
# iserver delete ocp mtv --mode nmap
  --cluster TEXT                  Cluster Name
  --namespace TEXT                Filter by namespace
  --name TEXT                     Filter by name
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver delete ocp mtv --cluster bm1 --mode nmap

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Network Map
=======================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

+----+---------------+-------+--------+---------+-------------+---------+--------+------+
| ID | NetworkMap    | Owner | Source | Network | Destination | Network | Status | Plan |
+----+---------------+-------+--------+---------+-------------+---------+--------+------+
| 1  | openshift-mtv | Plan  | vc     | mydvs1  | host        | pod     | Ready  | mtv1 |
|    | mtv1-vc-nets  | mtv1  |        |         |             |         |        |      |
+----+---------------+-------+--------+---------+-------------+---------+--------+------+
| 2  | openshift-mtv | ---   | vc     | mydvs1  | host        | pod     | Ready  | ---  |
|    | vc-nets       |       |        |         |             |         |        |      |
+----+---------------+-------+--------+---------+-------------+---------+--------+------+
Continue [Y/N]? y

Network maps being used and not to be deleted
- openshift-mtv/mtv1-vc-nets


Delete Network Map
------------------
- namespace: openshift-mtv
- name: vc-nets

Network map deleted

Wait for no network map...

Completed tasks
- selected network maps deleted
- network maps used by migration plans not deleted
```

[[Back]](./README.md)