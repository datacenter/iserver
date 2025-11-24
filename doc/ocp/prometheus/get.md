# Prometheus Operator - Get Information

## Workflow

- check user workload monitoring
- check metrics targets readiness

## Example

```
# iserver get ocp prometheus --cluster bm1

OpenShift Workflow - Prometheus - Get Information
=================================================

OpenShift Cluster: bm1

Check User Workload Monitoring
------------------------------
- config map namespace: openshift-monitoring
- config map name: cluster-monitoring-config
- enableUserWorkload enabled

Targets
-------
- platform targets: 127/127
- user targets: 1/1
```

[[Back]](./README.md)