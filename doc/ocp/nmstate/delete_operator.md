# NMState Operator - Delete Operator

[[Back]](./README.md)

## Workflow

- nmstate instance must not exist
- delete operator subscription
- delete operator group
- delete namespace

## Requirements

None

## Configurable options

```
# iserver delete ocp nmstate --mode operator
  --cluster TEXT         Cluster Name
```

## Example

```
# iserver delete ocp nmstate


OpenShift Workflow - NMState Operator - Delete Operator
=======================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-nmstate/kubernetes-nmstate-operator
- package               : openshift-marketplace/redhat-operators/kubernetes-nmstate-operator
- channel               : stable
- install plan          : openshift-nmstate/install-sh6mx
- install plan approved : ✓
- installed csv         : kubernetes-nmstate-operator.4.21.0-202609301335
- latest_csv            : ✓


Delete Subscription
-------------------
- subscription: openshift-nmstate/kubernetes-nmstate-operator
- checking cluster service version...
- csv found and will be deleted: openshift-nmstate/kubernetes-nmstate-operator.4.21.0-202609301335
- wait for no subscription
- check cluster service version: openshift-nmstate/kubernetes-nmstate-operator.4.21.0-202609301335
- wait for no csv
Wait for no Deployment openshift-nmstate/nmstate-controller-manager [timeout:180s]
Wait for no Deployment openshift-nmstate/nmstate-console-plugin [timeout:180s]
Wait for no Deployment openshift-nmstate/nmstate-metrics [timeout:180s]
Wait for no Deployment openshift-nmstate/nmstate-webhook [timeout:180s]
Wait for no DaemonSet openshift-nmstate/nmstate-handler [timeout:180s]
Subscription nmstate resources gone

Delete OperatorGroup
--------------------
- namespace: openshift-nmstate
- name: nmstate-operator-group
- deleted
Wait for no OperatorGroup openshift-nmstate/nmstate-operator-group [timeout:60s]

Delete Namespace
----------------
- name: openshift-nmstate

Namespace [openshift-nmstate] resources
- no deployments
- no daemon_sets
- no replica_sets
- no pods
- no services
- no pvcs
- no jobs
Wait for no Namespace openshift-nmstate [timeout:60s]

Completed tasks
- Subscription deleted
- Operator Group deleted
- Namespace deleted

+----+---------+---------+-----------------+---------+---------+--------------+
| ID | Target  | Scope   | Workflow        | Changes | Success | Duration [s] |
+----+---------+---------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | nmstate | delete operator | 4       | ✓       | 20           | 
+----+---------+---------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)