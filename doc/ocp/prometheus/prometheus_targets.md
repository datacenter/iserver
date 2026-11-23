# Prometheus Operator - Get Prometheus Targets

## Workflow

- get [platform metrics](./platform_metrics_targets_cli.md) via REST API
- get [user metrics](./user_metrics_targets_cli.md) via REST API
- filter the targets

## Requirements

None

## Configurable options

```
# iserver get k8s promtarget
  --cluster TEXT               Kubernetes cluster name
  --namespace TEXT             Filter by service monitor namespace
  --name TEXT                  Filter by service monitor name
  --type [all|platform|user]   [default: all]
```

## Example

```
# iserver get k8s promtarget --cluster bm1 --type user

+----+------+-------------------------------+-----------------+---------------+-------+---------------------+---------------+
| ID | Type | Endpoint                      | Service Monitor | Service       | Ready | Last Scrape         | Duration [ms] |
+----+------+-------------------------------+-----------------+---------------+-------+---------------------+---------------+
| 1  | U    | http://10.128.5.89:80/metrics | default         | default       | ✓     | 2025-11-14T07:23:03 | 0.54          |
|    |      |                               | monitor-test    | nginx-service |       |                     |               | 
|    |      |                               |                 | ep:web        |       |                     |               |
|    |      |                               |                 | pod:nginx     |       |                     |               |
+----+------+-------------------------------+-----------------+---------------+-------+---------------------+---------------+

Readiness summary: 1/1
```

[[Back]](./README.md)