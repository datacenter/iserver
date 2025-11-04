# Splunk Operator - Create Operator

## Workflow

- create splunk operator namespace 
- create operator group
- create subscription with user controlled channel or defaultChannelName
- wait for resources ready

## Requirements

None

## Configurable options

```
# iserver set ocp splunk --mode operator
  --cluster TEXT                  Cluster Name
  --channel TEXT                  Operator channel  [default: __default__]
  --no-confirm                    Confirmation mode
```

## Non-configurable defaults

```
{
    "namespace": "splunk-operator",
    "name": "splunk-operator",
    "operator-group-name": "splunk-operator-group"
}
```

## Expected Outcome

![OperatorCreate](../images/splunk/operator_create.png)

## Example

```
# iserver set ocp splunk --mode operator --no-confirm

OpenShift Workflow - Splunk Operator - Create Operator
======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "channel": "__default__",
    "confirmation": false,
    "check-verbose": true,
    "namespace": "splunk-operator",
    "name": "splunk-operator",
    "operator-group-name": "splunk-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Create Namespace
----------------
- name: splunk-operator

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: splunk-operator

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: splunk-operator/splunk-operator-group
Target namespaces: splunk-operator

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: splunk-operator-group
  namespace: splunk-operator
spec:
  targetNamespaces:
  - splunk-operator

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: splunk-operator/splunk-operator
Source: openshift-marketplace/certified-operators/splunk-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable
- CSV [splunk-operator.v3.0.0]
- CSV Display name [Splunk Operator]
- CVS Version [3.0.0]
- CSV Provider [{'name': 'Splunk Inc.', 'url': 'www.splunk.com'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: splunk-operator
  namespace: splunk-operator
spec:
  channel: stable
  installPlanApproval: Automatic
  name: splunk-operator
  source: certified-operators
  sourceNamespace: openshift-marketplace

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-n66z7
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- splunk-operator/splunk-operator-controller-manager

Completed tasks
- Namespace created
- Operator Group created
- Splunk Operator installed
```

[[Back]](./README.md)