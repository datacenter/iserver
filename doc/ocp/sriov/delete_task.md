# SR-IOV Network Operator - Delete via Task

## Input

```
[
    {
        "sriov": {
            "operator": {
                "channel": "xyz"
            },
            "instance": {}
        }
    }
]
```

Notes:
- [operator](./delete_operator.md) and [instance](./delete_instance.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters may be silently ignored
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

## Requirements

None

## Configurable options

```
# iserver delete ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
# iserver delete ocp task --file C:\tmp\task.json --cluster bm1             


OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


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

OpenShift Workflow - SRIOV - Delete Operator
============================================

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


Delete Subscription
-------------------
- subscription: openshift-sriov-network-operator/sriov-network-operator
- checking cluster service version...
- csv found and will be deleted: openshift-sriov-network-operator/sriov-network-operator.v4.18.0-202509240837
- wait for no subscription
- check cluster service version: openshift-sriov-network-operator/sriov-network-operator.v4.18.0-202509240837
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-sriov-network-operator/sriov-network-operator

Delete Operator Group
---------------------
- namespace: openshift-sriov-network-operator
- name: sriov-operator-group
- wait for no operator group

Delete PODs
-----------

Object filter
- namespace:openshift-sriov-network-operator

Delete
- sriov-network-operator-8674f96787-jp2gq
[ERROR] REST API failed

Delete Namespace
----------------
- name: openshift-sriov-network-operator

Namespace [openshift-sriov-network-operator] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- SRIOV Operator subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)