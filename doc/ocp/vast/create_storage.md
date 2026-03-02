# VAST Operator - Create storage via Task

## Input

```
[
    {
        "vast": {
            "storage": [
                {
                    "filename": "/tmp/vast_storage.yaml"
                },
                {
                    "name": "vast-nfs",
                    "vast_driver": "nfs",
                    "vast_cluster": "my-vast",
                    "storagePath": "/my-nfs-path",
                    "viewPolicy": "nfs-policy",
                    "deletionViewPolicy": "nfs-policy",
                    "vipPool": "pool-01",
                    "allowVolumeExpansion": true,
                    "createSnapshotClass": true,
                    "any": "value"
                }
            ]
        }
    }
]
```

`VastStorage` can be created from yaml input file or generated based on parameters
- namespace defaults to vast-csi
- vast_driver must reference to existing [driver](./create_driver.md)
- vast_cluster must reference to existing [cluster](./create_cluster.md)
- any other value will end up in spec of an object as-is

## Example

```
# iserver set ocp task --cluster bm1 --file C:\tmp\task.json --no-confirm
Cluster: bm1 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed

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

[Back](./create_task.md)