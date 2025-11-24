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
# iserver set ocp iotel --cluster bm1 --mode instance --template advisory

[...]

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
```

## Alarm

```
~~~
otel_collector_endpoint = "http://127.0.0.1:4317"



[[pollers]]
name = "intersight.alarm.count"
otel_attributes = { scope = "node:bm1-1", severity = "critical" }
api_query = "api/v1/cond/Alarms?$filter=Acknowledge eq 'None' and Severity eq 'Critical' and RegisteredDevice/Moid eq '444444'&$count=true"
aggregator = "result_count"
interval = 300

[[pollers]]
name = "intersight.alarm.count"
otel_attributes = { scope = "node:bm1-1", severity = "warning" }
api_query = "api/v1/cond/Alarms?$filter=Acknowledge eq 'None' and Severity eq 'Warning' and RegisteredDevice/Moid eq '444444'&$count=true"
aggregator = "result_count"
interval = 300

[[pollers]]
name = "intersight.alarm.count"
otel_attributes = { scope = "node:bm1-2", severity = "critical" }
api_query = "api/v1/cond/Alarms?$filter=Acknowledge eq 'None' and Severity eq 'Critical' and RegisteredDevice/Moid eq '555555'&$count=true"
aggregator = "result_count"
interval = 300

[[pollers]]
name = "intersight.alarm.count"
otel_attributes = { scope = "node:bm1-2", severity = "warning" }
api_query = "api/v1/cond/Alarms?$filter=Acknowledge eq 'None' and Severity eq 'Warning' and RegisteredDevice/Moid eq '555555'&$count=true"
aggregator = "result_count"
interval = 300

[[pollers]]
name = "intersight.alarm.count"
otel_attributes = { scope = "node:bm1-3", severity = "critical" }
api_query = "api/v1/cond/Alarms?$filter=Acknowledge eq 'None' and Severity eq 'Critical' and RegisteredDevice/Moid eq '666666'&$count=true"
aggregator = "result_count"
interval = 300

[[pollers]]
name = "intersight.alarm.count"
otel_attributes = { scope = "node:bm1-3", severity = "warning" }
api_query = "api/v1/cond/Alarms?$filter=Acknowledge eq 'None' and Severity eq 'Warning' and RegisteredDevice/Moid eq '666666'&$count=true"
aggregator = "result_count"
interval = 300

[[pollers]]
name = "intersight.alarm.count"
otel_attributes = { scope = "cluster:bm1", severity = "critical" }
api_query = "api/v1/cond/Alarms?$filter=Acknowledge eq 'None' and Severity eq 'Critical' and RegisteredDevice/Moid in ('444444', '555555', '666666')&$count=true"
aggregator = "result_count"
interval = 300

[[pollers]]
name = "intersight.alarm.count"
otel_attributes = { scope = "cluster:bm1", severity = "warning" }
api_query = "api/v1/cond/Alarms?$filter=Acknowledge eq 'None' and Severity eq 'Warning' and RegisteredDevice/Moid in ('444444', '555555', '666666')&$count=true"
aggregator = "result_count"
interval = 300

~~~
```

[[Back]](./README.md)