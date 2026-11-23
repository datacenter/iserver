# Node Feature Discovery Operator - Get

[[Back]](./README.md) [[Next]](./create_operator.md) [[Prev]](./delete_task.md)

## HowTo

```
# iserver get ocp nfd --cluster bm1
```

## Workflow

- get nfd operator state
- get node annotations with `annotation` view
- get resources details with `details` view

## Example

```
# iserver get ocp nfd --cluster bm1

OpenShift Workflow - Node Feature Discovery Operator - Get Information
======================================================================

OpenShift Cluster: bm1

Collecting state...

State
-----
- package          : openshift-marketplace/redhat-operators/nfd
- csv              : nfd.4.21.0-202604140347
- resources        : ✓
- instance         : ✓
- node annotations : 3/3
- no annotation    : ---
```

[[Back]](./README.md) [[Next]](./create_operator.md) [[Prev]](./delete_task.md)