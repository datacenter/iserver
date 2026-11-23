# Migration Toolkit for Virtualization - Create via Task

## Input

```
[
    {
        "mtv": {
            "operator": {},
            "instance": {},
            "provider": [
                {
                    "type": "vcenter",
                    "provider": "vc",
                    "url": "https://vc.domain.com/sdk",
                    "vddk": "image-registry.openshift-image-registry.svc:5000/openshift/vddk:latest",
                    "username": "Administrator",
                    "password": "password",
                    "ssl": false
                }
            ],
            "map": [
                {
                    "type": "network",
                    "map": "vc-nets",
                    "source": "vc",
                    "destination": "host",
                    "network": [
                        {
                            "source": "my-dvs1",
                            "destination": "pod"
                        }
                        
                    ]
                },
                {
                    "type": "storage",
                    "map": "vc-ds",
                    "source": "vc",
                    "destination": "host",
                    "storage": [
                        {
                            "source": "My-NAS",
                            "destination": "lvms-vg1"
                        }
                        
                    ]
                }
            ],
            "plan": [
                {
                    "plan": "mtv1",
                    "source": "vc",
                    "destination": "host",
                    "network": "vc-nets",
                    "storage": "vc-ds",
                    "vm": [
                        "usmall"
                    ],
                    "type": "cold",
                    "target": "default"
                }
            ],
            "migration": [
                {
                    "plan": "mtv1",
                    "action": "run"
                }
            ]
        }
    }
]
```

Notes:
- [operator](./create_operator.md), [instance](./create_instance.md), [provider](./create_provider.md), [network map](./create_network_map.md), [storage map](./create_storage_map.md), [plan](./create_plan.md) and [migration](./run_plan.md) trigger workflow execution with optional input parameters
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

