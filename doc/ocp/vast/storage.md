# VAST Storage

## Get state

```
# iserver get k8s vasts --cluster bm1
Cluster: bm1 (type: ocp)

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
| 2  | vast-csi     | V    | V   | {                                                             | [StorageClass] vast-csi/vast-nfs          |
|    | vast-nfs     |      |     |   "allowVolumeExpansion": true,                               | [VolumeSnapshotClass] vast-csi/vast-nfs   |
|    |              |      |     |   "blockingClones": false,                                    |                                           |
|    |              |      |     |   "clusterName": "",                                          |                                           |
|    |              |      |     |   "createSnapshotClass": true,                                |                                           |
|    |              |      |     |   "driverType": "nfs",                                        |                                           |
|    |              |      |     |   "ephemeralVolumeNameFormat": "csi:{namespace}:{name}:{id}", |                                           |
|    |              |      |     |   "mountOptions": [],                                         |                                           |
|    |              |      |     |   "provisioner": "nfs",                                       |                                           |
|    |              |      |     |   "reclaimPolicy": "Delete",                                  |                                           |
|    |              |      |     |   "secretName": "my-vast",                                    |                                           |
|    |              |      |     |   "secretNamespace": "vast-csi",                              |                                           |
|    |              |      |     |   "setDefaultStorageClass": false,                            |                                           |
|    |              |      |     |   "storagePath": "/my-nfs-path",                              |                                           |
|    |              |      |     |   "subsystem": "",                                            |                                           |
|    |              |      |     |   "viewPolicy": "nfs-policy",                                 |                                           |
|    |              |      |     |   "vipPool": "pool-01",                                       |                                           |
|    |              |      |     |   "vipPoolFQDNRandomPrefix": true,                            |                                           |
|    |              |      |     |   "volumeNameFormat": "csi:{namespace}:{name}:{id}"           |                                           |
|    |              |      |     | }                                                             |                                           |
+----+--------------+------+-----+---------------------------------------------------------------+-------------------------------------------+

Filter: namespace, name
View:   state (def), manifest
```

## Get release manifest

```
# iserver get k8s vasts --cluster bm1 -v manifest
Cluster: bm1 (type: ocp)

Vast Storage Manifest [vast-csi/vast-filesystem]
------------------------------------------------
~~~
---
# Source: vaststorage/templates/nfs-storage-class.yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
provisioner: vast-nfs
metadata:
  name: vast-filesystem
  namespace: "vast-csi"
  annotations:
    storageclass.kubernetes.io/is-default-class: "false"
  labels:
    helm.sh/chart: vaststorage-v2.6.4
    app.kubernetes.io/name: vaststorage
    app.kubernetes.io/instance: vast-filesystem
    app.kubernetes.io/managed-by: Helm
reclaimPolicy: Delete
parameters:
  eph_volume_name_fmt: csi:{namespace}:{name}:{id}
  root_export: /my-block-path
  view_policy: default
  vip_pool_name: vast-pool
  volume_name_fmt: csi:{namespace}:{name}:{id}
  vip_pool_fqdn_random_prefix: "true"
  csi.storage.k8s.io/provisioner-secret-name: "cluster"
  csi.storage.k8s.io/provisioner-secret-namespace: "vast-csi"
  csi.storage.k8s.io/controller-publish-secret-name: "cluster"
  csi.storage.k8s.io/controller-publish-secret-namespace: "vast-csi"
  csi.storage.k8s.io/node-publish-secret-name: "cluster"
  csi.storage.k8s.io/node-publish-secret-namespace: "vast-csi"
  csi.storage.k8s.io/node-stage-secret-name: "cluster"
  csi.storage.k8s.io/node-stage-secret-namespace: "vast-csi"
  csi.storage.k8s.io/controller-expand-secret-name: "cluster"
  csi.storage.k8s.io/controller-expand-secret-namespace: "vast-csi"
  csi.storage.k8s.io/node-expand-secret-name: "cluster"
  csi.storage.k8s.io/node-expand-secret-namespace: "vast-csi"
allowVolumeExpansion: true
mountOptions:
  []

~~~

Filter: namespace, name
View:   state (def), manifest
```

[[Back]](./README.md)