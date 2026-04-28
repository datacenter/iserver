# Node Feature Discover Operator - Delete Instance

[[Back]](./README.md) [[Next]](./delete_task.md) [[Prev]](./delete_operator.md)

## HowTo

```
# iserver delete ocp nfd --cluster bm1 --mode instance
```

## Workflow

- delete node feature discover instance
- wait for resources gone

## Example

```
# iserver delete ocp nfd --cluster bm1 --mode instance

OpenShift Workflow - Node Feature Discovery Operator - Delete Instance
======================================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-nfd/nfd
- package               : openshift-marketplace/redhat-operators/nfd
- channel               : stable
- install plan          : openshift-nfd/install-2pqw9
- install plan approved : ✓
- installed csv         : nfd.4.21.0-202604140347
- latest_csv            : ✓


Delete NodeFeatureDiscovery
---------------------------
- namespace: openshift-nfd
- name: nfd-instance
- deleted
- wait for no NodeFeatureDiscovery openshift-nfd/nfd-instance [timeout:60s]

Completed tasks
- Node feature discovery instances deleted

+----+---------+-------+-----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow        | Changes | Success | Duration [s] |
+----+---------+-------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | nfd   | delete instance | 1       | ✓       | 2            | 
+----+---------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[Next]](./delete_task.md) [[Prev]](./delete_operator.md)