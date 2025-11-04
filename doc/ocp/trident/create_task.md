# Trident Operator - Create via Task

## Input

```
[
    {
        "trident": {
            "operator": {}
        }
    }
]
```

Notes:
- [operator](./create_operator.md) trigger workflow execution with optional input parameters

## Requirements

None

## Configurable options

```
# iserver set ocp task 
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
        "trident": {
            "operator": {}
        }
    }
]
```

```
# iserver set ocp task --filename C:\tmp\task.json --cluster bm1 --no-confirm

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Trident Operator - Create Operator
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": true,
    "channel": "stable",
    "check-verbose": true,
    "namespace": "openshift-operators",
    "name": "trident-operator",
    "operator-group-name": "global-operators",
    "catalog": "certified-operators"
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok


Create Subscription
-------------------
Subscription: openshift-operators/trident-operator
Source: openshift-marketplace/certified-operators/trident-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Channel: stable
- CSV [trident-operator.v25.6.2]
- CSV Display name [NetApp Trident]
- CVS Version [25.6.2]
- CSV Provider [{'name': 'NetApp, Inc.', 'url': 'https://www.netapp.com/'}]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: trident-operator
  namespace: openshift-operators
spec:
  channel: stable
  installPlanApproval: Automatic
  name: trident-operator
  source: certified-operators
  sourceNamespace: openshift-marketplace

~~~
Continue [Y/N]? y

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-2576b
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-operators/trident-operator

Completed tasks
- Trident Operator installed
```

[[Back]](./README.md)