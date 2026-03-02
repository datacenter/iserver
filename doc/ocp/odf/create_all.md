# OpenShift Data Foundation (ODF) Operator - Create Operator and Cluster

## Workflow

Execute two workflows in sequence
- [create operator](./create_operator.md)
- [create cluster](./create_cluster.md)

## Requirements

Operator may be already installed, the workflow will finish early
No storage cluster may exist

## Configurable options

```
# iserver set ocp odf --mode all
  --cluster TEXT                 Cluster Name
  --channel TEXT                 Operator channel  [default: __default__]
  --filename TEXT                ODF Cluster
  --sc TEXT                      Storage class name  [default: odf-sc]
  --replica INTEGER              Replica  [default: 0]
  --count INTEGER                Count  [default: 0]
  --default-sc                   Set ODF storage class as default
  --nfs                          Enable nfs
  --flexible                     Flexible scaling
  --tools                        Ceph tools
  --no-confirm                   Confirmation mode
```

## Expected outcome

![OperatorCreate](../images/odf/operator_create.png)

![ClusterCreate](../images/odf/cluster_create.png)

## Example

```
python.exe .\iserver.py set ocp odf --mode all --replica 3 --count 2 --nfs --default-sc --flexible --cluster bm1 --no-confirm

OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Create Operator
===============================================================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: openshift-storage

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-storage

~~~

Namespace created

Wait for namespace [timeout:60]...

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

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-bhlzn
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

OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Create Cluster
==============================================================================

OpenShift Cluster: bm1

Checks
------
- odf subscription found
- local storage class: local-sc
- persistent volumes for local storage: 6
- enough pvs for repliaca [3] and count [2]

Create Storage Cluster
----------------------
- namespace: openshift-storage
- name: odf-cluster
- storage class: odf-sc
- default storage class: True
- default virtualization storage class: True
- nfs: True
- lso storage class: local-sc
- replica: 3
- count: 2
- flexible scaling: True
- ceph tools: False

~~~
apiVersion: ocs.openshift.io/v1
kind: StorageCluster
metadata:
  name: odf-cluster
  namespace: openshift-storage
spec:
  arbiter: {}
  encryption:
    keyRotation:
      schedule: '@weekly'
    kms: {}
  externalStorage: {}
  flexibleScaling: true
  managedResources:
    cephBlockPools:
      defaultStorageClass: true
      defaultVirtualizationStorageClass: true
    cephCluster: {}
    cephConfig: {}
    cephDashboard: {}
    cephFilesystems: {}
    cephNonResilientPools: {}
    cephObjectStoreUsers: {}
    cephObjectStores: {}
    cephRBDMirror: {}
    cephToolbox: {}
  monDataDirHostPath: /var/lib/rook
  nfnodeTopologies: {}
  nfs:
    enable: true
  storageDeviceSets:
  - config: {}
    count: 2
    dataPVCTemplate:
      metadata: {}
      spec:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: '1'
        storageClassName: local-sc
        volumeMode: Block
      status: {}
    name: odf-sc
    placement: {}
    preparePlacement: {}
    replica: 3
    resources: {}

~~~

- storage cluster created

- wait for storage cluster crd...
- wait for ceph cluster crd...
- wait for storage cluster resources...
Wait for deployments ready (optional: False, allow zero replicas: True)...
- openshift-storage/csi-rbdplugin-provisioner
- openshift-storage/csi-cephfsplugin-provisioner
- openshift-storage/noobaa-endpoint
- openshift-storage/ocs-metrics-exporter
- openshift-storage/rook-ceph-mon-a
- openshift-storage/rook-ceph-mon-b
- openshift-storage/rook-ceph-mon-c
- openshift-storage/rook-ceph-mgr-a
- openshift-storage/rook-ceph-mgr-b
- openshift-storage/rook-ceph-osd-0
- openshift-storage/rook-ceph-osd-1
- openshift-storage/rook-ceph-osd-2
- openshift-storage/rook-ceph-osd-3
- openshift-storage/rook-ceph-osd-4
- openshift-storage/rook-ceph-osd-5
- openshift-storage/rook-ceph-crashcollector-bm1-1
- openshift-storage/rook-ceph-exporter-bm1-1
- openshift-storage/rook-ceph-crashcollector-bm1-2
- openshift-storage/rook-ceph-exporter-bm1-2
- openshift-storage/rook-ceph-crashcollector-bm1-3
- openshift-storage/rook-ceph-exporter-bm1-3
- wait for storage cluster crd...

Completed tasks
- Cluster created and ready
```

