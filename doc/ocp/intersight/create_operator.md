# Cisco Intersight Plugin - Install operator

[[Back]](./README.md) [[Next]](./create_instance.md) [[kb]](./kb/operator.md)

## Workflow

Checks
- operator should not be already installed

Action
- create namespace
- create operator group
- create subscription
- wait for resources

## Expected outcome

![Operator](../images/intersight/operator_create.png)

## Configurable options

```
# iserver set ocp intersight --mode operator
  --cluster TEXT     Cluster Name
  --channel TEXT     Operator channel  [default: __default__]
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp intersight --cluster bm1 --mode operator

OpenShift Workflow - Cisco Intersight Operator - Create Operator
================================================================

OpenShift Cluster: bm1
Subscription not found: cisco-intersight

Create Namespace
----------------
- name: cisco-intersight

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: cisco-intersight
~~~
Namespace [cisco-intersight] created
Wait for namespace [timeout:60]...

Create OperatorGroup
--------------------
- namespace: cisco-intersight
- name: cisco-intersight

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: cisco-intersight
  namespace: cisco-intersight
spec:
  targetNamespaces:
  - cisco-intersight
  upgradeStrategy: Default
~~~
OperatorGroup [cisco-intersight/cisco-intersight] created
- wait for OperatorGroup cisco-intersight/cisco-intersight [timeout:60s]

Create Subscription
-------------------
Subscription: cisco-intersight/cisco-intersight
Source: openshift-marketplace/certified-operators/cisco-intersight
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable
- CSV [cisco-intersight.v1.0.0]
- CSV Display name [Cisco Intersight]
- CVS Version [1.0.0]
- CSV Provider [{'name': 'Cisco Intersight', 'url': 'https://intersight.com/help/saas'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: cisco-intersight
  namespace: cisco-intersight
spec:
  channel: stable
  installPlanApproval: Automatic
  name: cisco-intersight
  source: certified-operators
  sourceNamespace: openshift-marketplace
~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-v758v
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployment cisco-intersight/cisco-intersight-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Subscription intersight ready

Operator
- subscription          : cisco-intersight/cisco-intersight
- package               : openshift-marketplace/certified-operators/cisco-intersight
- channel               : stable
- install plan          : cisco-intersight/install-v758v
- install plan approved : ✓
- installed csv         : cisco-intersight.v1.0.0
- latest_csv            : ✓


Completed tasks
- Namespace created
- Operator Group created
- Cisco intersight operator installed
```

[[Back]](./README.md) [[Next]](./create_instance.md) [[kb]](./kb/operator.md)