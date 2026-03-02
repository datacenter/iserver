# OpenShift Data Foundation (ODF) Operator - Delete Cluster and Operator

## Workflow

Execute two workflows in sequence
- [delete cluster](./delete_cluster.md)
- [delete operator](./delete_operator.md)

## Requirements

ODF cluster may not be used

## Configurable options

```
# iserver delete ocp odf --mode all
  --cluster TEXT                 Cluster Name
```

## Example

```
# iserver delete ocp odf --cluster bm1 --mode all 

OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Delete Cluster
==============================================================================

OpenShift Cluster: bm1

Delete storage cluster
----------------------
- rest api successful
- wait for no storage cluster resources...
- wait for no storage cluster crd [timeout:60]...

Wipe rook filesystem
--------------------
- bm1-1
- bm1-2
- bm1-3

Completed tasks
- Cluster deleted

OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Delete Operator
===============================================================================

OpenShift Cluster: bm1

Check OpenShift Data Foundation (ODF) Operator Resources
--------------------------------------------------------
- checking storage cluster...

Check Subscription
------------------
- subscription found and will be deleted: odf-operator
- csv found and will be deleted: openshift-storage/odf-operator.v4.18.11-rhodf
- subscription deleted: openshift-storage/odf-operator
- wait for no subscription
- csv deleted: openshift-storage/odf-operator.v4.18.11-rhodf
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-storage/ceph-csi-controller-manager
- openshift-storage/csi-addons-controller-manager
- openshift-storage/noobaa-operator
- openshift-storage/ocs-client-operator-console
- openshift-storage/ocs-client-operator-controller-manager
- openshift-storage/ocs-operator
- openshift-storage/odf-console
- openshift-storage/odf-operator-controller-manager
- openshift-storage/prometheus-operator
- openshift-storage/rook-ceph-operator
- openshift-storage/ux-backend-server

Check Operator Group
--------------------
- operator group deleted: openshift-storage/openshift-storage-operator-group
- wait for no operator group

Delete namespaced jobs
----------------------
- namespace: openshift-storage

Delete namespaced services
--------------------------
- namespace: openshift-storage
- ux-backend-proxy

Delete PODs
-----------

Object filter
- namespace:openshift-storage

Delete
- csi-nfsplugin-provisioner-5f5b996867-6mvlm
- wait for no pod...
- csi-nfsplugin-provisioner-5f5b996867-c8bvv
[ERROR] REST API failed

Delete odf storage systems
--------------------------
- namespace: openshift-storage
- odf-cluster-storagesystem
- wait for no storage system...
[ERROR] Timed out
Remove finalizers

Delete odf ocs initialization
-----------------------------
- namespace: openshift-storage
- ocsinit

Delete Namespace
----------------
- name: openshift-storage

Namespace [openshift-storage] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- ODF resources checked
- Subscription and csv deleted
- Operator Group deleted
- Resources deleted
- Namespace deleted
```

[[Back]](./README.md)