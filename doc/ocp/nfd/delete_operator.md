# Node Feature Discover Operator - Delete Operator

## Workflow

- delete node feature discover instance
- delete operator subscription
- delete operator group
- delete namespace

## Requirements

None

## Configurable options

```
# iserver delete ocp nfd --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp nfd       
OpenShift Cluster: bm1


OpenShift Workflow - Node Feature Discover Operator - Delete Operator
=====================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-nfd",
    "name": "nfd",
    "operator-group-name": "nfd-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Delete Node Feature Discovery Instances
---------------------------------------
- openshift-nfd/nfd-instance
- wait for no nfd instance

Delete Subscription
-------------------
- subscription: openshift-nfd/nfd
- checking cluster service version...
- csv found and will be deleted: openshift-nfd/nfd.4.18.0-202509240837
- wait for no subscription
- check cluster service version: openshift-nfd/nfd.4.18.0-202509240837
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-nfd/nfd-controller-manager
- openshift-nfd/nfd-master
Wait for deamon sets deleted...
- openshift-nfd/nfd-worker

Delete Operator Group
---------------------
- namespace: openshift-nfd
- name: nfd-operator-group
- wait for no operator group

Delete Namespace
----------------
- name: openshift-nfd

Namespace [openshift-nfd] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- NFD instances deleted
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)