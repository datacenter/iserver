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

Operator
- subscription          : tetragon/tetragon-operator
- package               : tetragon/tetragon-catalog/tetragon-operator
- channel               : v1.18
- install plan          : tetragon/install-sd9g7
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
- wait for no Pod tetragon/tetragon-operator-646c4b6845-zw8bl [timeout:180s]
- wait for no DaemonSet tetragon/tetragon [timeout:180s]
- wait for no Pod tetragon/tetragon-6ckcp [timeout:180s]
- wait for no Pod tetragon/tetragon-9kvxr [timeout:180s]
- wait for no Pod tetragon/tetragon-skx88 [timeout:180s]
Subscription tetragon resources gone

Delete CatalogSource
--------------------
- namespace: tetragon
- name: tetragon-catalog
- deleted
- wait for no CatalogSource tetragon/tetragon-catalog [timeout:60s]
- wait for no Pod tetragon/tetragon-catalog-7vp8s [timeout:60s]

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
| 1  | ocp:bm1 | tetragon | delete operator | 6       | V       | 26           | 
+----+---------+----------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)