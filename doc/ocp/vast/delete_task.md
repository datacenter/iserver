# VAST CSI - Delete via Task

## HowTo

```json
[
  {
    "vast": {
      "operator": {},
      "driver": [
        {
          ...
        }
      ],
      "cluster": [
        {
          ...
        }
      ],
      "storage": [
        {
          ...
        }
      ]
    }
  }
]
```

```
# iserver delete ocp task --cluster bm1 --file C:\tmp\task.json --no-confirm
```

Notes:
- [operator](./delete_operator.md), [driver](./delete_driver.md), [cluster](./delete_cluster.md) and [storage](./delete_storage.md) trigger workflow execution with input parameters
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

## Example

```
# iserver delete ocp task --cluster bm1 --file C:\tmp\task.json --no-confirm

OpenShift Workflow - VAST CSI Operator - Storage Delete
=======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
- deployment vast-csi/vast-csi-operator-controller-manager ready

Delete VastStorage
------------------
- namespace: vast-csi
- name: vast-nfs
- deleted
- wait for no VastStorage vast-csi/vast-nfs [timeout:60s]

Completed tasks
- VAST CSI storage deleted

OpenShift Workflow - VAST CSI Operator - Delete Cluster
=======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
- deployment vast-csi/vast-csi-operator-controller-manager ready

Delete VastCluster
------------------
- namespace: vast-csi
- name: my-vast
- deleted
- wait for no VastCluster vast-csi/my-vast [timeout:60s]

Completed tasks
- VAST CSI cluster deleted

OpenShift Workflow - VAST CSI Operator - Delete Driver
======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
- deployment vast-csi/vast-csi-operator-controller-manager ready

Delete VastCSIDriver
--------------------
- namespace: vast-csi
- name: nfs
- deleted
- wait for no VastCSIDriver vast-csi/nfs [timeout:60s]
- wait for no DaemonSet vast-csi/csi-vast-node [timeout:60s]
- wait for no Pod vast-csi/csi-vast-node-d8dp7 [timeout:60s]
- wait for no Pod vast-csi/csi-vast-node-ssdxv [timeout:60s]
- wait for no Pod vast-csi/csi-vast-node-wm6l7 [timeout:60s]
- wait for no Deployment vast-csi/csi-vast-controller [timeout:60s]
- wait for no ReplicaSet vast-csi/csi-vast-controller-6f6c599d8c [timeout:600s]
- wait for no Pod vast-csi/csi-vast-controller-6f6c599d8c-p946s [timeout:60s]

Completed tasks
- VAST CSI driver deleted

OpenShift Workflow - VAST CSI Operator - Delete Operator
========================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
- deployment vast-csi/vast-csi-operator-controller-manager ready

VAST CSI Custom Resources
- 0/0 VastCSIDriver
- 0/0 VastCluster
- 0/0 VastStorage
- 0/0 default StorageClass
- 0/0 PersistentVolumeClaim

Operator
- subscription          : vast-csi/vast-csi-operator
- package               : openshift-marketplace/certified-operators/vast-csi-operator
- channel               : stable
- install plan          : vast-csi/install-ffkkv
- install plan approved : V
- installed csv         : vast-csi-operator.v2.6.4
- latest_csv            : V


Delete Subscription
-------------------
- subscription: vast-csi/vast-csi-operator
- checking cluster service version...
- csv found and will be deleted: vast-csi/vast-csi-operator.v2.6.4
- wait for no subscription
- check cluster service version: vast-csi/vast-csi-operator.v2.6.4
- wait for no csv
- wait for no Deployment vast-csi/vast-csi-operator-controller-manager [timeout:180s]

Delete OperatorGroup
--------------------
- namespace: vast-csi
- name: vast-operator-group
- deleted
- wait for no OperatorGroup vast-csi/vast-operator-group [timeout:60s]

Namespace [vast-csi] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- no user defined networks
- no cluster user defined networks

Delete Namespace
----------------
- name: vast-csi
- wait for no namespace

Completed tasks
- Subscription deleted
- Operator Group deleted
- Namespace deleted

Completed tasks
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted

+----+---------+-------+-----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow        | Changes | Success | Duration [s] |
+----+---------+-------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | vast  | delete storage  | 1       | V       | 7            | 
| 2  | ocp:bm1 | vast  | delete cluster  | 1       | V       | 12           | 
| 3  | ocp:bm1 | vast  | delete driver   | 1       | V       | 45           | 
| 4  | ocp:bm1 | vast  | delete operator | 4       | V       | 24           | 
+----+---------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)