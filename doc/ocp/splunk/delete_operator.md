# Splunk Operator - Delete Operator

## Workflow

- delete splunk operator subscription
- wait for resources deleted
- delete operator group
- delete namespace

## Requirements

No Splunk CRD may exist
- ClusterManager
- ClusterMaster
- IndexerCluster
- LicenseManager
- LicenseMaster
- MonitoringConsole
- SearchHeadCluster
- Standalone

## Configurable options

```
# iserver delete ocp splunk --mode operator
  --cluster TEXT                  Cluster Name
```

## Non-configurable defaults

```
{
    "namespace": "splunk-operator",
    "name": "splunk-operator",
    "operator-group-name": "splunk-operator-group",
    "delete-namespace": true
}
```

## Example

```
# iserver delete ocp splunk --mode operator --cluster bm1

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
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


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

Delete Operator Group
---------------------
- namespace: splunk-operator
- name: splunk-operator-group
- wait for no operator group

Delete Namespace
----------------
- name: splunk-operator

Namespace [splunk-operator] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- Splunk resources checked
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)