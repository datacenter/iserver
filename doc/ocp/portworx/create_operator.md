# MinIO AIStor Operator - Create Operator

## Workflow

- create openshift-minio namespace
- create operator group
- create subscription with user controlled channel or defaultChannelName
- wait for operator resources

Reference [documentation](https://docs.min.io/enterprise/aistor-object-store/installation/kubernetes/install/deploy-aistor-on-openshift/)

## Requirements

None

## Expected outcome

![OperatorCreate](../images/minio/operator_create.png)

## Configurable options

```
# iserver set ocp minio --mode operator
  --cluster TEXT     Cluster Name
  --channel TEXT     Operator channel  [default: __default__]
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp minio --mode operator --cluster bm1 --no-confirm


OpenShift Workflow - MinIO Operator - Create Operator
=====================================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: aistor

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: aistor

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: aistor/minio-operator-group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: minio-operator-group
  namespace: aistor
spec:
  upgradeStrategy: Default

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: aistor/minio-object-store-operator
Source: openshift-marketplace/certified-operators/minio-object-store-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable
- CSV [minio-object-store-operator.v2025.8.19175300]
- CSV Display name [Minio AIStor Object Store]
- CVS Version [2025.8.19175300]
- CSV Provider [{'name': 'MinIO', 'url': 'https://min.io'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: minio-object-store-operator
  namespace: aistor
spec:
  channel: stable
  installPlanApproval: Automatic
  name: minio-object-store-operator
  source: certified-operators
  sourceNamespace: openshift-marketplace
  startingCSV: minio-object-store-operator.v2025.8.19175300

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-rgttr
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...

Completed tasks
- Namespace created
- Operator Group created
- MinIO operator installed
```

[[Back]](./README.md)