# Tetragon Enterprise Operator - Create All

## Workflow

Workflows deployed in sequence
- [create operator](./create_operator.md)
- [enable prometheus](./enable_prometheus.md) 
- [create crd](./crete_crd.md) if any defined

## Requirements

None

## Configurable options

```
# iserver set ocp tetrag --mode all
  --cluster TEXT                  Cluster Name
  --channel TEXT                  Operator channel  [default: __default__]
  --image TEXT                    Tetragon Enterprise Operator image
  --crd TEXT                      Tetragon policy directory or file
  --no-confirm                    Confirmation mode
```

## Expected Outcome

- tetragon operator installed
- user-workload monitoring enabled
- prometheus integration enabled
- tetragon crds applied

## Example

```
# iserver set ocp tetragon --crd my-crd-absolute-location --cluster bm1 --mode all --image image-name-as-provided-by-isovalent

OpenShift Workflow - Tetragon Operator - Create Operator
========================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "channel": "__default__",
    "image": "user-defined",
    "confirmation": true,
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
    "confirmation": true,
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
    "confirmation": true,
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
Deployment [tetragon/tetragon-operator] restarted
Wait for service monitors...
- tetragon/tetragon

Completed tasks
- Tetragon service monitors enabled

OpenShift Workflow - Tetragon Operator - Create Policy
======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": true,
    "crd": "user-defined",
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

~~~
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: upper-layers
spec:
  parser:
    burstExitGen:
      enable: true
      interval: 1000
    dns:
      enable: true
    http:
      enable: true
      http2: true
      selectors:
      - matchPorts:
        - 8080
        - 80
    icmp:
      enable: true
    interface:
      enable: true
      packet: true
    tcp:
      enable: true
      histogram:
        enable: true
        max: 50000
        min: 0
      statsInterval: 20
    udp:
      cgroup: true
      enable: true
      statsInterval: 20

~~~
Continue [Y/N]? y

Tracing policy created

Wait for tracing policy [timeout:60]...

Completed tasks
- CRDs applied
```

[[Back]](./README.md)