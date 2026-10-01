# VAST CSI - Delete Storage

[[Back]](./README.md) [[kb]](./kb/storage.md)

## HowTo

```
# iserver delete ocp vast --cluster bm1 --mode storage --filename C:\tmp\storage.yaml

# iserver delete ocp vast --cluster bm1 --mode storage --name storage-name

# iserver delete ocp vast --mode storage
  --cluster TEXT            Cluster Name
  --filename TEXT           VAST CSI CRD
  --no-confirm              Confirmation mode
```

## Workflow

- check vast csi [operator](./create_operator.md)
- delete `VastStorage` resource if exists
- wait for resources gone

## Example

```
# iserver delete ocp vast --cluster bm1 --mode storage --filename C:\tmp\storage.yaml

OpenShift Workflow - VAST CSI Operator - Storage Delete
=======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
- deployment vast-csi/vast-csi-operator-controller-manager ready

Delete VastStorage
------------------
- namespace: vast-csi
- name: vast-nfs
- deleted
- wait for no VastStorage vast-csi/vast-nfs [timeout:60s]

Completed tasks
- VAST CSI storage deleted

+----+---------+-------+----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow       | Changes | Success | Duration [s] |
+----+---------+-------+----------------+---------+---------+--------------+
| 1  | ocp:bm1 | vast  | delete storage | 1       | V       | 8            | 
+----+---------+-------+----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[kb]](./kb/storage.md)