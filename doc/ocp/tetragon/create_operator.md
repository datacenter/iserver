# Tetragon Enterprise Operator - Create Operator

## Workflow

- create tetragon namespace 
- create operator group
- create catalog source with user-defined image
- create subscription with user controlled channel or defaultChannelName

## Requirements

Image value is required to install Tetragon Enterprise operator. Contact Isovalent@Cisco.

## Configurable options

```
# iserver set ocp tetragon --mode operator
  --cluster TEXT            Cluster Name
  --channel TEXT            Operator channel  [default: __default__]
  --image TEXT              Tetragon Enterprise Operator image
  --no-confirm              Confirmation mode
```

## Expected Outcome

![OperatorCreate](../images/tetragon/operator_create.png)

## Example

```
# iserver set ocp tetragon --mode operator --cluster bm1 --image image-name-as-provided-by-isovalent --no-confirm

OpenShift Workflow - Tetragon Operator - Create Operator
========================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "channel": "__default__",
    "image": "user-defined",
    "confirmation": false,
    "check-verbose": true,
    "namespace": "tetragon",
    "name": "tetragon-operator",
    "operator-group-name": "tetragon",
    "catalog-namespace": "tetragon",
    "catalog-name": "tetragon-catalog",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Create Namespace
----------------
- name: tetragon
- labels
        openshift.io/user-monitoring:true

~~~
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/user-monitoring: 'true'
  name: tetragon

~~~

Namespace created

Wait for namespace [timeout:60]...

Check labels
- openshift.io/user-monitoring:true

Create Operator Group
---------------------
Operator group: tetragon/tetragon

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: tetragon
  namespace: tetragon
spec:
  upgradeStrategy: Default

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Catalog Source
---------------------
- namespace: tetragon
- name: tetragon-catalog
- source: grpc

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: tetragon-catalog
  namespace: tetragon
spec:
  image: user-provided
  sourceType: grpc

~~~

Catalog source created

Wait for catalog source [timeout:60]...
Wait for tetragon package...

Create Subscription
-------------------
Subscription: tetragon/tetragon-operator
Source: tetragon/tetragon-catalog/tetragon-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: v1.17
- CSV [tetragon-operator.v1.17.0]
- CSV Display name [Tetragon Operator]
- CVS Version [1.17.0]
- CSV Provider [{'name': 'Isovalent', 'url': 'https://isovalent.com'}]
- CSV Maturity [alpha]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  labels:
    operators.coreos.com/tetragon-operator.tetragon: ''
  name: tetragon-operator
  namespace: tetragon
spec:
  channel: v1.17
  installPlanApproval: Automatic
  name: tetragon-operator
  source: tetragon-catalog
  sourceNamespace: tetragon

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-2l8ht
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- tetragon/tetragon-operator

Completed tasks
- Namespace created
- Operator Group created
- Tetragon Operator installed
```

[[Back]](./README.md)