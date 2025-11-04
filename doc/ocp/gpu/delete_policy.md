# NVIDIA GPU Operator - Delete Policy

## Workflow

Delete cluster policy object.

## Requirements

Monitoring dashboard must not exist.

## Configurable options

```
# iserver set ocp gpu --mode policy
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp gpu --mode policy

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
```

[[Back]](./README.md)