# Tetragon - Delete All

## Workflow

Workflows deployed in sequence
- [wipe resources](./delete_wipe.md)
- [delete operator](./delete_operator.md)

## Requirements

None

## Configurable options

```
# iserver delete ocp tetragon --mode all
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp tetragon --cluster bm1 --mode all

OpenShift Workflow - Tetragon - Wipe
====================================

OpenShift Cluster: bm1

Delete TracingPolicy
--------------------
- name: upper-layers
- deleted
- wait for no TracingPolicy upper-layers [timeout:60s]

Completed tasks
- Tetragon resources deleted

OpenShift Workflow - Tetragon - Delete Operator
===============================================

OpenShift Cluster: bm1

Operator
- subscription          : tetragon/tetragon-operator
- package               : tetragon/tetragon-catalog/tetragon-operator
- channel               : v1.18
- install plan          : tetragon/install-k9whc
- install plan approved : V
- installed csv         : tetragon-operator.v1.18.2
- latest_csv            : V


Delete Subscription
-------------------
- subscription: tetragon/tetragon-operator
- checking cluster service version...
- csv found and will be deleted: tetragon/tetragon-operator.v1.18.2
- wait for no subscription
- check cluster service version: tetragon/tetragon-operator.v1.18.2
- wait for no csv

Delete Config Map
-----------------
- namespace: tetragon
- name: tetragon-operator-config
- wait for no config map
- wait for no Deployment tetragon/tetragon-operator [timeout:180s]
- wait for no ReplicaSet tetragon/tetragon-operator-646c4b6845 [timeout:180s]
- wait for no Pod tetragon/tetragon-operator-646c4b6845-k9mp2 [timeout:180s]
- wait for no DaemonSet tetragon/tetragon [timeout:180s]
- wait for no Pod tetragon/tetragon-pdks7 [timeout:180s]
- wait for no Pod tetragon/tetragon-s4tvf [timeout:180s]
- wait for no Pod tetragon/tetragon-w7x5s [timeout:180s]
Subscription tetragon resources gone

Delete CatalogSource
--------------------
- namespace: tetragon
- name: tetragon-catalog
- deleted
- wait for no CatalogSource tetragon/tetragon-catalog [timeout:60s]
- wait for no Pod tetragon/tetragon-catalog-ptj2d [timeout:60s]

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
- wait for no OperatorGroup tetragon/tetragon [timeout:60s]

Namespace [tetragon] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- no user defined networks
- no cluster user defined networks

Delete Namespace
----------------
- name: tetragon
- wait for no namespace

Completed tasks
- Subscription deleted
- Operator Group deleted
- Namespace deleted

+----+---------+----------+-----------------+---------+---------+--------------+
| ID | Target  | Scope    | Workflow        | Changes | Success | Duration [s] |
+----+---------+----------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | tetragon | delete wipe     | 1       | V       | 2            | 
| 2  | ocp:bm1 | tetragon | delete operator | 6       | V       | 56           | 
+----+---------+----------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)