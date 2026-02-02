# Migration Toolkit for Virtualization - Delete via Task

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
- [operator](./delete_operator.md), [instance](./delete_instance.md), [provider](./delete_provider.md), [network map](./delete_network_map.md), [storage map](./delete_storage_map.md) and [plan](./delete_plan.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters may be silently ignored
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

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
# iserver delete ocp task --filename C:\tmp\task.json --cluster bm1 --no-confirm


OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Migraton Plan
=========================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

+----+----------------+-----------+------+-----+------+---------------+------------------------------------+-----------+-----------+
| ID | Migration Plan | State     | Type | Src | Dest | Network       | Storage                            | Source VM | Phase     |
+----+----------------+-----------+------+-----+------+---------------+------------------------------------+-----------+-----------+
| 1  | openshift-mtv  | Completed | cold | vc  | host | openshift-mtv | openshift-mtv                      | usmall    | Completed | 
|    | mtv1           |           |      |     |      | vc-nets       | vc-ds                              |           |           | 
|    |                |           |      |     |      | my-dvs => pod | My-NAS => lvms-vg1                 |           |           | 
+----+----------------+-----------+------+-----+------+---------------+------------------------------------+-----------+-----------+

Delete Migration Plan
---------------------
- namespace: openshift-mtv
- name: mtv1
- state: Completed

~~~
apiVersion: forklift.konveyor.io/v1beta1
kind: Plan
metadata:
  name: mtv1
  namespace: openshift-mtv
spec:
  archived: true

~~~

Migration plan patched
Wait for plan archived...

Migration plan deleted
Wait for migration plan gone

Completed tasks
- selected migration plans archived and deleted

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Network Map
=======================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

+----+---------------+-------+--------+---------+-------------+---------+--------+------+
| ID | Network Map   | Owner | Source | Network | Destination | Network | Status | Plan |
+----+---------------+-------+--------+---------+-------------+---------+--------+------+
| 1  | openshift-mtv | ---   | vc     | my-dvs  | host        | pod     | Ready  | ---  | 
|    | vc-nets       |       |        |         |             |         |        |      | 
+----+---------------+-------+--------+---------+-------------+---------+--------+------+

Delete Network Map
------------------
- namespace: openshift-mtv
- name: vc-nets

Network map deleted

Wait for no network map...

Completed tasks
- selected network maps deleted

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Storage Map
=======================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

+----+---------------+-------+--------+------------------------+-------------+----------+--------+------+
| ID | Storage Map   | Owner | Source | Storage                | Destination | Storage  | Status | Plan |
+----+---------------+-------+--------+------------------------+-------------+----------+--------+------+
| 1  | openshift-mtv | ---   | vc     | My-NAS                 | host        | lvms-vg1 | Ready  | ---  | 
|    | vc-ds         |       |        |                        |             |          |        |      | 
+----+---------------+-------+--------+------------------------+-------------+----------+--------+------+

Delete Storage Map
------------------
- namespace: openshift-mtv
- name: vc-ds

Storage map deleted

Wait for no storage map...

Completed tasks
- selected storage maps deleted

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Provider
====================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

+----+----------+---------+--------+----------------------------------+-------------+-------------+------+
| ID | Provider | Type    | Status | Endpoint                         | Network Map | Storage Map | Plan |
+----+----------+---------+--------+----------------------------------+-------------+-------------+------+
| 1  | vc       | vsphere | Ready  | https://vc.domain.com/sdk        | 0/0         | 0/0         | 0/0  | 
+----+----------+---------+--------+----------------------------------+-------------+-------------+------+

Delete Provider
---------------
- namespace: openshift-mtv
- name: vc

Provider and secret deleted

Wait for no provider...

Completed tasks
- selected providers deleted

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Forklift Controller Instance
========================================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

No providers found

No network maps found

No storage maps found

No migration plans

No migrations


Delete Forklift Controller
--------------------------
- namespace: openshift-mtv
- name: forklift-controller

Forklift controller instance deleted

Wait for no forklift controller instance...
Wait for no forklift controller instance resources...
Wait for deployments deleted (optional: False)...
- openshift-mtv/forklift-api
- openshift-mtv/forklift-cli-download
- openshift-mtv/forklift-controller
- openshift-mtv/forklift-ova-proxy
- openshift-mtv/forklift-ui-plugin
- openshift-mtv/forklift-validation
- openshift-mtv/forklift-volume-populator-controller

Completed tasks
- forklift controller instance deleted

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Operator
====================================================================================

OpenShift Cluster: bm1

No providers found

No network maps found

No storage maps found

No migration plans

No migrations


Delete Subscription
-------------------
- subscription: openshift-mtv/mtv-operator
- checking cluster service version...
- csv found and will be deleted: openshift-mtv/mtv-operator.v2.10.3
- wait for no subscription
- check cluster service version: openshift-mtv/mtv-operator.v2.10.3
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-mtv/forklift-operator

Delete Operator Group
---------------------
- namespace: openshift-mtv
- name: mtv-operator-group
- wait for no operator group

Delete Namespace
----------------
- name: openshift-mtv

Namespace [openshift-mtv] resources
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