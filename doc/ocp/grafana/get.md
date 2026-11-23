# Grafana Operator - Get Information

## Workflow

Check and show to the user information about grafana operator

## Example

```
# iserver get ocp grafana --cluster bm1

OpenShift Workflow - Splunk Operator - Get Information
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

Operator
--------
- subscription: grafana-operator/grafana-operator
- channel: v5
- csv: grafana-operator.v5.19.4
```

[[Back]](./README.md)