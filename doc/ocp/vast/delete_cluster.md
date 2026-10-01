# VAST CSI - Delete Cluster

[[Back]](./README.md) [[kb]](./kb/cluster.md)

## HowTo

```
# iserver delete ocp vast --cluster bm1 --mode cluster --filename C:\tmp\cluster.yaml

# iserver delete ocp vast --cluster bm1 --mode cluster --name cluster-name

# iserver delete ocp vast --mode cluster
  --cluster TEXT            Cluster Name
  --filename TEXT           VAST CSI CRD
  --no-confirm              Confirmation mode
```

## Workflow

- check vast csi [operator](./create_operator.md)
- delete `VastCluster` resource if exists
- wait for resources gone

## Example

```
# iserver delete ocp vast --cluster bm1 --mode cluster --filename C:\tmp\cluster.yaml

OpenShift Workflow - VAST CSI Operator - Delete Cluster
=======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
- deployment vast-csi/vast-csi-operator-controller-manager ready

Delete VastCluster
------------------
- namespace: vast-csi
- name: my-vast
- deleted
- wait for no VastCluster vast-csi/my-vast [timeout:60s]

Completed tasks
- VAST CSI cluster deleted

+----+---------+-------+----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow       | Changes | Success | Duration [s] |
+----+---------+-------+----------------+---------+---------+--------------+
| 1  | ocp:bm1 | vast  | delete cluster | 1       | V       | 7            | 
+----+---------+-------+----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[kb]](./kb/cluster.md)