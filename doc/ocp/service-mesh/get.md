# Service Mesh Operator - Get

## Workflow

- get service mesh operator state and configuration

## Requirements

None

## Example

```
# iserver get ocp service-mesh --cluster bm1

OpenShift Workflow - Service Mesh Operator - Get Information
============================================================

OpenShift Cluster: bm1

Operator (v2)
-------------
- subscription: openshift-operators/servicemeshoperator
- channel: stable
- csv: servicemeshoperator.v2.6.11

+----+---------------------------+-------------+-------+------------+--------------------+-------------+---------------------------+
| ID | Service Mesh Contol Plane | Version     | Ready | Conditions | Components         | Disabled    | Members                   |
+----+---------------------------+-------------+-------+------------+--------------------+-------------+---------------------------+
| 1  | istio-system              | OSSM_2.6.11 | ✓     | Installed  | ✓ istio-discovery  | api-gateway | ✓ knative-serving/default |
|    | data-science-smcp         |             |       | Ready      | ✓ istio-egress     | grafana     |                           |
|    |                           |             |       | Reconciled | ✓ istio-ingress    | kiali       |                           |
|    |                           |             |       |            | ✓ mesh-config      | prometheus  |                           |
|    |                           |             |       |            | ✓ telemetry-common | tracing     |                           |
|    |                           |             |       |            | ✓ istio-cni        |             |                           |
|    |                           |             |       |            | ✓ telemetry        |             |                           |
+----+---------------------------+-------------+-------+------------+--------------------+-------------+---------------------------+
```

[[Back]](./README.md)