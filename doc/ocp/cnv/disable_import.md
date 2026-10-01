# Container Virtualization Operator - Disable Data Import

## Workflow

- get cnv operator and hyperconverged instance state
- disable data import
- optionally wipe all downloaded data imports

## Example

```
# iserver delete ocp cnv --cluster bm1 --mode import

OpenShift Workflow - Container Virtualization Operator - Disable Data Import Cron
=================================================================================

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


~~~
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
  enableCommonBootImageImport: false
~~~

HyperConverged boot image import disabled


+----+---------+-------+---------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow      | Changes | Success | Duration [s] |
+----+---------+-------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | cnv   | delete import | 1       | V       | 8            | 
+----+---------+-------+---------------+---------+---------+--------------+
```

[[Back]](./README.md)