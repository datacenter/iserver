# NVIDIA GPU Operator - Create via Task

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
- [operator](./create_operator.md), [policy](./create_policy.md) and [dashboard](./create_dashboard.md) trigger workflow execution with optional input parameters
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies
- policy.filename is optional must contain ClusterPolicy CRD in YAML format, keep name to 'gpu-cluster-policy' value
  - the path defined in policy.filename can be relative and then expected to be in the same directory as task.json file
  - the path defined in policy.filename can be absolute

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

- gpu operator installed
- policy created
- dashboard crated

## Example

```
# iserver set ocp task --filename C:\tmp\task.json --no-confirm
OpenShift Cluster: bm1

Cluster: bm1 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - GPU Operator - Create Operator
===================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "channel": "__default__",
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


Create Namespace
----------------
- name: nvidia-gpu-operator
- labels
        openshift.io/cluster-monitoring:true

~~~
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: 'true'
  name: nvidia-gpu-operator

~~~

Namespace created

Wait for namespace [timeout:60]...

Check labels
- openshift.io/cluster-monitoring:true

Create Operator Group
---------------------
Operator group: nvidia-gpu-operator/gpu-operator-group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: gpu-operator-group
  namespace: nvidia-gpu-operator
spec:
  targetNamespaces:
  - nvidia-gpu-operator
  upgradeStrategy: Default

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: nvidia-gpu-operator/gpu-operator-certified
Source: openshift-marketplace/certified-operators/gpu-operator-certified
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: v25.3
- CSV [gpu-operator-certified.v25.3.4]
- CSV Display name [NVIDIA GPU Operator]
- CVS Version [25.3.4]
- CSV Provider [{'name': 'NVIDIA Corporation'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: gpu-operator-certified
  namespace: nvidia-gpu-operator
spec:
  channel: v25.3
  installPlanApproval: Automatic
  name: gpu-operator-certified
  source: certified-operators
  sourceNamespace: openshift-marketplace
  startingCSV: gpu-operator-certified.v25.3.4

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-t6sjj
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- nvidia-gpu-operator/gpu-operator

Completed tasks
- GPU Operator installed

OpenShift Workflow - GPU Operator - Create NVIDIA Cluster Policy
================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "policy": null,
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


Create NVIDIA Cluster Policy
----------------------------

~~~
apiVersion: nvidia.com/v1
kind: ClusterPolicy
metadata:
  name: gpu-cluster-policy
spec:
  daemonsets:
    rollingUpdate:
      maxUnavailable: '1'
    updateStrategy: RollingUpdate
  dcgm:
    enabled: true
  dcgmExporter:
    config:
      name: ''
    enabled: true
    serviceMonitor:
      enabled: true
  devicePlugin:
    config:
      default: ''
      name: ''
    enabled: true
    mps:
      root: /run/nvidia/mps
  driver:
    certConfig:
      name: ''
    enabled: true
    kernelModuleConfig:
      name: ''
    kernelModuleType: auto
    licensingConfig:
      configMapName: ''
      nlsEnabled: true
    repoConfig:
      configMapName: ''
    upgradePolicy:
      autoUpgrade: true
      drain:
        deleteEmptyDir: false
        enable: false
        force: false
        timeoutSeconds: 300
      maxParallelUpgrades: 1
      maxUnavailable: 25%
      podDeletion:
        deleteEmptyDir: false
        force: false
        timeoutSeconds: 300
      waitForCompletion:
        timeoutSeconds: 0
    useNvidiaDriverCRD: false
    virtualTopology:
      config: ''
  gdrcopy:
    enabled: false
  gds:
    enabled: false
  gfd:
    enabled: true
  mig:
    strategy: single
  migManager:
    enabled: true
  nodeStatusExporter:
    enabled: true
  operator:
    defaultRuntime: crio
    initContainer: {}
    use_ocp_driver_toolkit: true
  sandboxDevicePlugin:
    enabled: true
  sandboxWorkloads:
    defaultWorkload: container
    enabled: false
  toolkit:
    enabled: true
  validator:
    plugin:
      env: []
  vfioManager:
    enabled: true
  vgpuDeviceManager:
    enabled: true
  vgpuManager:
    enabled: false

~~~

Cluster policy created

Wait for cluster policy [timeout:60]...
Wait for cluster policy ready [timeout:180]...


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


Completed tasks
- NVIDIA Cluster Policy created

OpenShift Workflow - GPU Operator - Create DCGM Dashboard
=========================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
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


Monitoring dashboard source: https://github.com/NVIDIA/dcgm-exporter/raw/main/grafana/dcgm-exporter-dashboard.json

Dashboard content downloaded from url: https://github.com/NVIDIA/dcgm-exporter/raw/main/grafana/dcgm-exporter-dashboard.json
ConfigMap admin label: console.openshift.io/dashboard=true
Config map create with dashboard content: openshift-config-managed/nvidia-dcgm-exporter-dashboard

Completed tasks
- GPU Monitoring Dashboard created
```

[[Back]](./README.md)