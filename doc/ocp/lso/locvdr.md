# Local Volume Discovery Results

```
# iserver get k8s locvd --cluster bm1
Cluster: bm1 (type: ocp)

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

+-------+---------+-----------+----------------------------------------------+-------------+------------+------+--------+
| Node  | Summary | Path      | WWN                                          | Size        | Property   | Type | FSType |
+-------+---------+-----------+----------------------------------------------+-------------+------------+------+--------+
| bm1-1 | 2/6     | /dev/sda1 | wwn-0x6cc167e973700fc029771bd1c31a36fa-part1 | 1.05 [MB]   | Rotational | part |        |
|       |         | /dev/sda2 | wwn-0x6cc167e973700fc029771bd1c31a36fa-part2 | 133.17 [MB] | Rotational | part |        |
|       |         | /dev/sda3 | wwn-0x6cc167e973700fc029771bd1c31a36fa-part3 | 402.65 [MB] | Rotational | part |        |
|       |         | /dev/sda4 | wwn-0x6cc167e973700fc029771bd1c31a36fa-part4 | 1.2 [TB]    | Rotational | part |        |
+-------+---------+-----------+----------------------------------------------+-------------+------------+------+--------+
| bm1-2 | 2/6     | /dev/sda1 | wwn-0x6cc167e9737016c02968b46a8e803f3a-part1 | 1.05 [MB]   | Rotational | part |        |
|       |         | /dev/sda2 | wwn-0x6cc167e9737016c02968b46a8e803f3a-part2 | 133.17 [MB] | Rotational | part |        |
|       |         | /dev/sda3 | wwn-0x6cc167e9737016c02968b46a8e803f3a-part3 | 402.65 [MB] | Rotational | part |        |
|       |         | /dev/sda4 | wwn-0x6cc167e9737016c02968b46a8e803f3a-part4 | 1.2 [TB]    | Rotational | part |        |
+-------+---------+-----------+----------------------------------------------+-------------+------------+------+--------+
| bm1-3 | 2/6     | /dev/sdc1 | wwn-0x6cc167e973700ac027abe4e420649a76-part1 | 1.05 [MB]   | Rotational | part |        |
|       |         | /dev/sdc2 | wwn-0x6cc167e973700ac027abe4e420649a76-part2 | 133.17 [MB] | Rotational | part |        | 
|       |         | /dev/sdc3 | wwn-0x6cc167e973700ac027abe4e420649a76-part3 | 402.65 [MB] | Rotational | part |        |
|       |         | /dev/sdc4 | wwn-0x6cc167e973700ac027abe4e420649a76-part4 | 1.2 [TB]    | Rotational | part |        |
+-------+---------+-----------+----------------------------------------------+-------------+------------+------+--------+

Filter: --
View:   state (def)
```

[[Back]](./README.md)