# Local Storage Operator - Create Operator

## Workflow

- create openshift-local-storage namespace
  - annotations for node selector (optional)
  - annotations for sno (detected and automatic)
- create operator group
- create subscription

## Requirements

None

## Configurable options

```
# iserver set ocp lso --mode operator
  --cluster TEXT                Cluster Name
  --nso                         Enable node selector override namespace annotation [default: false]
  --channel TEXT                Operator channel  [default: __default__]
  --no-confirm                  Confirmation mode
```

## Expected Outcome

![OperatorCreate](../images/lso/operator_create.png)

## Example

```
# iserver set ocp lso --cluster bm1 --mode operator
OpenShift Cluster: bm1


OpenShift Workflow - Local Storage Operator - Create Operator
=============================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "node-selector-override": false,
    "channel": "__default__",
    "confirmation": true,
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


Create Namespace
----------------
- name: openshift-local-storage
- labels
        workload.openshift.io/allowed:management

~~~
apiVersion: v1
kind: Namespace
metadata:
  labels:
    workload.openshift.io/allowed: management
  name: openshift-local-storage

~~~
Continue [Y/N]? y

Namespace created

Wait for namespace [timeout:60]...

Check labels
- workload.openshift.io/allowed:management

Create Operator Group
---------------------
Operator group: openshift-local-storage/local-operator-group
Target namespaces: openshift-local-storage

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: local-operator-group
  namespace: openshift-local-storage
spec:
  targetNamespaces:
  - openshift-local-storage

~~~
Continue [Y/N]? y

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: openshift-local-storage/local-storage-operator
Source: openshift-marketplace/redhat-operators/local-storage-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable
- CSV [local-storage-operator.v4.18.0-202509240837]
- CSV Display name [Local Storage]
- CVS Version [4.18.0-202509240837]
- CSV Provider [{'name': 'Red Hat'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: local-storage-operator
  namespace: openshift-local-storage
spec:
  channel: stable
  installPlanApproval: Automatic
  name: local-storage-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace

~~~
Continue [Y/N]? y

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-r757s
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: False, allow zero replicas: False)...
- openshift-local-storage/local-storage-operator

Completed tasks
- Namespace created
- Operator Group created
- Local Storage Operator installed
```

[[Back]](./README.md)