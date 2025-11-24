# Serverless Operator - Delete Operator

## Workflow

- delete operator subscription
- delete operator group
- delete namespace

## Requirements

None

## Configurable options

```
# iserver delete ocp serverless --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp serverless --cluster bm1


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