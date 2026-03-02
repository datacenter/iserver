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

## Example (discover-all mode)

```
# iserver get ocp lso --cluster bm1

OpenShift Workflow - Local Storage Operator - Get Information
=============================================================

OpenShift Cluster: bm1

Local Storage Operator Subscription
-----------------------------------
- subscription: openshift-local-storage/local-storage-operator
- package: local-storage-operator
- csv: local-storage-operator.v4.18.0-202602132343

Local Storage Operator Resources
--------------------------------
- deployment openshift-local-storage/local-storage-operator ready
- 0 local volume
- 1 local volume set
- 1 local volume discovery
- 3 local volume discovery result

+----+-------------------------+-----------+-------------+
| ID | Local Volume Discovery  | Available | Phase       |
+----+-------------------------+-----------+-------------+
| 1  | openshift-local-storage | V         | Discovering | 
|    | auto-discover-devices   |           |             | 
+----+-------------------------+-----------+-------------+

+----+---------------------+-----------+----------+----------------------------------------+------------+---------------+------+--------+
| ID | LV Discovery Result | Available | Path     | WWN                                    | Size       | Property      | Type | FSType |
+----+---------------------+-----------+----------+----------------------------------------+------------+---------------+------+--------+
| 1  | bm1-1               | 10/14     | /dev/sdb | wwn-0x55cd2e414e3ba224                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sdc | wwn-0x500a07511c54a9e9                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sdd | wwn-0x55cd2e414e3ba1f8                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sde | wwn-0x5000c500af4a7bab                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sdf | wwn-0x55cd2e414e3bc3de                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sdg | wwn-0x5000c500af4a79cf                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sdh | wwn-0x5000c500af4a64bb                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sdi | wwn-0x5000c500af4a689b                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sdn | wwn-0x500a07511c5401fc                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sdo | wwn-0x55cd2e414e3ba1bd                 | 960.2 [GB] | NonRotational | disk |        | 
+----+---------------------+-----------+----------+----------------------------------------+------------+---------------+------+--------+
| 2  | bm1-2               | 10/14     | /dev/sda | wwn-0x55cd2e414e3b9850                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sdb | wwn-0x500a07511c54ae16                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sdc | wwn-0x500a07511c54a905                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sde | wwn-0x55cd2e414e3bc355                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sdf | wwn-0x5000c500af4a7c5b                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sdg | wwn-0x5000c500af4367db                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sdh | wwn-0x5000c500af4a76a7                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sdi | wwn-0x5000c500af4a68ef                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sdj | wwn-0x55cd2e414e3ba24a                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sdk | wwn-0x55cd2e414e3b9843                 | 960.2 [GB] | NonRotational | disk |        | 
+----+---------------------+-----------+----------+----------------------------------------+------------+---------------+------+--------+
| 3  | bm1-3               | 10/14     | /dev/sda | wwn-0x5000c500af4365ff                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sdb | wwn-0x5000c500af4a6c23                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sdc | wwn-0x5000c500af4a7b83                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sdd | wwn-0x5000c500af4a7c37                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sde | wwn-0x5000c500af4a62f3                 | 1.2 [TB]   | Rotational    | disk |        | 
|    |                     |           | /dev/sdf | wwn-0x55cd2e414e3bc38d                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sdg | wwn-0x500a07511c54a934                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sdh | wwn-0x500a07511c54a9fd                 | 960.2 [GB] | NonRotational | disk |        | 
|    |                     |           | /dev/sdi | wwn-0x6cc167e9736d2e40290bd43c2a70ef70 | 1.92 [TB]  | Rotational    | disk |        | 
|    |                     |           | /dev/sdk | wwn-0x55cd2e414e3ba1b2                 | 960.2 [GB] | NonRotational | disk |        | 
+----+---------------------+-----------+----------+----------------------------------------+------------+---------------+------+--------+

+----+---------------------+-------------+-----------+----------------------------------------------+-------------+------------+------+--------+
| ID | LV Discovery Result | Unavailable | Path      | WWN                                          | Size        | Property   | Type | FSType |
+----+---------------------+-------------+-----------+----------------------------------------------+-------------+------------+------+--------+
| 1  | bm1-1               | 10/14       | /dev/sdj1 | wwn-0x6cc167e973662d402b2222eac991d155-part1 | 1.05 [MB]   | Rotational | part |        | 
|    |                     |             | /dev/sdj2 | wwn-0x6cc167e973662d402b2222eac991d155-part2 | 133.17 [MB] | Rotational | part | vfat   | 
|    |                     |             | /dev/sdj3 | wwn-0x6cc167e973662d402b2222eac991d155-part3 | 402.65 [MB] | Rotational | part | ext4   | 
|    |                     |             | /dev/sdj4 | wwn-0x6cc167e973662d402b2222eac991d155-part4 | 1.2 [TB]    | Rotational | part | xfs    | 
+----+---------------------+-------------+-----------+----------------------------------------------+-------------+------------+------+--------+
| 2  | bm1-2               | 10/14       | /dev/sdd1 | wwn-0x6cc167e9736dad002b22899acfd6e42e-part1 | 1.05 [MB]   | Rotational | part |        | 
|    |                     |             | /dev/sdd2 | wwn-0x6cc167e9736dad002b22899acfd6e42e-part2 | 133.17 [MB] | Rotational | part | vfat   | 
|    |                     |             | /dev/sdd3 | wwn-0x6cc167e9736dad002b22899acfd6e42e-part3 | 402.65 [MB] | Rotational | part | ext4   | 
|    |                     |             | /dev/sdd4 | wwn-0x6cc167e9736dad002b22899acfd6e42e-part4 | 1.2 [TB]    | Rotational | part | xfs    | 
+----+---------------------+-------------+-----------+----------------------------------------------+-------------+------------+------+--------+
| 3  | bm1-3               | 10/14       | /dev/sdj1 | wwn-0x50000399c851c571-part1                 | 1.05 [MB]   | Rotational | part |        | 
|    |                     |             | /dev/sdj2 | wwn-0x50000399c851c571-part2                 | 133.17 [MB] | Rotational | part | vfat   | 
|    |                     |             | /dev/sdj3 | wwn-0x50000399c851c571-part3                 | 402.65 [MB] | Rotational | part | ext4   | 
|    |                     |             | /dev/sdj4 | wwn-0x50000399c851c571-part4                 | 1.2 [TB]    | Rotational | part | xfs    | 
+----+---------------------+-------------+-----------+----------------------------------------------+-------------+------------+------+--------+

+----+-------------------------+---------------+-------------+-----------+------------+-----------+
| ID | Local Volume Set        | Storage Class | Volume Mode | Available | Disk Maker | # Devices |
+----+-------------------------+---------------+-------------+-----------+------------+-----------+
| 1  | openshift-local-storage | local-sc      | Block       | V         | V          | 6         | 
|    | my-local-disks          |               |             |           |            |           | 
+----+-------------------------+---------------+-------------+-----------+------------+-----------+

+----+---------------+---------+------------------------------+----------------+----------------------+------------------------+----+
| ID | Storage Class | Default | Provisioner                  | Reclaim Policy | Volume Binding Mode  | Allow Volume Expansion | PV |
+----+---------------+---------+------------------------------+----------------+----------------------+------------------------+----+
| 1  | local-sc      |         | kubernetes.io/no-provisioner | Delete         | WaitForFirstConsumer | ---                    | 6  | 
+----+---------------+---------+------------------------------+----------------+----------------------+------------------------+----+

+----+-------------------+-----------+-------+----------+--------+--------+-----+-------+
| ID | Persistent Volume | Status    | Mode  | SC       | Size   | Access | PVC | Age   |
+----+-------------------+-----------+-------+----------+--------+--------+-----+-------+
| 1  | local-pv-1a28a040 | Available | Block | local-sc | 894Gi  | RWO    | --  | 2h28m | 
| 2  | local-pv-21e09790 | Available | Block | local-sc | 894Gi  | RWO    | --  | 2h28m | 
| 3  | local-pv-290dd896 | Available | Block | local-sc | 894Gi  | RWO    | --  | 2h28m | 
| 4  | local-pv-8476522  | Available | Block | local-sc | 894Gi  | RWO    | --  | 2h28m | 
| 5  | local-pv-bfe2de2d | Available | Block | local-sc | 1117Gi | RWO    | --  | 2h28m | 
| 6  | local-pv-d27c3b90 | Available | Block | local-sc | 1117Gi | RWO    | --  | 2h28m | 
+----+-------------------+-----------+-------+----------+--------+--------+-----+-------+
```

