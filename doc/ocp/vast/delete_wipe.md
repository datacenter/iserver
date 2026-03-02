# VAST Operator - Delete operator

## Workflow

- get vast crds: `VastCSIDriver`, `VastCluster`, `VastStorage` 
- delete one-by-one

## Requirements

None

## Configurable options

```
# iserver delete ocp vast --mode wipe
  --cluster TEXT                Cluster Name
```

## Example

```
# iserver delete ocp vast --cluster bm1 --mode wipe

OpenShift Workflow - VAST CSI Operator - Wipe
=============================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
------------------------------
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
---------------------------
- deployment vast-csi/vast-csi-operator-controller-manager ready
- 2 driver
- 1 cluster
- 2 storage
- 2 storage class
- 2 pvc

Delete VastStorage
------------------
- namespace: vast-csi
- name: vast-block
- deleted
- wait for no VastStorage vast-csi/vast-block [timeout:60s]

Delete VastStorage
------------------
- namespace: vast-csi
- name: vast-nfs
- deleted
- wait for no VastStorage vast-csi/vast-nfs [timeout:60s]

Delete VastCluster
------------------
- namespace: vast-csi
- name: my-vast
- deleted
- wait for no VastCluster vast-csi/my-vast [timeout:60s]

Delete VastCSIDriver
--------------------
- namespace: vast-csi
- name: block
- deleted
- wait for no VastCSIDriver vast-csi/block [timeout:60s]
- wait for no DaemonSet vast-csi/block-vast-node [timeout:60s]
- wait for no Deployment vast-csi/block-vast-controller [timeout:60s]

Delete VastCSIDriver
--------------------
- namespace: vast-csi
- name: nfs
- deleted
- wait for no VastCSIDriver vast-csi/nfs [timeout:60s]
- wait for no DaemonSet vast-csi/csi-vast-node [timeout:60s]
- wait for no Deployment vast-csi/csi-vast-controller [timeout:60s]

Completed tasks
- VAST CRDs deleted
```

[[Back]](./README.md)