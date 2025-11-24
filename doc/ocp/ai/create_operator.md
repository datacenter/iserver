# Data Science (AI) Operator - Create Operator

## Workflow

- create redhat-ods-operator namespace
- create operator group
- create subscription with user controlled channel or defaultChannelName
- wait for operator resources
- wait for auth ready
- wait for data science cluster initialization ready

## Requirements

None

## Expected outcome

![OperatorCreate](../images/ai/operator_create.png)

![OperatorResources](../images/ai/operator_resources.png)

## Configurable options

```
# iserver set ocp ai --mode operator
  --cluster TEXT     Cluster Name
  --channel TEXT     Operator channel  [default: __default__]
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp ai --cluster bm1 --mode operator --no-confirm


OpenShift Workflow - Data Science (AI) - Create Operator
========================================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: redhat-ods-operator

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: redhat-ods-operator

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: redhat-ods-operator/ods-operator-group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: ods-operator-group
  namespace: redhat-ods-operator
spec:
  upgradeStrategy: Default

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: redhat-ods-operator/rhods-operator
Source: openshift-marketplace/redhat-operators/rhods-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable
- CSV [rhods-operator.2.25.0]
- CSV Display name [Red Hat OpenShift AI]
- CVS Version [2.25.0]
- CSV Provider [{'name': 'Red Hat, Inc.'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: rhods-operator
  namespace: redhat-ods-operator
spec:
  channel: stable
  installPlanApproval: Automatic
  name: rhods-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-fpq55
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- redhat-ods-operator/rhods-operator
Wait for data science cluster initialization...
default-dsci
Wait for data science cluster initialization [default-dsci] ready...
Wait for auth...
auth
Wait for auth [auth] ready...

Completed tasks
- Namespace created
- Operator Group created
- Data Science (AI) Operator installed
- Data Science Cluster Initialization ready
- Auth ready
```

[[Back]](./README.md)