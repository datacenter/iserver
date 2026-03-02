# VAST Operator - Create driver via Task

## Input

```
[
    {
        "vast": {
            "driver": [
                {
                    "filename": "/tmp/vast_csi_driver.yaml"
                },
                {
                    "name": "from-params",
                    "type": "nfs",
                    "repository": "docker.io/vastdataorg/csi:v2.6.4",
                    "any": "value"
                }
            ]
        }
    }
]
```

`VastCSIDriver` can be created from yaml input file or generated based on parameters
- namespace defaults to vast-csi
- name must be defined
- type must be nfs or block
- repository defaults to docker.io/vastdataorg/csi:v2.6.4
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
```

[Back](./create_task.md)