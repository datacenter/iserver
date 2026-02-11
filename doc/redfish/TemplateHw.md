# Hardware Template

[[Next]](./TemplateIdentity.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v hw

+----+--------+--------+---------+------------------------------------------+-------+---------+------+-------------+----------------------+-------------+------+
| Id | Socket | Health | State   | Model                                    | Cores | Threads | Arch | Instruction | Manufacturer         | Speed [MHz] | Step |
+----+--------+--------+---------+------------------------------------------+-------+---------+------+-------------+----------------------+-------------+------+
| 1  | CPU1   | OK     | Enabled | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | 20    | 40      | x86  | x86-64      | Intel(R) Corporation | 4000        | 7    |
| 2  | CPU2   | OK     | Enabled | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | 20    | 40      | x86  | x86-64      | Intel(R) Corporation | 4000        | 7    |
+----+--------+--------+---------+------------------------------------------+-------+---------+------+-------------+----------------------+-------------+------+

+----+---------+------------------------------+--------------+---------------+----------+
| ID | GPU Id  | Name                         | Model        | Serial        | Firmware |
+----+---------+------------------------------+--------------+---------------+----------+
| 1  | GPU-7-0 | NVIDIA A16 PCIe FHFL DS 250W | UCSC-GPU-A16 | 1111111111111 | 22222222 | 
| 2  | GPU-7-1 | NVIDIA A16 PCIe FHFL DS 250W | UCSC-GPU-A16 | 1111111111111 | 22222222 | 
| 3  | GPU-7-2 | NVIDIA A16 PCIe FHFL DS 250W | UCSC-GPU-A16 | 1111111111111 | 22222222 | 
| 4  | GPU-7-3 | NVIDIA A16 PCIe FHFL DS 250W | UCSC-GPU-A16 | 1111111111111 | 22222222 | 
+----+---------+------------------------------+--------------+---------------+----------+

+----+-----------+--------+---------+---------+-------------+-------------+--------+---------+------+-------------+----------------------+---------------+
| ID | Memory Id | Health | State   | Locator | CapacityMiB | Speed [Mhz] | Socket | Channel | Type | Device Type | Part Number          | Serial Number |
+----+-----------+--------+---------+---------+-------------+-------------+--------+---------+------+-------------+----------------------+---------------+
| 1  | 1         | OK     | Enabled | DIMM_A1 | 32768       | 2933        | 0      | 0       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 2  | 3         | OK     | Enabled | DIMM_B1 | 32768       | 2933        | 0      | 1       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 3  | 5         | OK     | Enabled | DIMM_C1 | 32768       | 2933        | 0      | 2       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 4  | 7         | OK     | Enabled | DIMM_D1 | 32768       | 2933        | 0      | 3       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 5  | 9         | OK     | Enabled | DIMM_E1 | 32768       | 2933        | 0      | 4       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 6  | 11        | OK     | Enabled | DIMM_F1 | 32768       | 2933        | 0      | 5       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 7  | 13        | OK     | Enabled | DIMM_G1 | 32768       | 2933        | 1      | 0       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 8  | 15        | OK     | Enabled | DIMM_H1 | 32768       | 2933        | 1      | 1       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 9  | 17        | OK     | Enabled | DIMM_J1 | 32768       | 2933        | 1      | 2       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 10 | 19        | OK     | Enabled | DIMM_K1 | 32768       | 2933        | 1      | 3       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 11 | 21        | OK     | Enabled | DIMM_L1 | 32768       | 2933        | 1      | 4       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 12 | 23        | OK     | Enabled | DIMM_M1 | 32768       | 2933        | 1      | 5       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
+----+-----------+--------+---------+---------+-------------+-------------+--------+---------+------+-------------+----------------------+---------------+

+----+-------------+------------------+------------------------------------------------------------------+-------------------+------------+----------+---------+--------+----------+--------------+----+----+
| ID | Controller  | Pid              | Model                                                            | Vendor            | Serial     | Firmware | State   | Health | PCI Slot | Raid Support | PD | VD |
+----+-------------+------------------+------------------------------------------------------------------+-------------------+------------+----------+---------+--------+----------+--------------+----+----+
| 1  | MRAID       | UCSC-RAID-M5     | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | Cisco Systems Inc | Serial123  | 1.1      | Enabled | OK     | MRAID    | RAID0        | 10 | 1  | 
|    |             |                  |                                                                  |                   |            |          |         |        |          | RAID1        |    |    | 
|    |             |                  |                                                                  |                   |            |          |         |        |          | RAID5        |    |    | 
|    |             |                  |                                                                  |                   |            |          |         |        |          | RAID6        |    |    | 
|    |             |                  |                                                                  |                   |            |          |         |        |          | RAID10       |    |    | 
|    |             |                  |                                                                  |                   |            |          |         |        |          | RAID50       |    |    | 
|    |             |                  |                                                                  |                   |            |          |         |        |          | RAID60       |    |    | 
+----+-------------+------------------+------------------------------------------------------------------+-------------------+------------+----------+---------+--------+----------+--------------+----+----+
| 2  | PCIe-Switch | PFX 48XG3        | NVME-MSWITCH                                                     | MICROSEM          | ---        | 1.1      | ---     | OK     | ---      | ---          | 0  | 0  | 
+----+-------------+------------------+------------------------------------------------------------------+-------------------+------------+----------+---------+--------+----------+--------------+----+----+

+----+------------+-------+------------+------------+------+----------+----------+------------+--------+---------------------------------------------+----------+----+-----------+
| ID | PhyDisk Id | State | Controller | Size       | Type | Protocol | Bootable | Link Speed | Pid    | Model                                       | Vendor   | Fw | Serial    |
+----+------------+-------+------------+------------+------+----------+----------+------------+--------+---------------------------------------------+----------+----+-----------+
| 1  | 9          | V     | MRAID      | 960.2 [GB] | SSD  | SATA     | X        | 6 gb/s     | UCS-SD | 960GB 2.5 inch Enterprise Value 6G SATA SSD | V1       | ab | Serial123 | 
| 2  | 10         | V     | MRAID      | 960.2 [GB] | SSD  | SATA     | X        | 6 gb/s     | UCS-SD | 960GB 2.5 inch Enterprise Value 6G SATA SSD | V1       | ab | Serial123 | 
| 3  | 11         | V     | MRAID      | 960.2 [GB] | SSD  | SATA     | X        | 6 gb/s     | UCS-SD | 960GB 2.5 inch Enterprise Value 6G SATA SSD | V1       | ab | Serial123 | 
| 4  | 12         | V     | MRAID      | 960.2 [GB] | SSD  | SATA     | X        | 6 gb/s     | UCS-SD | 960GB 2.5 inch Enterprise Value 6G SATA SSD | V1       | ab | Serial123 | 
| 5  | 13         | V     | MRAID      | 1.2 [TB]   | HDD  | SAS      | X        | 12 gb/s    | UCS-HD | 1.2TB 12G SAS 10K RPM SFF HDD               | V2       | ab | Serial123 | 
| 6  | 14         | V     | MRAID      | 1.2 [TB]   | HDD  | SAS      | X        | 12 gb/s    | UCS-HD | 1.2TB 12G SAS 10K RPM SFF HDD               | V2       | ab | Serial123 | 
| 7  | 15         | V     | MRAID      | 1.2 [TB]   | HDD  | SAS      | X        | 12 gb/s    | UCS-HD | 1.2TB 12G SAS 10K RPM SFF HDD               | V2       | ab | Serial123 | 
| 8  | 16         | V     | MRAID      | 1.2 [TB]   | HDD  | SAS      | X        | 12 gb/s    | UCS-HD | 1.2TB 12G SAS 10K RPM SFF HDD               | V2       | ab | Serial123 | 
| 9  | 17         | V     | MRAID      | 1.2 [TB]   | HDD  | SAS      | X        | 12 gb/s    | UCS-HD | 1.2TB 12G SAS 10K RPM SFF HDD               | V2       | ab | Serial123 | 
| 10 | 18         | V     | MRAID      | 1.2 [TB]   | HDD  | SAS      | X        | 12 gb/s    | UCS-HD | 1.2TB 12G SAS 10K RPM SFF HDD               | V3       | ab | Serial123 | 
+----+------------+-------+------------+------------+------+----------+----------+------------+--------+---------------------------------------------+----------+----+-----------+

+----+------------------+-------+------------+----------+-------+-------+------+----------+--------------+-------------------------+
| ID | Virtual Drive Id | State | Controller | Size     | Disks | Type  | Name | Bootable | Write Cache  | Raid SupportDrive State |
+----+------------------+-------+------------+----------+-------+-------+------+----------+--------------+-------------------------+
| 1  | 0                | V     | MRAID      | 1.2 [TB] | 2     | RAID1 | vd-0 | V        | WriteThrough | Optimal                 |
+----+------------------+-------+------------+----------+-------+-------+------+----------+--------------+-------------------------+

+----+--------+--------------------+-------------------+-------------------+
| ID | Net Id | Name               | BIA               | MAC               |
+----+--------+--------------------+-------------------+-------------------+
| 1  | 3.1    | Ethernet Interface | aa:bb:cc:ee:2c:30 | aa:bb:cc:ee:2c:30 |
| 2  | 3.2    | Ethernet Interface | aa:bb:cc:ee:2c:31 | aa:bb:cc:ee:2c:31 |
| 3  | 6.1    | Ethernet Interface | aa:bb:cc:ee:2d:60 | aa:bb:cc:ee:2d:60 |
| 4  | 6.2    | Ethernet Interface | aa:bb:cc:ee:2d:61 | aa:bb:cc:ee:2d:61 |
| 5  | L.1    | Ethernet Interface | aa:bb:cc:26:37:b2 | aa:bb:cc:26:37:b2 |
| 6  | L.2    | Ethernet Interface | aa:bb:cc:26:37:b3 | aa:bb:cc:26:37:b3 |
| 7  | MLOM.0 | Ethernet Interface | aa:bb:cc:CC:0E:3E | aa:bb:cc:CC:0E:3E |
| 8  | MLOM.1 | Ethernet Interface | aa:bb:cc:CC:0E:40 | aa:bb:cc:CC:0E:40 |
| 9  | MLOM.2 | Ethernet Interface | aa:bb:cc:CC:0E:3F | aa:bb:cc:CC:0E:3F |
| 10 | MLOM.3 | Ethernet Interface | aa:bb:cc:CC:0E:41 | aa:bb:cc:CC:0E:41 |
+----+--------+--------------------+-------------------+-------------------+

+----+--------+------------------------------------------------------------------+---------+--------+--------+--------+-----------+-----+-----+---------+--------+
| ID | PCI Id | Name                                                             | Fw      | DevId  | Vendor | SubId  | SubVendor | Net | Eth | Storage | Drives |
+----+--------+------------------------------------------------------------------+---------+--------+--------+--------+-----------+-----+-----+---------+--------+
| 1  | MRAID  | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | N/A     | 0x0014 | 0x1000 | 0x020e | 0x1137    | 0   | 0   | 1       | 26     | 
| 2  | MLOM   | Cisco UCS VIC 1457 MLOM                                          | 1.1     | 0x0042 | 0x1137 | 0x0218 | 0x1137    | 7   | 4   | 0       | 0      | 
| 3  | L      | Intel X550 LOM                                                   | 2.2     | 0x1563 | 0x8086 | 0x01a4 | 0x1137    | 0   | 2   | 0       | 0      | 
| 4  | 3      | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 2.2     | 0x158b | 0x8086 | 0x0225 | 0x1137    | 0   | 2   | 0       | 0      | 
| 5  | 6      | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 2.2     | 0x158b | 0x8086 | 0x0225 | 0x1137    | 0   | 2   | 0       | 0      | 
+----+--------+------------------------------------------------------------------+---------+--------+--------+--------+-----------+-----+-----+---------+--------+

+----+----+-----------------+---------+--------+---------+-------+
| ID | Id | Name            | State   | Health | Reading | Units |
+----+----+-----------------+---------+--------+---------+-------+
| 1  | 1  | MOD1_FAN1_SPEED | Enabled | OK     | 7070    | RPM   | 
| 2  | 2  | MOD1_FAN2_SPEED | Enabled | OK     | 7056    | RPM   | 
| 3  | 3  | MOD2_FAN1_SPEED | Enabled | OK     | 6868    | RPM   | 
| 4  | 4  | MOD2_FAN2_SPEED | Enabled | OK     | 7056    | RPM   | 
| 5  | 5  | MOD3_FAN1_SPEED | Enabled | OK     | 6868    | RPM   | 
| 6  | 6  | MOD3_FAN2_SPEED | Enabled | OK     | 7056    | RPM   | 
| 7  | 7  | MOD4_FAN1_SPEED | Enabled | OK     | 6868    | RPM   | 
| 8  | 8  | MOD4_FAN2_SPEED | Enabled | OK     | 7056    | RPM   | 
| 9  | 9  | MOD5_FAN1_SPEED | Enabled | OK     | 7070    | RPM   | 
| 10 | 10 | MOD5_FAN2_SPEED | Enabled | OK     | 7056    | RPM   | 
| 11 | 11 | MOD6_FAN1_SPEED | Enabled | OK     | 6868    | RPM   | 
| 12 | 12 | MOD6_FAN2_SPEED | Enabled | OK     | 7350    | RPM   | 
| 13 | 13 | MOD7_FAN1_SPEED | Absent  | ---    | ---     | ---   | 
+----+----+-----------------+---------+--------+---------+-------+

+----+--------+------+---------+-------------------+---------------+-------------+---------------+-------------------+----------+
| ID | PSU Id | Name | State   | Vendor            | Model         | Part Number | Serial Number | Spare Part Number | Firmware |
+----+--------+------+---------+-------------------+---------------+-------------+---------------+-------------------+----------+
| 1  | 1      | PSU1 | Enabled | Cisco Systems Inc | PSU-111-22-33 | abc         | 1111          | def               | 2222     |
| 2  | 2      | PSU2 | Enabled | Cisco Systems Inc | PSU-111-22-33 | abc         | 2222          | def               | 3333     |
+----+--------+------+---------+-------------------+---------------+-------------+---------------+-------------------+----------+

View: access, account, bios, cpu, fan, gpu, hw, identity (def), mem, net, pci, power, psu, role, storage, thermal, all
```

[[Back]](./README.md)