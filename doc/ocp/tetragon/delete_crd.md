# Tetragon Enterprise Operator - Delete Policy

## Workflow

- delete tetragon crds from user-provided locations
- multiple locations can be defined, each can be filename or directory

## Requirements

- Tetragon Enterprise operator must be installed
- directory is expected to have files (no subdirectories)
- files or files in directory must be yaml with Tetragon CRD

## Configurable options

```
# iserver delete ocp tetragon --mode crd
  --cluster TEXT            Cluster Name
  --crd TEXT                Tetragon policy directory or file
```

## Example

```
# iserver delete ocp tetragon --mode crd --cluster bm1 --crd my-crd-absolute-location

OpenShift Workflow - Tetragon Operator - Delete Policy
======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
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


Delete Tracing Policy
---------------------
- name: upper-layers
- wait for no tracing policy

Completed tasks
- CRDs deleted
```

[[Back]](./README.md)