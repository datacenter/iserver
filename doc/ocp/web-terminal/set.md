# CLI Web Terminal - Create Operator

## Workflow

- create subscription with user controlled channel or defaultChannelName
- wait for resources ready 

## Requirements

None

## Expected outcome

![OperatorCreate](../images/web-terminal/operator_create.png)

## Configurable options

```
# iserver set ocp cnv --mode operator
  --cluster TEXT                  Cluster Name
  --channel TEXT                  Operator channel  [default: __default__]
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver set ocp terminal --cluster bm1

OpenShift Workflow - Web Terminal Operator - Create Operator
============================================================

OpenShift Cluster: bm1
Subscription not found web-terminal

Create Namespace
----------------
- name: openshift-operators
- already created

Create Subscription
-------------------
Subscription: openshift-operators/web-terminal
Source: openshift-marketplace/redhat-operators/web-terminal
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: fast
- CSV [web-terminal.v1.16.0]
- CSV Display name [Web Terminal]
- CVS Version [1.16.0]
- CSV Provider [{'name': 'Red Hat'}]
- CSV Maturity [alpha]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: web-terminal
  namespace: openshift-operators
spec:
  channel: fast
  installPlanApproval: Automatic
  name: web-terminal
  source: redhat-operators
  sourceNamespace: openshift-marketplace
~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-zlp2x
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployment openshift-operators/web-terminal-controller ready (optional: True, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-operators/devworkspace-controller-manager ready (optional: True, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-operators/devworkspace-webhook-server ready (optional: True, allow zero replicas: False, timeout: 600s)...

Operator
- subscription          : openshift-operators/web-terminal
- package               : openshift-marketplace/redhat-operators/web-terminal
- channel               : fast
- install plan          : openshift-operators/install-zlp2x
- install plan approved : V
- installed csv         : web-terminal.v1.16.0
- latest_csv            : V


Completed tasks
- Namespace created
- Operator Group created
- Subscription created

+----+---------+----------+-----------------+---------+---------+--------------+
| ID | Target  | Scope    | Workflow        | Changes | Success | Duration [s] |
+----+---------+----------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | terminal | create operator | 1       | V       | 62           | 
+----+---------+----------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)