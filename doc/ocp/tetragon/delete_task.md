# Grafana Operator - Delete via Task

## Input

```
[
    {
        "tetragon": {
            "operator": {
                "image": "image-name-as-provided-by-isovalent"
            },
            "crd": {
                "filename": [
                    "policy/policy.yaml"
                ]
            },
            "wipe": {}
        }
    }
]
```

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm
```

Notes:
- [crd](./delete_crd.md), [wipe](./delete_wipe.md) and [operator](./delete_operator.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some tasks or task parameters may be silently ignored
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies
- if you want to clean up setup, use "wipe" option in case some crds are not deleted in task way
- "wipe" option in [create task](./create_task.md) is ignored

## Requirements

None

## Configurable options

```
# iserver delete ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

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

OpenShift Workflow - Tetragon - Delete Policy
=============================================

OpenShift Cluster: bm1
File: policy/policy.yaml

TracingPolicy upper-layers already deleted

Completed tasks
- CRDs deleted

OpenShift Workflow - Tetragon - Delete Operator
===============================================

OpenShift Cluster: bm1

Operator
- subscription          : tetragon/tetragon-operator
- package               : tetragon/tetragon-catalog/tetragon-operator
- channel               : v1.18
- install plan          : tetragon/install-jk5j4
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
- wait for no Pod tetragon/tetragon-operator-646c4b6845-99fd7 [timeout:180s]
- wait for no DaemonSet tetragon/tetragon [timeout:180s]
- wait for no Pod tetragon/tetragon-5ggkq [timeout:180s]
- wait for no Pod tetragon/tetragon-ltgzf [timeout:180s]
- wait for no Pod tetragon/tetragon-p4nrr [timeout:180s]
Subscription tetragon resources gone

Delete CatalogSource
--------------------
- namespace: tetragon
- name: tetragon-catalog
- deleted
- wait for no CatalogSource tetragon/tetragon-catalog [timeout:60s]
- wait for no Pod tetragon/tetragon-catalog-f9nd7 [timeout:60s]

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
| 2  | ocp:bm1 | tetragon | delete crd      | 0       | V       | 1            | 
| 3  | ocp:bm1 | tetragon | delete operator | 6       | V       | 31           | 
+----+---------+----------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)