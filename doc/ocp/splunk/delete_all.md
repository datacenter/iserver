# Splunk Operator - Delete All

## Workflow

Workflows deployed in sequence
- [delete instance](./delete_instance.md)
- [delete operator](./delete_operator.md)

## Requirements

None

## Configurable options

```
# iserver delete ocp splunk --mode all
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp splunk --cluster bm1 --mode all


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
- install plan          : splunk-operator/install-t9dsg
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