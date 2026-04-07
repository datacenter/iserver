# NMState Operator - Delete via Task

[[Back]](./README.md)

## Input

```
[
    {
        "nmstate": {
            "operator": {}
        }
    }
]
```

Notes:
- [operator](./delete_operator.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters e.g. filename or workflows e.g. lldp are silently ignored

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
[
    {
        "nmstate": {
            "operator": {}
        }
    }
]
```

```
# iserver delete ocp task --file C:\tmp\task.json --cluster bm1             
OpenShift Cluster: bm1

Cluster: bm1 (type: ocp)

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - NMState Operator - Delete Operator
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-nmstate",
    "name": "kubernetes-nmstate-operator",
    "operator-group-name": "nmstate-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Delete Node Network Configuration Policies
------------------------------------------
- no nncp found

Delete NMState Instance
-----------------------
- wait for no nmstate instance

Delete Subscription
-------------------
- subscription: openshift-nmstate/kubernetes-nmstate-operator
- checking cluster service version...
- csv found and will be deleted: openshift-nmstate/kubernetes-nmstate-operator.4.18.0-202509241752
- wait for no subscription
- check cluster service version: openshift-nmstate/kubernetes-nmstate-operator.4.18.0-202509241752
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-nmstate/nmstate-console-plugin
- openshift-nmstate/nmstate-operator
- openshift-nmstate/nmstate-webhook

Delete Operator Group
---------------------
- namespace: openshift-nmstate
- name: kubernetes-nmstate-operator
- already deleted

Delete Namespace
----------------
- name: openshift-nmstate

Namespace [openshift-nmstate] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- NMState resources deleted
- NMState operator unconfigured and deleted
```

[[Back]](./README.md)