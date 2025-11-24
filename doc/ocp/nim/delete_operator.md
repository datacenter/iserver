# NVIDIA NIM Operator - Delete Operator

## Workflow

- delete operator subscription
- delete operator group
- delete namespace

## Requirements

None

## Configurable options

```
# iserver delete ocp nim --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp nim --cluster bm1

OpenShift Workflow - NVIDIA NIM Operator - Delete Operator
==========================================================

OpenShift Cluster: bm1

Delete Subscription
-------------------
- subscription: openshift-operators/nim-operator-certified
- checking cluster service version...
- csv found and will be deleted: openshift-operators/nim-operator-certified.v3.0.1
- wait for no subscription
- check cluster service version: openshift-operators/nim-operator-certified.v3.0.1
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-operators/k8s-nim-operator
Wait for pods deleted...

Completed tasks
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)