# VAST CSI - Delete Driver

[[Back]](./README.md) [[kb]](./kb/driver.md)

## HowTo

```
# iserver delete ocp vast --cluster bm1 --mode driver --filename C:\tmp\driver.yaml

# iserver delete ocp vast --cluster bm1 --mode driver --name driver-name

# iserver delete ocp vast --mode driver
  --cluster TEXT            Cluster Name
  --filename TEXT           VAST CSI CRD
  --no-confirm              Confirmation mode
```

## Workflow

- check vast csi [operator](./create_operator.md)
- delete `VastCSIDriver` resource if exists
- wait for resources gone

## Example

```
# iserver delete ocp vast --cluster bm1 --mode driver --filename C:\tmp\driver.yaml

OpenShift Workflow - VAST CSI Operator - Delete Driver
======================================================

OpenShift Cluster: bm1

VAST CSI Operator Subscription
- subscription: vast-csi/vast-csi-operator
- package: vast-csi-operator
- csv: vast-csi-operator.v2.6.4

VAST CSI Operator Resources
- deployment vast-csi/vast-csi-operator-controller-manager ready

Delete VastCSIDriver
--------------------
- namespace: vast-csi
- name: nfs
- deleted
- wait for no VastCSIDriver vast-csi/nfs [timeout:60s]
- wait for no DaemonSet vast-csi/csi-vast-node [timeout:60s]
- wait for no Deployment vast-csi/csi-vast-controller [timeout:60s]

Completed tasks
- VAST CSI driver deleted

+----+---------+-------+---------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow      | Changes | Success | Duration [s] |
+----+---------+-------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | vast  | delete driver | 1       | V       | 7            | 
+----+---------+-------+---------------+---------+---------+--------------+
```

[[Back]](./README.md) [[kb]](./kb/driver.md)