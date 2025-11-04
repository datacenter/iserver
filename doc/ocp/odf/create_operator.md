# OpenShift Data Foundation (ODF) Operator - Create Operator

## Workflow

- create openshift-storage namespace
- create operator group
- create subscription
- wait for installation complete

## Requirements

None

## Configurable options

```
# iserver set ocp odf --mode operator
  --cluster TEXT                Cluster Name
  --channel TEXT                Operator channel  [default: __default__]
  --no-confirm                  Confirmation mode
```

## Expected Outcome

![OperatorCreate](../images/lso/operator_create.png)

## Example

```
python.exe .\iserver.py set ocp odf --mode operator   

OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Create Operator
===============================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "channel": "__default__",
    "confirmation": true,
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


Create Namespace
----------------
- name: openshift-storage
- already defined

Create Operator Group
---------------------
Operator group: openshift-storage/openshift-storage-operator-group
Target namespaces: openshift-storage

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-storage-operator-group
  namespace: openshift-storage
spec:
  targetNamespaces:
  - openshift-storage

~~~
Continue [Y/N]? y

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: openshift-storage/odf-operator
Source: openshift-marketplace/redhat-operators/odf-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable-4.18
- CSV [odf-operator.v4.18.11-rhodf]
- CSV Display name [OpenShift Data Foundation]
- CVS Version [4.18.11-rhodf]
- CSV Provider [{'name': 'Red Hat'}]
- CSV Maturity [alpha]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: odf-operator
  namespace: openshift-storage
spec:
  channel: stable-4.18
  installPlanApproval: Automatic
  name: odf-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace

~~~
Continue [Y/N]? y

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-mlm2k
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: False, allow zero replicas: True)...
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

Completed tasks
- Namespace created
- Operator Group created
- OpenShift Data Foundation (ODF) Operator installed
```

```
python.exe .\iserver.py get ocp odf

OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Get Information
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

Operator
--------
- subscription: openshift-storage/odf-operator
- channel: stable-4.18
- csv: odf-operator.v4.18.11-rhodf

Get ODF CRD
-----------
- CephBlockPool
- CephBlockPoolRadosNamespace
- CephBucketNotification
- CephBucketTopic
- CephClient
- ClientProfile
- ClientProfileMapping
- CephCluster
- CephConnection
- CephCOSIDriver
- Driver
- CephFilesystem
- CephFilesystemMirror
- CephFilesystemSubVolumeGroup
- CephNFS
- CephObjectRealm
- CephObjectStore
- CephObjectStoreUser
- CephObjectZone
- CephObjectZoneGroup
- OperatorConfig
- CephRBDMirror
- StorageSystem
- OCSInitialization
- StorageClaim
- StorageClient
- StorageCluster
- StorageClusterPeer
- StorageConsumer
- StorageRequest
- Job


OCS Initialization
------------------
- Name        : openshift-storage/ocsinit
- Phase       : Ready
- Ready       : ✓
- Available   : ✓
- Upgradeable : ✓
```

[[Back]](./README.md)