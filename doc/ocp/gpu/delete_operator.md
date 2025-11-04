# NVIDIA GPU Operator - Delete Operator

## Workflow

- delete GPU operator subscription
- delete operator group
- delete namespace

## Requirements

Monitoring dashboard and cluster policy must not exist.

## Configurable options

```
# iserver delete ocp gpu --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp gpu --mode operator

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