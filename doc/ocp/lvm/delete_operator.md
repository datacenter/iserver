# LVM Storage - Delete operator

## Workflow

- delete LVM storage operator subscription
- delete operator group
- delete namespace

## Requirements

LVM Cluster instance must not exist.

## Configurable options

```
# iserver delete ocp lvm --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp lvm --cluster bm1 --mode operator
 
OpenShift Workflow - LVM - Delete Operator
==========================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-storage/lvms
- package               : openshift-marketplace/redhat-operators/lvms-operator
- channel               : stable-4.18
- install plan          : openshift-storage/install-2658c
- install plan approved : ✓
- installed csv         : lvms-operator.v4.18.4
- latest_csv            : ✓


Delete Subscription
-------------------
- subscription: openshift-storage/lvms-operator
- checking cluster service version...
- csv found and will be deleted: openshift-storage/lvms-operator.v4.18.4
- wait for no subscription
- check cluster service version: openshift-storage/lvms-operator.v4.18.4
- wait for no csv
- wait for no Deployment openshift-storage/lvms-operator [timeout:180s]
- wait for no ReplicaSet openshift-storage/lvms-operator-5d8fcfdfbc [timeout:180s]
- wait for no ReplicaSet openshift-storage/lvms-operator-776775ff8f [timeout:180s]
- wait for no Pod openshift-storage/lvms-operator-776775ff8f-rh4dc [timeout:180s]
- wait for no DaemonSet openshift-storage/vg-manager [timeout:180s]
Subscription lvm resources gone

OperatorGroup openshift-storage/lvm-operator-group already deleted

Namespace [openshift-storage] resources
- no deployments
- no daemon_sets
- no replica_sets
- no pods
- no services
- no pvcs
- no jobs

Delete Namespace
----------------
- name: openshift-storage
- wait for no namespace

+----+---------+-------+-----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow        | Changes | Success | Duration [s] |
+----+---------+-------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | lvm   | delete operator | 3       | V       | 76           | 
+----+---------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)