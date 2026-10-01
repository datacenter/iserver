# VAST CSI - Create Storage

[[Back]](./README.md) [[kb]](./kb/storage.md)

## HowTo

```
# iserver set ocp vast --cluster bm1 --mode storage --filename C:\tmp\storage.yaml --no-confirm

# iserver set ocp vast --mode storage
  --cluster TEXT            Cluster Name
  --filename TEXT           VAST CSI CRD
  --no-confirm              Confirmation mode
```

## Workflow

- check vast csi [operator](./create_operator.md)
- create `VastStorage` resource
- wait for initiatlization and deployed status

## Example

```
# iserver set ocp vast --cluster bm1 --mode storage --filename C:\tmp\storage.yaml --no-confirm

OpenShift Workflow - VAST CSI Operator - Create Storage
=======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
- deployment vast-csi/vast-csi-operator-controller-manager ready

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
  deletionViewPolicy: ocpai-02-nfs
  driverType: nfs
  provisioner: nfs
  secretName: my-vast
  secretNamespace: vast-csi
  setDefaultStorageClass: true
  storagePath: /ocpai-02-nfs
  viewPolicy: ocpai-02-nfs
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
|    |              |      |     |   "setDefaultStorageClass": true,                             |                                         | 
|    |              |      |     |   "storagePath": "/ocpai-02-nfs",                             |                                         | 
|    |              |      |     |   "subsystem": "",                                            |                                         | 
|    |              |      |     |   "viewPolicy": "ocpai-02-nfs",                               |                                         | 
|    |              |      |     |   "vipPool": "pool-01",                                       |                                         | 
|    |              |      |     |   "vipPoolFQDNRandomPrefix": true,                            |                                         | 
|    |              |      |     |   "volumeNameFormat": "csi:{namespace}:{name}:{id}"           |                                         | 
|    |              |      |     | }                                                             |                                         | 
+----+--------------+------+-----+---------------------------------------------------------------+-----------------------------------------+

Completed tasks
- VAST storage created

+----+------------+-------+----------------+---------+---------+--------------+
| ID | Target     | Scope | Workflow       | Changes | Success | Duration [s] |
+----+------------+-------+----------------+---------+---------+--------------+
| 1  | ocp:bm1    | vast  | create storage | 1       | V       | 14           | 
+----+------------+-------+----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[kb]](./kb/storage.md)