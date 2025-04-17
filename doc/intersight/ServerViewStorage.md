# Intersight Server

## storage view

```
# iserver get server --group test -v storage

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Storage Controller [#16]
------------------------

+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server    | Controller  | Model                          | Vendor            | Serial | Presence | PCI Slot    | Raid Support | PD | VD |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server373 | MRAID       | Cisco 12G Modular Raid         | LSI Logic         | SN-75  | equipped | MRAID       | yes          | 10 | 1  |
|           |             | Controller with 2GB cache      |                   |        |          |             |              |    |    |
|           |             | (max 16 drives)                |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server373 | PCIe-Switch | --                             | Cisco Systems Inc | SN-70  | equipped | PCIe-Switch | N/A          | 0  | 0  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server403 | MRAID       | Cisco 12G Modular Raid         | LSI Logic         | SN-49  | equipped | MRAID       | yes          | 10 | 1  |
|           |             | Controller with 2GB cache      |                   |        |          |             |              |    |    |
|           |             | (max 16 drives)                |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server403 | PCIe-Switch | --                             | Cisco Systems Inc | SN-47  | equipped | PCIe-Switch | N/A          | 0  | 0  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server568 | MRAID       | Cisco 12G Modular Raid         | LSI Logic         | SN-71  | equipped | MRAID       | yes          | 10 | 1  |
|           |             | Controller with 2GB cache      |                   |        |          |             |              |    |    |
|           |             | (max 16 drives)                |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server568 | PCIe-Switch | --                             | Cisco Systems Inc | SN-77  | equipped | PCIe-Switch | N/A          | 0  | 0  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server855 | MSTOR-RAID  | Cisco Boot optimized M.2 Raid  | Marvell           | SN-68  | equipped | MSTOR-RAID  | yes          | 2  | 1  |
|           |             | controller                     |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server855 | MRAID       | Cisco 12G SAS RAID Controller  | LSI Logic         | SN-78  | equipped | MRAID       | yes          | 4  | 0  |
|           |             | with 4GB FBWC (16 Drives)      |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server405 | 1           | UCSB-MRAID12G-HE               | Cisco Systems Inc | SN-55  | equipped | FMEZZ1-SAS  | RAID0, RAID1 | 2  | 1  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server405 | 1           | Lewisburg SSATA Controller     | Intel Corp.       | SN-17  | equipped |             | RAID0, RAID1 | 0  | 0  |
|           |             | [AHCI mode]                    |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server861 | 1           | Lewisburg SSATA Controller     | Intel Corp.       | SN-82  | equipped |             | RAID0, RAID1 | 0  | 0  |
|           |             | [AHCI mode]                    |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server861 | 1           | UCSB-MRAID12G-HE               | Cisco Systems Inc | SN-77  | equipped | FMEZZ1-SAS  | RAID0, RAID1 | 2  | 1  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server375 | 1           | UCSB-MRAID12G-HE               | Cisco Systems Inc | SN-58  | equipped | FMEZZ1-SAS  | RAID0, RAID1 | 2  | 1  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server375 | 1           | Lewisburg SSATA Controller     | Intel Corp.       | SN-34  | equipped |             | RAID0, RAID1 | 0  | 0  |
|           |             | [AHCI mode]                    |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server344 | 1           | UCSB-MRAID12G-HE               | Cisco Systems Inc | SN-54  | equipped | FMEZZ1-SAS  | RAID0, RAID1 | 2  | 1  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server344 | 1           | Lewisburg SSATA Controller     | Intel Corp.       | SN-15  | equipped |             | RAID0, RAID1 | 0  | 0  |
|           |             | [AHCI mode]                    |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+

Physical Disk - State [#44]
---------------------------

+-----------+-------+------------+---------+----+-------------+------+----------+----------+------------+---------+--------+----------+
| Server    | State | Controller | Disk Id | VD | Size        | Type | Protocol | Bootable | Link Speed | Fw      | State  | Presence |
+-----------+-------+------------+---------+----+-------------+------+----------+----------+------------+---------+--------+----------+
| Server373 | V     | MRAID      | 9       | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server373 | V     | MRAID      | 10      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server373 | V     | MRAID      | 11      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server373 | V     | MRAID      | 12      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server373 | V     | MRAID      | 13      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server373 | V     | MRAID      | 14      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server373 | V     | MRAID      | 15      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server373 | V     | MRAID      | 16      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server373 | V     | MRAID      | 17      | 0  | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server373 | V     | MRAID      | 18      | 0  | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server403 | V     | MRAID      | 9       | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server403 | V     | MRAID      | 10      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server403 | V     | MRAID      | 11      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server403 | V     | MRAID      | 12      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server403 | V     | MRAID      | 13      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server403 | V     | MRAID      | 14      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server403 | V     | MRAID      | 15      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server403 | V     | MRAID      | 16      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server403 | V     | MRAID      | 17      | 0  | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server403 | V     | MRAID      | 18      | 0  | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server568 | V     | MRAID      | 9       | 0  | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server568 | V     | MRAID      | 10      | 0  | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server568 | V     | MRAID      | 11      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server568 | V     | MRAID      | 12      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server568 | V     | MRAID      | 13      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server568 | V     | MRAID      | 14      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server568 | V     | MRAID      | 15      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server568 | V     | MRAID      | 16      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server568 | V     | MRAID      | 17      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server568 | V     | MRAID      | 18      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server855 | V     | MRAID      | 1       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server855 | V     | MRAID      | 2       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server855 | V     | MRAID      | 3       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server855 | V     | MRAID      | 4       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server855 | V     | MSTOR-RAID | 253     | 0  | 240.06 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server855 | V     | MSTOR-RAID | 254     | 0  | 240.06 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server405 | V     | 1          | 1       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server405 | V     | 1          | 2       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server861 | V     | 1          | 1       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server861 | V     | 1          | 2       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server375 | V     | 1          | 1       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server375 | V     | 1          | 2       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server344 | V     | 1          | 1       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server344 | V     | 1          | 2       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
+-----------+-------+------------+---------+----+-------------+------+----------+----------+------------+---------+--------+----------+

Physical Disk - Inventory [#44]
-------------------------------

+-----------+---------+--------+-----------+-------+---------+--------+
| Server    | Disk Id | Pid    | Model     | PN    | Vendor  | Serial |
+-----------+---------+--------+-----------+-------+---------+--------+
| Server373 | 9       | PID-65 | Model-XYZ | PN-69 | ATA     | SN-19  |
| Server373 | 10      | PID-71 | Model-XYZ | PN-20 | ATA     | SN-60  |
| Server373 | 11      | PID-45 | Model-XYZ | PN-53 | ATA     | SN-54  |
| Server373 | 12      | PID-37 | Model-XYZ | PN-45 | ATA     | SN-65  |
| Server373 | 13      | PID-56 | Model-XYZ | PN-16 | SEAGATE | SN-84  |
| Server373 | 14      | PID-23 | Model-XYZ | PN-93 | SEAGATE | SN-96  |
| Server373 | 15      | PID-13 | Model-XYZ | PN-69 | SEAGATE | SN-42  |
| Server373 | 16      | PID-11 | Model-XYZ | PN-25 | SEAGATE | SN-16  |
| Server373 | 17      | PID-51 | Model-XYZ | PN-74 | SEAGATE | SN-23  |
| Server373 | 18      | PID-10 | Model-XYZ | PN-54 | TOSHIBA | SN-15  |
| Server403 | 9       | PID-41 | Model-XYZ | PN-83 | ATA     | SN-25  |
| Server403 | 10      | PID-19 | Model-XYZ | PN-95 | ATA     | SN-79  |
| Server403 | 11      | PID-59 | Model-XYZ | PN-97 | ATA     | SN-73  |
| Server403 | 12      | PID-99 | Model-XYZ | PN-72 | ATA     | SN-66  |
| Server403 | 13      | PID-24 | Model-XYZ | PN-73 | SEAGATE | SN-91  |
| Server403 | 14      | PID-27 | Model-XYZ | PN-18 | SEAGATE | SN-99  |
| Server403 | 15      | PID-45 | Model-XYZ | PN-50 | SEAGATE | SN-36  |
| Server403 | 16      | PID-80 | Model-XYZ | PN-76 | SEAGATE | SN-77  |
| Server403 | 17      | PID-19 | Model-XYZ | PN-83 | SEAGATE | SN-63  |
| Server403 | 18      | PID-92 | Model-XYZ | PN-43 | SEAGATE | SN-34  |
| Server568 | 9       | PID-54 | Model-XYZ | PN-65 | ATA     | SN-53  |
| Server568 | 10      | PID-52 | Model-XYZ | PN-47 | ATA     | SN-24  |
| Server568 | 11      | PID-39 | Model-XYZ | PN-83 | ATA     | SN-68  |
| Server568 | 12      | PID-90 | Model-XYZ | PN-50 | ATA     | SN-12  |
| Server568 | 13      | PID-23 | Model-XYZ | PN-14 | SEAGATE | SN-70  |
| Server568 | 14      | PID-38 | Model-XYZ | PN-16 | SEAGATE | SN-93  |
| Server568 | 15      | PID-90 | Model-XYZ | PN-70 | SEAGATE | SN-85  |
| Server568 | 16      | PID-59 | Model-XYZ | PN-34 | SEAGATE | SN-57  |
| Server568 | 17      | PID-81 | Model-XYZ | PN-79 | SEAGATE | SN-95  |
| Server568 | 18      | PID-29 | Model-XYZ | PN-94 | TOSHIBA | SN-50  |
| Server855 | 1       | PID-57 | Model-XYZ | PN-72 | ATA     | SN-88  |
| Server855 | 2       | PID-22 | Model-XYZ | PN-97 | ATA     | SN-45  |
| Server855 | 3       | PID-55 | Model-XYZ | PN-15 | ATA     | SN-24  |
| Server855 | 4       | PID-18 | Model-XYZ | PN-96 | ATA     | SN-29  |
| Server855 | 253     | PID-94 | Model-XYZ | PN-11 | ATA     | SN-43  |
| Server855 | 254     | PID-81 | Model-XYZ | PN-48 | ATA     | SN-32  |
| Server405 | 1       | PID-50 | Model-XYZ | PN-92 | SEAGATE | SN-79  |
| Server405 | 2       | PID-21 | Model-XYZ | PN-46 | SEAGATE | SN-63  |
| Server861 | 1       | PID-33 | Model-XYZ | PN-40 | SEAGATE | SN-39  |
| Server861 | 2       | PID-22 | Model-XYZ | PN-97 | SEAGATE | SN-74  |
| Server375 | 1       | PID-13 | Model-XYZ | PN-23 | SEAGATE | SN-67  |
| Server375 | 2       | PID-93 | Model-XYZ | PN-70 | SEAGATE | SN-89  |
| Server344 | 1       | PID-60 | Model-XYZ | PN-93 | SEAGATE | SN-24  |
| Server344 | 2       | PID-82 | Model-XYZ | PN-14 | SEAGATE | SN-56  |
+-----------+---------+--------+-----------+-------+---------+--------+

Virtual Drive [#8]
------------------

+-----------+-------+------------+----------+-------------+-------+--------+-------------+----------+---------------+-------------+
| Server    | State | Controller | Drive Id | Size        | Disks | Type   | Name        | Bootable | Write Cache   | Drive State |
+-----------+-------+------------+----------+-------------+-------+--------+-------------+----------+---------------+-------------+
| Server373 | V     | MRAID      | 0        | 1.2 [TB]    | 2     | RAID 1 | vd-0        | V        | write-through | Optimal     |
| Server403 | V     | MRAID      | 0        | 1.2 [TB]    | 2     | RAID 1 | vd-0        | V        | write-through | Optimal     |
| Server568 | V     | MRAID      | 0        | 1.92 [TB]   | 2     | RAID 0 | RAID0_910   | V        | write-through | Optimal     |
| Server855 | V     | MSTOR-RAID | 0        | 239.99 [GB] | 2     | RAID 1 | MStorBootVd | V        | write-through | Optimal     |
| Server405 | V     | 1          | 0        | 299.0 [GB]  | 2     | mirror |             | V        | write-through | optimal     |
| Server861 | V     | 1          | 0        | 299.0 [GB]  | 2     | mirror |             | V        | write-through | optimal     |
| Server375 | V     | 1          | 0        | 299.0 [GB]  | 2     | mirror |             | V        | write-through | optimal     |
| Server344 | V     | 1          | 0        | 299.0 [GB]  | 2     | mirror |             | V        | write-through | optimal     |
+-----------+-------+------------+----------+-------------+-------+--------+-------------+----------+---------------+-------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)