# Serverless Operator - Delete via Task

## Input

```
[
    {
        "serverless": {
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


OpenShift Workflow - Serverless Operator - Delete Operator
==========================================================

OpenShift Cluster: bm1

Delete Subscription
-------------------
- subscription: openshift-serverless/serverless-operator
- checking cluster service version...
- csv found and will be deleted: openshift-serverless/serverless-operator.v1.36.1
- wait for no subscription
- check cluster service version: openshift-serverless/serverless-operator.v1.36.1
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-serverless/knative-openshift
- openshift-serverless/knative-openshift-ingress
- openshift-serverless/knative-operator-webhook
Wait for pods deleted...
- openshift-serverless/knative-openshift-7dd8dd6787-s47zr
- openshift-serverless/knative-openshift-ingress-9f488465c-sbs8h
- openshift-serverless/knative-operator-webhook-6868ccb55c-89d6l

Delete Operator Group
---------------------
- namespace: openshift-serverless
- name: serverless-operator-group
- wait for no operator group

Delete Namespace
----------------
- name: openshift-serverless

Namespace [openshift-serverless] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)