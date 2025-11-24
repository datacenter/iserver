# Prometheus Operator - Enable user-workload monitoring

## Workflow

- create config map in openshift-monitoring namespace that enables user workload monitoring
- wait for resources to be created

## Requirements

None

## Configurable options

```
# iserver set ocp prometheus --mode user
  --cluster TEXT                  Cluster Name
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver set ocp prometheus --cluster bm1 --mode user 

OpenShift Workflow - Prometheus - Enable user-workload monitoring
=================================================================


OpenShift Cluster: bm1

Config Map
----------
- namespace: openshift-monitoring
- name: cluster-monitoring-config
- not found and will be created

Create Config Map
-----------------
- namespace: openshift-monitoring
- name: cluster-monitoring-config
- destination: config.yaml

~~~
enableUserWorkload: true

~~~

Config map created

Wait for config map [timeout:60]...

Check for resources
-------------------
Wait for deployments ready (optional: False, allow zero replicas: False)...
- openshift-user-workload-monitoring/prometheus-operator
Wait for stateful sets ready...
- openshift-user-workload-monitoring/prometheus-user-workload
- openshift-user-workload-monitoring/thanos-ruler-user-workload


Completed tasks
---------------
- User workload monitoring enabled
```

[[Back]](./README.md)