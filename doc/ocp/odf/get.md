# OpenShift Data Foundation (ODF) Operator - Get Information

## Workflow

- check odf operator subscription
- check all odf related objects 
- check pv and pvc

## Requirements

None

## Configurable options

```
# iserver get ocp lso 
  --cluster TEXT                Cluster Name
```

## Example

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
- PV
- PVC


Storage Cluster
---------------
- Namespace         : openshift-storage
- Name              : odf-cluster
- Owner             : StorageSystem/odf-cluster-storagesystem
- Phase             : Ready
- Ready             : ✓
- Current monitors  : 3
- Expected OSD      : 6
- Nodes             : bm1-1, bm1-2, bm1-3
- Version           : 4.18.11
- LSO Storage Class : local-sc
- ODF Storage Class : odf-sc



Ceph Cluster
------------
- Namespace      : openshift-storage
- Name           : odf-cluster-cephcluster
- Owner          : StorageCluster/odf-cluster
- Ready          : ✓
- Created        : ✓
- Healthy        : ✓
- Health         : HEALTH_OK
- Version        : 19.2.1-245
- Manager Count  : 2
- Monitor Count  : 3
- Total Capacity : 5.76 [TB]
- Used           : 6.39 [GB]
- Used pct       : 0.11%
- Available      : 5.75 [TB]


+-------------------+--------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+----------------------------------------+-----+
| PV                | Status | Mode  | SC       | Size  | Access Mode   | CSI Driver  | CSI Handle               | Device                         | PVC                                    | Age |
+-------------------+--------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+----------------------------------------+-----+
| local-pv-487bfb48 | Bound  | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-0e096b56fce6 | wwn-0x500a075118ef25d9 [bm1-2] | openshift-storage/odf-sc-0-data-024cpc | 9d  |
| local-pv-810111b0 | Bound  | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-b7720c780b5d | wwn-0x500a075118ef2777 [bm1-1] | openshift-storage/odf-sc-1-data-0kj5rx | 9d  |
| local-pv-8ff7b89e | Bound  | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-cdf8a2ac0775 | wwn-0x500a075118ef291c [bm1-3] | openshift-storage/odf-sc-1-data-1bhk8s | 9d  |
| local-pv-bf5ba6b4 | Bound  | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-3472ed1dabf2 | wwn-0x500a075118ef25c1 [bm1-1] | openshift-storage/odf-sc-2-data-1n424p | 9d  |
| local-pv-c6bf5067 | Bound  | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-29ed1a4a39f4 | wwn-0x500a075118ef266c [bm1-2] | openshift-storage/odf-sc-2-data-07wxgk | 9d  |
| local-pv-fe6e649c | Bound  | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-87325b1e9cbc | wwn-0x500a075118ef2616 [bm1-3] | openshift-storage/odf-sc-0-data-1skwms | 9d  |
+-------------------+--------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+----------------------------------------+-----+

+----------------------------------------+--------+-------------------+-------+---------------+---------------+------+-----+
| PVC                                    | Status | Volume            | Size  | Access Mode   | Storage Class | Snap | Age |
+----------------------------------------+--------+-------------------+-------+---------------+---------------+------+-----+
| openshift-storage/odf-sc-0-data-024cpc | Bound  | local-pv-487bfb48 | 894Gi | ReadWriteOnce | local-sc      | --   | 7d  |
| openshift-storage/odf-sc-0-data-1skwms | Bound  | local-pv-fe6e649c | 894Gi | ReadWriteOnce | local-sc      | --   | 7d  |
| openshift-storage/odf-sc-1-data-0kj5rx | Bound  | local-pv-810111b0 | 894Gi | ReadWriteOnce | local-sc      | --   | 7d  |
| openshift-storage/odf-sc-1-data-1bhk8s | Bound  | local-pv-8ff7b89e | 894Gi | ReadWriteOnce | local-sc      | --   | 7d  |
| openshift-storage/odf-sc-2-data-07wxgk | Bound  | local-pv-c6bf5067 | 894Gi | ReadWriteOnce | local-sc      | --   | 7d  |
| openshift-storage/odf-sc-2-data-1n424p | Bound  | local-pv-bf5ba6b4 | 894Gi | ReadWriteOnce | local-sc      | --   | 7d  |
+----------------------------------------+--------+-------------------+-------+---------------+---------------+------+-----+
```

[[Back]](./README.md)