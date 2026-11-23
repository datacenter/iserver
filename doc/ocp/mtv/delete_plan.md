# Migration Toolkit for Virtualization - Delete Migration Plan

## Workflow

- archive and delete selected|all migration plans
- skip running plans
- wipe option deletes migrated virtual machines associated with the plan

## Requirements

mtv operator [installed](./create_operator.md)

## Configurable options

```
# iserver delete ocp mtv --mode plan
  --cluster TEXT                  Cluster Name
  --namespace TEXT                Filter by namespace
  --name TEXT                     Filter by name
  --wipe                          Wipe plans
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver delete ocp mtv --cluster bm1 --mode plan

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Migraton Plan
=========================================================================================

OpenShift Cluster: bm3

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

+----+----------------+-----------+------+-----+------+---------------+--------------------+-----------+-----------+
| ID | Migration Plan | State     | Type | Src | Dest | Network       | Storage            | Source VM | Phase     |
+----+----------------+-----------+------+-----+------+---------------+--------------------+-----------+-----------+
| 1  | openshift-mtv  | Completed | cold | vc  | host | openshift-mtv | openshift-mtv      | usmall    | Completed |
|    | mtv1           |           |      |     |      | mtv1-vc-nets  | mtv1-vc-ds         |           |           |
|    |                |           |      |     |      | my-dvs => pod | My-NAS => lvms-vg1 |           |           |
+----+----------------+-----------+------+-----+------+---------------+--------------------+-----------+-----------+
| 2  | openshift-mtv  | Ready     | cold | vc  | host | openshift-mtv | openshift-mtv      | csmall    | Pending   |
|    | mtv2           |           |      |     |      | mtv2-vc-nets  | mtv2-vc-ds         |           |           |
|    |                |           |      |     |      | my-dvs => pod | My-NAS => lvms-vg1 |           |           |
+----+----------------+-----------+------+-----+------+---------------+--------------------+-----------+-----------+
Continue [Y/N]? y

Delete Migration Plan
---------------------
- namespace: openshift-mtv
- name: mtv1
- state: Completed

~~~
apiVersion: forklift.konveyor.io/v1beta1
kind: Plan
metadata:
  name: mtv1
  namespace: openshift-mtv
spec:
  archived: true

~~~

Migration plan patched
Wait for plan archived...

Migration plan deleted
Wait for migration plan gone

Delete Migration Plan
---------------------
- namespace: openshift-mtv
- name: mtv2
- state: None

~~~
apiVersion: forklift.konveyor.io/v1beta1
kind: Plan
metadata:
  name: mtv2
  namespace: openshift-mtv
spec:
  archived: true

~~~

Migration plan patched
Wait for plan archived...

Migration plan deleted
Wait for migration plan gone

Completed tasks
- selected migration plans archived and deleted
```

[[Back]](./README.md)