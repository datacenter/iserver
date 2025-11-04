# LVM Storage Operator - Delete operator

## Workflow

- delete LVM storage operator subscription
- delete operator group
- delete namespace

## Requirements

LVM Cluster instance must not exist.

## Configurable options

```
# iserver delete ocp lvm --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp lvm --mode operator

OpenShift Workflow - LVM Operator - Delete Operator
===================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-storage",
    "name": "lvms-operator",
    "operator-group-name": "lvm-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Delete Subscription
-------------------
- subscription: openshift-storage/lvms-operator
- checking cluster service version...
- csv found and will be deleted: openshift-storage/lvms-operator.v4.18.3
- wait for no subscription
- check cluster service version: openshift-storage/lvms-operator.v4.18.3
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-storage/lvms-operator
Wait for deamon sets deleted...
- openshift-storage/vg-manager

Delete Operator Group
---------------------
- namespace: openshift-storage
- name: openshift-storage-operatorgroup
- wait for no operator group

Delete Namespace
----------------
- name: openshift-storage

Namespace [openshift-storage] resources
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