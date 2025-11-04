# Tetragon Enterprise Operator - Create Policy

## Workflow

- create tetragon crds from user-provided locations
- multiple locations can be defined, each can be filename or directory

## Requirements

- Tetragon Enterprise operator must be installed
- directory is expected to have files (no subdirectories)
- files or files in directory must be yaml with Tetragon CRD

## Configurable options

```
# iserver set ocp tetragon --mode crd
  --cluster TEXT            Cluster Name
  --crd TEXT                Tetragon policy directory or file
  --no-confirm              Confirmation mode
```

## Example

```
# iserver set ocp tetragon --mode crd --cluster bm1 --crd my-crd-absolute-location

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