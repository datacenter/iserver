# Intersight Open Telemetry - Delete Instance

## Workflow

- delete kubernetes resources for instance selected with --suffix
  - service monitor
  - service
  - deployment
  - configmaps
  - secret
- delete intersight-otel namespace (if there are no resources left)

## Requirements

None

## Configurable options

```
# iserver delete ocp iotel --mode instance
  --cluster TEXT     Cluster Name
  --suffix TEXT      Resources name suffix
  --verbose          Verbose output
  --no-confirm       Confirmation mode
```

## Expected outcome

Resources deleted

## Example

```
# iserver delete ocp iotel --cluster bm1 --suffix iac

OpenShift Workflow - Intersight Open Telemetry (iotel) - Delete Instance
========================================================================

OpenShift Cluster: bm1

Resources
---------
namespace: intersight-otel
intersight-otel secret: intersight-otel/intersight-iac
intersight-otel config map: intersight-otel/intersight-iac
otel-collector config map: intersight-otel/otel-iac
deployment: intersight-otel/instance-iac
service: intersight-otel/otel-iac
service monitor: intersight-otel/otel-iac

Delete Service Monitor
----------------------
- namespace: intersight-otel
- name: otel-iac
- wait for no service monitor

Delete Service
--------------
- namespace: intersight-otel
- name: otel-iac
- wait for no service

Delete Deployment
-----------------
- namespace: intersight-otel
- name: instance-iac
- replica set: instance-iac-7d7859b78f
- pod: instance-iac-7d7859b78f-bcvrh
- wait for no deployment
- wait for no pod: instance-iac-7d7859b78f-bcvrh

Delete Config Map
-----------------
- namespace: intersight-otel
- name: intersight-iac
- wait for no config map

Delete Config Map
-----------------
- namespace: intersight-otel
- name: otel-iac
- wait for no config map

Delete Secret
-------------
- namespace: intersight-otel
- name: intersight-iac
- wait for no secret

Namespace [intersight-otel] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs

Delete Namespace
----------------
- name: intersight-otel
- wait for no namespace

Completed tasks
- Service monitor deleted
- Service deleted
- Deployment deleted
- ConfigMap for intersight poller deleted
- ConfigMap for otel-collector deleted
- Secret with intersight authentication deleted
- Namespace deleted (if empty)
```

[[Back]](./README.md)