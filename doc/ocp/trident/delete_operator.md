# Trident Operator - Delete Operator

## Workflow

- delete trident operator subscription
- wait for resources deleted

## Requirements

None

## Configurable options

```
# iserver delete ocp trident --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp trident --mode operator --cluster bm1


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