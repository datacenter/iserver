# Prometheus Operator - Get Service Monitors

## Overview

The ServiceMonitor custom resource definition (CRD) defines how Prometheus and PrometheusAgent can scrape metrics from a group of services.

Definition includes:
- the services to scrape via label selectors
- the container ports to scrape
- authentication credentials to use
- target and metric relabeling

ServiceMonitor CRD has no status information.

CRD [documentation](https://docs.okd.io/4.18/rest_api/monitoring_apis/servicemonitor-monitoring-coreos-com-v1.html) and [quick reference guide](./service_monitor_crd.md)

## Workflow

- get ServiceMonitor CRD 
- get [Prometheus targets](./targets.md) to add target information
- get Endpoint CRD to add endpoint information and detect endpoint mismatch scenario
- show combined view

## Need for cross crd checks

Valid and consistent ServiceMonitor CRD triggers [metric target](./targets.md). 

At the same time there are multiple reason why ServiceMonitor CRD exists and there is not target and scraped metrics
- missing label service/endpoint
- label mismatch between service monitor selector and service/endpoint
- missing or mismatch between service port name and service monitor endpoint port name
- no endpoint for service (typically due to no port up)

The enhanced service monitor output can help to pinpoint such problems.

## Requirements

None

## Configurable options

```
# iserver get k8s smon
  --cluster TEXT               Kubernetes cluster name
  --namespace TEXT             Filter by service monitor namespace
  --name TEXT                  Filter by service monitor name
```

## Example: all good

```
# iserver get k8s smon --cluster bm1 --namespace default

+----+-----------------+-------+---------------+---------------+--------+
| ID | Service Monitor | Owner | Endpoint      | POD           | Target |
+----+-----------------+-------+---------------+---------------+--------+
| 1  | default         | ---   | default       | default/nginx | ✓      |
|    | monitor-test    |       | nginx-service |               |        |
+----+-----------------+-------+---------------+---------------+--------+
```

## Example: possible service monitor label selector mismatch

```
+----+-----------------+-------+----------+-----+--------+
| ID | Service Monitor | Owner | Endpoint | POD | Target |
+----+-----------------+-------+----------+-----+--------+
| 1  | default         | ---   | ---      | --- | ---    |
|    | monitor-test    |       |          |     |        |
+----+-----------------+-------+----------+-----+--------+
```

## Example: pod down or pod label mismatch

```
+----+-----------------+-------+---------------+-----+--------+
| ID | Service Monitor | Owner | Endpoint      | POD | Target |
+----+-----------------+-------+---------------+-----+--------+
| 1  | default         | ---   | default       | --- | ---    |
|    | monitor-test    |       | nginx-service |     |        |
+----+-----------------+-------+---------------+-----+--------+
```

## Example: possible service monitor port name mismatch

```
+----+-----------------+-------+---------------+---------------+--------+
| ID | Service Monitor | Owner | Endpoint      | POD           | Target |
+----+-----------------+-------+---------------+---------------+--------+
| 1  | default         | ---   | default       | default/nginx | ---    |
|    | monitor-test    |       | nginx-service |               |        |
+----+-----------------+-------+---------------+---------------+--------+
```

## Example: pod may not exposing metrics or service monitor path mismatch

```
+----+-----------------+-------+---------------+---------------+--------+
| ID | Service Monitor | Owner | Endpoint      | POD           | Target |
+----+-----------------+-------+---------------+---------------+--------+
| 1  | default         | ---   | default       | default/nginx | ✗      |
|    | monitor-test    |       | nginx-service |               |        |
+----+-----------------+-------+---------------+---------------+--------+
```

[[Back]](./README.md)