## Example (explicit mode)

```
# iserver get ocp lso --cluster bm1

OpenShift Workflow - Local Storage Operator - Get Information
=============================================================

OpenShift Cluster: bm1

Local Storage Operator Subscription
-----------------------------------
- subscription: openshift-local-storage/local-storage-operator
- package: local-storage-operator
- csv: local-storage-operator.v4.18.0-202602132343

Local Storage Operator Resources
--------------------------------
- deployment openshift-local-storage/local-storage-operator ready
- 2 local volume
- 0 local volume set
- 0 local volume discovery
- 0 local volume discovery result

+----+--------------------------+-------+------------------------+---------------+-------+
| ID | Local Volume             | Node  | Device                 | Storage Class | Mode  |
+----+--------------------------+-------+------------------------+---------------+-------+
| 1  | openshift-local-storage  | bm1-1 | wwn-0x55cd2e414e3ba224 | local-sc      | Block | 
|    | local-disks-28d64d3253f6 |       |                        |               |       | 
+----+--------------------------+-------+------------------------+---------------+-------+
| 2  | openshift-local-storage  | bm1-2 | wwn-0x500a07511c54ae16 | local-sc      | Block | 
|    | local-disks-8e19cf339648 |       |                        |               |       | 
+----+--------------------------+-------+------------------------+---------------+-------+

+----+---------------+---------+------------------------------+----------------+----------------------+------------------------+----+
| ID | Storage Class | Default | Provisioner                  | Reclaim Policy | Volume Binding Mode  | Allow Volume Expansion | PV |
+----+---------------+---------+------------------------------+----------------+----------------------+------------------------+----+
| 1  | local-sc      |         | kubernetes.io/no-provisioner | Delete         | WaitForFirstConsumer | ---                    | 2  | 
+----+---------------+---------+------------------------------+----------------+----------------------+------------------------+----+

+----+-------------------+-----------+-------+----------+-------+--------+-----+------+
| ID | Persistent Volume | Status    | Mode  | SC       | Size  | Access | PVC | Age  |
+----+-------------------+-----------+-------+----------+-------+--------+-----+------+
| 1  | local-pv-21e09790 | Available | Block | local-sc | 894Gi | RWO    | --  | 1h0m | 
| 2  | local-pv-290dd896 | Available | Block | local-sc | 894Gi | RWO    | --  | 1h0m | 
+----+-------------------+-----------+-------+----------+-------+--------+-----+------+
```

[[Back]](./README.md)