# Grafana Operator - Delete grafana resources

## Workflow

Delete grafana-related resources
- GrafanaAlertRuleGroup
- GrafanaContactPoint
- GrafanaFolder
- GrafanaLibraryPanel
- GrafanaMuteTiming
- GrafanaNotificationPolicy
- GrafanaNotificationPolicyRoute
- GrafanaNotificationTemplate

## Requirements

Grafana operator installed

## Configurable options

```
# iserver delete ocp grafana --mode wipe
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp grafana --mode wipe

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
- no resources found

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
- grafana-operator/prometheus-test

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
```

[[Back]](./README.md)