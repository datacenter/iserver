# Container Virtualization Operator - Get State

## Workflow

- get cnv operator state
- get hyperconverged instance state
- collect cnv related crds

## Example

```
# iserver get ocp cnv --cluster bm1

OpenShift Workflow - Container Virtualization Operator - Get Information
========================================================================

OpenShift Cluster: bm1

Collecting state...


State
-----
- package          : openshift-marketplace/redhat-operators/kubevirt-hyperconverged
- csv              : kubevirt-hyperconverged-operator.v4.21.3
- operator ready   : V
- instance         : openshift-cnv/kubevirt-hyperconverged
- instance healthy : V
- import enabled   : V



Containerized Data Importer (CDI)
---------------------------------
- Name  : cdi-kubevirt-hyperconverged
- Phase : Deployed
- Ready : V



Network Addons Config
---------------------
- Name  : cluster
- Ready : V


View: state (def), import, crd
```

[[Back]](./README.md)