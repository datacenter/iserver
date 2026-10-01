# MinIO AIStor Operator - Get

## Workflow

- get minio operator state
- get minio CRDs

## Requirements

None

## Example

```
# iserver get ocp minio --cluster bm1

OpenShift Workflow - MinIO Operator - Get Information
=====================================================

OpenShift Cluster: bm1
Operator
--------
- subscription: aistor/minio-object-store-operator
- channel: stable
- csv: minio-object-store-operator.v2025.8.19175300

+----+-----------+
| ID | Admin Job |
+----+-----------+
+----+-----------+

+----+----------------+
| ID | Policy Binding |
+----+----------------+
+----+----------------+

+----+--------------+
| ID | Object Store |
+----+--------------+
+----+--------------+
```

[[Back]](./README.md)