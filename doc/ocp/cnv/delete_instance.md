# Container Virtualization Operator - Delete Instance

## Workflow

- delete hyperconverged instance
- wait for resources gone

## Requirements

- no data volume can have associated pvc

## Configurable options

```
# iserver delete ocp cnv --mode instance
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp cnv --mode instance --cluster bm1

OpenShift Workflow - Container Virtualization Operator - Delete HyperConverged Instance
=======================================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-cnv",
    "name": "kubevirt-hyperconverged",
    "operator-group-name": "cnv-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

No ready data volumes found <=> virtualization subsystem is not using storage

Delete HyperConverged Instance
------------------------------
- namespace: openshift-cnv
- name: kubevirt-hyperconverged
- wait for no hyperconverged instance and resources

Completed tasks
- Hyperconverged instance deleted
```

[[Back]](./README.md)