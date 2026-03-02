# VAST Operator - Create Operator

## Workflow

- create `vast-csi` namespace
- create operator group
- create subscription

## Requirements

None

## Configurable options

```
# iserver set ocp vast --mode operator
  --cluster TEXT             Cluster Name
  --channel TEXT             Operator channel  [default: __default__]
  --verbose                  Verbose output
  --no-confirm               Confirmation mode
```

## Expected outcome

![OperatorCreate](../images/vast/operator_create.png)

## Example

```
# iserver set ocp vast --cluster bm1 --mode operator

OpenShift Workflow - VAST CSI Operator - Create Operator
========================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
------------------------------
Operator vast-csi-operator not found

Create Namespace
----------------
- name: vast-csi

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: vast-csi

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: vast-csi/vast-operator-group
Target namespaces: vast-csi

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: vast-operator-group
  namespace: vast-csi
spec:
  targetNamespaces:
  - vast-csi

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: vast-csi/vast-csi-operator
Source: openshift-marketplace/certified-operators/vast-csi-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable
- CSV [vast-csi-operator.v2.6.4]
- CSV Display name [VAST CSI driver operator]
- CVS Version [2.6.4]
- CSV Provider [{'name': 'VASTData', 'url': 'https://www.vastdata.com'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: vast-csi-operator
  namespace: vast-csi
spec:
  channel: stable
  installPlanApproval: Automatic
  name: vast-csi-operator
  source: certified-operators
  sourceNamespace: openshift-marketplace

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-gwf5z
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: False, allow zero replicas: False)...
- vast-csi/vast-csi-operator-controller-manager

Completed tasks
- VAST CSI operator installed
```

[[Back]](./README.md)