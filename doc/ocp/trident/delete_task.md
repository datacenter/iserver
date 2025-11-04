# Trident Operator - Delete via Task

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
- [operator](./delete_operator.md) trigger workflow execution with optional input parameters

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
        "trident": {
            "operator": {}
        }
    }
]
```

```
# iserver delete ocp task --file C:\tmp\task.json --cluster bm1             
OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Trident Operator - Delete Operator
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
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


Delete Subscription
-------------------
- subscription: openshift-operators/trident-operator
- checking cluster service version...
- csv found and will be deleted: openshift-operators/trident-operator.v25.6.2
- wait for no subscription
- check cluster service version: openshift-operators/trident-operator.v25.6.2
- wait for no csv
Wait for deployments deleted (optional: True)...
- openshift-operators/trident-operator

Completed tasks
- Trident operator deleted
```

[[Back]](./README.md)