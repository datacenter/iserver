# CDI Data Import Cron - Disable

## Workflow

- get cnv operator state
- get hyperconverged instance state
- disable cdi data import cron

## Requirements

- cnv operator installed
- hyperconverged instance created

## Configurable options

```
# iserver delete ocp cnv --mode import
  --cluster TEXT          Cluster Name
  --no-confirm            Confirmation mode
```

## Example

```
# iserver delete ocp cnv --cluster bm1 --mode import

OpenShift Workflow - Container Virtualization Operator - Disable Data Import Cron
=================================================================================

OpenShift Cluster: bm1

Operator
--------
- subscription: openshift-cnv/kubevirt-hyperconverged
- channel: stable
- csv: kubevirt-hyperconverged-operator.v4.18.23

HyperConverged
--------------
- instance: kubevirt-hyperconverged
- data import cron: enabled

~~~
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
  featureGates:
    enableCommonBootImageImport: false

~~~
Continue [Y/N]? y 

HyperConverged boot image import disabled
```

[[Back]](./README.md)