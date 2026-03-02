# VAST CSI Driver

## Get state

```
# iserver get k8s vastd --cluster bm1
Cluster: bm1 (type: ocp)

+----+-------------+------+-----+--------------------------------------------------------+-------------------------------------------------------------+--------------+
| ID | Vast Driver | Init | Dep | Spec                                                   | Resource                                                    | Vast Storage |
+----+-------------+------+-----+--------------------------------------------------------+-------------------------------------------------------------+--------------+
| 1  | vast-csi    | V    | V   | {                                                      | [CSIDriver] block                                           | vast-block   |
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
| 2  | vast-csi    | V    | V   | {                                                      | [CSIDriver] nfs                                             | vast-nfs     |
|    | nfs         |      |     |   "applySecurityContextConstraints": true,             | [ClusterRole] nfs-vast-attacher-role                        |              |
|    |             |      |     |   "attachRequired": true,                              | [ClusterRole] nfs-vast-provisioner-role                     |              |
|    |             |      |     |   "blockHostsAutoPrune": false,                        | [ClusterRole] nfs-vast-resizer-role                         |              |
|    |             |      |     |   "dontUseTrashApi": false,                            | [ClusterRoleBinding] nfs-vast-attacher-binding              |              |
|    |             |      |     |   "driverType": "nfs",                                 | [ClusterRoleBinding] nfs-vast-provisioner-binding           |              |
|    |             |      |     |   "image": {                                           | [ClusterRoleBinding] nfs-vast-resizer-binding               |              |
|    |             |      |     |     "csiVastPlugin": {                                 | [DaemonSet] vast-csi/csi-vast-node                          |              |
|    |             |      |     |       "imagePullPolicy": "IfNotPresent",               | [Deployment] vast-csi/csi-vast-controller                   |              |
|    |             |      |     |       "repository": "docker.io/vastdataorg/csi:v2.6.4" | [RoleBinding] vast-csi/nfs-vast-controller-scc-sa-binding   |              |
|    |             |      |     |     }                                                  | [RoleBinding] vast-csi/nfs-vast-node-scc-sa-binding         |              |
|    |             |      |     |   },                                                   | [ServiceAccount] vast-csi/nfs-vast-controller-sa            |              |
|    |             |      |     |   "kubeletPath": "/var/lib/kubelet",                   | [ServiceAccount] vast-csi/nfs-vast-node-sa                  |              |
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
Filter: namespace, name
View:   state (def), manifest
```

## Get release manifest

