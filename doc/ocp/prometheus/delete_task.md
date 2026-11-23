# Prometheus Operator - Delete via Task

## Input

```
[
  {
    "prometheus": {
      "user": {}
    }
  }
]
```

Notes:
- [user](./enable_monitoring.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters may be silently ignored
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

## Requirements

None

## Configurable options

```
# iserver delete ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Prometheus - Disable user-workload monitoring
==================================================================


OpenShift Cluster: bm1

Config Map
----------
- namespace: openshift-monitoring
- name: cluster-monitoring-config
- found and will be checked
- enableUserWorkload value will be changed in config map

Change Config Map
-----------------
- namespace: openshift-monitoring
- name: cluster-monitoring-config

~~~
apiVersion: v1
data:
  config.yaml: |-
    enableUserWorkload: false
kind: ConfigMap
metadata:
  name: name
  namespace: namespace

~~~
Config map updated

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