```
# iserver set ocp task --filename C:\tmp\task.json --cluster bm1 --no-confirm

Cluster: bm1 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Migration Toolkit for Virtualization Operator - Create Operator
====================================================================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: openshift-mtv

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-mtv

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: openshift-mtv/mtv-operator-group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: mtv-operator-group
  namespace: openshift-mtv
spec:
  targetNamespaces:
  - openshift-mtv
  upgradeStrategy: Default

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: openshift-mtv/mtv-operator
Source: openshift-marketplace/redhat-operators/mtv-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: release-v2.10
- CSV [mtv-operator.v2.10.3]
- CSV Display name [Migration Toolkit for Virtualization Operator]
- CVS Version [2.10.3]
- CSV Provider [{'name': 'Red Hat'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: mtv-operator
  namespace: openshift-mtv
spec:
  channel: release-v2.10
  installPlanApproval: Automatic
  name: mtv-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-2xgt6
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-mtv/forklift-operator

Completed tasks
- Namespace created
- Operator Group created
- Mtv Operator installed

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Create Forklift Controller Instance
========================================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

Mtv Forklift Controller
- no instance found

Create Forklift Controller
--------------------------
- namespace: openshift-mtv
- name: forklift-controller

~~~
apiVersion: forklift.konveyor.io/v1beta1
kind: ForkliftController
metadata:
  name: forklift-controller
  namespace: openshift-mtv
spec:
  feature_ui_plugin: 'true'
  feature_validation: 'true'
  feature_volume_populator: 'true'

~~~

Forklift controller instance created

Wait for forklift controller instance...
Wait for forklift controller instance resources...
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-mtv/forklift-api
- openshift-mtv/forklift-cli-download
- openshift-mtv/forklift-controller
- openshift-mtv/forklift-ova-proxy
- openshift-mtv/forklift-ui-plugin
- openshift-mtv/forklift-validation
- openshift-mtv/forklift-volume-populator-controller
Wait for forklift controller instance ready state...

Completed tasks
- forklift controller instance created and ready

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Create vCenter Provider
============================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

Create vCenter Provider
-----------------------
- namespace: openshift-mtv
- name: vc
- vCenter: https://vc.domain.com/sdk (Administrator, password) ssl[False]
- vddk: image-registry.openshift-image-registry.svc:5000/openshift/vddk:latest

~~~
apiVersion: v1
data:
  insecureSkipVerify: ...
  password: ...
  url: ...
  user: ...
kind: Secret
metadata:
  name: vc
  namespace: openshift-mtv
type: Opaque

---
apiVersion: forklift.konveyor.io/v1beta1
kind: Provider
metadata:
  name: vc
  namespace: openshift-mtv
spec:
  secret:
    name: vc
    namespace: openshift-mtv
  settings:
    sdkEndpoint: vcenter
    vddkInitImage: image-registry.openshift-image-registry.svc:5000/openshift/vddk:latest
  type: vsphere
  url: https://vc.domain.com/sdk

~~~

Secret and provider created

Wait for provider...
Wait for provider ready state...

Completed tasks
- provider created and ready

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Create Network Map
=======================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

Create Network Map
------------------
- namespace: openshift-mtv
- name: vc-nets

~~~
apiVersion: forklift.konveyor.io/v1beta1
kind: NetworkMap
metadata:
  name: vc-nets
  namespace: openshift-mtv
spec:
  map:
  - destination:
      type: pod
    source:
      name: my-dvs
  provider:
    destination:
      apiVersion: forklift.konveyor.io/v1beta1
      kind: Provider
      name: host
      namespace: openshift-mtv
    source:
      apiVersion: forklift.konveyor.io/v1beta1
      kind: Provider
      name: vc
      namespace: openshift-mtv

~~~

Network map created

Wait for network map...
Wait for network map ready state...

Completed tasks
- network map created and ready

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Create Storage Map
=======================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

Create Storage Map
------------------
- namespace: openshift-mtv
- name: vc-ds

~~~
apiVersion: forklift.konveyor.io/v1beta1
kind: StorageMap
metadata:
  name: vc-ds
  namespace: openshift-mtv
spec:
  map:
  - destination:
      storageClass: lvms-vg1
    source:
      name: My-NAS
  provider:
    destination:
      apiVersion: forklift.konveyor.io/v1beta1
      kind: Provider
      name: host
      namespace: openshift-mtv
    source:
      apiVersion: forklift.konveyor.io/v1beta1
      kind: Provider
      name: vc
      namespace: openshift-mtv

~~~

Storage map created

Wait for storage map...
Wait for storage map ready state...

Completed tasks
- storage map created and ready

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Create Migration Plan
==========================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

Validation checks
- provider vc found
- provider host found
- network map vc-nets found
- storage map vc-ds found
- target namespace default found

Create Migration Plan
---------------------
- namespace: openshift-mtv
- name: mtv1

~~~
apiVersion: forklift.konveyor.io/v1beta1
kind: Plan
metadata:
  name: mtv1
  namespace: openshift-mtv
spec:
  map:
    network:
      name: vc-nets
      namespace: openshift-mtv
    storage:
      name: vc-ds
      namespace: openshift-mtv
  provider:
    destination:
      name: host
      namespace: openshift-mtv
    source:
      name: vc
      namespace: openshift-mtv
  targetNamespace: default
  type: cold
  vms:
  - name: usmall

~~~

Plan created

Wait for plan...
Wait for plan ready state...

+----+----------------+-------+------+-----+------+---------------+---------------+-----------+---------+
| ID | Migration Plan | State | Type | Src | Dest | Network       | Storage       | Source VM | Phase   |
+----+----------------+-------+------+-----+------+---------------+---------------+-----------+---------+
| 1  | openshift-mtv  | Ready | cold | vc  | host | openshift-mtv | openshift-mtv | usmall    | Pending | 
|    | mtv1           |       |      |     |      | vc-nets       | vc-ds         |           |         | 
+----+----------------+-------+------+-----+------+---------------+---------------+-----------+---------+

Completed tasks
- migration plan created and ready to run

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Run Migration
==================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

Start Migration
---------------
- namespace: openshift-mtv
- plan: mtv1
- migration: mtv1-aa5efd0b943f

~~~
apiVersion: forklift.konveyor.io/v1beta1
kind: Migration
metadata:
  name: mtv1-aa5efd0b943f
  namespace: openshift-mtv
spec:
  plan:
    name: mtv1
    namespace: openshift-mtv

~~~

Migration created

Wait for migration...
Wait for migration finished...
VM [usmall] Phase [WaitForPowerOff]
VM [usmall] Phase [CreateGuestConversionPod]
VM [usmall] PVC [default/mtv1-vm-61951-jmqs6] Capacity [None] Phase [Pending]
VM [usmall] DV [default/mtv1-vm-61951-jmqs6] Progress [N/A] Phase [PendingPopulation]
VM [usmall] Pod [default/mtv1-vm-61951-c4bhc] Phase [Pending]
VM [usmall] Phase [ConvertGuest]
VM [usmall] DV [default/mtv1-vm-61951-jmqs6] Progress [N/A] Phase [ImportInProgress]
VM [usmall] PVC [default/mtv1-vm-61951-jmqs6] Capacity [8Gi] Phase [Bound]
VM [usmall] DV [default/mtv1-vm-61951-jmqs6] Progress [100.0%] Phase [Succeeded]
VM [usmall] Pod [default/mtv1-vm-61951-c4bhc] Phase [Running]
VM [usmall] Phase [CopyDisksVirtV2V] Progress [0/8192 MB]
VM [usmall] Phase [CreateVM]
VM [usmall] Virtual Machine [default/usmall] State [Stopped]
VM [usmall] Pod [default/mtv1-vm-61951-c4bhc] Phase [Succeeded]
VM [usmall] Phase [Completed] Success

Completed tasks
- migration completed successfully
```

[[Back]](./README.md)