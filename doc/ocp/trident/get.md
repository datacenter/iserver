# Trident Operator - Get Information

## Workflow

Check trident operator state

## Example

```
# iserver get ocp trident --cluster bm1


OpenShift Workflow - Trident Operator - Get Information
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

Operator
--------
- subscription: openshift-operators/trident-operator
- channel: stable
- csv: trident-operator.v25.6.2
```

[[Back]](./README.md)