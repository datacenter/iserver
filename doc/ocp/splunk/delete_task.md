# Splunk Operator - Delete via Task

## Input

```
[
    {
        "splunk": {
            "operator": {
                "channel": "channel-name"
            },
            "instance": [
                {
                    "instance": "instance-name"
                }
            ]
        }
    }
]
```

Notes:
- [instance](./delete_instance.md) and [operator](./delete_operator.md) trigger workflow execution with optional input parameters
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
# iserver delete ocp task --file C:\tmp\task.json --cluster bm1             


OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Splunk Operator - Delete Instance
======================================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok


Delete splunk instance route
----------------------------
- instance namespace: splunk-operator
- instance name: s1
- route namespace: splunk-operator
- route name: splunk-s1-standalone-service

Route deleted

Delete Splunk Standalone Cluster
--------------------------------
- namespace: splunk-operator
- name: s1

Standalone cluster deleted

Wait for no pod splunk-operator/splunk-s1-standalone-0...
Wait for no standalone splunk-operator/s1...

+----+------------+-------+-----+-----+---------+-------+-----+
| ID | Standalone | Ready | Pod | PVC | Service | Route | URL |
+----+------------+-------+-----+-----+---------+-------+-----+
+----+------------+-------+-----+-----+---------+-------+-----+

Completed tasks
- Standalone instance deleted

OpenShift Workflow - Splunk Operator - Delete Instance
======================================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok


Delete splunk instance route
----------------------------
- instance namespace: splunk-operator
- instance name: s2
- route namespace: splunk-operator
- route name: splunk-s2-standalone-service

Route deleted

Delete Splunk Standalone Cluster
--------------------------------
- namespace: splunk-operator
- name: s2

Standalone cluster deleted

Wait for no pod splunk-operator/splunk-s2-standalone-0...
Wait for no standalone splunk-operator/s2...

+----+------------+-------+-----+-----+---------+-------+-----+
| ID | Standalone | Ready | Pod | PVC | Service | Route | URL |
+----+------------+-------+-----+-----+---------+-------+-----+
+----+------------+-------+-----+-----+---------+-------+-----+

Completed tasks
- Standalone instance deleted

OpenShift Workflow - Splunk Operator - Delete Operator
======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "splunk-operator",
    "name": "splunk-operator",
    "operator-group-name": "splunk-operator-group",
    "license-at-splunk": true,
    "role-binding": true,
    "role-binding-name": "system:openshift:scc:nonroot-v2",
    "pvc-finalizers": true,
    "delete-namespace": false
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok



Operator
--------
- subscription          : splunk-operator/splunk-operator
- package               : openshift-marketplace/certified-operators/splunk-operator
- channel               : stable
- install plan          : splunk-operator/install-qtr82
- install plan approved : ✓
- installed csv         : splunk-operator.v3.0.0
- latest_csv            : ✓


ClusterManager
--------------
- no resources found

ClusterMaster
-------------
- no resources found

IndexerCluster
--------------
- no resources found

LicenseManager
--------------
- no resources found

LicenseMaster
-------------
- no resources found

MonitoringConsole
-----------------
- no resources found

SearchHeadCluster
-----------------
- no resources found

Standalone
----------
- no resources found

Delete Subscription
-------------------
- subscription: splunk-operator/splunk-operator
- checking cluster service version...
- csv found and will be deleted: splunk-operator/splunk-operator.v3.0.0
- wait for no subscription
- check cluster service version: splunk-operator/splunk-operator.v3.0.0
- wait for no csv
Wait for deployments deleted (optional: True)...
- splunk-operator/splunk-operator-controller-manager

Delete OpenShift policy for Splunk operator
- namespace: splunk-operator
- name: system:openshift:scc:nonroot-v2
- deleted

Delete Operator Group
---------------------
- namespace: splunk-operator
- name: splunk-operator-group
- wait for no operator group

Completed tasks
- Splunk resources checked
- Subscription and csv deleted
- Role binding deleted
- Operator Group deleted
```

[[Back]](./README.md)