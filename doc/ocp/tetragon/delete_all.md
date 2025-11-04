# Tetragon Enterprise Operator - Delete All

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
python.exe .\iserver.py delete ocp tetragon --mode all

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
- no resources found

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