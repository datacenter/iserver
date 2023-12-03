# Kubernetes

## Persistent Volume Claim

### Get

Get all pvc objects from selected cluster. Use --namespace or --name options to filter the results.

```
# iserver get k8s pvc --name dev-cnf/cat8000v-generic*
Cluster: Milan-BM1 (type: ocp)

PVC [#1]
--------

+-----------+-----------------------+--------+------------------------------------------+------+---------------+---------------+-----+
| Namespace | Name                  | Status | Volume                                   | Size | Access Mode   | Storage Class | Age |
+-----------+-----------------------+--------+------------------------------------------+------+---------------+---------------+-----+
| dev-cnf   | cat8000v-generic-day0 | Bound  | pvc-f793a2d0-0c26-4363-b299-2d84feec2d5c | 1Gi  | ReadWriteOnce | lvms-vg1      | 2d  |
+-----------+-----------------------+--------+------------------------------------------+------+---------------+---------------+-----+
```

Define --view option: state (default), metadata, pv, usage or all, to get different details of selected pvc objects.

```
# iserver get k8s pvc --name dev-cnf/cat8000v-generic-day0 -v all
Cluster: Milan-BM1 (type: ocp)

PVC [#1]
--------

+-----------+-----------------------+--------+------------------------------------------+------+---------------+---------------+-----+
| Namespace | Name                  | Status | Volume                                   | Size | Access Mode   | Storage Class | Age |
+-----------+-----------------------+--------+------------------------------------------+------+---------------+---------------+-----+
| dev-cnf   | cat8000v-generic-day0 | Bound  | pvc-f793a2d0-0c26-4363-b299-2d84feec2d5c | 1Gi  | ReadWriteOnce | lvms-vg1      | 2d  |
+-----------+-----------------------+--------+------------------------------------------+------+---------------+---------------+-----+

PVC - Metadata [#1]
-------------------

+-----------+-----------------------+-------+------------------------------------------------------+------------------------------------------------------------------------+
| Namespace | Name                  | Owner | Label                                                | Annotation                                                             |
+-----------+-----------------------+-------+------------------------------------------------------+------------------------------------------------------------------------+
| dev-cnf   | cat8000v-generic-day0 | --    | alerts.k8s.io/KubePersistentVolumeFillingUp:disabled | cdi.kubevirt.io/storage.bind.immediate.requested:true                  |
|           |                       |       | app:containerized-data-importer                      | cdi.kubevirt.io/storage.condition.bound:true                           |
|           |                       |       | app.kubernetes.io/component:storage                  | cdi.kubevirt.io/storage.condition.bound.message:                       |
|           |                       |       | app.kubernetes.io/managed-by:cdi-controller          | cdi.kubevirt.io/storage.condition.bound.reason:                        |
|           |                       |       | app.kubernetes.io/part-of:hyperconverged-cluster     | cdi.kubevirt.io/storage.condition.running:false                        |
|           |                       |       | app.kubernetes.io/version:4.12.7                     | cdi.kubevirt.io/storage.condition.running.message:Upload Complete      |
|           |                       |       |                                                      | cdi.kubevirt.io/storage.condition.running.reason:Completed             |
|           |                       |       |                                                      | cdi.kubevirt.io/storage.contentType:kubevirt                           |
|           |                       |       |                                                      | cdi.kubevirt.io/storage.deleteAfterCompletion:true                     |
|           |                       |       |                                                      | cdi.kubevirt.io/storage.pod.phase:Succeeded                            |
|           |                       |       |                                                      | cdi.kubevirt.io/storage.pod.ready:false                                |
|           |                       |       |                                                      | cdi.kubevirt.io/storage.pod.restarts:0                                 |
|           |                       |       |                                                      | cdi.kubevirt.io/storage.preallocation.requested:false                  |
|           |                       |       |                                                      | cdi.kubevirt.io/storage.upload.target:                                 |
|           |                       |       |                                                      | cdi.kubevirt.io/storage.uploadPodName:cdi-upload-cat8000v-generic-day0 |
|           |                       |       |                                                      | pv.kubernetes.io/bind-completed:yes                                    |
|           |                       |       |                                                      | pv.kubernetes.io/bound-by-controller:yes                               |
|           |                       |       |                                                      | volume.beta.kubernetes.io/storage-provisioner:topolvm.io               |
|           |                       |       |                                                      | volume.kubernetes.io/selected-node:ocp-bm1                             |
|           |                       |       |                                                      | volume.kubernetes.io/storage-provisioner:topolvm.io                    |
+-----------+-----------------------+-------+------------------------------------------------------+------------------------------------------------------------------------+

PVC - Volume [#1]
-----------------

+-----------+-----------------------+------------------------------------------+--------+------------+---------------+--------------+--------------+
| Namespace | Name                  | Volume                                   | Status | Mode       | Storage Class | Storege Type | Storage Node |
+-----------+-----------------------+------------------------------------------+--------+------------+---------------+--------------+--------------+
| dev-cnf   | cat8000v-generic-day0 | pvc-f793a2d0-0c26-4363-b299-2d84feec2d5c | Bound  | Filesystem | lvms-vg1      | topolvm.io   | ocp-bm1      |
+-----------+-----------------------+------------------------------------------+--------+------------+---------------+--------------+--------------+

PVC - Usage [#1]
----------------

+-----------+-----------------------+------+----------------------------------+-------------------------+
| Namespace | Name                  | Used | Pod                              | Virtual Machine Instace |
+-----------+-----------------------+------+----------------------------------+-------------------------+
| dev-cnf   | cat8000v-generic-day0 | ✓    | dev-cnf/virt-launcher-srtr-hw7hh | dev-cnf/srtr            |
+-----------+-----------------------+------+----------------------------------+-------------------------+
```

