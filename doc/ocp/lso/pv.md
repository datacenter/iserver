# Persistent Volume

```
# iserver get k8s locvd --cluster bm1
Cluster: bm1 (type: ocp)

+-------------------+-----------+-------+----------+-------+---------------+----------------+----------------+--------------------------------+-----+--------+
| Name              | Status    | Mode  | SC       | Size  | Access Mode   | CSI Driver     | CSI Handle     | Device                         | PVC | Age    |
+-------------------+-----------+-------+----------+-------+---------------+----------------+----------------+--------------------------------+-----+--------+
| local-pv-487bfb48 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef25d9 [bm1-2] | --  | 11h20m |
| local-pv-810111b0 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef2777 [bm1-1] | --  | 11h20m |
| local-pv-8ff7b89e | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef291c [bm1-3] | --  | 11h20m |
| local-pv-bf5ba6b4 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef25c1 [bm1-1] | --  | 11h20m |
| local-pv-c6bf5067 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef266c [bm1-2] | --  | 11h20m |
| local-pv-fe6e649c | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolumeSet | my-local-disks | wwn-0x500a075118ef2616 [bm1-3] | --  | 11h20m |
+-------------------+-----------+-------+----------+-------+---------------+----------------+----------------+--------------------------------+-----+--------+

Filter: name
View:   state (def)
```

[[Back]](./README.md)