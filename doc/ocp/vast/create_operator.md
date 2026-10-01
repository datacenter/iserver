# VAST CSI - Create Operator

[[Back]](./README.md) [[kb]](./kb/operator.md)

## HowTo

```
# iserver set ocp vast --cluster bm1 --mode operator --no-confirm

# iserver set ocp vast --mode operator
  --cluster TEXT             Cluster Name
  --channel TEXT             Operator channel  [default: __default__]
  --no-confirm               Confirmation mode
```

## Workflow

- create `vast-csi` namespace
- create operator group
- create subscription

## Expected outcome

![OperatorCreate](../images/vast/operator_create.png)

## Example

```
# iserver set ocp vast --cluster bm1 --mode operator

OpenShift Workflow - VAST CSI Operator - Create Operator
========================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
Operator vast-csi-operator not found
Subscription not found vast-csi-operator

Create Namespace
----------------
- name: vast-csi

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: vast-csi
~~~
Namespace [vast-csi] created
Wait for namespace [timeout:60]...

Create OperatorGroup
--------------------
- namespace: vast-csi
- name: vast-operator-group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: vast-operator-group
  namespace: vast-csi
spec:
  targetNamespaces:
  - vast-csi
  upgradeStrategy: Default
~~~
OperatorGroup [vast-csi/vast-operator-group] created
- wait for OperatorGroup vast-csi/vast-operator-group [timeout:60s]

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
Install plan: install-dqzk5
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployment vast-csi/vast-csi-operator-controller-manager ready (optional: False, allow zero replicas: False, timeout: 600s)...

Operator
- subscription          : vast-csi/vast-csi-operator
- package               : openshift-marketplace/certified-operators/vast-csi-operator
- channel               : stable
- install plan          : vast-csi/install-dqzk5
- install plan approved : V
- installed csv         : vast-csi-operator.v2.6.4
- latest_csv            : V


Completed tasks
- Namespace created
- Operator Group created
- Subscription created

Completed tasks
- VAST CSI operator installed

+----+------------+-------+-----------------+---------+---------+--------------+
| ID | Target     | Scope | Workflow        | Changes | Success | Duration [s] |
+----+------------+-------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1    | vast  | create operator | 3       | V       | 45           | 
+----+------------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[kb]](./kb/operator.md)