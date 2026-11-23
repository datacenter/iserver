# Migration Toolkit for Virtualization - Get State

## Workflow

- get mtv operator state
- collect mtv related crds

## Example

```
# iserver get ocp mtv --cluster bm1

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Get Information
====================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

Mtv Forklift Controller
- namespace: openshift-mtv
- name: forklift-controller
- ready

+----+----------+-----------+--------+---------------------------+-------------+-------------+
| ID | Provider | Type      | Status | Endpoint                  | Network Map | Storage Map |
+----+----------+-----------+--------+---------------------------+-------------+-------------+
| 1  | host     | openshift | Ready  |                           | 2/2         | 2/2         |
| 2  | vc       | vsphere   | Ready  | https://vc.domain.com/sdk | 2/2         | 2/2         |
+----+----------+-----------+--------+---------------------------+-------------+-------------+

+----+----------------+---------+------+-----+------+---------------+--------------------+-----------+--------------+
| ID | Migration Plan | State   | Type | Src | Dest | Network       | Storage            | Source VM | Phase        |
+----+----------------+---------+------+-----+------+---------------+--------------------+-----------+--------------+
| 1  | openshift-mtv  | Running | cold | vc  | host | openshift-mtv | openshift-mtv      | usmall    | ConvertGuest |
|    | mtv1           |         |      |     |      | mtv1-vc-nets  | mtv1-vc-ds         |           |              |
|    |                |         |      |     |      | my-dvs => pod | my-nas => lvms-vg1 |           |              |
+----+----------------+---------+------+-----+------+---------------+--------------------+-----------+--------------+

+----+---------------+------+------------+--------------------------------------------------------------------------------------+
| ID | Migration     | Plan | Conditions | State                                                                                |
+----+---------------+------+------------+--------------------------------------------------------------------------------------+
| 1  | openshift-mtv | mtv1 | Ready      | VM [usmall] Phase [ConvertGuest]                                                     |
|    | mtv1-lnb5s    |      | Running    | VM [usmall] PVC [default/mtv1-vm-61951-q4nd4] Capacity [None] Phase [Pending]        |
|    |               |      |            | VM [usmall] DV [default/mtv1-vm-61951-q4nd4] Progress [N/A] Phase [ImportInProgress] |
|    |               |      |            | VM [usmall] Pod [default/mtv1-vm-61951-z2ztd] Phase [Pending]                        |
+----+---------------+------+------------+--------------------------------------------------------------------------------------+
```

[[Back]](./README.md)