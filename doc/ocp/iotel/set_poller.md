# Intersight Open Telemetry - Set Pollers

## Workflow

- modify pollers config map of the selected instance

Parameter | Generation | Intent 
--- | ---| --- 
--pollers /tmp/pollers.txt --pmode set | no | set pollers from file 
--pollers /tmp/pollers.txt --pmode add | no | add pollers from file 
--template all --target ocp:bm2 --pmode set | yes | set generated pollers for all templates in scope of selected cluster 
--template all --target ocp:bm2 --pmode add | yes | as above but add to existing pollers in configmap 

Allowed targets
- ocp:bm1 where bm1 is configured [connector](../Access.md)
- server-ip:10.1.1.1 
- server-name:abc 

Targets are resolved to server moid values.

Refer to [pollers](./pollers.md) and [templates](./templates.md) documentation for more details.

## Requirements

- instance must be [created](./create_instance.md)

## Configurable options

```
# iserver set ocp iotel --mode poller
  --cluster TEXT     Cluster Name
  --suffix TEXT      Resources name suffix
  --pollers TEXT     Pollers definition file
  --template [advisory|alarm|all]
  --target TEXT                 
  --pmode [add|set]  [default: add]
  --verbose          Verbose output
  --no-confirm       Confirmation mode
```

## Non-configurable defaults

```
{
    "namespace": "intersight-otel",
    "deployment-basename": "instance",
    "secret-basename": "intersight",
    "intersight-basename": "intersight",
    "otel-basename": "otel",
    "service-basename": "otel",
    "service-monitor-basename": "otel",
    "intersight-image": "ghcr.io/cgascoig/intersight-otel:v0.1.2",
    "otel-image": "otel/opentelemetry-collector:0.59.0",
    "mon-namespace": "openshift-monitoring",
    "mon-name": "cluster-monitoring-config",
    "delete-namespace": true
}
```

## Expected outcome

![Targets](../images/iotel/targets.png)

![Matrics](../images/iotel/metrics.png)

## Example

```
# iserver set ocp iotel --cluster bm1 --mode poller --suffix iac --pollers C:\tmp\pollers.txt

OpenShift Workflow - Intersight Open Telemetry (iotel) - Set Poller
===================================================================

OpenShift Cluster: bm1
Collect resources
- deployment
- config map

Instance
--------
- deployment intersight-otel/instance-iac
- config map intersight-otel/intersight-iac
- mode: add
- no template
- user-provided poller

~~~
otel_collector_endpoint = "http://127.0.0.1:4317"


[[pollers]]
name = "intersight.tam.advisory.count"
otel_attributes = { scope = "node:bm1-1" }
api_query = "api/v1/tam/AdvisoryInstances?$filter=AffectedObjectMoid eq '111111'"
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
    name = "intersight.tam.advisory.count"
    otel_attributes = { scope = "node:bm1-1" }
    api_query = "api/v1/tam/AdvisoryInstances?$filter=AffectedObjectMoid eq '111111'"
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