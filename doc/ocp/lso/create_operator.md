# Local Storage Operator - Create Operator

## Workflow

- create `openshift-local-storage` namespace
- create operator group
- create subscription

LSO by default selects only the worker nodes for local disk resources and local volumes creation i.e., management and infrastructure node are excluded
- in case of Single Node OpenShift (SNO) deployment, the `openshift-local-storage` namespace is automatically annotated with `workload.openshift.io/allowed:management` to allow LSO to run on the management CPU pool
- in case of infrastructure node, the `openshift-local-storage` namespace can be annotated with `openshift.io/node-selector:''` if enabled with --nso flag

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

## Expected outcome

![OperatorCreate](../images/lso/operator_create.png)

## Example

```
# iserver set ocp lso --cluster bm1 --mode operator

OpenShift Workflow - Local Storage Operator - Create Operator
=============================================================

OpenShift Cluster: bm1

Local Storage Operator Subscription
-----------------------------------
Operator local-storage-operator not found

Create Namespace
----------------
- name: openshift-local-storage

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-local-storage

~~~

Namespace created

Wait for namespace [timeout:60]...

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
- CSV [local-storage-operator.v4.18.0-202602132343]
- CSV Display name [Local Storage]
- CVS Version [4.18.0-202602132343]
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

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-kmw2r
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