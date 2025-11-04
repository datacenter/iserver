# Tetragon Enterprise Operator - Delete tetragon resources

## Workflow

Delete tetragon-related resources
- AlertRule
- SandboxPolicy
- SandboxPolicyNamespaced
- TetragonNetworkPolicy
- TetragonNetworkPolicyNamespaced
- TracingPolicy
- TracingPolicyNamespaced

## Requirements

Tetragon Enterprise operator installed

## Configurable options

```
# iserver delete ocp tetragon --mode wipe
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp tetragon --cluster bm1 --mode wipe

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
- no resources found

Tracing Policy Namespaced
-------------------------
- no resources found

Completed tasks
- Tetragon resources deleted
```

[[Back]](./README.md)