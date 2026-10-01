# Serverless - Get

## Workflow

- get serverless operator state
- get serverless CRDs

## Requirements

None

## Example

```
# iserver get ocp serverless --cluster bm1

OpenShift Workflow - Serverless Operator - Get Information
==========================================================

OpenShift Cluster: bm1

Collecting state...


State
-----
- package   : openshift-marketplace/redhat-operators/serverless-operator
- csv       : serverless-operator.v1.37.1
- resources : V



Serverless Custom Resources
---------------------------
- eventing : 0
- serving  : 0
- kafka    : 0


View: state (def), res, all
```

[[Back]](./README.md)