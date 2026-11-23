# SR-IOV Network Operator - Delete Instance

## Workflow

- delete sriov operator configuration instance
- wait for resources gone

## Requirements

- no sriov network node policy may exist

## Configurable options

```
# iserver delete ocp sriov --mode instance
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp sriov --mode instance --cluster bm1


OpenShift Workflow - SRIOV Operator - Delete Instance
=====================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-sriov-network-operator",
    "name": "sriov-network-operator",
    "operator-group-name": "sriov-operator-group",
    "config": {
        "name": "default",
        "injector": true,
        "webhook": true
    },
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

SRIOV network operator installed
SRIOV operator configuration defined
No sriov network node policy found

Delete SRIOV Operator Config
----------------------------
- name: default

SRIOV operator config deleted

Wait for no sriov operator config [timeout:60]...
Wait for no sriov operator config resources...
Wait for deamon sets deleted...
- openshift-sriov-network-operator/network-resources-injector
- openshift-sriov-network-operator/operator-webhook
- openshift-sriov-network-operator/sriov-network-config-daemon

- SRIOV Operator configuration deleted
```

[[Back]](./README.md)