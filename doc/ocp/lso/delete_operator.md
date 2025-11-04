# Local Storage Operator - Delete operator

## Workflow

- check local volume, local volume set and local volume discovery resources (none is expected to continue)
- delete subscription
- delete operator group
- delete namespace

## Requirements

None

## Configurable options

```
# iserver set ocp lso --mode operator
  --cluster TEXT                Cluster Name
```

## Example

```
# iserver delete ocp lso --mode operator

OpenShift Workflow - Local Storage Operator - Delete Operator
=============================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-local-storage",
    "name": "local-storage-operator",
    "operator-group-name": "local-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Check Local Storage Operator Resources
--------------------------------------
- checking local volume...
- checking local volume set...
- checking local volume discovery...

Delete Subscription
-------------------
- subscription: openshift-local-storage/local-storage-operator
- checking cluster service version...
- csv found and will be deleted: openshift-local-storage/local-storage-operator.v4.18.0-202509240837
- wait for no subscription
- check cluster service version: openshift-local-storage/local-storage-operator.v4.18.0-202509240837
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-local-storage/local-storage-operator

Delete Operator Group
---------------------
- namespace: openshift-local-storage
- name: local-operator-group
- wait for no operator group

Delete Namespace
----------------
- name: openshift-local-storage

Namespace [openshift-local-storage] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- No volumes checked
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)