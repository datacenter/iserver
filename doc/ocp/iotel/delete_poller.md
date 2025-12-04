# Intersight Open Telemetry - Delete Poller

## Workflow

- get pollers from config map of instance selected with --suffix
- modify config map data
  - if no extra --metric or --attribute parameter defined, then delete all pollers
  - selected to-be-deleted-pollers with --metric and --attribute parameters
  - logical OR in case of multiple metric parameters or multiple attribute parameters
  - logical AND when both metric and attribute defined
  - explicit string match by default, use '*' at the beginning or end of the value for pattern match
- patch config map
- restart deployment

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
# iserver delete ocp iotel --cluster bm1 --suffix iac --mode poller  --attribute scope=node:bm1* --metric intersight.advisory.count

OpenShift Workflow - Intersight Open Telemetry (iotel) - Delete Poller
======================================================================

OpenShift Cluster: bm1
Collect resources
- deployment
- config map

Poller selection
----------------
- suffix: iac
- metric: intersight.advisory.count
- attribute: scope=node:bm1*

Instance
--------
- deployment intersight-otel/instance-iac
- config map intersight-otel/intersight-otel

Removed pollers
---------------

[[pollers]]
name = "intersight.advisory.count"
otel_attributes = { scope = "node:bm1-1" }
api_query = "api/v1/tam/AdvisoryInstances?$filter=AffectedObjectMoid eq '111111'"
aggregator = "count_results"
interval = 60

[[pollers]]
name = "intersight.advisory.count"
otel_attributes = { scope = "node:bm1-2" }
api_query = "api/v1/tam/AdvisoryInstances?$filter=AffectedObjectMoid eq '222222'"
aggregator = "count_results"
interval = 60

[[pollers]]
name = "intersight.advisory.count"
otel_attributes = { scope = "node:bm1-3" }
api_query = "api/v1/tam/AdvisoryInstances?$filter=AffectedObjectMoid eq '333333'"
aggregator = "count_results"
interval = 60


New pollers
-----------

otel_collector_endpoint = "http://127.0.0.1:4317"

[[pollers]]
name = "intersight.advisory.count"
otel_attributes = { scope = "node:bm3-1" }
api_query = "api/v1/tam/AdvisoryInstances?$filter=AffectedObjectMoid eq '444444'"
aggregator = "count_results"
interval = 60

[[pollers]]
name = "intersight.advisory.count"
otel_attributes = { scope = "node:bm3-2" }
api_query = "api/v1/tam/AdvisoryInstances?$filter=AffectedObjectMoid eq '555555'"
aggregator = "count_results"
interval = 60

[[pollers]]
name = "intersight.advisory.count"
otel_attributes = { scope = "node:bm3-3" }
api_query = "api/v1/tam/AdvisoryInstances?$filter=AffectedObjectMoid eq '666666'"
aggregator = "count_results"
interval = 60

Configure deployment replicas
-----------------------------
- namespace: intersight-otel
- name: instance-iac
- replicas: 0

~~~
apiVersion: apps/v1
kind: Deployment
metadata:
  name: instance-iac
  namespace: intersight-otel
spec:
  replicas: 0

~~~
Patch successful

Wait for desired replica pods...

Change Config Map
-----------------
- namespace: intersight-otel
- name: intersight-iac

Config map updated

Configure deployment replicas
-----------------------------
- namespace: intersight-otel
- name: instance-iac
- replicas: 1

~~~
apiVersion: apps/v1
kind: Deployment
metadata:
  name: instance-iac
  namespace: intersight-otel
spec:
  replicas: 1

~~~
Patch successful

Wait for desired replica pods...

Completed tasks
- Config map changed
- Deployment restarted
```

[[Back]](./README.md)