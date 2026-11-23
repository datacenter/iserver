# Trident - Delete Operator

[[Back]](./README.md)

## Workflow

- delete trident operator subscription
- wait for resources deleted

## Requirements

None

## Configurable options

```
# iserver delete ocp trident --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp trident --cluster bm1 --mode operator

OpenShift Workflow - Trident Operator - Delete Operator
=======================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-operators/trident-operator
- package               : openshift-marketplace/certified-operators/trident-operator
- channel               : stable
- install plan          : openshift-operators/install-hv429
- install plan approved : V
- installed csv         : trident-operator.v26.2.0
- latest_csv            : V


Delete Subscription
-------------------
- subscription: openshift-operators/trident-operator
- checking cluster service version...
- csv found and will be deleted: openshift-operators/trident-operator.v26.2.0
- wait for no subscription
- check cluster service version: openshift-operators/trident-operator.v26.2.0
- wait for no csv
- wait for no Deployment openshift-operators/trident-operator [timeout:180s]
- wait for no ReplicaSet openshift-operators/trident-operator-5f4b49d487 [timeout:180s]
- wait for no Pod openshift-operators/trident-operator-5f4b49d487-cppq8 [timeout:180s]
- wait for no Deployment trident/trident-controller [timeout:180s]
- wait for no DaemonSet trident/trident-node-linux [timeout:180s]
Subscription trident resources gone

Completed tasks
- Subscription deleted
- Operator Group deleted
- Namespace deleted

+----+---------+---------+-----------------+---------+---------+--------------+
| ID | Target  | Scope   | Workflow        | Changes | Success | Duration [s] |
+----+---------+---------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | trident | delete operator | 2       | V       | 10           | 
+----+---------+---------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)