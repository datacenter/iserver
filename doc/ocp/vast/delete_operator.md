# VAST CSI - Delete operator

## Workflow

- get vast crds: `VastCSIDriver`, `VastCluster`, `VastStorage` (none is expected to continue)
- delete subscription
- delete operator group
- delete namespace

## Requirements

None

## Configurable options

```
# iserver delete ocp vast --mode operator
  --cluster TEXT                Cluster Name
```

## Example

```
# iserver delete ocp vast --cluster bm1 --mode operator

OpenShift Workflow - VAST CSI Operator - Delete Operator
========================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
- deployment vast-csi/vast-csi-operator-controller-manager ready

VAST CSI Custom Resources
- 0/0 VastCSIDriver
- 0/0 VastCluster
- 0/0 VastStorage
- 0/0 default StorageClass
- 0/0 PersistentVolumeClaim

Operator
- subscription          : vast-csi/vast-csi-operator
- package               : openshift-marketplace/certified-operators/vast-csi-operator
- channel               : stable
- install plan          : vast-csi/install-xc8bk
- install plan approved : V
- installed csv         : vast-csi-operator.v2.6.4
- latest_csv            : V


Delete Subscription
-------------------
- subscription: vast-csi/vast-csi-operator
- checking cluster service version...
- csv found and will be deleted: vast-csi/vast-csi-operator.v2.6.4
- wait for no subscription
- check cluster service version: vast-csi/vast-csi-operator.v2.6.4
- wait for no csv
- wait for no Deployment vast-csi/vast-csi-operator-controller-manager [timeout:180s]

Delete OperatorGroup
--------------------
- namespace: vast-csi
- name: vast-operator-group
- deleted
- wait for no OperatorGroup vast-csi/vast-operator-group [timeout:60s]

Namespace [vast-csi] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- no user defined networks
- no cluster user defined networks

Delete Namespace
----------------
- name: vast-csi
- wait for no namespace

Completed tasks
- Subscription deleted
- Operator Group deleted
- Namespace deleted

Completed tasks
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted

+----+---------+-------+-----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow        | Changes | Success | Duration [s] |
+----+---------+-------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | vast  | delete operator | 4       | V       | 32           | 
+----+---------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)