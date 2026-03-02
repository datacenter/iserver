# VAST Operator - Delete operator

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
------------------------------
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
---------------------------
- deployment vast-csi/vast-csi-operator-controller-manager ready
- 0 driver
- 0 cluster
- 0 storage
- 0 storage class
- 0 pvc

Delete Subscription
-------------------
- subscription: vast-csi/vast-csi-operator
- checking cluster service version...
- csv found and will be deleted: vast-csi/vast-csi-operator.v2.6.4
- wait for no subscription
- check cluster service version: vast-csi/vast-csi-operator.v2.6.4
- wait for no csv
Wait for deployments deleted (optional: False)...
- vast-csi/vast-csi-operator-controller-manager

Delete Operator Group
---------------------
- namespace: vast-csi
- name: vast-operator-group
- wait for no operator group

Delete Namespace
----------------
- name: vast-csi

Namespace [vast-csi] resources
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