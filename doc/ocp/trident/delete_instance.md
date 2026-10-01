# Trident - Delete Instance

[[Back]](./README.md) [[Next]](./delete_task.md) [[Prev]](./delete_operator.md)

## HowTo

```
# iserver delete ocp trident --cluster bm1 --mode instance
```

## Workflow

- delete trident orchestrator instance
- wait for resources gone

## Example

```
# iserver delete ocp trident --cluster bm1 --mode instance

OpenShift Workflow - Trident Operator - Delete Instance
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


Delete TridentOrchestrator
--------------------------
- name: trident
- deleted
- wait for no TridentOrchestrator trident [timeout:60s]
- wait for no Deployment trident/trident-controller [timeout:180s]
- wait for no ReplicaSet trident/trident-controller-7f78d7cb96 [timeout:180s]
- wait for no Pod trident/trident-controller-7f78d7cb96-mf425 [timeout:180s]
- wait for no DaemonSet trident/trident-node-linux [timeout:180s]
- wait for no Pod trident/trident-node-linux-hvc8t [timeout:180s]
- wait for no Pod trident/trident-node-linux-jqndr [timeout:180s]
- wait for no Pod trident/trident-node-linux-n7lvx [timeout:180s]
Subscription trident resources gone

Completed tasks
- Trident orchestrator instances deleted

+----+---------+---------+-----------------+---------+---------+--------------+
| ID | Target  | Scope   | Workflow        | Changes | Success | Duration [s] |
+----+---------+---------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | trident | delete instance | 1       | V       | 7            | 
+----+---------+---------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[Next]](./delete_task.md) [[Prev]](./delete_operator.md)