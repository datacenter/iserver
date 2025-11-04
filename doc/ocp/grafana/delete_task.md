# Grafana Operator - Delete via Task

## Input

```
[
    {
        "grafana": {
            "operator": {},
            "mon": {},
            "instance": [
                ...
            ]
        }
    }
]
```

```
[
    {
        "grafana": {
            "operator": {},
            "mon": {},
            "wipe": {}
        }
    }
]
```

Notes:
- [instance](./delete_instance.md), [mon](./disable_monitoring.md) and [operator](./delete_operator.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters may be silently ignored
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies
- if you want to clean up setup, use "wipe" option in case some instances are not included in task
- "wipe" option in [create task](./create_task.md) will be ignored

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

## Expected Outcome

- grafana instance deleted
- all resources wiped
- monoring disabled
- operator deleted

## Example

```
[
    {
        "grafana": {
            "operator": {},
            "mon": {},
            "wipe": {}
        }
    }
]
```

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json 
OpenShift Cluster: bm1

Cluster: bm1 (type: ocp)

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Grafana Operator - Wipe Resources
======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "grafana-operator",
    "name": "grafana-operator",
    "operator-group-name": "grafana-operator-group",
    "mon-namespace": "openshift-monitoring",
    "mon-name": "cluster-monitoring-config",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Grafana
-------
- grafana-operator/testa
- grafana-operator/testb

GrafanaAlertRuleGroup
---------------------
- no resources found

GrafanaContactPoint
-------------------
- no resources found

GrafanaDashboard
----------------
- no resources found

GrafanaDatasource
-----------------
- grafana-operator/prometheus-testa
- grafana-operator/prometheus-testb

GrafanaFolder
-------------
- no resources found

GrafanaLibraryPanel
-------------------
- no resources found

GrafanaMuteTiming
-----------------
- no resources found

GrafanaNotificationPolicy
-------------------------
- no resources found

GrafanaNotificationPolicyRoute
------------------------------
- no resources found

GrafanaNotificationTemplate
---------------------------
- no resources found

Completed tasks
- Grafana resources deleted

OpenShift Workflow - Grafana Operator - Disable user-workload monitoring
========================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "grafana-operator",
    "name": "grafana-operator",
    "operator-group-name": "grafana-operator-group",
    "mon-namespace": "openshift-monitoring",
    "mon-name": "cluster-monitoring-config",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Config Map
----------
- namespace: openshift-monitoring
- name: cluster-monitoring-config
- found and will be checked
- enableUserWorkload value will be changed in config map
Config map udpated

Check for resources gone
------------------------
Wait for deployments deleted (optional: False)...
- openshift-user-workload-monitoring/prometheus-operator
Wait for stateful sets deleted (optional: False)...
- openshift-user-workload-monitoring/prometheus-user-workload
- openshift-user-workload-monitoring/thanos-ruler-user-workload


Completed tasks
---------------
- User workload monitoring disabled

OpenShift Workflow - Grafana Operator - Delete Operator
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "grafana-operator",
    "name": "grafana-operator",
    "operator-group-name": "grafana-operator-group",
    "mon-namespace": "openshift-monitoring",
    "mon-name": "cluster-monitoring-config",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Check Grafana resource
----------------------
- Grafana
- GrafanaAlertRuleGroup
- GrafanaContactPoint
- GrafanaDashboard
- GrafanaDatasource
- GrafanaFolder
- GrafanaLibraryPanel
- GrafanaMuteTiming
- GrafanaNotificationPolicy
- GrafanaNotificationPolicyRoute
- GrafanaNotificationTemplate

Delete Subscription
-------------------
- subscription: grafana-operator/grafana-operator
- checking cluster service version...
- csv found and will be deleted: grafana-operator/grafana-operator.v5.19.4
- wait for no subscription
- check cluster service version: grafana-operator/grafana-operator.v5.19.4
- wait for no csv
Wait for deployments deleted (optional: False)...
- grafana-operator/grafana-operator-controller-manager-v5

Delete Operator Group
---------------------
- namespace: grafana-operator
- name: grafana-operator-group
- wait for no operator group

Delete Namespace
----------------
- name: grafana-operator

Namespace [grafana-operator] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- Grafana Operator deleted
- Operator group deleted
- Namespace deleted
```

[[Back]](./README.md)