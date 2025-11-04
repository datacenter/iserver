# OpenShift Data Foundation (ODF) Operator - Create Operator

## Workflow

- delete subscription
- delete operator group
- cleanup stale resources
- delete openshift-storage namespace

## Requirements

No odf cluster expected

## Configurable options

```
# iserver delete ocp odf --mode operator
  --cluster TEXT                 Cluster Name
```

## Example

```
python.exe .\iserver.py delete ocp odf --mode operator   

OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Delete Operator
===============================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-storage",
    "name": "odf-operator",
    "cluster-name": "odf-cluster",
    "operator-group-name": "openshift-storage-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


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
- ocs-operator-565775cfb8-jj4cq
- wait for no pod...

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