# LVM Storage - Test

## Workflow

- check lvm storage operator subscription
- check lvm storage operator resources (deployments and daemon_sets)
- check lvmcluster CRD and its state
- check storage class
- create test namespace controlled with --test-namespace and test-lvm as default value
- create pvc "for every node"
- create pod tainted to each node and mounting one pvc
- pod should be up and pvc should be bound
- create volume snapshot for every pvc
- check resources consistency (pod, pvc, pv, volume snapshot, topolvm logical volume, linux-level logical volume)
- delete all resources (use --keep to override)

## Requirements

- LVM Cluster instance must exist and be ready

## Configurable options

```
# iserver set ocp lvm --mode test
  --cluster TEXT                  Cluster Name
  --test-namespace TEXT           Test namespace  [default: test-lvm]
  --keep                          Keep test resources
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver set ocp lvm --cluster bm1 --mode test

OpenShift Workflow - LVM Operator - Functional Test
===================================================

OpenShift Cluster: bm1

LVM Operator
------------
LVM Operator [openshift-storage/lvms] with csv [lvms-operator.v4.18.3]
LVM Subscription resources deployed
LVM Cluster instance: openshift-storage/lvmcluster
LVM Cluster instance: ready
Storage class: lvms-vg1
Prepare test resources
- namespace: test-lvm
- namespace does not exist

Create Namespace
----------------
- name: test-lvm

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: test-lvm

~~~

Namespace created

Wait for namespace [timeout:60]...
- namespace created
~~~
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: bm1-1
  namespace: test-lvm
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    limits:
      storage: 2Gi
    requests:
      storage: 1Gi
  storageClassName: lvms-vg1
  volumeMode: Block

~~~
- pvc [test-lvm/bm1-1] created
- wait for pvc [timeout:60s]...
~~~
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: bm1-2
  namespace: test-lvm
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    limits:
      storage: 2Gi
    requests:
      storage: 1Gi
  storageClassName: lvms-vg1
  volumeMode: Block

~~~
- pvc [test-lvm/bm1-2] created
- wait for pvc [timeout:60s]...
~~~
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: bm1-3
  namespace: test-lvm
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    limits:
      storage: 2Gi
    requests:
      storage: 1Gi
  storageClassName: lvms-vg1
  volumeMode: Block

~~~
- pvc [test-lvm/bm1-3] created
- wait for pvc [timeout:60s]...
~~~
apiVersion: v1
kind: Pod
metadata:
  name: bm1-1
  namespace: test-lvm
spec:
  containers:
  - command:
    - /bin/sleep
    - infinity
    image: quay.io/centos/centos:latest
    name: centos
    volumeDevices:
    - devicePath: /dev/xvda
      name: data
  nodeSelector:
    kubernetes.io/hostname: bm1-1
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: bm1-1

~~~
- pod [test-lvm/bm1-1] created
- wait for pod running [timeout:600s]...
- wait for pvc [test-lvm/bm1-1] bound [timeout:60s]...
~~~
apiVersion: v1
kind: Pod
metadata:
  name: bm1-2
  namespace: test-lvm
spec:
  containers:
  - command:
    - /bin/sleep
    - infinity
    image: quay.io/centos/centos:latest
    name: centos
    volumeDevices:
    - devicePath: /dev/xvda
      name: data
  nodeSelector:
    kubernetes.io/hostname: bm1-2
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: bm1-2

~~~
- pod [test-lvm/bm1-2] created
- wait for pod running [timeout:600s]...
- wait for pvc [test-lvm/bm1-2] bound [timeout:60s]...
~~~
apiVersion: v1
kind: Pod
metadata:
  name: bm1-3
  namespace: test-lvm
spec:
  containers:
  - command:
    - /bin/sleep
    - infinity
    image: quay.io/centos/centos:latest
    name: centos
    volumeDevices:
    - devicePath: /dev/xvda
      name: data
  nodeSelector:
    kubernetes.io/hostname: bm1-3
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: bm1-3

~~~
- pod [test-lvm/bm1-3] created
- wait for pod running [timeout:600s]...
- wait for pvc [test-lvm/bm1-3] bound [timeout:60s]...
~~~
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: bm1-1-snap
  namespace: test-lvm
spec:
  source:
    persistentVolumeClaimName: bm1-1
  volumeSnapshotClassName: lvms-vg1

~~~
- volume snapshot [test-lvm/bm1-1-snap] created
~~~
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: bm1-2-snap
  namespace: test-lvm
spec:
  source:
    persistentVolumeClaimName: bm1-2
  volumeSnapshotClassName: lvms-vg1

~~~
- volume snapshot [test-lvm/bm1-2-snap] created
~~~
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: bm1-3-snap
  namespace: test-lvm
spec:
  source:
    persistentVolumeClaimName: bm1-3
  volumeSnapshotClassName: lvms-vg1

~~~
- volume snapshot [test-lvm/bm1-3-snap] created

PODs
----

+----+----------+-------+---------+--------------------+------+-------+--------------+-----+-----+----------+
| ID | Pod      | Ready | Status  | Condition          | Age  | Node  | IP           | Net | Svc | Restarts |
+----+----------+-------+---------+--------------------+------+-------+--------------+-----+-----+----------+
| 1  | test-lvm | 1/1   | Running | Initialized: ✓     | 1h0m | bm1-1 | 10.128.2.99  | 1   |     | 0        | 
|    | bm1-1    |       |         | PodScheduled: ✓    |      |       |              |     |     |          | 
|    |          |       |         | ContainersReady: ✓ |      |       |              |     |     |          | 
|    |          |       |         | Ready: ✓           |      |       |              |     |     |          | 
+----+----------+-------+---------+--------------------+------+-------+--------------+-----+-----+----------+
| 2  | test-lvm | 1/1   | Running | Initialized: ✓     | 1h0m | bm1-2 | 10.128.1.146 | 1   |     | 0        | 
|    | bm1-2    |       |         | PodScheduled: ✓    |      |       |              |     |     |          | 
|    |          |       |         | ContainersReady: ✓ |      |       |              |     |     |          | 
|    |          |       |         | Ready: ✓           |      |       |              |     |     |          | 
+----+----------+-------+---------+--------------------+------+-------+--------------+-----+-----+----------+
| 3  | test-lvm | 1/1   | Running | Initialized: ✓     | 1h0m | bm1-3 | 10.128.5.241 | 1   |     | 0        | 
|    | bm1-3    |       |         | PodScheduled: ✓    |      |       |              |     |     |          | 
|    |          |       |         | ContainersReady: ✓ |      |       |              |     |     |          | 
|    |          |       |         | Ready: ✓           |      |       |              |     |     |          | 
+----+----------+-------+---------+--------------------+------+-------+--------------+-----+-----+----------+

Persistent Volume Claims
------------------------

+-----------+-------+--------+------------------------------------------+------+---------------+---------------+----------------+-------+------+
| Namespace | Name  | Status | Volume                                   | Size | Access Mode   | Storage Class | Usage          | Owner | Age  |
+-----------+-------+--------+------------------------------------------+------+---------------+---------------+----------------+-------+------+
| test-lvm  | bm1-1 | Bound  | pvc-4915bbd8-c653-4b6c-aaf1-bc35856acdc0 | 1Gi  | ReadWriteOnce | lvms-vg1      | test-lvm/bm1-1 | --    | 1h0m | 
| test-lvm  | bm1-2 | Bound  | pvc-d9fff49d-a715-4b34-b5db-9dd3a03b2966 | 1Gi  | ReadWriteOnce | lvms-vg1      | test-lvm/bm1-2 | --    | 1h0m | 
| test-lvm  | bm1-3 | Bound  | pvc-1053f75f-17cb-4d32-b58b-d46f1e406341 | 1Gi  | ReadWriteOnce | lvms-vg1      | test-lvm/bm1-3 | --    | 1h0m | 
+-----------+-------+--------+------------------------------------------+------+---------------+---------------+----------------+-------+------+

Persistent Volumes
------------------

+------------------------------------------+--------+-------+----------+------+---------------+------------+--------------------------------------+--------+----------------+------+
| PV                                       | Status | Mode  | SC       | Size | Access Mode   | CSI Driver | CSI Handle                           | Device | PVC            | Age  |
+------------------------------------------+--------+-------+----------+------+---------------+------------+--------------------------------------+--------+----------------+------+
| pvc-1053f75f-17cb-4d32-b58b-d46f1e406341 | Bound  | Block | lvms-vg1 | 1Gi  | ReadWriteOnce | topolvm.io | c41b7dc0-efce-42f8-af0b-1cb3ef713598 | --     | test-lvm/bm1-3 | 1h0m | 
| pvc-4915bbd8-c653-4b6c-aaf1-bc35856acdc0 | Bound  | Block | lvms-vg1 | 1Gi  | ReadWriteOnce | topolvm.io | 620ed5d7-414e-4b13-99ea-7a326ebb222c | --     | test-lvm/bm1-1 | 1h0m | 
| pvc-d9fff49d-a715-4b34-b5db-9dd3a03b2966 | Bound  | Block | lvms-vg1 | 1Gi  | ReadWriteOnce | topolvm.io | 0fc6e51f-fff8-4567-b775-acea0e4858ae | --     | test-lvm/bm1-2 | 1h0m | 
+------------------------------------------+--------+-------+----------+------+---------------+------------+--------------------------------------+--------+----------------+------+

Volume Snapshots
----------------

+---------------------+-------+-------+----------+------+------+
| Volume Snapshot     | Ready | PVC   | Class    | Size | Age  |
+---------------------+-------+-------+----------+------+------+
| test-lvm/bm1-1-snap | ✓     | bm1-1 | lvms-vg1 | 1Gi  | 1h0m | 
| test-lvm/bm1-2-snap | ✓     | bm1-2 | lvms-vg1 | 1Gi  | 1h0m | 
| test-lvm/bm1-3-snap | ✓     | bm1-3 | lvms-vg1 | 1Gi  | 1h0m | 
+---------------------+-------+-------+----------+------+------+

Logical Volumes (TopoLVM)
-------------------------

+------------------------------------------+-------+--------------+----------+-----------+--------------------------------------+
| Logical Volume                           | Node  | Device Class | Req Size | Curr Size | Volume                               |
+------------------------------------------+-------+--------------+----------+-----------+--------------------------------------+
| pvc-1053f75f-17cb-4d32-b58b-d46f1e406341 | bm1-3 | vg1          | 1Gi      | 1Gi       | c41b7dc0-efce-42f8-af0b-1cb3ef713598 | 
| pvc-4915bbd8-c653-4b6c-aaf1-bc35856acdc0 | bm1-1 | vg1          | 1Gi      | 1Gi       | 620ed5d7-414e-4b13-99ea-7a326ebb222c | 
| pvc-d9fff49d-a715-4b34-b5db-9dd3a03b2966 | bm1-2 | vg1          | 1Gi      | 1Gi       | 0fc6e51f-fff8-4567-b775-acea0e4858ae | 
+------------------------------------------+-------+--------------+----------+-----------+--------------------------------------+

Collect linux level lv state...

Logical Volumes (LVM) [bm1-1]
-----------------------------

+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-----------------------+
| LV Name                                  | VG  | LV Pool     | Dev   | LV Size | MSize | Layout | Role         | Snap | K8s Usage             |
+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-----------------------+
| 620ed5d7-414e-4b13-99ea-7a326ebb222c     | vg1 | thin-pool-1 | 253:4 | 1.00g   | 0.00% | thin   | public       | 1    | (pvc) test-lvm/bm1-1  | 
|                                          |     |             |       |         |       | sparse | origin       |      |                       | 
|                                          |     |             |       |         |       |        | thinorigin   |      |                       | 
+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-----------------------+
| 2a265e64-24c3-4f91-b1ea-099eb39c09fe     | vg1 | thin-pool-1 | 253:5 | 1.00g   | 0.00% | thin   | public       | --   | (snap) test-lvm/bm1-1 | 
| [S] 620ed5d7-414e-4b13-99ea-7a326ebb222c |     |             |       |         |       | sparse | snapshot     |      |                       | 
|                                          |     |             |       |         |       |        | thinsnapshot |      |                       | 
+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-----------------------+

Logical Volumes (LVM) [bm1-2]
-----------------------------

+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-----------------------+
| LV Name                                  | VG  | LV Pool     | Dev   | LV Size | MSize | Layout | Role         | Snap | K8s Usage             |
+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-----------------------+
| 0fc6e51f-fff8-4567-b775-acea0e4858ae     | vg1 | thin-pool-1 | 253:4 | 1.00g   | 0.00% | thin   | public       | 1    | (pvc) test-lvm/bm1-2  | 
|                                          |     |             |       |         |       | sparse | origin       |      |                       | 
|                                          |     |             |       |         |       |        | thinorigin   |      |                       | 
+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-----------------------+
| dde487fd-0d92-44be-868f-c2d652e30463     | vg1 | thin-pool-1 | 253:5 | 1.00g   | 0.00% | thin   | public       | --   | (snap) test-lvm/bm1-2 | 
| [S] 0fc6e51f-fff8-4567-b775-acea0e4858ae |     |             |       |         |       | sparse | snapshot     |      |                       | 
|                                          |     |             |       |         |       |        | thinsnapshot |      |                       | 
+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-----------------------+

Logical Volumes (LVM) [bm1-3]
-----------------------------

+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-----------------------+
| LV Name                                  | VG  | LV Pool     | Dev   | LV Size | MSize | Layout | Role         | Snap | K8s Usage             |
+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-----------------------+
| c41b7dc0-efce-42f8-af0b-1cb3ef713598     | vg1 | thin-pool-1 | 253:4 | 1.00g   | 0.00% | thin   | public       | 1    | (pvc) test-lvm/bm1-3  | 
|                                          |     |             |       |         |       | sparse | origin       |      |                       | 
|                                          |     |             |       |         |       |        | thinorigin   |      |                       | 
+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-----------------------+
| e884aeb1-2c4f-4bd0-b3f4-aef37f39dade     | vg1 | thin-pool-1 | 253:5 | 1.00g   | 0.00% | thin   | public       | --   | (snap) test-lvm/bm1-3 | 
| [S] c41b7dc0-efce-42f8-af0b-1cb3ef713598 |     |             |       |         |       | sparse | snapshot     |      |                       | 
|                                          |     |             |       |         |       |        | thinsnapshot |      |                       | 
+------------------------------------------+-----+-------------+-------+---------+-------+--------+--------------+------+-----------------------+

Consistency Checks
------------------
- pvc: test-lvm/bm1-1 [node:bm1-1]
- pv found: [name:pvc-4915bbd8-c653-4b6c-aaf1-bc35856acdc0] [csi handle:620ed5d7-414e-4b13-99ea-7a326ebb222c]
- topolvm logical volume found: [name:pvc-4915bbd8-c653-4b6c-aaf1-bc35856acdc0] [volume:620ed5d7-414e-4b13-99ea-7a326ebb222c] with csi handle match
- lv found: [node:bm1-1] [name:620ed5d7-414e-4b13-99ea-7a326ebb222c] [uuid:xGEXnv-Agcb-3RKu-4gxF-UIjq-mczc-Fdsmqn]
- pvc: test-lvm/bm1-2 [node:bm1-2]
- pv found: [name:pvc-d9fff49d-a715-4b34-b5db-9dd3a03b2966] [csi handle:0fc6e51f-fff8-4567-b775-acea0e4858ae]
- topolvm logical volume found: [name:pvc-d9fff49d-a715-4b34-b5db-9dd3a03b2966] [volume:0fc6e51f-fff8-4567-b775-acea0e4858ae] with csi handle match
- lv found: [node:bm1-2] [name:0fc6e51f-fff8-4567-b775-acea0e4858ae] [uuid:CrutHR-X64J-l1j4-FiZP-KAr8-eEO0-Q4KV2q]
- pvc: test-lvm/bm1-3 [node:bm1-3]
- pv found: [name:pvc-1053f75f-17cb-4d32-b58b-d46f1e406341] [csi handle:c41b7dc0-efce-42f8-af0b-1cb3ef713598]
- topolvm logical volume found: [name:pvc-1053f75f-17cb-4d32-b58b-d46f1e406341] [volume:c41b7dc0-efce-42f8-af0b-1cb3ef713598] with csi handle match
- lv found: [node:bm1-3] [name:c41b7dc0-efce-42f8-af0b-1cb3ef713598] [uuid:onJ7Of-N1F6-pRIE-DcPy-JAh3-FgF1-1x6iXc]

Delete test resources
- delete pod test-lvm/bm1-1
- pod delete request successful
- wait for no pod...
- delete pod test-lvm/bm1-2
- pod delete request successful
- wait for no pod...
- delete pod test-lvm/bm1-3
- pod delete request successful
- wait for no pod...
- all pods deleted
- delete snapshot test-lvm/bm1-1-snap
- volume snapshot delete request successful
- wait for no snapshot...
- delete snapshot test-lvm/bm1-2-snap
- volume snapshot delete request successful
- wait for no snapshot...
- delete snapshot test-lvm/bm1-3-snap
- volume snapshot delete request successful
- wait for no snapshot...
- all snapshots deleted
- delete pvc test-lvm/bm1-1
- pvc delete request successful
- wait for no pvc...
- delete pvc test-lvm/bm1-2
- pvc delete request successful
- wait for no pvc...
- delete pvc test-lvm/bm1-3
- pvc delete request successful
- wait for no pvc...
- all pvcs deleted
- namespace deleted: test-lvm
```

[[Back]](./README.md)