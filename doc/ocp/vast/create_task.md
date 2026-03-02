# VAST Operator - Create via Task

## Input

```
[
    {
        "vast": {
            "operator": {},
            "driver": [],
            "cluster": [],
            "storage": []
        }
    }
]
```

Notes:
- [operator](./create_operator.md), [driver](./create_driver.md), [cluster](./create_cluster.md) and [storage](./create_storage.md) trigger workflow execution with input parameters
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
# iserver set ocp task --cluster bm1 --file C:\tmp\task.json --no-confirm
Cluster: bm1 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - VAST CSI Operator - Create Operator
========================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
------------------------------
Operator vast-csi-operator not found

Create Namespace
----------------
- name: vast-csi

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: vast-csi

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: vast-csi/vast-operator-group
Target namespaces: vast-csi

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: vast-operator-group
  namespace: vast-csi
spec:
  targetNamespaces:
  - vast-csi

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: vast-csi/vast-csi-operator
Source: openshift-marketplace/certified-operators/vast-csi-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable
- CSV [vast-csi-operator.v2.6.4]
- CSV Display name [VAST CSI driver operator]
- CVS Version [2.6.4]
- CSV Provider [{'name': 'VASTData', 'url': 'https://www.vastdata.com'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: vast-csi-operator
  namespace: vast-csi
spec:
  channel: stable
  installPlanApproval: Automatic
  name: vast-csi-operator
  source: certified-operators
  sourceNamespace: openshift-marketplace

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-bgrtp
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: False, allow zero replicas: False)...
- vast-csi/vast-csi-operator-controller-manager

Completed tasks
- VAST CSI operator installed

OpenShift Workflow - VAST CSI Operator - Create Driver
======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
------------------------------
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
---------------------------
- deployment vast-csi/vast-csi-operator-controller-manager ready

Create VastCSIDriver
--------------------
- namespace: vast-csi
- name: nfs

~~~
apiVersion: storage.vastdata.com/v1
kind: VastCSIDriver
metadata:
  name: nfs
  namespace: vast-csi
spec:
  driverType: nfs
  image:
    csiVastPlugin:
      repository: docker.io/vastdataorg/csi:v2.6.4

~~~
VastCSIDriver [vast-csi/nfs] created
- wait for VastCSIDriver vast-csi/nfs [timeout:60s]
- wait for VastCSIDriver vast-csi/nfs [timeout:360s] with {"initialized_status": "True"}
- wait for VastCSIDriver vast-csi/nfs [timeout:360s] with {"deployed_status": "True"}
- wait for DaemonSet vast-csi/csi-vast-node ready [timeout:180s]
- wait for Deployment vast-csi/csi-vast-controller ready [timeout:180s]

+----+-------------+------+-----+--------------------------------------------------------+-----------------------------------------------------------+--------------+
| ID | Vast Driver | Init | Dep | Spec                                                   | Resource                                                  | Vast Storage |
+----+-------------+------+-----+--------------------------------------------------------+-----------------------------------------------------------+--------------+
| 1  | vast-csi    | V    | V   | {                                                      | [CSIDriver] nfs                                           | ---          | 
|    | nfs         |      |     |   "applySecurityContextConstraints": true,             | [ClusterRole] nfs-vast-attacher-role                      |              | 
|    |             |      |     |   "attachRequired": true,                              | [ClusterRole] nfs-vast-provisioner-role                   |              | 
|    |             |      |     |   "blockHostsAutoPrune": false,                        | [ClusterRole] nfs-vast-resizer-role                       |              | 
|    |             |      |     |   "dontUseTrashApi": false,                            | [ClusterRoleBinding] nfs-vast-attacher-binding            |              | 
|    |             |      |     |   "driverType": "nfs",                                 | [ClusterRoleBinding] nfs-vast-provisioner-binding         |              | 
|    |             |      |     |   "image": {                                           | [ClusterRoleBinding] nfs-vast-resizer-binding             |              | 
|    |             |      |     |     "csiVastPlugin": {                                 | [DaemonSet] vast-csi/csi-vast-node                        |              | 
|    |             |      |     |       "imagePullPolicy": "IfNotPresent",               | [Deployment] vast-csi/csi-vast-controller                 |              | 
|    |             |      |     |       "repository": "docker.io/vastdataorg/csi:v2.6.4" | [RoleBinding] vast-csi/nfs-vast-controller-scc-sa-binding |              | 
|    |             |      |     |     }                                                  | [RoleBinding] vast-csi/nfs-vast-node-scc-sa-binding       |              | 
|    |             |      |     |   },                                                   | [ServiceAccount] vast-csi/nfs-vast-controller-sa          |              | 
|    |             |      |     |   "kubeletPath": "/var/lib/kubelet",                   | [ServiceAccount] vast-csi/nfs-vast-node-sa                |              | 
|    |             |      |     |   "logLevel": 5,                                       |                                                           |              | 
|    |             |      |     |   "numWorkers": 10,                                    |                                                           |              | 
|    |             |      |     |   "operationRetryIntervalMax": 60,                     |                                                           |              | 
|    |             |      |     |   "operationRetryIntervalStart": 10,                   |                                                           |              | 
|    |             |      |     |   "operationTimeout": 15,                              |                                                           |              | 
|    |             |      |     |   "truncateVolumeName": 64,                            |                                                           |              | 
|    |             |      |     |   "useLocalIpForMount": "",                            |                                                           |              | 
|    |             |      |     |   "verifySsl": false                                   |                                                           |              | 
|    |             |      |     | }                                                      |                                                           |              | 
+----+-------------+------+-----+--------------------------------------------------------+-----------------------------------------------------------+--------------+

Completed tasks
- VAST CSI driver created

OpenShift Workflow - VAST CSI Operator - Create Driver
======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
------------------------------
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
---------------------------
- deployment vast-csi/vast-csi-operator-controller-manager ready

Create VastCSIDriver
--------------------
- namespace: vast-csi
- name: block

~~~
apiVersion: storage.vastdata.com/v1
kind: VastCSIDriver
metadata:
  name: block
  namespace: vast-csi
spec:
  driverType: block
  image:
    csiVastPlugin:
      repository: docker.io/vastdataorg/csi:v2.6.4

~~~
VastCSIDriver [vast-csi/block] created
- wait for VastCSIDriver vast-csi/block [timeout:60s]
- wait for VastCSIDriver vast-csi/block [timeout:360s] with {"initialized_status": "True"}
- wait for VastCSIDriver vast-csi/block [timeout:360s] with {"deployed_status": "True"}
- wait for DaemonSet vast-csi/block-vast-node ready [timeout:180s]
- wait for Deployment vast-csi/block-vast-controller ready [timeout:180s]

+----+-------------+------+-----+--------------------------------------------------------+-------------------------------------------------------------+--------------+
| ID | Vast Driver | Init | Dep | Spec                                                   | Resource                                                    | Vast Storage |
+----+-------------+------+-----+--------------------------------------------------------+-------------------------------------------------------------+--------------+
| 1  | vast-csi    | V    | V   | {                                                      | [CSIDriver] block                                           | ---          | 
|    | block       |      |     |   "applySecurityContextConstraints": true,             | [ClusterRole] block-vast-attacher-role                      |              | 
|    |             |      |     |   "attachRequired": true,                              | [ClusterRole] block-vast-provisioner-role                   |              | 
|    |             |      |     |   "blockHostsAutoPrune": false,                        | [ClusterRole] block-vast-resizer-role                       |              | 
|    |             |      |     |   "dontUseTrashApi": false,                            | [ClusterRoleBinding] block-vast-attacher-binding            |              | 
|    |             |      |     |   "driverType": "block",                               | [ClusterRoleBinding] block-vast-provisioner-binding         |              | 
|    |             |      |     |   "image": {                                           | [ClusterRoleBinding] block-vast-resizer-binding             |              | 
|    |             |      |     |     "csiVastPlugin": {                                 | [DaemonSet] vast-csi/block-vast-node                        |              | 
|    |             |      |     |       "imagePullPolicy": "IfNotPresent",               | [Deployment] vast-csi/block-vast-controller                 |              | 
|    |             |      |     |       "repository": "docker.io/vastdataorg/csi:v2.6.4" | [RoleBinding] vast-csi/block-vast-controller-scc-sa-binding |              | 
|    |             |      |     |     }                                                  | [RoleBinding] vast-csi/block-vast-node-scc-sa-binding       |              | 
|    |             |      |     |   },                                                   | [ServiceAccount] vast-csi/block-vast-controller-sa          |              | 
|    |             |      |     |   "kubeletPath": "/var/lib/kubelet",                   | [ServiceAccount] vast-csi/block-vast-node-sa                |              | 
|    |             |      |     |   "logLevel": 5,                                       |                                                             |              | 
|    |             |      |     |   "numWorkers": 10,                                    |                                                             |              | 
|    |             |      |     |   "operationRetryIntervalMax": 60,                     |                                                             |              | 
|    |             |      |     |   "operationRetryIntervalStart": 10,                   |                                                             |              | 
|    |             |      |     |   "operationTimeout": 15,                              |                                                             |              | 
|    |             |      |     |   "truncateVolumeName": 64,                            |                                                             |              | 
|    |             |      |     |   "useLocalIpForMount": "",                            |                                                             |              | 
|    |             |      |     |   "verifySsl": false                                   |                                                             |              | 
|    |             |      |     | }                                                      |                                                             |              | 
+----+-------------+------+-----+--------------------------------------------------------+-------------------------------------------------------------+--------------+

Completed tasks
- VAST CSI driver created

OpenShift Workflow - VAST CSI Operator - Create Cluster
=======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
------------------------------
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
---------------------------
- deployment vast-csi/vast-csi-operator-controller-manager ready

Create VastCluster
------------------
- namespace: vast-csi
- name: my-vast

~~~
apiVersion: storage.vastdata.com/v1
kind: VastCluster
metadata:
  name: my-vast
  namespace: vast-csi
spec:
  endpoint: my-vast.domain.com
  password: password
  username: admin

~~~
VastCluster [vast-csi/my-vast] created
- wait for VastCluster vast-csi/my-vast [timeout:60s]
- wait for VastCluster vast-csi/my-vast [timeout:360s] with {"initialized_status": "True"}
- wait for VastCluster vast-csi/my-vast [timeout:360s] with {"deployed_status": "True"}

+----+--------------+------+-----+---------------------------------------------------+---------+
| ID | Vast Cluster | Init | Dep | Spec                                              | Storage |
+----+--------------+------+-----+---------------------------------------------------+---------+
| 1  | vast-csi     | V    | V   | {                                                 | ---     | 
|    | my-vast      |      |     |   "endpoint": "my-vast.domain.com",               |         | 
|    |              |      |     |   "password": "password",                         |         | 
|    |              |      |     |   "username": "admin"                             |         | 
|    |              |      |     | }                                                 |         | 
+----+--------------+------+-----+---------------------------------------------------+---------+

Completed tasks
- VAST cluster created

OpenShift Workflow - VAST CSI Operator - Create Storage
=======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
------------------------------
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
---------------------------
- deployment vast-csi/vast-csi-operator-controller-manager ready

Check references
----------------
- vast driver vast-csi/nfs found
- vast cluster vast-csi/my-vast found

Create VastStorage
------------------
- namespace: vast-csi
- name: vast-nfs

~~~
apiVersion: storage.vastdata.com/v1
kind: VastStorage
metadata:
  name: vast-nfs
  namespace: vast-csi
spec:
  allowVolumeExpansion: true
  createSnapshotClass: true
  deletionViewPolicy: nfs-policy
  driverType: nfs
  provisioner: nfs
  secretName: my-vast
  secretNamespace: vast-csi
  storagePath: /my-nfs-path
  viewPolicy: nfs-policy
  vipPool: pool-01

~~~
VastStorage [vast-csi/vast-nfs] created
- wait for VastStorage vast-csi/vast-nfs [timeout:60s]
- wait for VastStorage vast-csi/vast-nfs [timeout:360s] with {"initialized_status": "True"}
- wait for VastStorage vast-csi/vast-nfs [timeout:360s] with {"deployed_status": "True"}

+----+--------------+------+-----+---------------------------------------------------------------+-----------------------------------------+
| ID | Vast Storage | Init | Dep | Spec                                                          | Resource                                |
+----+--------------+------+-----+---------------------------------------------------------------+-----------------------------------------+
| 1  | vast-csi     | V    | V   | {                                                             | [StorageClass] vast-csi/vast-nfs        | 
|    | vast-nfs     |      |     |   "allowVolumeExpansion": true,                               | [VolumeSnapshotClass] vast-csi/vast-nfs | 
|    |              |      |     |   "blockingClones": false,                                    |                                         | 
|    |              |      |     |   "clusterName": "",                                          |                                         | 
|    |              |      |     |   "createSnapshotClass": true,                                |                                         | 
|    |              |      |     |   "driverType": "nfs",                                        |                                         | 
|    |              |      |     |   "ephemeralVolumeNameFormat": "csi:{namespace}:{name}:{id}", |                                         | 
|    |              |      |     |   "mountOptions": [],                                         |                                         | 
|    |              |      |     |   "provisioner": "nfs",                                       |                                         | 
|    |              |      |     |   "reclaimPolicy": "Delete",                                  |                                         | 
|    |              |      |     |   "secretName": "my-vast",                                    |                                         | 
|    |              |      |     |   "secretNamespace": "vast-csi",                              |                                         | 
|    |              |      |     |   "setDefaultStorageClass": false,                            |                                         | 
|    |              |      |     |   "storagePath": "/my-nfs-path",                              |                                         | 
|    |              |      |     |   "subsystem": "",                                            |                                         | 
|    |              |      |     |   "viewPolicy": "nfs-policy",                                 |                                         | 
|    |              |      |     |   "vipPool": "pool-01",                                       |                                         | 
|    |              |      |     |   "vipPoolFQDNRandomPrefix": true,                            |                                         | 
|    |              |      |     |   "volumeNameFormat": "csi:{namespace}:{name}:{id}"           |                                         | 
|    |              |      |     | }                                                             |                                         | 
+----+--------------+------+-----+---------------------------------------------------------------+-----------------------------------------+

Completed tasks
- VAST storage created

OpenShift Workflow - VAST CSI Operator - Create Storage
=======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
------------------------------
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
---------------------------
- deployment vast-csi/vast-csi-operator-controller-manager ready

Check references
----------------
- vast driver vast-csi/block found
- vast cluster vast-csi/my-vast found

Create VastStorage
------------------
- namespace: vast-csi
- name: vast-block

~~~
apiVersion: storage.vastdata.com/v1
kind: VastStorage
metadata:
  name: vast-block
  namespace: vast-csi
spec:
  allowVolumeExpansion: true
  createSnapshotClass: true
  deletionViewPolicy: block-policy
  driverType: block
  provisioner: block
  secretName: my-vast
  secretNamespace: vast-csi
  storagePath: /my-block-path
  subsystem: BlockView
  viewPolicy: block-policy
  vipPool: pool-01

~~~
VastStorage [vast-csi/vast-block] created
- wait for VastStorage vast-csi/vast-block [timeout:60s]
- wait for VastStorage vast-csi/vast-block [timeout:360s] with {"initialized_status": "True"}
- wait for VastStorage vast-csi/vast-block [timeout:360s] with {"deployed_status": "True"}

+----+--------------+------+-----+---------------------------------------------------------------+-------------------------------------------+
| ID | Vast Storage | Init | Dep | Spec                                                          | Resource                                  |
+----+--------------+------+-----+---------------------------------------------------------------+-------------------------------------------+
| 1  | vast-csi     | V    | V   | {                                                             | [StorageClass] vast-csi/vast-block        | 
|    | vast-block   |      |     |   "allowVolumeExpansion": true,                               | [VolumeSnapshotClass] vast-csi/vast-block | 
|    |              |      |     |   "blockingClones": false,                                    |                                           | 
|    |              |      |     |   "clusterName": "",                                          |                                           | 
|    |              |      |     |   "createSnapshotClass": true,                                |                                           | 
|    |              |      |     |   "driverType": "block",                                      |                                           | 
|    |              |      |     |   "ephemeralVolumeNameFormat": "csi:{namespace}:{name}:{id}", |                                           | 
|    |              |      |     |   "mountOptions": [],                                         |                                           | 
|    |              |      |     |   "provisioner": "block",                                     |                                           | 
|    |              |      |     |   "reclaimPolicy": "Delete",                                  |                                           | 
|    |              |      |     |   "secretName": "my-vast",                                    |                                           | 
|    |              |      |     |   "secretNamespace": "vast-csi",                              |                                           | 
|    |              |      |     |   "setDefaultStorageClass": false,                            |                                           | 
|    |              |      |     |   "storagePath": "/my-block-path",                            |                                           | 
|    |              |      |     |   "subsystem": "BlockView",                                   |                                           | 
|    |              |      |     |   "viewPolicy": "block-policy",                               |                                           | 
|    |              |      |     |   "vipPool": "pool-01",                                       |                                           | 
|    |              |      |     |   "vipPoolFQDNRandomPrefix": true,                            |                                           | 
|    |              |      |     |   "volumeNameFormat": "csi:{namespace}:{name}:{id}"           |                                           | 
|    |              |      |     | }                                                             |                                           | 
+----+--------------+------+-----+---------------------------------------------------------------+-------------------------------------------+

Completed tasks
- VAST storage created
```

[Back](./README.md)