# Tetragon Enterprise Operator - Delete Operator

## Workflow

- delete tetragon operator subscription
- delete catalog source
- delete operator group
- delete config maps in tetragon namespace
- delete service monitor and service
- delete namespace

## Requirements

No Tetragon CRD may exist. [Wipe](./delete_wipe.md) it first if needed.

## Configurable options

```
# iserver delete ocp tetragon --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp tetragon --cluster bm1 --mode operator

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

Delete Operator Group
---------------------
- namespace: tetragon
- name: tetragon-operator
- already deleted

Delete Service Monitor
----------------------
- namespace: tetragon
- name: tetragon
- already deleted

Delete Service
----------------------
- namespace: tetragon
- name: tetragon
- wait for no service

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