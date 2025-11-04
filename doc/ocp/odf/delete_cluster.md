# OpenShift Data Foundation (ODF) Operator - Delete Cluster

## Workflow

- delete StorageCluster CRD 
- wait for cluster cleanup to complete
- delete rook filesystem from every cluster node

## Requirements

ODF cluster may not be used

## Configurable options

```
# iserver delete ocp odf --mode cluster
  --cluster TEXT                 Cluster Name
```

## Example

```
# iserver delete ocp odf --mode cluster --cluster bm1

OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Delete Cluster
==============================================================================

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
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok


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
```

If you get odf cluster again it should show no cluster e.g.

```
# iserver get ocp odf --cluster bm1

OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Get Information
===============================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "view": [
        "state"
    ],
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

Get OpenShift Data Foundation (ODF) CRD
---------------------------------------
- CephCluster
- StorageCluster

No storage cluster

No ceph cluster
```

[[Back]](./README.md)