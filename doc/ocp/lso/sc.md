# Storage Class

```
# iserver get k8s sc -v res
Cluster: bm1 (type: ocp)

Storage Class [#1]
------------------

+----------+---------+------------------------------+----------------+----------------------+------------------------+-----+----+
| Name     | Default | Provisioner                  | Reclaim Policy | Volume Binding Mode  | Allow Volume Expansion | PVC | PV |
+----------+---------+------------------------------+----------------+----------------------+------------------------+-----+----+
| local-sc |         | kubernetes.io/no-provisioner | Delete         | WaitForFirstConsumer | None                   | --   | 2  |
+----------+---------+------------------------------+----------------+----------------------+------------------------+-----+----+

PV [#2]
-------

+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+--------+
| Name              | Status    | Mode  | SC       | Size  | Access Mode   | CSI Driver  | CSI Handle               | Device                         | PVC | Age    |
+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+--------+
| local-pv-bf5ba6b4 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-1e8768503e49 | wwn-0x500a075118ef25c1 [bm1-1] | --  | 14h30m |
| local-pv-c6bf5067 | Available | Block | local-sc | 894Gi | ReadWriteOnce | LocalVolume | local-disks-bad10c4184e5 | wwn-0x500a075118ef266c [bm1-2] | --  | 14h30m |
+-------------------+-----------+-------+----------+-------+---------------+-------------+--------------------------+--------------------------------+-----+--------+

Filter: namespace, name
View:   state (def), res
```

[[Back]](./README.md)