# Tetragon Operator - Create via Task

## Input

```
[
    {
        "tetragon": {
            "operator": {
                "image": "image-name-as-provided-by-isovalent"
            },
            "prometheus": {},
            "wipe": {},
            "crd": {
                "crd": [
                  "filename-or-directory"
                ]
            }
        }
    }
]
```

Notes:
- [operator](./create_operator.md), [prometheus](./enable_prometheus.md), [wipe](./delete_wipe.md) and [crd](./create_crd.md) trigger workflow execution with optional input parameters
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies
- tasks exeucition order

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Expected Outcome

- tetragon operator installed
- prometheus service monitors enabled
- policies applied

## Example

```
python.exe .\iserver.py set ocp task --filename C:\tmp\task.json --cluster bm1 --no-confirm
Cluster: bm1 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Tetragon Operator - Create Operator
========================================================

Workflow Parameters
-------------------
{
    "image": "user-defined",
    "cluster": "bm1",
    "confirmation": false,
    "channel": "__default__",
    "check-verbose": true,
    "namespace": "tetragon",
    "name": "tetragon-operator",
    "operator-group-name": "tetragon",
    "catalog-namespace": "tetragon",
    "catalog-name": "tetragon-catalog",
    "operator-cm-namespace": "tetragon",
    "operator-cm-name": "tetragon-operator-config",
    "cm-namespace": "tetragon",
    "cm-name": "tetragon-config",
    "sm-namespace": "tetragon",
    "sm-name": "tetragon",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

Tetragon Operator already created

OpenShift Workflow - Grafana Operator - Enable user-workload monitoring
=======================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
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
- enableUserWorkload already enabled

Check for resources
-------------------
Wait for deployments ready (optional: False, allow zero replicas: False)...
- openshift-user-workload-monitoring/prometheus-operator
Wait for stateful sets ready...
- openshift-user-workload-monitoring/prometheus-user-workload
- openshift-user-workload-monitoring/thanos-ruler-user-workload


Completed tasks
---------------
- User workload monitoring enabled

OpenShift Workflow - Tetragon Operator - Enable Prometheus Service Monitor
==========================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "check-verbose": true,
    "namespace": "tetragon",
    "name": "tetragon-operator",
    "operator-group-name": "tetragon",
    "catalog-namespace": "tetragon",
    "catalog-name": "tetragon-catalog",
    "operator-cm-namespace": "tetragon",
    "operator-cm-name": "tetragon-operator-config",
    "cm-namespace": "tetragon",
    "cm-name": "tetragon-config",
    "sm-namespace": "tetragon",
    "sm-name": "tetragon",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

Config map [tetragon/tetragon-operator-config] found
agentDaemonSet found in config map data
serviceMonitorEnabled already set to true

Completed tasks
- Tetragon service monitors enabled

OpenShift Workflow - Tetragon Operator - Wipe Resources
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "tetragon",
    "name": "tetragon-operator",
    "operator-group-name": "tetragon",
    "catalog-namespace": "tetragon",
    "catalog-name": "tetragon-catalog",
    "operator-cm-namespace": "tetragon",
    "operator-cm-name": "tetragon-operator-config",
    "cm-namespace": "tetragon",
    "cm-name": "tetragon-config",
    "sm-namespace": "tetragon",
    "sm-name": "tetragon",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Alert Rule
----------
- no resources found

Sandbox Policy
--------------
- no resources found

Sandbox Policy Namespaced
-------------------------
- no resources found

Tetragon Network Policy
-----------------------
- no resources found

Tetragon Network Policy Namespaced
----------------------------------
- no resources found

Tracing Policy
--------------
- upper-layers

Tracing Policy Namespaced
-------------------------
- no resources found

Completed tasks
- Tetragon resources deleted

OpenShift Workflow - Tetragon Operator - Create Policy
======================================================

Workflow Parameters
-------------------
{
    "crd": "user-defined",
    "cluster": "bm1",
    "confirmation": false,
    "check-verbose": true,
    "namespace": "tetragon",
    "name": "tetragon-operator",
    "operator-group-name": "tetragon",
    "catalog-namespace": "tetragon",
    "catalog-name": "tetragon-catalog",
    "operator-cm-namespace": "tetragon",
    "operator-cm-name": "tetragon-operator-config",
    "cm-namespace": "tetragon",
    "cm-name": "tetragon-config",
    "sm-namespace": "tetragon",
    "sm-name": "tetragon",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Create Tracing Policy
---------------------
- name: upper-layers

Tracing policy created

Wait for tracing policy [timeout:60]...

Completed tasks
- CRDs applied
```

[[Back]](./README.md)