If you get odf cluster e.g.

```
python.exe .\iserver.py get ocp odf --cluster bm1

OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Get Information
===============================================================================

OpenShift Cluster: bm1

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
- Used           : 442.21 [MB]
- Used pct       : 0.01%
- Available      : 5.76 [TB]


+-------------------+--------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+----------------------------------------+-------+
| PV                | Status | Mode  | SC       | Size  | Access Mode   | CSI Driver  | CSI Handle               | Device                         | PVC                                    | Age   |
+-------------------+--------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+----------------------------------------+-------+
| local-pv-487bfb48 | Bound  | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-0e096b56fce6 | wwn-0x500a075118ef25d9 [bm1-2] | openshift-storage/odf-sc-2-data-0gp9mq | 2h47m |
| local-pv-810111b0 | Bound  | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-b7720c780b5d | wwn-0x500a075118ef2777 [bm1-1] | openshift-storage/odf-sc-1-data-0bfbsw | 2h47m |
| local-pv-8ff7b89e | Bound  | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-cdf8a2ac0775 | wwn-0x500a075118ef291c [bm1-3] | openshift-storage/odf-sc-0-data-1xhcxv | 2h47m |
| local-pv-bf5ba6b4 | Bound  | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-3472ed1dabf2 | wwn-0x500a075118ef25c1 [bm1-1] | openshift-storage/odf-sc-2-data-14lg6n | 2h47m |
| local-pv-c6bf5067 | Bound  | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-29ed1a4a39f4 | wwn-0x500a075118ef266c [bm1-2] | openshift-storage/odf-sc-0-data-09l7vn | 2h47m |
| local-pv-fe6e649c | Bound  | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-87325b1e9cbc | wwn-0x500a075118ef2616 [bm1-3] | openshift-storage/odf-sc-1-data-1glcqk | 2h47m |
+-------------------+--------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+----------------------------------------+-------+

+----------------------------------------+--------+-------------------+-------+---------------+---------------+------+-------+
| PVC                                    | Status | Volume            | Size  | Access Mode   | Storage Class | Snap | Age   |
+----------------------------------------+--------+-------------------+-------+---------------+---------------+------+-------+
| openshift-storage/odf-sc-0-data-09l7vn | Bound  | local-pv-c6bf5067 | 894Gi | ReadWriteOnce | local-sc      | --   | 2h27m |
| openshift-storage/odf-sc-0-data-1xhcxv | Bound  | local-pv-8ff7b89e | 894Gi | ReadWriteOnce | local-sc      | --   | 2h27m |
| openshift-storage/odf-sc-1-data-0bfbsw | Bound  | local-pv-810111b0 | 894Gi | ReadWriteOnce | local-sc      | --   | 2h27m | 
| openshift-storage/odf-sc-1-data-1glcqk | Bound  | local-pv-fe6e649c | 894Gi | ReadWriteOnce | local-sc      | --   | 2h27m |
| openshift-storage/odf-sc-2-data-0gp9mq | Bound  | local-pv-487bfb48 | 894Gi | ReadWriteOnce | local-sc      | --   | 2h27m |
| openshift-storage/odf-sc-2-data-14lg6n | Bound  | local-pv-bf5ba6b4 | 894Gi | ReadWriteOnce | local-sc      | --   | 2h27m |
+----------------------------------------+--------+-------------------+-------+---------------+---------------+------+-------+
```

[[Back]](./README.md)