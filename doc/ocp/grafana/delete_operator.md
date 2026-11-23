# Grafana Operator - Delete Operator

## Workflow

- delete grafana operator subscription
- delete operator group
- delete namespace

## Requirements

No Grafana CRD may exist
- GrafanaAlertRuleGroup
- GrafanaContactPoint
- GrafanaFolder
- GrafanaLibraryPanel
- GrafanaMuteTiming
- GrafanaNotificationPolicy
- GrafanaNotificationPolicyRoute
- GrafanaNotificationTemplate

## Configurable options

```
# iserver delete ocp grafana --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp grafana --mode operator --cluster bm1

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