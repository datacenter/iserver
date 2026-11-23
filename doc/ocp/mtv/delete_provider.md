# Migration Toolkit for Virtualization - Delete Provider

## Workflow

- delete selected|all provider definitions
- skip providers associated with network maps, storage maps or migration plans
- skip 'host' provider automatically created and owned by mtv operator

## Requirements

mtv operator [installed](./create_operator.md)

## Configurable options

```
# iserver delete ocp mtv --mode provider
  --cluster TEXT                  Cluster Name
  --name TEXT                     Filter by name
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver delete ocp mtv --cluster bm1 --mode provider

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Provider
====================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

+----+----------+---------+--------+---------------------------+-------------+-------------+------+
| ID | Provider | Type    | Status | Endpoint                  | Network Map | Storage Map | Plan |
+----+----------+---------+--------+---------------------------+-------------+-------------+------+
| 1  | vc       | vsphere | Ready  | https://vc.domain.com/sdk | 0/0         | 0/0         | 0/0  |
+----+----------+---------+--------+---------------------------+-------------+-------------+------+
Continue [Y/N]? y

Delete Provider
---------------
- namespace: openshift-mtv
- name: vc

Provider and secret deleted

Wait for no provider...

Completed tasks
- selected providers deleted
```

[[Back]](./README.md)