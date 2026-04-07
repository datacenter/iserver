# NMState Operator - Delete Operator

[[Back]](./README.md)

## Workflow

- delete NodeNetworkConfigurationPolicy objects
- delete operator subscription
- delete operator group
- delete namespace

## Requirements

None

## Configurable options

```
# iserver delete ocp nmstate --mode operator
  --cluster TEXT         Cluster Name
```

## Example

```
python.exe .\iserver.py delete ocp nmstate

OpenShift Workflow - NMState Operator - Delete Operator
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-nmstate",
    "name": "kubernetes-nmstate-operator",
    "operator-group-name": "nmstate-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Delete Node Network Configuration Policies
------------------------------------------
- no nncp found

Delete Subscription
-------------------
- subscription: openshift-nmstate/kubernetes-nmstate-operator
- checking cluster service version...
- csv found and will be deleted: openshift-nmstate/kubernetes-nmstate-operator.4.18.0-202509241752
- wait for no subscription
- check cluster service version: openshift-nmstate/kubernetes-nmstate-operator.4.18.0-202509241752
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-nmstate/nmstate-console-plugin
- openshift-nmstate/nmstate-operator
- openshift-nmstate/nmstate-webhook

Delete Operator Group
---------------------
- namespace: openshift-nmstate
- name: kubernetes-nmstate-operator
- already deleted

Delete Namespace
----------------
- name: openshift-nmstate

Namespace [openshift-nmstate] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- NMState resources deleted
- NMState operator unconfigured and deleted
```

[[Back]](./README.md)