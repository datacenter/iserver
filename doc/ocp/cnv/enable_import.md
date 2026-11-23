# Container Virtualization Operator - Enable Data Import

## Workflow

- get cnv operator and hyperconverged instance state
- enable data import

## Example

```
# iserver set ocp cnv --cluster bm1 --mode import

OpenShift Workflow - Container Virtualization Operator - Enable Data Import Cron
================================================================================

OpenShift Cluster: bm1

Collecting state...


State
-----
- package          : openshift-marketplace/redhat-operators/kubevirt-hyperconverged
- csv              : kubevirt-hyperconverged-operator.v4.21.3
- operator ready   : V
- instance         : openshift-cnv/kubevirt-hyperconverged
- instance healthy : V
- import enabled   : X


~~~
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
  enableCommonBootImageImport: true
~~~

HyperConverged boot image import enabled


+----+---------+-------+---------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow      | Changes | Success | Duration [s] |
+----+---------+-------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | cnv   | create import | 1       | V       | 9            | 
+----+---------+-------+---------------+---------+---------+--------------+
```

[[Back]](./README.md)