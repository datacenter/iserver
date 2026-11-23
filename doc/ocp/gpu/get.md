# NVIDIA GPU Operator - Get Information

## Workflow

Check and show to the user information about
- gpu operator
- cluster policy
- monitoring dashboard

## Example

```
# iserver get ocp gpu --cluster bm1

OpenShift Workflow - GPU Operator - Get Information
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

Operator
--------
- subscription: nvidia-gpu-operator/gpu-operator-certified
- channel: v25.3
- csv: gpu-operator-certified.v25.3.4


NVIDIA Cluster Policy
---------------------
- Namespace             : nvidia-gpu-operator
- Name                  : gpu-cluster-policy
- State                 : ready
- DCGM                  : ✓
- DCGM Exporter         : ✓
- DCGM Service Monitor  : ✓
- Device Plugin         : ✓
- Driver                : ✓
- GDR Copy              : ✗
- GDS                   : ✗
- GFD                   : ✓
- Mig Strategy          : single
- Mig Manager           : ✓
- Node Status Exporter  : ✓
- Sandbox Device Plugin : ✓
- Toolkit               : ✓
- VFID Manager          : ✓
- vGPU Device Manager   : ✓
- vGPU Manager          : ✗


Operator
--------
Monitoring dashboard config map exists: openshift-config-managed/nvidia-dcgm-exporter-dashboard
```

[[Back]](./README.md)