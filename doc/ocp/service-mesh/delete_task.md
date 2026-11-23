# Service Mesh Operator - Delete via Task

## Input

```
[
    {
        "service-mesh": {
            "operator": {
                "channel": "__default__"
            }
        }
    }
]
```

Notes:
- [operator](./delete_operator.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters may be silently ignored

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


OpenShift Workflow - Service Mesh Operator - Delete Operator
============================================================

OpenShift Cluster: bm3

Delete Subscription
-------------------
- subscription: openshift-operators/servicemeshoperator3
- checking cluster service version...
- csv found and will be deleted: openshift-operators/servicemeshoperator3.v3.2.0
- wait for no subscription
- check cluster service version: openshift-operators/servicemeshoperator3.v3.2.0
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-operators/servicemesh-operator3
Wait for pods deleted...

Completed tasks
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)