# Node Feature Discover Operator - Delete All

[[Back]](./README.md) [[Next]](./delete_task.md) [[Prev]](./delete_instance.md)

## HowTo

```
# iserver delete ocp nfd --cluster bm1 --mode all
```

## Workflow

- delete node feature discover instance
- wait for resources gone
- delete operator subscription
- delete operator group
- delete namespace

## Example

```
# iserver delete ocp nfd --cluster bm1 --mode all

OpenShift Workflow - Node Feature Discovery Operator - Delete Instance
======================================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-nfd/nfd
- package               : openshift-marketplace/redhat-operators/nfd
- channel               : stable
- install plan          : openshift-nfd/install-tfwcl
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

OpenShift Workflow - Node Feature Discovery Operator - Delete Operator
======================================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-nfd/nfd
- package               : openshift-marketplace/redhat-operators/nfd
- channel               : stable
- install plan          : openshift-nfd/install-tfwcl
- install plan approved : ✓
- installed csv         : nfd.4.21.0-202604140347
- latest_csv            : ✓


Delete Subscription
-------------------
- subscription: openshift-nfd/nfd
- checking cluster service version...
- csv found and will be deleted: openshift-nfd/nfd.4.21.0-202604140347
- wait for no subscription
- check cluster service version: openshift-nfd/nfd.4.21.0-202604140347
- wait for no csv
- wait for no Deployment openshift-nfd/nfd-controller-manager [timeout:180s]
- wait for no ReplicaSet openshift-nfd/nfd-controller-manager-6bb88d9dbf [timeout:180s]
- wait for no Pod openshift-nfd/nfd-controller-manager-6bb88d9dbf-2htbs [timeout:180s]
- wait for no Deployment openshift-nfd/nfd-master [timeout:180s]
- wait for DaemonSet openshift-nfd/nfd-worker [timeout:180s]
Subscription nfd resources gone

Delete OperatorGroup
--------------------
- namespace: openshift-nfd
- name: nfd-operator-group
- deleted
- wait for no OperatorGroup openshift-nfd/nfd-operator-group [timeout:60s]

Namespace [openshift-nfd] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- no user defined networks
- no cluster user defined networks

Delete Namespace
----------------
- name: openshift-nfd
- wait for no namespace

Completed tasks
- Subscription deleted
- Operator Group deleted
- Namespace deleted

+----+---------+-------+-----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow        | Changes | Success | Duration [s] |
+----+---------+-------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | nfd   | delete instance | 1       | ✓       | 2            | 
| 2  | ocp:bm1 | nfd   | delete operator | 4       | ✓       | 24           | 
+----+---------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[Next]](./delete_task.md) [[Prev]](./delete_instance.md)