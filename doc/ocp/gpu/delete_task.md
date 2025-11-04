# NVIDIA GPU Operator - Delete via Task

## Input

```
[
    {
        "gpu": {
            "operator": {
                "channel": "abc"
            },
            "policy": {
                "filename": "xyz"
            },
            "dashboard": {}
        }
    }
]
```

Notes:
- [dashboard](./delete_dashboard.md), [policy](./delete_policy.md) and [operator](./delete_operator.md) trigger workflow execution
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

## Expected Outcome

- policies deleted
- prometheus service monitors disabled
- gpu operator deleted

## Example

```
# iserver delete ocp task --file C:\tmp\task.json
OpenShift Cluster: bm1

Cluster: bm1 (type: ocp)

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - GPU Operator - Delete DCGM Dashboard
=========================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "nvidia-gpu-operator",
    "name": "gpu-operator-certified",
    "operator-group-name": "gpu-operator-group",
    "delete-namespace": true,
    "monitoring": {
        "dashboard_url": "https://github.com/NVIDIA/dcgm-exporter/raw/main/grafana/dcgm-exporter-dashboard.json",
        "dashboard_namespace": "openshift-config-managed",
        "dashboard_name": "nvidia-dcgm-exporter-dashboard",
        "admin": true,
        "developer": false
    }
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Delete Config Map
-----------------
- namespace: openshift-config-managed
- name: nvidia-dcgm-exporter-dashboard
- wait for no config map

Completed tasks
- GPU Monitoring Dashboard deleted

OpenShift Workflow - GPU Operator - Delete NVIDIA Cluster Policy
================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "nvidia-gpu-operator",
    "name": "gpu-operator-certified",
    "operator-group-name": "gpu-operator-group",
    "delete-namespace": true,
    "monitoring": {
        "dashboard_url": "https://github.com/NVIDIA/dcgm-exporter/raw/main/grafana/dcgm-exporter-dashboard.json",
        "dashboard_namespace": "openshift-config-managed",
        "dashboard_name": "nvidia-dcgm-exporter-dashboard",
        "admin": true,
        "developer": false
    }
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Delete Cluster Policy
---------------------
- name: gpu-cluster-policy
- wait for no cluster policy

Completed tasks
- NVIDIA Cluster Policy deleted

OpenShift Workflow - GPU Operator - Delete Operator
===================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "nvidia-gpu-operator",
    "name": "gpu-operator-certified",
    "operator-group-name": "gpu-operator-group",
    "delete-namespace": true,
    "monitoring": {
        "dashboard_url": "https://github.com/NVIDIA/dcgm-exporter/raw/main/grafana/dcgm-exporter-dashboard.json",
        "dashboard_namespace": "openshift-config-managed",
        "dashboard_name": "nvidia-dcgm-exporter-dashboard",
        "admin": true,
        "developer": false
    }
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

No nvidia cluster policy found

Delete Subscription
-------------------
- subscription: nvidia-gpu-operator/gpu-operator-certified
- checking cluster service version...
- csv found and will be deleted: nvidia-gpu-operator/gpu-operator-certified.v25.3.4
- wait for no subscription
- check cluster service version: nvidia-gpu-operator/gpu-operator-certified.v25.3.4
- wait for no csv
Wait for deployments deleted (optional: False)...
- nvidia-gpu-operator/gpu-operator

Delete Operator Group
---------------------
- namespace: nvidia-gpu-operator
- name: gpu-operator-group
- wait for no operator group

Delete Namespace
----------------
- name: nvidia-gpu-operator

Namespace [nvidia-gpu-operator] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- GPU Operator removed
```

[[Back]](./README.md)