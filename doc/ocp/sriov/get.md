# SR-IOV Network Operator - Get

## Workflow

- get sriov operator state
- get sriov operator configuration

## Example

```
# iserver get ocp sriov --cluster bm1


OpenShift Workflow - SRIOV Operator - Get Information
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

Operator
--------
- subscription: openshift-sriov-network-operator/sriov-network-operator
- channel: stable
- csv: sriov-network-operator.v4.18.0-202509240837

SRIOV operator configuration
----------------------------
- namespace: openshift-sriov-network-operator
- name: default

~~~
{
    "enableInjector": true,
    "enableOperatorWebhook": true,
    "logLevel": 2
}
~~~
```

[[Back]](./README.md)