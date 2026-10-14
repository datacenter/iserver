# Tetragon - Delete Operator

[[Back]](./README.md)

## Workflow

- delete tetragon operator subscription
- delete catalog source
- delete operator group
- delete config maps in tetragon namespace
- delete service monitor and service
- delete namespace

## Configurable options

```
# iserver delete ocp tetragon --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp tetragon --cluster bm1 --mode operator


OpenShift Workflow - Tetragon - Delete Operator
===============================================

OpenShift Cluster: bm1

Delete Subscription
-------------------
- subscription: tetragon/tetragon-operator
- checking cluster service version...
- csv found and will be deleted: tetragon/tetragon-operator.v1.20.0-pre.3
- wait for no subscription
- check cluster service version: tetragon/tetragon-operator.v1.20.0-pre.3
- wait for no csv

Delete Config Map
-----------------
- namespace: tetragon
- name: tetragon-operator-config
- wait for no config map
Wait for no Deployment tetragon/tetragon-operator [timeout:180s]
Wait for no ReplicaSet tetragon/tetragon-operator-6cfb585fd [timeout:180s]
Wait for no ReplicaSet tetragon/tetragon-operator-dd8d5848 [timeout:180s]
Wait for no Pod tetragon/tetragon-operator-dd8d5848-2sxnc [timeout:180s]
Wait for no DaemonSet tetragon/tetragon [timeout:180s]
Wait for no Pod tetragon/tetragon-85mjh [timeout:180s]
Subscription tetragon resources gone

Delete CatalogSource
--------------------
- namespace: tetragon
- name: tetragon-catalog
- deleted
Wait for no CatalogSource tetragon/tetragon-catalog [timeout:60s]
Wait for no Pod tetragon/tetragon-catalog-ghkhc [timeout:60s]

Delete Config Map
-----------------
- namespace: tetragon
- name: tetragon-config
- already deleted

Delete Config Map
-----------------
- namespace: tetragon
- name: tetragon-operator-config
- already deleted

Delete Service Monitor
----------------------
- namespace: tetragon
- name: tetragon
- already deleted

Delete Service
--------------
- namespace: tetragon
- name: tetragon
- already deleted

Delete OperatorGroup
--------------------
- namespace: tetragon
- name: tetragon
- deleted
Wait for no OperatorGroup tetragon/tetragon [timeout:60s]

Delete Namespace
----------------
- name: tetragon

Namespace [tetragon] resources
- no deployments
- no daemon_sets
- no replica_sets
- no pods
- no services
- no pvcs
- no jobs
Wait for no Namespace tetragon [timeout:60s]

Completed tasks
- Subscription deleted
- Operator Group deleted
- Namespace deleted

+----+---------+----------+-----------------+---------+---------+--------------+
| ID | Target  | Scope    | Workflow        | Changes | Success | Duration [s] |
+----+---------+----------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | tetragon | delete operator | 6       | ✓       | 36           | 
+----+---------+----------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)