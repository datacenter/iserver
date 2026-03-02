# VAST Operator - Delete via Task

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

## Requirements

None

## Configurable options

```
# iserver delete ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
# iserver delete ocp task --cluster bm1 --file C:\tmp\task.json  --no-confirm

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - VAST CSI Operator - Delete Storage
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

Delete VastStorage
------------------
- namespace: vast-csi
- name: vast-nfs
- deleted
- wait for no VastStorage vast-csi/vast-nfs [timeout:60s]

Completed tasks
- VAST CSI storage deleted

OpenShift Workflow - VAST CSI Operator - Delete Storage
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

Delete VastStorage
------------------
- namespace: vast-csi
- name: vast-block
- deleted
- wait for no VastStorage vast-csi/vast-block [timeout:60s]

Completed tasks
- VAST CSI storage deleted

OpenShift Workflow - VAST CSI Operator - Delete Cluster
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
------------------------------
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
---------------------------
- deployment vast-csi/vast-csi-operator-controller-manager ready

Delete VastCSIDriver
--------------------
- namespace: vast-csi
- name: nfs
- deleted
- wait for no VastCSIDriver vast-csi/nfs [timeout:60s]
- wait for no DaemonSet vast-csi/csi-vast-node [timeout:60s]
- wait for no Deployment vast-csi/csi-vast-controller [timeout:60s]

Completed tasks
- VAST CSI driver deleted

OpenShift Workflow - VAST CSI Operator - Delete Driver
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

Delete VastCSIDriver
--------------------
- namespace: vast-csi
- name: block
- deleted
- wait for no VastCSIDriver vast-csi/block [timeout:60s]
- wait for no DaemonSet vast-csi/block-vast-node [timeout:60s]
- wait for no Deployment vast-csi/block-vast-controller [timeout:60s]

Completed tasks
- VAST CSI driver deleted

OpenShift Workflow - VAST CSI Operator - Delete Operator
========================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
------------------------------
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
---------------------------
- deployment vast-csi/vast-csi-operator-controller-manager ready
- 0 driver
- 0 cluster
- 0 storage
- 0 storage class
- 0 pvc

Delete Subscription
-------------------
- subscription: vast-csi/vast-csi-operator
- checking cluster service version...
- csv found and will be deleted: vast-csi/vast-csi-operator.v2.6.4
- wait for no subscription
- check cluster service version: vast-csi/vast-csi-operator.v2.6.4
- wait for no csv
Wait for deployments deleted (optional: False)...
- vast-csi/vast-csi-operator-controller-manager

Delete Operator Group
---------------------
- namespace: vast-csi
- name: vast-operator-group
- wait for no operator group
Wait no pod vast-csi/block-vast-controller-74ff4df6bc-ztmp7
Wait no pod vast-csi/block-vast-node-5glcv
Wait no pod vast-csi/block-vast-node-gdn7p
Wait no pod vast-csi/block-vast-node-r8gvp
Wait no pod vast-csi/csi-vast-controller-6f6c599d8c-j29cw
Wait no pod vast-csi/csi-vast-node-694f9
Wait no pod vast-csi/csi-vast-node-fcgkt
Wait no pod vast-csi/csi-vast-node-pc8gb

Delete Namespace
----------------
- name: vast-csi

Namespace [vast-csi] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)