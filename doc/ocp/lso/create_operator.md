# Local Storage - Create Operator

[[Back]](./README.md)

## Workflow

- create `openshift-local-storage` namespace
- create operator group
- create subscription

LSO by default selects only the worker nodes for local disk resources and local volumes creation i.e., management and infrastructure node are excluded
- in case of Single Node OpenShift (SNO) deployment, the `openshift-local-storage` namespace is automatically annotated with `workload.openshift.io/allowed:management` to allow LSO to run on the management CPU pool
- in case of infrastructure node, the `openshift-local-storage` namespace can be annotated with `openshift.io/node-selector:''` if enabled with --nso flag

## Requirements

None

## Configurable options

```
# iserver set ocp lso --mode operator
  --cluster TEXT                Cluster Name
  --nso                         Enable node selector override namespace annotation [default: false]
  --channel TEXT                Operator channel  [default: __default__]
  --no-confirm                  Confirmation mode
```

## Expected outcome

![OperatorCreate](../images/lso/operator_create.png)

## Example

```
# iserver set ocp lso --cluster bm1 --mode operator

```

[[Back]](./README.md)