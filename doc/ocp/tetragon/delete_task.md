# Grafana Operator - Delete via Task

## Input

```
[
    {
        "tetragon": {
            "operator": {
                "image": "image-name-as-provided-by-isovalent"
            },
            "prometheus": {},
            "wipe": {},
            "crd": {
                "crd": [
                  "filename-or-directory"
                ]
            }
        }
    }
]
```

Notes:
- [crd](./delete_crd.md), [prometheus](./disable_prometheus.md), [wipe](./delete_wipe.md) and [operator](./delete_operator.md) trigger workflow execution with optional input parameters
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
python.exe .\iserver.py delete ocp task --filename C:\tmp\task.json --cluster bm1 --no-confirm
OpenShift Cluster: bm1

Cluster: bm1 (type: ocp)

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Tetragon Operator - Wipe Resources
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "tetragon",
    "name": "tetragon-operator",
    "operator-group-name": "tetragon",
    "catalog-namespace": "tetragon",
    "catalog-name": "tetragon-catalog",
    "operator-cm-namespace": "tetragon",
    "operator-cm-name": "tetragon-operator-config",
    "cm-namespace": "tetragon",
    "cm-name": "tetragon-config",
    "sm-namespace": "tetragon",
    "sm-name": "tetragon",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Alert Rule
----------
- no resources found

Sandbox Policy
--------------
- no resources found

Sandbox Policy Namespaced
-------------------------
- no resources found

Tetragon Network Policy
-----------------------
- no resources found

Tetragon Network Policy Namespaced
----------------------------------
- no resources found

Tracing Policy
--------------
- upper-layers

Tracing Policy Namespaced
-------------------------
- no resources found

Completed tasks
- Tetragon resources deleted

OpenShift Workflow - Tetragon Operator - Delete Operator
========================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "tetragon",
    "name": "tetragon-operator",
    "operator-group-name": "tetragon",
    "catalog-namespace": "tetragon",
    "catalog-name": "tetragon-catalog",
    "operator-cm-namespace": "tetragon",
    "operator-cm-name": "tetragon-operator-config",
    "cm-namespace": "tetragon",
    "cm-name": "tetragon-config",
    "sm-namespace": "tetragon",
    "sm-name": "tetragon",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Alert Rule
----------
- no resources found

Sandbox Policy
--------------
- no resources found

Sandbox Policy Namespaced
-------------------------
- no resources found

Tetragon Network Policy
-----------------------
- no resources found

Tetragon Network Policy Namespaced
----------------------------------
- no resources found

Tracing Policy
--------------
- no resources found

Tracing Policy Namespaced
-------------------------
- no resources found
- no resources found

Delete Subscription
-------------------
- subscription: tetragon/tetragon-operator
- checking cluster service version...
- csv found and will be deleted: tetragon/tetragon-operator.v1.17.0
- wait for no subscription
- check cluster service version: tetragon/tetragon-operator.v1.17.0
- wait for no csv
Wait for deployments deleted (optional: True)...
- tetragon/tetragon-operator

Delete Catalog Source
---------------------
- namespace: tetragon
- name: tetragon-catalog
- wait for no catalog source
- wait for no catalog source pod

Delete Config Map
-----------------
- namespace: tetragon
- name: tetragon-config
- wait for no config map

Delete Config Map
-----------------
- namespace: tetragon
- name: tetragon-operator-config
- wait for no config map

Delete Service Monitor
----------------------
- namespace: tetragon
- name: tetragon
- wait for no service monitor

Delete Service
--------------
- namespace: tetragon
- name: tetragon
- wait for no service

Delete Operator Group
---------------------
- namespace: tetragon
- name: tetragon-operator
- already deleted

Delete Namespace
----------------
- name: tetragon

Namespace [tetragon] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace
```

[[Back]](./README.md)