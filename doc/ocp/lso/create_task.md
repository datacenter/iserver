# Local Storage Operator - Create via Task

## Input

```
[
    {
        "lso": {
            "operator": {},
            "volume": {
                "sc": "local-sc",
                "device": ["bm1-1:wwn-0x500a075118ef25c1", "bm1-2:wwn-0x500a075118ef266c"],
                "volume": "block",
                "max": 2,
                "limit": ["type:disk"]
            }
        }
    }
]
```

Notes:
- [operator](./create_operator.md) and [volume](./create_volume.md) trigger workflow execution with optional input parameters
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

With task input as above

```
# iserver set ocp task --cluster bm1 --file C:\tmp\task.json --no-confirm
OpenShift Cluster: bm1

Cluster: bm1 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Local Storage Operator - Create Operator
=============================================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: openshift-local-storage

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-local-storage

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: openshift-local-storage/local-operator-group
Target namespaces: openshift-local-storage

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: local-operator-group
  namespace: openshift-local-storage
spec:
  targetNamespaces:
  - openshift-local-storage

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: openshift-local-storage/local-storage-operator
Source: openshift-marketplace/redhat-operators/local-storage-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Channel: stable
- CSV [local-storage-operator.v4.18.0-202509240837]
- CSV Display name [Local Storage]
- CVS Version [4.18.0-202509240837]
- CSV Provider [{'name': 'Red Hat'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: local-storage-operator
  namespace: openshift-local-storage
spec:
  channel: stable
  installPlanApproval: Automatic
  name: local-storage-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-t9xhv
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: False, allow zero replicas: False)...
- openshift-local-storage/local-storage-operator

Completed tasks
- Namespace created
- Operator Group created
- Local Storage Operator installed

OpenShift Workflow - Local Storage Operator - Create Local Volume
=================================================================

OpenShift Cluster: bm1

Local Storage Operator
----------------------
- namespace: openshift-local-storage/local-storage-operator
- package: local-storage-operator
- csv: local-storage-operator.v4.18.0-202509240837

Collect cluster state and validate input values
-----------------------------------------------
- get kubernetes node names
- get linux level block devices for all nodes
- get local volumes
- get local volume sets
- get local volume discovery
- detected volume create mode: explicit
- state and values verified

Label Nodes
-----------
- node label: cluster.ocs.openshift.io/openshift-storage=""
- node: bm1-1
- node: bm1-2

Create Local Volume
-------------------
- namespace: openshift-local-storage
- name: local-disks-20b59c6289fd
- nodes: bm1-1
- device paths: /dev/disk/by-id/wwn-0x500a075118ef25c1
- volume mode: block
- storage class: local-sc

~~~
apiVersion: local.storage.openshift.io/v1
kind: LocalVolume
metadata:
  name: local-disks-20b59c6289fd
  namespace: openshift-local-storage
spec:
  nodeSelector:
    nodeSelectorTerms:
    - matchExpressions:
      - key: kubernetes.io/hostname
        operator: In
        values:
        - bm1-1
  storageClassDevices:
  - devicePaths:
    - /dev/disk/by-id/wwn-0x500a075118ef25c1
    forceWipeDevicesAndDestroyAllData: false
    storageClassName: local-sc
    volumeMode: Block

~~~

- Local volume created

- wait for LocalVolume crd [timeout:60]...
- wait for persistent volumes [timeout:180]...

Create Local Volume
-------------------
- namespace: openshift-local-storage
- name: local-disks-3e6f21e12e8d
- nodes: bm1-2
- device paths: /dev/disk/by-id/wwn-0x500a075118ef266c
- volume mode: block
- storage class: local-sc

~~~
apiVersion: local.storage.openshift.io/v1
kind: LocalVolume
metadata:
  name: local-disks-3e6f21e12e8d
  namespace: openshift-local-storage
spec:
  nodeSelector:
    nodeSelectorTerms:
    - matchExpressions:
      - key: kubernetes.io/hostname
        operator: In
        values:
        - bm1-2
  storageClassDevices:
  - devicePaths:
    - /dev/disk/by-id/wwn-0x500a075118ef266c
    forceWipeDevicesAndDestroyAllData: false
    storageClassName: local-sc
    volumeMode: Block

~~~

- Local volume created

- wait for LocalVolume crd [timeout:60]...
- wait for persistent volumes [timeout:180]...

+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+------+
| Name              | Status    | Mode  | SC       | Size  | Access Mode   | CSI Driver  | CSI Handle               | Device                         | PVC | Age  |
+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+------+
| local-pv-bf5ba6b4 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-20b59c6289fd | wwn-0x500a075118ef25c1 [bm1-1] | --  | 2h0m |
| local-pv-c6bf5067 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-3e6f21e12e8d | wwn-0x500a075118ef266c [bm1-2] | --  | 2h0m |
+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+------+

Completed tasks
- Volumes created
```

[Back](./README.md)