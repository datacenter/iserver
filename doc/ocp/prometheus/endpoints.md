# Prometheus Operator - Get Endpoints

## Workflow

- get kubernetes endpoints via REST API

## Requirements

None

## Configurable options

```
# iserver get k8s ep
  --cluster TEXT               Kubernetes cluster name
  --namespace TEXT             Filter by namespace
  --name TEXT                  Filter by name
```

## Example

```
# iserver get k8s ep --namespace openshift-monitoring --name alertmanager* 
Cluster: bm3 (type: ocp)
|
+----+-----------------------+----------+---------------------+----------------------+---------------------+
| ID | Endpoint              | Headless | Pod                 | Address              | Port                |
+----+-----------------------+----------+---------------------+----------------------+---------------------+
| 1  | openshift-monitoring  | ✗        | alertmanager-main-1 | 10.128.0.11 [bm3-2]  | TCP/9095 [web]      |
|    | alertmanager-main     |          | alertmanager-main-0 | 10.128.3.179 [bm3-1] | TCP/9097 [metrics]  |
|    |                       |          |                     |                      | TCP/9092 [tenancy]  |
+----+-----------------------+----------+---------------------+----------------------+---------------------+
| 2  | openshift-monitoring  | ✓        | alertmanager-main-1 | 10.128.0.11 [bm3-2]  | TCP/9095 [web]      |
|    | alertmanager-operated |          | alertmanager-main-0 | 10.128.3.179 [bm3-1] | UDP/9094 [udp-mesh] |
|    |                       |          |                     |                      | TCP/9094 [tcp-mesh] |
+----+-----------------------+----------+---------------------+----------------------+---------------------+
```

[[Back]](./README.md)