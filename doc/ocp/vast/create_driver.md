# VAST CSI - Create Driver

[[Back]](./README.md) [[kb]](./kb/driver.md)

## HowTo

```
# iserver set ocp vast --cluster bm1 --mode driver --filename C:\tmp\driver.yaml --no-confirm

# iserver set ocp vast --mode driver
  --cluster TEXT            Cluster Name
  --filename TEXT           VAST CSI CRD
  --no-confirm              Confirmation mode
```

## Workflow

- check vast csi [operator](./create_operator.md)
- create `VastCSIDriver` resource
- wait for initiatlization and deployed status
- wait for associated deployment and daemon set ready

## Example

```
# iserver set ocp vast --cluster bm1 --mode driver --filename C:\tmp\driver.yaml --no-confirm

OpenShift Workflow - VAST CSI Operator - Create Driver
======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
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

+----+-------------+------+-----+--------------------------------------------------------+-----------------------------------------------------------+
| ID | Vast Driver | Init | Dep | Spec                                                   | Resource                                                  |
+----+-------------+------+-----+--------------------------------------------------------+-----------------------------------------------------------+
| 1  | vast-csi    | V    | V   | {                                                      | [CSIDriver] nfs                                           | 
|    | nfs         |      |     |   "applySecurityContextConstraints": true,             | [ClusterRole] nfs-vast-attacher-role                      | 
|    |             |      |     |   "attachRequired": true,                              | [ClusterRole] nfs-vast-provisioner-role                   | 
|    |             |      |     |   "blockHostsAutoPrune": false,                        | [ClusterRole] nfs-vast-resizer-role                       | 
|    |             |      |     |   "dontUseTrashApi": false,                            | [ClusterRoleBinding] nfs-vast-attacher-binding            | 
|    |             |      |     |   "driverType": "nfs",                                 | [ClusterRoleBinding] nfs-vast-provisioner-binding         | 
|    |             |      |     |   "image": {                                           | [ClusterRoleBinding] nfs-vast-resizer-binding             | 
|    |             |      |     |     "csiVastPlugin": {                                 | [DaemonSet] vast-csi/csi-vast-node                        | 
|    |             |      |     |       "imagePullPolicy": "IfNotPresent",               | [Deployment] vast-csi/csi-vast-controller                 | 
|    |             |      |     |       "repository": "docker.io/vastdataorg/csi:v2.6.4" | [RoleBinding] vast-csi/nfs-vast-controller-scc-sa-binding | 
|    |             |      |     |     }                                                  | [RoleBinding] vast-csi/nfs-vast-node-scc-sa-binding       | 
|    |             |      |     |   },                                                   | [ServiceAccount] vast-csi/nfs-vast-controller-sa          | 
|    |             |      |     |   "kubeletPath": "/var/lib/kubelet",                   | [ServiceAccount] vast-csi/nfs-vast-node-sa                | 
|    |             |      |     |   "logLevel": 5,                                       |                                                           | 
|    |             |      |     |   "numWorkers": 10,                                    |                                                           | 
|    |             |      |     |   "operationRetryIntervalMax": 60,                     |                                                           | 
|    |             |      |     |   "operationRetryIntervalStart": 10,                   |                                                           | 
|    |             |      |     |   "operationTimeout": 15,                              |                                                           | 
|    |             |      |     |   "truncateVolumeName": 64,                            |                                                           | 
|    |             |      |     |   "useLocalIpForMount": "",                            |                                                           | 
|    |             |      |     |   "verifySsl": false                                   |                                                           | 
|    |             |      |     | }                                                      |                                                           | 
+----+-------------+------+-----+--------------------------------------------------------+-----------------------------------------------------------+

Completed tasks
- VAST CSI driver created

+----+------------+-------+---------------+---------+---------+--------------+
| ID | Target     | Scope | Workflow      | Changes | Success | Duration [s] |
+----+------------+-------+---------------+---------+---------+--------------+
| 1  | ocp:bm1    | vast  | create driver | 1       | V       | 26           | 
+----+------------+-------+---------------+---------+---------+--------------+
```

[[Back]](./README.md) [[kb]](./kb/driver.md)