### Create

Create pvc checks if pvc exists and in such case it will be deleted first (unless used or owned by different object).

```
# iserver create k8s pvc --type day0 --namespace dev-cnf --name my-day0 --size 1G --location .\samples\ocp\kubevirt\cat8kv\basic\iosxe_config.txt
Cluster: Milan-BM1 (type: ocp)

PVC dev-cnf/my-day0 already exists. Remove it?
Continue [Y/N]? y
PVC deleted
Creating PVC dev-cnf/my-day0 from file .\samples\ocp\kubevirt\cat8kv\basic\iosxe_config.txt
-PVC created

PVC [#1]
--------

+-----------+---------+--------+------------------------------------------+------+---------------+---------------+------+
| Namespace | Name    | Status | Volume                                   | Size | Access Mode   | Storage Class | Age  |
+-----------+---------+--------+------------------------------------------+------+---------------+---------------+------+
| dev-cnf   | my-day0 | Bound  | pvc-59ad1a40-24a1-423f-bc1f-4e8235b85db9 | 1Gi  | ReadWriteOnce | lvms-vg1      | 2h0m |
+-----------+---------+--------+------------------------------------------+------+---------------+---------------+------+

PVC - Metadata [#1]
-------------------

+-----------+---------+-------+------------------------------------------------------+-------------------------------------------------------------------+
| Namespace | Name    | Owner | Label                                                | Annotation                                                        |
+-----------+---------+-------+------------------------------------------------------+-------------------------------------------------------------------+
| dev-cnf   | my-day0 | --    | alerts.k8s.io/KubePersistentVolumeFillingUp:disabled | cdi.kubevirt.io/storage.bind.immediate.requested:true             |
|           |         |       | app:containerized-data-importer                      | cdi.kubevirt.io/storage.condition.bound:true                      |
|           |         |       | app.kubernetes.io/component:storage                  | cdi.kubevirt.io/storage.condition.bound.message:                  |
|           |         |       | app.kubernetes.io/managed-by:cdi-controller          | cdi.kubevirt.io/storage.condition.bound.reason:                   |
|           |         |       | app.kubernetes.io/part-of:hyperconverged-cluster     | cdi.kubevirt.io/storage.condition.running:false                   |
|           |         |       | app.kubernetes.io/version:4.12.7                     | cdi.kubevirt.io/storage.condition.running.message:Upload Complete |
|           |         |       |                                                      | cdi.kubevirt.io/storage.condition.running.reason:Completed        |
|           |         |       |                                                      | cdi.kubevirt.io/storage.contentType:kubevirt                      |
|           |         |       |                                                      | cdi.kubevirt.io/storage.deleteAfterCompletion:true                |
|           |         |       |                                                      | cdi.kubevirt.io/storage.pod.phase:Succeeded                       |
|           |         |       |                                                      | cdi.kubevirt.io/storage.pod.ready:false                           |
|           |         |       |                                                      | cdi.kubevirt.io/storage.pod.restarts:0                            |
|           |         |       |                                                      | cdi.kubevirt.io/storage.preallocation.requested:false             |
|           |         |       |                                                      | cdi.kubevirt.io/storage.upload.target:                            |
|           |         |       |                                                      | cdi.kubevirt.io/storage.uploadPodName:cdi-upload-my-day0          |
|           |         |       |                                                      | pv.kubernetes.io/bind-completed:yes                               |
|           |         |       |                                                      | pv.kubernetes.io/bound-by-controller:yes                          |
|           |         |       |                                                      | volume.beta.kubernetes.io/storage-provisioner:topolvm.io          |
|           |         |       |                                                      | volume.kubernetes.io/selected-node:ocp-bm1                        |
|           |         |       |                                                      | volume.kubernetes.io/storage-provisioner:topolvm.io               |
+-----------+---------+-------+------------------------------------------------------+-------------------------------------------------------------------+
```

### Delete

Delete pvc checks pvc usage (pod or virtual machine instance) as well as ownership. If pvc is used or owned by another object then no delete action is taken.

```
# iserver delete k8s pvc --name dev-cnf/my-day0
Cluster: Milan-BM1 (type: ocp)

PVC [#1]
--------

+-----------+---------+--------+------------------------------------------+------+---------------+---------------+-------+-------+------+
| Namespace | Name    | Status | Volume                                   | Size | Access Mode   | Storage Class | Usage | Owner | Age  |
+-----------+---------+--------+------------------------------------------+------+---------------+---------------+-------+-------+------+
| dev-cnf   | my-day0 | Bound  | pvc-5c85f0be-83ef-4f67-b93c-156ef1d153b9 | 1Gi  | ReadWriteOnce | lvms-vg1      | ✗     | --    | 2h2m |
+-----------+---------+--------+------------------------------------------+------+---------------+---------------+-------+-------+------+
[ERROR] PVC dev-cnf/my-day0 is owned by different object
```

```
# iserver delete k8s pvc --name dev-cnf/my-day0
Cluster: Milan-BM1 (type: ocp)

PVC [#1]
--------

+-----------+---------+--------+------------------------------------------+------+---------------+---------------+-------+-------+------+
| Namespace | Name    | Status | Volume                                   | Size | Access Mode   | Storage Class | Usage | Owner | Age  |
+-----------+---------+--------+------------------------------------------+------+---------------+---------------+-------+-------+------+
| dev-cnf   | my-day0 | Bound  | pvc-5c85f0be-83ef-4f67-b93c-156ef1d153b9 | 1Gi  | ReadWriteOnce | lvms-vg1      | ✗     | --    | 2h2m |
+-----------+---------+--------+------------------------------------------+------+---------------+---------------+-------+-------+------+
[ERROR] PVC dev-cnf/my-day0 is owned by different object
```

[[Back]](./README.md)