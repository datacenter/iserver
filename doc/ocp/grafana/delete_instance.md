# Grafana Operator - Delete instance

## Workflow

- delete data source (if any)
- delete cluster role binding (if any)
- delete grafana instance
- wait until resources are gone

## Requirements

Grafana operator installed
Grafana instance defined

## Configurable options

```
# iserver delete ocp grafana --mode instance
  --cluster TEXT                  Cluster Name
  --instance TEXT                 Grafana instance name
```

## Example

```
# iserver delete ocp grafana --mode instance --cluster bm1 --instance test

OpenShift Workflow - Grafana Operator - Delete instance
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "instance": "test",
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


Grafana Data Source
-------------------
- delete prometheus-test

Cluster Role Binding
--------------------
Service Account [test-sa] associated with role [cluster-monitoring-view] in ClusterRoleBinding CR [test-sa-view]
Delete ClusterRoleBinding CR [test-sa-view]

Delete Grafana Instance
-----------------------
- namespace: grafana-operator
- name: grafana-operator
Wait until grafana gone [timeout:60s]...
Wait until grafana resources are gone [timeout:60s]...
Wait for deployments deleted (optional: False)...
- grafana-operator/test-deployment
Wait for no service account...


Completed tasks
---------------
- Grafana instance deleted
```

[[Back]](./README.md)