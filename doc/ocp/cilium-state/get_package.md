# Cilium - Get package

## Workflow

- get cilium operator package and subscription details

## Requirements

None

## Configurable options

```
# iserver get ocp cilium package
  --cluster TEXT   Cluster Name
```

## Example

```
# iserver get ocp cilium package --cluster bm1

OpenShift Workflow - Cilium - Get cni package
=============================================

OpenShift Cluster: bm1

Operator
--------
- subscription          : cilium/clife
- package               : openshift-marketplace/certified-operators/clife
- channel               : 1.17
- install plan          : cilium/install-8wqkc
- install plan approved : ✗
- installed csv         : clife.v1.17.9-cee.1
- latest_csv            : ✗
```

[[Back]](./README.md)