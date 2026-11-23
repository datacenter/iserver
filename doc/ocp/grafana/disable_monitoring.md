# Grafana Operator - Disable user-workload monitoring

## Workflow

- check config map in openshift-monitoring namespace that enables user workload monitoring and update it
- wait for resources to be gone

## Requirements

None

## Configurable options

```
# iserver delete ocp grafana --mode mon
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp grafana --mode mon --cluster bm1

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
```

[[Back]](./README.md)