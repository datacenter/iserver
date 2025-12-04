# Intersight Open Telemetry - Pollers Template

[Pollers](./pollers.md) define metrics pulled from Intersight via REST API. 

Templates can generate the pollers for selected OpenShift cluster
- --template selects the support template using advisory, alarm or all values
- --target selects the cluster for which the pollers are prepared

## Sub-Workflow

- collect Intersight server ids from selected cluster's nodes annotation
- generate pollers
- generated pollers can replace the currently configured pollers or can extend them, controlled with --pmode parameter

## Requirements

[Intersight Server Discovery](../imm/README.md)

## Advisory

```
# iserver set ocp iotel --cluster bm1 --mode poller --suffix iac --template advisory --target ocp:bm1


OpenShift Workflow - Intersight Open Telemetry (iotel) - Set Poller
===================================================================

OpenShift Cluster: bm1
Collect resources
- deployment
- secret
- config map

Instance
--------
- deployment intersight-otel/instance-iac
- config map intersight-otel/intersight-iac
- mode: add
- template: advisory
- target: ocp:bm1
- empty user-provided poller

Resolving cluster nodes intersight ids
--------------------------------------
Select servers...
Collect server api objects [122]...
Selected servers: 122

Cluster: bm1
- node: bm1-1
	id: 111111
	device id: 444444
	server found
- node: bm1-2
	id: 222222
	device id: 555555
	server found
- node: bm1-3
	id: 333333
	device id: 666666
	server found

~~~
otel_collector_endpoint = "http://127.0.0.1:4317"



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

[[pollers]]
name = "intersight.advisory.count"
otel_attributes = { scope = "cluster:bm1" }
api_query = "api/v1/tam/AdvisoryInstances?$filter=AffectedObjectMoid in ('111111', '222222', '333333')"
aggregator = "count_results"
interval = 60

~~~


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

~~~
apiVersion: v1
data:
  intersight-otel.toml: |-
    otel_collector_endpoint = "http://127.0.0.1:4317"



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

    [[pollers]]
    name = "intersight.advisory.count"
    otel_attributes = { scope = "cluster:bm1" }
    api_query = "api/v1/tam/AdvisoryInstances?$filter=AffectedObjectMoid in ('111111', '222222', '333333')"
    aggregator = "count_results"
    interval = 60
kind: ConfigMap
metadata:
  name: name
  namespace: namespace

~~~
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