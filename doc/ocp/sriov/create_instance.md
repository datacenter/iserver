# SR-IOV Network Operator - Create Instance

## Workflow

- create sriov configuration instance based on default values
- wait for resources ready

## Requirements

- sriov operator must be [created](./create_operator.md)

## Expected Outcome

![InstanceCreate](../images/sriov/instance_create.png)

## Configurable options

```
# iserver set ocp sriov --mode instance
  --cluster TEXT                  Cluster Name
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver set ocp sriov --mode instance --cluster bm1 --no-confirm


OpenShift Workflow - SRIOV Operator - Create Instance
=====================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
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


Create SRIOV Operator Config
----------------------------
- namespace: openshift-sriov-network-operator
- name: default
- injector: True
- webhook: True

~~~
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: openshift-sriov-network-operator
spec:
  enableInjector: true
  enableOperatorWebhook: true
  logLevel: 2

~~~

SRIOV operator config created

Wait for operator config [timeout:60]...
Wait for operator config resources...
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-sriov-network-operator/sriov-network-operator
Wait for deamon sets ready...
- openshift-sriov-network-operator/network-resources-injector
- openshift-sriov-network-operator/operator-webhook
- openshift-sriov-network-operator/sriov-network-config-daemon

- SRIOV Operator configuration created
```

[[Back]](./README.md)