```
# iserver get k8s vastd --cluster bm1 -v manifest
Cluster: bm1 (type: ocp)

Vast Driver Manifest [vast-csi/vast-nfs]
----------------------------------------
~~~
---
# Source: vastcsidriver/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: vast-nfs-vast-controller-sa
  namespace: "vast-csi"
  labels:
    helm.sh/chart: vastcsidriver-v2.6.4
    app.kubernetes.io/name: vastcsidriver
    app.kubernetes.io/instance: vast-nfs
    app.kubernetes.io/managed-by: Helm
    storage.vastdata.com/driverType: nfs
---
# Source: vastcsidriver/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: vast-nfs-vast-node-sa
  namespace: "vast-csi"
  labels:
    helm.sh/chart: vastcsidriver-v2.6.4
    app.kubernetes.io/name: vastcsidriver
    app.kubernetes.io/instance: vast-nfs
    app.kubernetes.io/managed-by: Helm
    storage.vastdata.com/driverType: nfs
---
# Source: vastcsidriver/templates/clusterrole.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: vast-nfs-vast-provisioner-role
  labels:
    helm.sh/chart: vastcsidriver-v2.6.4
    app.kubernetes.io/name: vastcsidriver
    app.kubernetes.io/instance: vast-nfs
    app.kubernetes.io/managed-by: Helm
    storage.vastdata.com/driverType: nfs
rules:
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get", "list"]
  - apiGroups: [""]
    resources: ["persistentvolumes"]
    verbs: ["get", "list", "watch", "create", "delete"]
  - apiGroups: [""]
    resources: ["persistentvolumeclaims"]
    verbs: ["get", "list", "watch", "update"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["storageclasses"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["csinodes"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [""]
    resources: ["events"]
    verbs: ["list", "watch", "create", "update", "patch"]
  - apiGroups: ["snapshot.storage.k8s.io"]
    resources: ["volumesnapshots"]
    verbs: ["get", "list"]
  - apiGroups: ["snapshot.storage.k8s.io"]
    resources: ["volumesnapshotcontents"]
    verbs: ["get", "list", "watch", "update", "patch"]
  - apiGroups: [""]
    resources: ["nodes"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["snapshot.storage.k8s.io"]
    resources: ["volumesnapshotclasses"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["snapshot.storage.k8s.io"]
    resources: ["volumesnapshotcontents/status"]
    verbs: ["update", "patch"]
---
# Source: vastcsidriver/templates/clusterrole.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: vast-nfs-vast-attacher-role
  labels:
    helm.sh/chart: vastcsidriver-v2.6.4
    app.kubernetes.io/name: vastcsidriver
    app.kubernetes.io/instance: vast-nfs
    app.kubernetes.io/managed-by: Helm
    storage.vastdata.com/driverType: nfs
rules:
  - apiGroups: [""]
    resources: ["persistentvolumes"]
    verbs: ["get", "list", "watch", "update", "patch"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["csinodes"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["volumeattachments"]
    verbs: ["get", "list", "watch", "update", "patch"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["volumeattachments/status"]
    verbs: ["patch"]
---
# Source: vastcsidriver/templates/clusterrole.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: vast-nfs-vast-resizer-role
  labels:
    helm.sh/chart: vastcsidriver-v2.6.4
    app.kubernetes.io/name: vastcsidriver
    app.kubernetes.io/instance: vast-nfs
    app.kubernetes.io/managed-by: Helm
    storage.vastdata.com/driverType: nfs
rules:
  - apiGroups: [""]
    resources: ["persistentvolumes"]
    verbs: ["get", "list", "watch", "patch"]
  - apiGroups: [""]
    resources: ["persistentvolumeclaims"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [""]
    resources: ["persistentvolumeclaims/status"]
    verbs: ["patch"]
  - apiGroups: [""]
    resources: ["events"]
    verbs: ["list", "watch", "create", "update", "patch"]
---
# Source: vastcsidriver/templates/clusterrolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: vast-nfs-vast-provisioner-binding
  labels:
    helm.sh/chart: vastcsidriver-v2.6.4
    app.kubernetes.io/name: vastcsidriver
    app.kubernetes.io/instance: vast-nfs
    app.kubernetes.io/managed-by: Helm
    storage.vastdata.com/driverType: nfs
subjects:
  - kind: ServiceAccount
    name: vast-nfs-vast-controller-sa
    namespace: "vast-csi"
roleRef:
  kind: ClusterRole
  name: vast-nfs-vast-provisioner-role
  apiGroup: rbac.authorization.k8s.io
---
# Source: vastcsidriver/templates/clusterrolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: vast-nfs-vast-attacher-binding
  labels:
    helm.sh/chart: vastcsidriver-v2.6.4
    app.kubernetes.io/name: vastcsidriver
    app.kubernetes.io/instance: vast-nfs
    app.kubernetes.io/managed-by: Helm
    storage.vastdata.com/driverType: nfs
subjects:
  - kind: ServiceAccount
    name: vast-nfs-vast-controller-sa
    namespace: "vast-csi"
roleRef:
  kind: ClusterRole
  name: vast-nfs-vast-attacher-role
  apiGroup: rbac.authorization.k8s.io
---
# Source: vastcsidriver/templates/clusterrolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: vast-nfs-vast-resizer-binding
  labels:
    helm.sh/chart: vastcsidriver-v2.6.4
    app.kubernetes.io/name: vastcsidriver
    app.kubernetes.io/instance: vast-nfs
    app.kubernetes.io/managed-by: Helm
    storage.vastdata.com/driverType: nfs
subjects:
  - kind: ServiceAccount
    name: vast-nfs-vast-controller-sa
    namespace: "vast-csi"
roleRef:
  kind: ClusterRole
  name: vast-nfs-vast-resizer-role
  apiGroup: rbac.authorization.k8s.io
---
# Source: vastcsidriver/templates/csi-scc.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: vast-nfs-vast-controller-scc-sa-binding
  namespace: vast-csi
subjects:
- kind: ServiceAccount
  name: vast-nfs-vast-controller-sa
  namespace: vast-csi
roleRef:
  kind: ClusterRole
  name: system:openshift:scc:privileged
  apiGroup: rbac.authorization.k8s.io
---
# Source: vastcsidriver/templates/csi-scc.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: vast-nfs-vast-node-scc-sa-binding
  namespace: vast-csi
subjects:
- kind: ServiceAccount
  name: vast-nfs-vast-node-sa
  namespace: vast-csi
roleRef:
  kind: ClusterRole
  name: system:openshift:scc:privileged
  apiGroup: rbac.authorization.k8s.io
---
# Source: vastcsidriver/templates/node.yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: csi-vast-node
  namespace: "vast-csi"
  labels:
    helm.sh/chart: vastcsidriver-v2.6.4
    app.kubernetes.io/name: vastcsidriver
    app.kubernetes.io/instance: vast-nfs
    app.kubernetes.io/managed-by: Helm
    storage.vastdata.com/driverType: nfs
    app.kubernetes.io/csi-role: "node"
spec:
...
---
# Source: vastcsidriver/templates/controller.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: csi-vast-controller
  namespace: "vast-csi"
  labels:
    helm.sh/chart: vastcsidriver-v2.6.4
    app.kubernetes.io/name: vastcsidriver
    app.kubernetes.io/instance: vast-nfs
    app.kubernetes.io/managed-by: Helm
    storage.vastdata.com/driverType: nfs
    app.kubernetes.io/csi-role: "controller"
spec:
...
---
# Source: vastcsidriver/templates/csi-driver.yaml
apiVersion: storage.k8s.io/v1
kind: CSIDriver
metadata:
  name: vast-nfs
  labels:
    helm.sh/chart: vastcsidriver-v2.6.4
    app.kubernetes.io/name: vastcsidriver
    app.kubernetes.io/instance: vast-nfs
    app.kubernetes.io/managed-by: Helm
    storage.vastdata.com/driverType: nfs
spec:
  attachRequired: true
  podInfoOnMount: true
  volumeLifecycleModes:
    - Persistent
    - Ephemeral
~~~

Filter: namespace, name
View:   state (def), manifest
```

[[Back]](./README.md)