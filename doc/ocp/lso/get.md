# Local Storage Operator - Get

## Workflow

- check lso storage operator subscription
- check local volume, local volume set and local volume discovery resources
- check storage class
- check persistent volumes

## Requirements

None

## Configurable options

```
# iserver get ocp lso 
  --cluster TEXT                Cluster Name
```

## Example (discovery mode)

```
# iserver get ocp lso

OpenShift Workflow - Local Storage Operator - Get Information
=============================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-local-storage",
    "name": "local-storage-operator",
    "operator-group-name": "local-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

Operator
--------
- subscription: openshift-local-storage/local-storage-operator
- channel: stable
- csv: local-storage-operator.v4.18.0-202509240837

Operator functional readiness
-----------------------------
ready

Local Volume Discovery [#1]
---------------------------

+-------------------------+-----------------------+-----------+-------------+
| Namespace               | Name                  | Available | Phase       |
+-------------------------+-----------------------+-----------+-------------+
| openshift-local-storage | auto-discover-devices | ✓         | Discovering |
+-------------------------+-----------------------+-----------+-------------+

Local Volume Discovery Result - Available Devices
-------------------------------------------------

+-------+---------+----------+------------------------+------------+---------------+------+--------+
| Node  | Summary | Path     | WWN                    | Size       | Property      | Type | FSType |
+-------+---------+----------+------------------------+------------+---------------+------+--------+
| bm1-1 | 2/6     | /dev/sdb | wwn-0x500a075118ef25c1 | 960.2 [GB] | NonRotational | disk |        |
|       |         | /dev/sdc | wwn-0x500a075118ef2777 | 960.2 [GB] | NonRotational | disk |        |
+-------+---------+----------+------------------------+------------+---------------+------+--------+
| bm1-2 | 2/6     | /dev/sdb | wwn-0x500a075118ef266c | 960.2 [GB] | NonRotational | disk |        |
|       |         | /dev/sdc | wwn-0x500a075118ef25d9 | 960.2 [GB] | NonRotational | disk |        |
+-------+---------+----------+------------------------+------------+---------------+------+--------+
| bm1-3 | 2/6     | /dev/sda | wwn-0x500a075118ef291c | 960.2 [GB] | NonRotational | disk |        |
|       |         | /dev/sdb | wwn-0x500a075118ef2616 | 960.2 [GB] | NonRotational | disk |        |
+-------+---------+----------+------------------------+------------+---------------+------+--------+

Local Volume Discovery Result - Unavailable Devices
---------------------------------------------------

+-------+-----------+----------------------------------------------+-------------+------------+------+--------+
| Node  | Path      | WWN                                          | Size        | Property   | Type | FSType |
+-------+-----------+----------------------------------------------+-------------+------------+------+--------+
| bm1-1 | /dev/sda1 | wwn-0x6cc167e973700fc029771bd1c31a36fa-part1 | 1.05 [MB]   | Rotational | part |        |
|       | /dev/sda2 | wwn-0x6cc167e973700fc029771bd1c31a36fa-part2 | 133.17 [MB] | Rotational | part |        |
|       | /dev/sda3 | wwn-0x6cc167e973700fc029771bd1c31a36fa-part3 | 402.65 [MB] | Rotational | part |        |
|       | /dev/sda4 | wwn-0x6cc167e973700fc029771bd1c31a36fa-part4 | 1.2 [TB]    | Rotational | part |        |
+-------+-----------+----------------------------------------------+-------------+------------+------+--------+
| bm1-2 | /dev/sda1 | wwn-0x6cc167e9737016c02968b46a8e803f3a-part1 | 1.05 [MB]   | Rotational | part |        |
|       | /dev/sda2 | wwn-0x6cc167e9737016c02968b46a8e803f3a-part2 | 133.17 [MB] | Rotational | part |        |
|       | /dev/sda3 | wwn-0x6cc167e9737016c02968b46a8e803f3a-part3 | 402.65 [MB] | Rotational | part |        |
|       | /dev/sda4 | wwn-0x6cc167e9737016c02968b46a8e803f3a-part4 | 1.2 [TB]    | Rotational | part |        |
+-------+-----------+----------------------------------------------+-------------+------------+------+--------+
| bm1-3 | /dev/sdc1 | wwn-0x6cc167e973700ac027abe4e420649a76-part1 | 1.05 [MB]   | Rotational | part |        |
|       | /dev/sdc2 | wwn-0x6cc167e973700ac027abe4e420649a76-part2 | 133.17 [MB] | Rotational | part |        | 
|       | /dev/sdc3 | wwn-0x6cc167e973700ac027abe4e420649a76-part3 | 402.65 [MB] | Rotational | part |        |
|       | /dev/sdc4 | wwn-0x6cc167e973700ac027abe4e420649a76-part4 | 1.2 [TB]    | Rotational | part |        |
+-------+-----------+----------------------------------------------+-------------+------------+------+--------+

LocalVolumeSet [#1]
-------------------

+-------------------------+----------------+---------------+-------------+-----------+------------+---------+
| Namespace               | Name           | Storage Class | Volume Mode | Available | Disk Maker | Devices |
+-------------------------+----------------+---------------+-------------+-----------+------------+---------+
| openshift-local-storage | my-local-disks | local-sc      | Block       | ✓         | ✓          | 6       |
+-------------------------+----------------+---------------+-------------+-----------+------------+---------+

Local Volume [#0]
-----------------
None

Storage Class [#1]
------------------

+----------+---------+------------------------------+----------------+----------------------+------------------------+----+
| Name     | Default | Provisioner                  | Reclaim Policy | Volume Binding Mode  | Allow Volume Expansion | PV |
+----------+---------+------------------------------+----------------+----------------------+------------------------+----+
| local-sc |         | kubernetes.io/no-provisioner | Delete         | WaitForFirstConsumer | None                   | 6  |
+----------+---------+------------------------------+----------------+----------------------+------------------------+----+

PV [#6]
-------

+-------------------+-----------+-------+----------+-------+---------------+----------------+----------------+--------------------------------+-----+-------+
| Name              | Status    | Mode  | SC       | Size  | Access Mode   | CSI Driver     | CSI Handle     | Device                         | PVC | Age   |
+-------------------+-----------+-------+----------+-------+---------------+----------------+----------------+--------------------------------+-----+-------+
| local-pv-487bfb48 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef25d9 [bm1-2] | --  | 2h11m |
| local-pv-810111b0 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef2777 [bm1-1] | --  | 2h11m |
| local-pv-8ff7b89e | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef291c [bm1-3] | --  | 2h11m |
| local-pv-bf5ba6b4 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef25c1 [bm1-1] | --  | 2h11m |
| local-pv-c6bf5067 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef266c [bm1-2] | --  | 2h11m |
| local-pv-fe6e649c | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef2616 [bm1-3] | --  | 2h11m |
+-------------------+-----------+-------+----------+-------+---------------+----------------+----------------+--------------------------------+-----+-------+
```

