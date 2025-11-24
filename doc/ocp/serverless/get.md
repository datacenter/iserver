# Serverless Operator - Get

## Workflow

- get serverless operator state
- get serverless CRDs

## Requirements

None

## Example

```
# iserver get ocp serverless --cluster bm1

OpenShift Workflow - Serverless Operator - Get Information
==========================================================

OpenShift Cluster: bm1
Operator
--------
- subscription: openshift-serverless/serverless-operator
- channel: stable
- csv: serverless-operator.v1.36.1

+----+------------------+
| ID | Knative Eventing |
+----+------------------+
+----+------------------+

+----+-----------------+---------+-------+--------------------------+---------+------------------------+
| ID | Knative Serving | Version | Ready | Conditions               | Ingress | Deployment             |
+----+-----------------+---------+-------+--------------------------+---------+------------------------+
| 1  | knative-serving | 1.16    | ✓     | DependenciesInstalled    | istio   | ✓ activator            |
|    | knative-serving |         |       | DeploymentsAvailable     |         | ✓ autoscaler           |
|    |                 |         |       | InstallSucceeded         |         | ✓ autoscaler-hpa       |
|    |                 |         |       | Ready                    |         | ✓ controller           |
|    |                 |         |       | VersionMigrationEligible |         | ✓ net-istio-controller |
|    |                 |         |       |                          |         | ✓ net-istio-webhook    |
|    |                 |         |       |                          |         | ✓ webhook              |
+----+-----------------+---------+-------+--------------------------+---------+------------------------+

+----+---------------+
| ID | Knative Kafka |
+----+---------------+
+----+---------------+
```

[[Back]](./README.md)