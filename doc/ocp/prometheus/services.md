# Prometheus Operator - Get Services

## Workflow

- get kubernetes services via REST API

## Requirements

None

## Configurable options

```
# iserver get k8s svc
  --cluster TEXT               Kubernetes cluster name
  --namespace TEXT             Filter by namespace
  --name TEXT                  Filter by name
```

## Example

```
# iserver get k8s svc --cluster bm1 --namespace openshift-monitoring --name alertmanager*

+----+-----------------------+-----------+---------------+---------------------+------------------------------------------------+---------------------+-----+
| ID | Service               | Type      | IP            | Port                | Selector                                       | POD                 | Age |
+----+-----------------------+-----------+---------------+---------------------+------------------------------------------------+---------------------+-----+
| 1  | openshift-monitoring  | ClusterIP | 172.30.73.180 | TCP/9094 [web]      | app.kubernetes.io/component:alert-router       | alertmanager-main-0 | 14d |
|    | alertmanager-main     |           |               | TCP/9092 [tenancy]  | app.kubernetes.io/instance:main                | alertmanager-main-1 |     |
|    |                       |           |               | TCP/9097 [metrics]  | app.kubernetes.io/name:alertmanager            |                     |     |
|    |                       |           |               |                     | app.kubernetes.io/part-of:openshift-monitoring |                     |     |
+----+-----------------------+-----------+---------------+---------------------+------------------------------------------------+---------------------+-----+
| 2  | openshift-monitoring  | ClusterIP | ---           | TCP/9093 [web]      | app.kubernetes.io/name:alertmanager            | alertmanager-main-0 | 14d |
|    | alertmanager-operated |           |               | TCP/9094 [tcp-mesh] |                                                | alertmanager-main-1 |     |
|    |                       |           |               | UDP/9094 [udp-mesh] |                                                |                     |     |
+----+-----------------------+-----------+---------------+---------------------+------------------------------------------------+---------------------+-----+
```

[[Back]](./README.md)