# Local Volume Set

## Get

```
# iserver get k8s locvd --cluster bm1
Cluster: bm1 (type: ocp)

+-------------------------+----------------+---------------+-------------+-----------+------------+---------+
| Namespace               | Name           | Storage Class | Volume Mode | Available | Disk Maker | Devices |
+-------------------------+----------------+---------------+-------------+-----------+------------+---------+
| openshift-local-storage | my-local-disks | local-sc      | Block       | ✓         | ✓          | 6       |
+-------------------------+----------------+---------------+-------------+-----------+------------+---------+

Filter: --
View:   state (def)
```

## Delete

```
# iserver delete k8s locvs
Cluster: bm1 (type: ocp)

LocalVolumeSet [#1]
-------------------

+-------------------------+----------------+---------------+-------------+-----------+------------+---------+
| Namespace               | Name           | Storage Class | Volume Mode | Available | Disk Maker | Devices |
+-------------------------+----------------+---------------+-------------+-----------+------------+---------+
| openshift-local-storage | my-local-disks | local-sc      | Block       | ✓         | ✓          | 4       |
+-------------------------+----------------+---------------+-------------+-----------+------------+---------+

+-------------------+-----------+-------+----------+-------+---------------+----------------+----------------+--------------------------------+-----+-------+
| Name              | Status    | Mode  | SC       | Size  | Access Mode   | CSI Driver     | CSI Handle     | Device                         | PVC | Age   |
+-------------------+-----------+-------+----------+-------+---------------+----------------+----------------+--------------------------------+-----+-------+
| local-pv-487bfb48 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef25d9 [bm1-2] | --  | 2h10m |
| local-pv-810111b0 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef2777 [bm1-1] | --  | 2h10m |
| local-pv-bf5ba6b4 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef25c1 [bm1-1] | --  | 2h10m |
| local-pv-c6bf5067 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef266c [bm1-2] | --  | 2h10m |
+-------------------+-----------+-------+----------+-------+---------------+----------------+----------------+--------------------------------+-----+-------+
Continue [Y/N]? y

Delete local volume sets
------------------------
- openshift-local-storage/my-local-disks
        REST API successful
        Wait for no local volume [timeout:360]...
```

[[Back]](./README.md)