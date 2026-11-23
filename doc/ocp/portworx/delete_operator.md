# MinIO AIStor Operator - Delete Operator

## Workflow

- delete operator subscription
- delete operator group
- delete namespace

## Requirements

None

## Configurable options

```
# iserver delete ocp minio --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp minio --cluster bm1

OpenShift Workflow - MinIO Operator - Delete Operator
=====================================================

OpenShift Cluster: bm1
Checking MinIO related objects
- no AdminJob
- no PolicyBinding
- no ObjectStore

Delete Subscription
-------------------
- subscription: aistor/minio-object-store-operator
- checking cluster service version...
- csv found and will be deleted: aistor/minio-object-store-operator.v2025.8.19175300
- wait for no subscription
- check cluster service version: aistor/minio-object-store-operator.v2025.8.19175300
- wait for no csv
Wait for deployments deleted (optional: False)...
Wait for pods deleted...

Delete Operator Group
---------------------
- namespace: aistor
- name: minio-operator-group
- wait for no operator group

Delete Namespace
----------------
- name: aistor

Namespace [aistor] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)