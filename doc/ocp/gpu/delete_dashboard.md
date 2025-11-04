# NVIDIA GPU Operator - Delete monitoring dashboard

## Workflow

Delete GPU monitoring dashboard that is stored in Config Map object.

## Requirements

None

## Configurable options

```
# iserver delete ocp gpu --mode dashboard
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp gpu --mode dashboard

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
```

[[Back]](./README.md)