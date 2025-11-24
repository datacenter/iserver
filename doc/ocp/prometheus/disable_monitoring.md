# Prometheus Operator - Disable user-workload monitoring

## Workflow

- check config map in openshift-monitoring namespace that enables user workload monitoring and update it
- wait for resources to be gone

## Requirements

None

## Configurable options

```
# iserver delete ocp prometheus --mode user
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp prometheus --cluster bm1 --mode user

OpenShift Workflow - Prometheus - Disable user-workload monitoring
==================================================================


OpenShift Cluster: bm1

Config Map
----------
- namespace: openshift-monitoring
- name: cluster-monitoring-config
- found and will be checked
- enableUserWorkload value will be changed in config map
Config map udpated

Check for resources gone
------------------------
Wait for deployments deleted (optional: False)...
- openshift-user-workload-monitoring/prometheus-operator
Wait for stateful sets deleted (optional: False)...
- openshift-user-workload-monitoring/prometheus-user-workload
- openshift-user-workload-monitoring/thanos-ruler-user-workload


Completed tasks
---------------
- User workload monitoring disabled
```

[[Back]](./README.md)