# Node Feature Discovery Operator - Get

## Workflow

- get nfd operator state
- get node annotations with --verbose option

## Example

```
# iserver get ocp nfd --cluster bm1 --verbose


OpenShift Workflow - Node Feature Discover Operator - Get Information
=====================================================================

OpenShift Cluster: bm1


Operator
--------
- subscription          : openshift-nfd/nfd
- package               : openshift-marketplace/redhat-operators/nfd
- channel               : stable
- install plan          : openshift-nfd/install-9xtp4
- install plan approved : ✓
- installed csv         : nfd.4.21.0-202603230446
- latest_csv            : ✓

Instance
--------
- name: nfd-instance

Operator resources
------------------
- deployment openshift-nfd/nfd-master: ready
- deployment openshift-nfd/nfd-controller-manager: ready
- daemonset openshift-nfd/nfd-worker: ready
Subscription nfd ready

NFD node annotations
--------------------
- node [bm1-1]
	cpu-cpuid.ADX
	cpu-cpuid.AESNI
	cpu-cpuid.AMXFP8
...
```

[[Back]](./README.md)