## Example (explicit mode)

```
# iserver get ocp lso

OpenShift Workflow - Local Storage Operator - Get Information
=============================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-local-storage",
    "name": "local-storage-operator",
    "operator-group-name": "local-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

Operator
--------
- subscription: openshift-local-storage/local-storage-operator
- channel: stable
- csv: local-storage-operator.v4.18.0-202509240837

Operator functional readiness
-----------------------------
ready

Local Volume Discovery [#0]
---------------------------
None

Local Volume Discovery Result - Available Devices
-------------------------------------------------
None

LocalVolumeSet [#0]
-------------------
None

Local Volume [#2]
-----------------

+-------------------------+--------------------------+-------+------------------------+---------------+-------+
| Namespace               | Name                     | Node  | Device                 | Storage Class | Mode  |
+-------------------------+--------------------------+-------+------------------------+---------------+-------+
| openshift-local-storage | local-disks-9771d08f5910 | bm1-1 | wwn-0x500a075118ef25c1 | local-sc      | Block |
| openshift-local-storage | local-disks-ab01fadc9907 | bm1-2 | wwn-0x500a075118ef266c | local-sc      | Block |
+-------------------------+--------------------------+-------+------------------------+---------------+-------+

Storage Class [#1]
------------------

+----------+---------+------------------------------+----------------+----------------------+------------------------+----+
| Name     | Default | Provisioner                  | Reclaim Policy | Volume Binding Mode  | Allow Volume Expansion | PV |
+----------+---------+------------------------------+----------------+----------------------+------------------------+----+
| local-sc |         | kubernetes.io/no-provisioner | Delete         | WaitForFirstConsumer | None                   | 2  |
+----------+---------+------------------------------+----------------+----------------------+------------------------+----+

PV [#2]
-------

+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+------+
| Name              | Status    | Mode  | SC       | Size  | Access Mode   | CSI Driver  | CSI Handle               | Device                         | PVC | Age  |
+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+------+
| local-pv-bf5ba6b4 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-9771d08f5910 | wwn-0x500a075118ef25c1 [bm1-1] | --  | 2h2m |
| local-pv-c6bf5067 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-ab01fadc9907 | wwn-0x500a075118ef266c [bm1-2] | --  | 2h2m |
+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+------+
```

[[Back]](./README.md)