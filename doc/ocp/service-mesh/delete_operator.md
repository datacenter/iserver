# Service Mesh Operator - Delete Operator

## Workflow

- delete operator subscription
- wait for no resources

## Requirements

None

## Configurable options

```
# iserver delete ocp service-mesh --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp service-mesh --cluster bm1


OpenShift Workflow - Service Mesh Operator - Delete Operator
============================================================

OpenShift Cluster: bm1

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