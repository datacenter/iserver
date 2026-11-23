# NVIDIA NIM Operator - Create Operator

## Workflow

- create subscription with user controlled channel or defaultChannelName
- wait for nim resources

## Requirements

None

## Expected outcome

![OperatorCreate](../images/nim/operator_create.png)

## Configurable options

```
# iserver set ocp nim --mode operator
  --cluster TEXT     Cluster Name
  --channel TEXT     Operator channel  [default: __default__]
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp nim --cluster bm1 --mode operator --no-confirm

OpenShift Workflow - NVIDIA NIM Operator - Create Operator
==========================================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: openshift-operators
- already defined

Create Subscription
-------------------
Subscription: openshift-operators/nim-operator-certified
Source: openshift-marketplace/certified-operators/nim-operator-certified
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable
- CSV [nim-operator-certified.v3.0.1]
- CSV Display name [The NVIDIA NIM Operator for Kubernetes]
- CVS Version [3.0.1]
- CSV Provider [{'name': 'NVIDIA'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: nim-operator-certified
  namespace: openshift-operators
spec:
  channel: stable
  installPlanApproval: Automatic
  name: nim-operator-certified
  source: certified-operators
  sourceNamespace: openshift-marketplace

~~~
Continue [Y/N]? y

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-gmggv
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-operators/k8s-nim-operator

Completed tasks
- Namespace created
- Operator Group created
- NVIDIA NIM operator installed
```

[[Back]](./README.md)