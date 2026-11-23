# Migration Toolkit for Virtualization - Delete Operator

## Workflow

- delete mtv operator
- delete operator group
- delete any stale vddk validator completed jobs in mtv namespace
- delete namespace

## Requirements

- [no forklift controller instance](./delete_instance.md)
- [no plan](./delete_plan.md)
- [no storage map](./delete_storage_map.md)
- [no network map](./delete_network_map.md)
- [no provider](./delete_provider.md)

## Configurable options

```
# iserver delete ocp mtv --mode operator
  --cluster TEXT                  Cluster Name
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver delete ocp mtv --cluster bm1 --mode operator

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Operator
====================================================================================

OpenShift Cluster: bm1

No providers found

No network maps found

No storage maps found

No migration plans

No migrations


Delete Subscription
-------------------
- subscription: openshift-mtv/mtv-operator
- checking cluster service version...
- csv found and will be deleted: openshift-mtv/mtv-operator.v2.10.3
- wait for no subscription
- check cluster service version: openshift-mtv/mtv-operator.v2.10.3
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-mtv/forklift-operator

Delete Operator Group
---------------------
- namespace: openshift-mtv
- name: mtv-operator-group
- wait for no operator group

Delete Pod
----------
- namespace: openshift-mtv
- name: vddk-validator-mtv1vkjvf-sk4cp
- wait for no pod

Delete Namespace
----------------
- name: openshift-mtv

Namespace [openshift-mtv] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)