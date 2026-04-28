# Node Feature Discovery Operator - Create Operator

[[Back]](./README.md) [[Next]](./create_instance.md) [[Prev]](./get.md)

## HowTo

```
# iserver set ocp nfd --cluster bm1 --mode operator --no-confirm

# iserver set ocp nfd --mode operator
  --cluster TEXT     Cluster Name
  --channel TEXT     Operator channel  [default: __default__]
  --no-confirm       Confirmation mode
```

## Workflow

- create openshift-nfd namespace
- create operator group
- create subscription with user controlled channel or defaultChannelName

## Requirements

None

## Expected outcome

![OperatorCreate](../images/nfd/operator_create.png)

## Example

```
# iserver set ocp nfd --cluster bm1 --mode operator --no-confirm

OpenShift Workflow - Node Feature Discovery Operator - Create Operator
======================================================================

OpenShift Cluster: bm1
Subscription not found nfd

Create Namespace
----------------
- name: openshift-nfd

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-nfd
~~~
Namespace [openshift-nfd] created
Wait for namespace [timeout:60]...

Create OperatorGroup
--------------------
- namespace: openshift-nfd
- name: nfd-operator-group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: nfd-operator-group
  namespace: openshift-nfd
spec:
  targetNamespaces:
  - openshift-nfd
  upgradeStrategy: Default
~~~
OperatorGroup [openshift-nfd/nfd-operator-group] created
- wait for OperatorGroup openshift-nfd/nfd-operator-group [timeout:60s]

Create Subscription
-------------------
Subscription: openshift-nfd/nfd
Source: openshift-marketplace/redhat-operators/nfd
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable
- CSV [nfd.4.21.0-202604140347]
- CSV Display name [Node Feature Discovery Operator]
- CVS Version [4.21.0-202604140347]
- CSV Provider [{'name': 'Red Hat', 'url': 'https://github.com/openshift/cluster-nfd-operator'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: nfd
  namespace: openshift-nfd
spec:
  channel: stable
  installPlanApproval: Automatic
  name: nfd
  source: redhat-operators
  sourceNamespace: openshift-marketplace
~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-2pqw9
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployment openshift-nfd/nfd-controller-manager ready (optional: False, allow zero replicas: False, timeout: 600s)...
Subscription nfd ready

Operator
- subscription          : openshift-nfd/nfd
- package               : openshift-marketplace/redhat-operators/nfd
- channel               : stable
- install plan          : openshift-nfd/install-2pqw9
- install plan approved : ✓
- installed csv         : nfd.4.21.0-202604140347
- latest_csv            : ✓


Completed tasks
- Namespace created
- Operator Group created
- Subscription created

+----+---------+-------+-----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow        | Changes | Success | Duration [s] |
+----+---------+-------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | nfd   | create operator | 3       | ✓       | 30           | 
+----+---------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[Next]](./create_instance.md) [[Prev]](./get.md)