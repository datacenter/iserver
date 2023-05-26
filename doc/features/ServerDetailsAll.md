# Server Details - All Information

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --all

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+---------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    | Fw      |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+---------+
| P+ H | CRi | C2      | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 4.2(2a) | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+---------+

Alarm Summary
-------------
- Critical : 0
- Warning  : 0
- Info     : 0


Advisory Summary
----------------
- High : 0
- Info : 0


HCL Status
----------
- Overall : Not-Listed


HCL - Server Hardware Compliance
--------------------------------
- Status   : Validated
- Model    : UCSC-C240-M5SN
- CPU      : Intel Xeon Processor Scalable Family
- Firmware : 4.2(2)


HCL - Server Software Compliance
--------------------------------
- Status     : Validated
- Reason     : Incompatible-Components
- OS Vendor  : VMware
- OS Version : ESXi 7.0 U3


HCL - Adapter Compliance
------------------------
- Status : Not-Listed
- Reason : Incompatible-Components


+------------+------------+---------------------+---------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| Status     | Hardware   | Software            | Reason              | Model                                                            | Cimc Version | Driver Name | Driver Version | Firmware Version   |
+------------+------------+---------------------+---------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| Not-Listed | Compatible | Incompatible-Driver | Incompatible-Driver | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(2)       | i40en       | 2.2.7.0        | 0x8000B900-1.826.0 | 
| Not-Listed | Compatible | Incompatible-Driver | Incompatible-Driver | Cisco(R) LOM X550-T2                                             | 4.2(2)       | ixgben      | 1.12.3.0       | 0x800016F9-1.826.0 | 
| Validated  | Compatible | Compatible          | Compatible          | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 4.2(2)       | lsi_mr3     | 7.718.02.00    | 51.19.0-4296       | 
| Validated  | Compatible | Compatible          | Compatible          | UCSC-MLOM-C25Q-04                                                | 4.2(2)       | nenic       | 1.0.42.0       | 5.2(2)             | 
| Not-Listed | Compatible | Incompatible-Driver | Incompatible-Driver | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(2)       | i40en       | 2.2.7.0        | 0x8000B900-1.826.0 | 
+------------+------------+---------------------+---------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+

Device Connector
----------------
- Connection Status             : Connected
- Connector Version             : 1.0.11-2611
- Claimed By                    : ttrabatt@cisco.com
- Claimed Time                  : 2020-12-20T18:46:00.104Z
- Connection Status Last Update : 2022-12-21T09:54:28.112Z
- Platform Type                 : IMCM5
- Device External IP Address    : 173.38.209.11


Contract Coverage
-----------------
- Contract Status       : Not Covered
- Contract Number       : 
- Start Date            : 0001-01-01T00:00:00Z
- End Date              : 0001-01-01T00:00:00Z
- Last Updated          : 2023-01-04T15:04:47.634Z
- Service Description   : UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS
- Service Level         : 
- Service Sku           : 
- Purchase Order Number : 6710008753
- Sales Order Number    : 110208990

License Tier: Premier

Motherboard Hardware Summary
----------------------------
- Board Id                     : 0
- Model                        : UCSC-C240-M5SN
- Serial                       : WZP23400AJW
- Vendor                       : Cisco Systems Inc
- Processors                   : 2
- Memory Arrays                : 1
- Storage Controller           : 2
- Storage Flex Util Controller : 1
- TPM                          : 1


Boot Settings
-------------
- Configured Boot Mode : Legacy
- Actual Boot Mode     : Legacy
- Secure Boot          : disabled


+-------+----------+----------+----------+
| Order | Name     | Type     | State    |
+-------+----------+----------+----------+
| 1     | localhdd | LOCALHDD | Disabled | 
| 2     | pxeboot  | PXE      | Disabled | 
| 3     | vmedia   | VMEDIA   | Disabled | 
+-------+----------+----------+----------+

+-------+--------+--------+----------------------+------+------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+
| State | CPU Id | Socket | Vendor               | Arch | Model                                    | Cores | Enabled | Threads | Speed [GHz] | Stepping | Presence | OperState |
+-------+--------+--------+----------------------+------+------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+
| V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | 
| V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | 
+-------+--------+--------+----------------------+------+------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+

+
|
+
+

Kvm Settings
------------
- Kvm Server State Enabled : False
- Kvm Vendor               : Avocent
- Tunneled Kvm             : False


+---------+-------------+-----------------+-------------+-----------+------------+----------+----------+
| Name    | Address     | Subnet          | Gateway     | Http Port | Https Port | Kvm Port | Kvm Vlan |
+---------+-------------+-----------------+-------------+-----------+------------+----------+----------+
| Outband | 10.58.50.41 | 255.255.255.224 | 10.58.50.62 | 80        | 443        | 2068     | 1        | 
+---------+-------------+-----------------+-------------+-----------+------------+----------+----------+

+-------+-----------+-------+------+----------+----------+-------------+---------+--------------+--------------+----------------------+----------+------------+----------+---------+
| State | Memory Id | Array | Bank | Location | Capacity | Clock       | Latency | Form Factor  | Type         | Model                | Serial   | Oper State | Presence | Thermal |
+-------+-----------+-------+------+----------+----------+-------------+---------+--------------+--------------+----------------------+----------+------------+----------+---------+
| V     | 1         | 1     | 0    | DIMM_A1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73490 | operable   | equipped |         | 
| X     | 2         | 1     | 0    | DIMM_A2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 3         | 1     | 0    | DIMM_B1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72CD9 | operable   | equipped |         | 
| X     | 4         | 1     | 0    | DIMM_B2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 5         | 1     | 0    | DIMM_C1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F7348D | operable   | equipped |         | 
| X     | 6         | 1     | 0    | DIMM_C2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 7         | 1     | 0    | DIMM_D1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F734A7 | operable   | equipped |         | 
| X     | 8         | 1     | 0    | DIMM_D2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 9         | 1     | 0    | DIMM_E1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73492 | operable   | equipped |         | 
| X     | 10        | 1     | 0    | DIMM_E2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 11        | 1     | 0    | DIMM_F1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73498 | operable   | equipped |         | 
| X     | 12        | 1     | 0    | DIMM_F2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 13        | 1     | 0    | DIMM_G1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F7348E | operable   | equipped |         | 
| X     | 14        | 1     | 0    | DIMM_G2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 15        | 1     | 0    | DIMM_H1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73495 | operable   | equipped |         | 
| X     | 16        | 1     | 0    | DIMM_H2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 17        | 1     | 0    | DIMM_J1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72CCC | operable   | equipped |         | 
| X     | 18        | 1     | 0    | DIMM_J2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 19        | 1     | 0    | DIMM_K1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73493 | operable   | equipped |         | 
| X     | 20        | 1     | 0    | DIMM_K2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 21        | 1     | 0    | DIMM_L1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73494 | operable   | equipped |         | 
| X     | 22        | 1     | 0    | DIMM_L2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 23        | 1     | 0    | DIMM_M1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F734AD | operable   | equipped |         | 
| X     | 24        | 1     | 0    | DIMM_M2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
+-------+-----------+-------+------+----------+----------+-------------+---------+--------------+--------------+----------------------+----------+------------+----------+---------+

+--------------------+-------------+--------------------+----------------------------+----------------------------------------------------------+
| Name               | Component   | Type               | Version                    | Dn                                                       |
+--------------------+-------------+--------------------+----------------------------+----------------------------------------------------------+
| Adapter            | system      | adaptor            | 5.2(2b)                    | sys/rack-unit-1/adaptor-MLOM/mgmt/fw-system              | 
| Adapter            | system      | adaptor            | 0x8000B900-1.826.0         | sys/rack-unit-1/network-adapter-3/mgmt/fw-system         | 
| Adapter            | system      | adaptor            | 0x8000B900-1.826.0         | sys/rack-unit-1/network-adapter-6/mgmt/fw-system         | 
| Adapter            | system      | adaptor            | 0x800016F9-1.826.0         | sys/rack-unit-1/network-adapter-L/mgmt/fw-system         | 
| BIOS               | boot-loader | blade-bios         | C240M5.4.2.2b.0.0613220203 | sys/rack-unit-1/bios/fw-boot-loader                      | 
| Board Controller   | boot-loader | blade-controller   | 4.2(2a)                    | sys/rack-unit-1/mgmt/fw-boot-loader                      | 
| CIMC Controller    | system      | blade-controller   | 4.2(2a)                    | sys/rack-unit-1/mgmt/fw-system                           | 
| Storage Controller | system      | storage-controller | 1.8.0.58-24b3              | sys/rack-unit-1/board/storage-NVMe-PCIe-Switch/fw-system | 
| Storage Controller | boot-loader | storage-controller | 7.19.00.0_0x07130200       | sys/rack-unit-1/board/storage-SAS-MRAID/fw-boot-loader   | 
| Storage Controller | system      | storage-controller | 51.19.0-4296               | sys/rack-unit-1/board/storage-SAS-MRAID/fw-system        | 
+--------------------+-------------+--------------------+----------------------------+----------------------------------------------------------+

Storage Summary
- Controllers            : 2
- Disks Count            : 10
- Capacity               : 11.03 [TB]
- HDD Count              : 6
- HDD Capacity           : 7.19 [TB]
- SSD Count              : 4
- SSD Capacity           : 3.84 [TB]
- Virtual Drive Count    : 1
- Virtual Drive Capacity : 1.2 [TB]


Storage Controller
- Model                : Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)
- Vendor               : LSI Logic
- Serial               : SK00188839
- Presence             : equipped
- Status               : 
- PCIe Address         : 
- PCI Slot             : MRAID
- Controller Id        : MRAID
- Name                 : storage-SAS-MRAID
- Dn                   : sys/rack-unit-1/board/storage-SAS-MRAID
- Raid Support         : yes
- Physical Disks Count : 10
- Virtual Drives Count : 1


Storage Controller
- Model                : 
- Vendor               : Cisco Systems Inc
- Serial               : 
- Presence             : equipped
- Status               : 
- PCIe Address         : 
- PCI Slot             : PCIe-Switch
- Controller Id        : PCIe-Switch
- Name                 : storage-NVMe-PCIe-Switch
- Dn                   : sys/rack-unit-1/board/storage-NVMe-PCIe-Switch
- Raid Support         : N/A
- Physical Disks Count : 0
- Virtual Drives Count : 0


+-------+---------+------------+------+----------+------------+-------------------+----------+----------------+---------+----------+----------------------+-------+----------+-----------------------------------------------+
| State | Disk Id | Size       | Type | Bootable | Link Speed | Controller        | Drive Id | Model          | Vendor  | Fw       | Serial               | State | Presence | Dn                                            |
+-------+---------+------------+------+----------+------------+-------------------+----------+----------------+---------+----------+----------------------+-------+----------+-----------------------------------------------+
| V     | 9       | 959.0 [GB] | SSD  | X        | 6.0 Gb/s   | storage-SAS-MRAID |          | SSDSC2KB960G7K | ATA     | SCV1CS08 | PHYS746002YU960CGN   | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-9  | 
| V     | 10      | 959.0 [GB] | SSD  | X        | 6.0 Gb/s   | storage-SAS-MRAID |          | SSDSC2KB960G7K | ATA     | SCV1CS08 | PHYS746002XE960CGN   | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-10 | 
| V     | 11      | 959.0 [GB] | SSD  | X        | 6.0 Gb/s   | storage-SAS-MRAID |          | SSDSC2KB960G7K | ATA     | SCV1CS08 | PHYS746002VN960CGN   | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-11 | 
| V     | 12      | 959.0 [GB] | SSD  | X        | 6.0 Gb/s   | storage-SAS-MRAID |          | SSDSC2KB960G7K | ATA     | SCV1CS08 | PHYS74610194960CGN   | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-12 | 
| V     | 13      | 1.2 [TB]   | HDD  | X        | 12.0 Gb/s  | storage-SAS-MRAID |          | ST1200MM0009   | SEAGATE | CN03     | WFK654680000C024C6NE | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-13 | 
| V     | 14      | 1.2 [TB]   | HDD  | X        | 12.0 Gb/s  | storage-SAS-MRAID |          | ST1200MM0009   | SEAGATE | CN03     | WFK65J9T0000C025976H | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-14 | 
| V     | 15      | 1.2 [TB]   | HDD  | X        | 12.0 Gb/s  | storage-SAS-MRAID |          | ST1200MM0009   | SEAGATE | CN03     | WFK65HVV0000C024KK59 | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-15 | 
| V     | 16      | 1.2 [TB]   | HDD  | X        | 12.0 Gb/s  | storage-SAS-MRAID |          | ST1200MM0009   | SEAGATE | CN03     | WFK65M390000C024KKSN | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-16 | 
| V     | 17      | 1.2 [TB]   | HDD  | X        | 12.0 Gb/s  | storage-SAS-MRAID | 0        | ST1200MM0009   | SEAGATE | CN03     | WFK654FJ0000C024KKCC | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-17 | 
| V     | 18      | 1.2 [TB]   | HDD  | X        | 12.0 Gb/s  | storage-SAS-MRAID | 0        | AL15SEB120N    | TOSHIBA | 5703     | Y9G0A06DFJMF         | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-18 | 
+-------+---------+------------+------+----------+------------+-------------------+----------+----------------+---------+----------+----------------------+-------+----------+-----------------------------------------------+

+-------+----------+----------+-------+--------+------+----------+---------------+-------------------+---------+----------------------------------------------+
| State | Drive Id | Size     | Disks | Type   | Name | Bootable | Write Cache   | Controller        | State   | Dn                                           |
+-------+----------+----------+-------+--------+------+----------+---------------+-------------------+---------+----------------------------------------------+
| V     | 0        | 1.2 [TB] | 2     | RAID 1 | vd-0 | V        | write-through | storage-SAS-MRAID | Optimal | sys/rack-unit-1/board/storage-SAS-MRAID/vd-0 | 
+-------+----------+----------+-------+--------+------+----------+---------------+-------------------+---------+----------------------------------------------+

+--------------+---------+--------------------------------------------+-------------+-------------------+-----+-----+-----+
| Name         | PciSlot | Model                                      | Serial      | Vendor            | Eth | HBA | DCE |
+--------------+---------+--------------------------------------------+-------------+-------------------+-----+-----+-----+
| Adapter 3    | 3       | Cisco(R) Ethernet Converged NIC XXV710-DA2 |             |                   | 2   | 0   | 0   | 
| Adapter 6    | 6       | Cisco(R) Ethernet Converged NIC XXV710-DA2 |             |                   | 2   | 0   | 0   | 
| Adapter L    | L       | Cisco(R) LOM X550-T2                       |             |                   | 2   | 0   | 0   | 
| Adapter MLOM | MLOM    | UCSC-MLOM-C25Q-04                          | FCH24157D1V | Cisco Systems Inc | 4   | 4   | 4   | 
+--------------+---------+--------------------------------------------+-------------+-------------------+-----+-----+-----+

+----------------------------------------+---------------+-------------------+
| Adapter Dn                             | DCE Interface | MAC Address       |
+----------------------------------------+---------------+-------------------+
| sys/rack-unit-1/adaptor-MLOM/ext-eth-0 | 0             | 3C:57:31:CC:0E:3E | 
| sys/rack-unit-1/adaptor-MLOM/ext-eth-1 | 1             | 3C:57:31:CC:0E:40 | 
| sys/rack-unit-1/adaptor-MLOM/ext-eth-2 | 2             | 3C:57:31:CC:0E:3F | 
| sys/rack-unit-1/adaptor-MLOM/ext-eth-3 | 3             | 3C:57:31:CC:0E:41 | 
+----------------------------------------+---------------+-------------------+

+--------------+----------------+-------------------+
| Adapter Name | Interface Name | MAC Address       |
+--------------+----------------+-------------------+
| Adapter 3    | eth-1          | 3c:fd:fe:ee:2c:30 | 
| Adapter 3    | eth-2          | 3c:fd:fe:ee:2c:31 | 
| Adapter 6    | eth-1          | 3c:fd:fe:ee:2d:60 | 
| Adapter 6    | eth-2          | 3c:fd:fe:ee:2d:61 | 
| Adapter L    | eth-1          | 5c:71:0d:26:37:b2 | 
| Adapter L    | eth-2          | 5c:71:0d:26:37:b3 | 
| Adapter MLOM | eth0           | 3C:57:31:CC:0E:46 | 
| Adapter MLOM | eth1           | 3C:57:31:CC:0E:47 | 
| Adapter MLOM | eth2           | 3C:57:31:CC:0E:48 | 
| Adapter MLOM | eth3           | 3C:57:31:CC:0E:49 | 
+--------------+----------------+-------------------+

+--------------+----------------+-------------------------+-------------------------+
| Adapter Name | Interface Name | WWNN                    | WWPN                    |
+--------------+----------------+-------------------------+-------------------------+
| Adapter MLOM | fc0            | 10:00:3C:57:31:CC:0E:4A | 20:00:3C:57:31:CC:0E:4A | 
| Adapter MLOM | fc1            | 10:00:3C:57:31:CC:0E:4B | 20:00:3C:57:31:CC:0E:4B | 
| Adapter MLOM | fc2            | 10:00:3C:57:31:CC:0E:4C | 20:00:3C:57:31:CC:0E:4C | 
| Adapter MLOM | fc3            | 10:00:3C:57:31:CC:0E:4D | 20:00:3C:57:31:CC:0E:4D | 
+--------------+----------------+-------------------------+-------------------------+

+------------------------------------------------------------------+-------------------+--------+--------+--------------------+-------------------------------------+
| PCI Device Model                                                 | Pid               | SlotId | Vendor | Firmware           | Dn                                  |
+------------------------------------------------------------------+-------------------+--------+--------+--------------------+-------------------------------------+
| Cisco(R) Ethernet Converged NIC XXV710-DA2                       | UCSC-PCIE-ID25GF  | 3      | 0x8086 | 0x8000B900-1.826.0 | sys/rack-unit-1/equipped-slot-3     | 
| Cisco(R) Ethernet Converged NIC XXV710-DA2                       | UCSC-PCIE-ID25GF  | 6      | 0x8086 | 0x8000B900-1.826.0 | sys/rack-unit-1/equipped-slot-6     | 
| Intel X550 LOM                                                   | UNKNOWN           | L      | 0x8086 | 0x800016F9-1.826.0 | sys/rack-unit-1/equipped-slot-L     | 
| Cisco UCS VIC 1457 MLOM                                          | UCSC-MLOM-C25Q-04 | MLOM   | 0x1137 | 5.2(2b)            | sys/rack-unit-1/equipped-slot-MLOM  | 
| Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | UCSC-RAID-M5      | MRAID  | 0x1000 | N/A                | sys/rack-unit-1/equipped-slot-MRAID | 
+------------------------------------------------------------------+-------------------+--------+--------+--------------------+-------------------------------------+

+-------+---------------+-----------+----------+--------------------------------+
| State | Fan Module Id | OperState | Presence | Dn                             |
+-------+---------------+-----------+----------+--------------------------------+
| V     | 1             | operable  | equipped | sys/rack-unit-1/fan-module-1-1 | 
| V     | 2             | operable  | equipped | sys/rack-unit-1/fan-module-1-2 | 
| V     | 3             | operable  | equipped | sys/rack-unit-1/fan-module-1-3 | 
| V     | 4             | operable  | equipped | sys/rack-unit-1/fan-module-1-4 | 
| V     | 5             | operable  | equipped | sys/rack-unit-1/fan-module-1-5 | 
| V     | 6             | operable  | equipped | sys/rack-unit-1/fan-module-1-6 | 
| X     | 7             | unknown   | missing  | sys/rack-unit-1/fan-module-1-7 | 
+-------+---------------+-----------+----------+--------------------------------+

+-------+-----------------------+---------------+-------------+-------------------+------+---------+
| State | Dn                    | PSU Model     | Serial      | Vendor            | On   | Voltage |
+-------+-----------------------+---------------+-------------+-------------------+------+---------+
| V     | sys/rack-unit-1/psu-1 | PS-2112-9S-LF | LIT241244MU | Cisco Systems Inc | True | ok      | 
| V     | sys/rack-unit-1/psu-2 | PS-2112-9S-LF | LIT241244Z5 | Cisco Systems Inc | True | ok      | 
+-------+-----------------------+---------------+-------------+-------------------+------+---------+

Power Consumption (Watt)
------------------------
- Current      : 324
- Min          : 177
- Average      : 335
- Max          : 490
- Limit action : NoAction


+----------------+---------+--------+-------+-----------------+
| Sensor Name    | State   | Health | Volts | Upper Threshold |
+----------------+---------+--------+-------+-----------------+
| PSU1_VOUT      | Enabled | OK     | 12.1  | 14              | 
| PSU2_VOUT      | Enabled | OK     | 12.2  | 14              | 
| P12V           | Enabled | OK     | 11.89 | 13.166          | 
| P3V_BAT_SCALED | Enabled | OK     | 3.026 | 3.588           | 
+----------------+---------+--------+-------+-----------------+

+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| PSU Name | State   | Health | Serial      | Firmware | Output (Watt) | Input (Watt) | Max (V) | Min (V) | Max (Hz) | Min (Hz) |
+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| PSU1     | Enabled | OK     | LIT241244MU | 10062019 | 148           | 165          | 264     | 180     | 63       | 47       | 
| PSU2     | Enabled | OK     | LIT241244Z5 | 10062019 | 149           | 164          | 264     | 180     | 63       | 47       | 
+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+

Thermal Summary
---------------
- Sensors Health   : True
- Highest (C)      : 54
- Smallest Gap (C) : 20
- Over Threshold   : 0
- Fans Health      : True


+------------------+---------+--------+------------------+-----------------+---------------------------+
| Sensor Name      | State   | Health | Location         | Value (Celcius) | Upper Threshold (Celcius) |
+------------------+---------+--------+------------------+-----------------+---------------------------+
| DDR4_P1_A1_TMP   | Enabled | OK     | Memory           | 29              | 85                        | 
| DDR4_P1_B1_TMP   | Enabled | OK     | Memory           | 28              | 85                        | 
| DDR4_P1_C1_TMP   | Enabled | OK     | Memory           | 28              | 85                        | 
| DDR4_P1_D1_TMP   | Enabled | OK     | Memory           | 29              | 85                        | 
| DDR4_P1_E1_TMP   | Enabled | OK     | Memory           | 29              | 85                        | 
| DDR4_P1_F1_TMP   | Enabled | OK     | Memory           | 28              | 85                        | 
| DDR4_P2_G1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P2_H1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P2_J1_TMP   | Enabled | OK     | Memory           | 28              | 85                        | 
| DDR4_P2_K1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P2_L1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P2_M1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| MLOM_TEMP        | Enabled | OK     | NetworkingDevice | 54              | 90                        | 
| P1_TEMP_SENS     | Enabled | OK     | CPU              | 39.5            | 100                       | 
| P2_TEMP_SENS     | Enabled | OK     | CPU              | 39.5            | 100                       | 
| PCH_TEMP_SENS    | Enabled | OK     | SystemBoard      | 33              | 85                        | 
| PCIE_SWITCH_TMP  | Enabled | OK     | SystemBoard      | 39              | 100                       | 
| PSU1_TEMP        | Enabled | OK     | PowerSupply      | 21              | 65                        | 
| PSU2_TEMP        | Enabled | OK     | PowerSupply      | 19              | 65                        | 
| RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 32              | 70                        | 
| RISER1_TEMP      | Enabled | OK     | SystemBoard      | 24              | 70                        | 
| RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 31              | 70                        | 
| RISER2_TEMP      | Enabled | OK     | SystemBoard      | 27              | 70                        | 
| TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 25              | 45                        | 
+------------------+---------+--------+------------------+-----------------+---------------------------+

+-----------------+---------+--------+----------+
| Fan Name        | State   | Health | Value    |
+-----------------+---------+--------+----------+
| MOD1_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD1_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD2_FAN1_SPEED | Enabled | OK     | 7070 RPM | 
| MOD2_FAN2_SPEED | Enabled | OK     | 7350 RPM | 
| MOD3_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD3_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD4_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD4_FAN2_SPEED | Enabled | OK     | 7350 RPM | 
| MOD5_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD5_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD6_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD6_FAN2_SPEED | Enabled | OK     | 7350 RPM | 
| MOD7_FAN1_SPEED | Absent  |        |          | 
+-----------------+---------+--------+----------+

+-------+-------------------+-------------+---------+-------+--------+--------+
| TPM   | Activation Status | Admin State | Version | Model | Vendor | Serial |
+-------+-------------------+-------------+---------+-------+--------+--------+
| empty | unknown           | unknown     | NA      | NA    | NA     | NA     | 
+-------+-------------------+-------------+---------+-------+--------+--------+
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --all

{
    "__Output": {
        "FlagState": ":GG.G",
        "FlagManagement": ":GGY",
        "FlagWorkflow": ":GG"
    },
    "Moid": "5fdf9c016176752d35e44795",
    "DeviceMoId": "5fdf9be76f72612d300a8d81",
    "Name": "comp-1-p2b-eu-spdc-WZP23400AJW",
    "Model": "UCSC-C240-M5SN",
    "Serial": "WZP23400AJW",
    "ManagementMode": "IntersightStandalone",
    "OperPowerState": "on",
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C240-M5SN",
    "AdvisorySummary": {
        "__Output": {
            "High": "Red",
            "Info": "Blue"
        },
        "High": 0,
        "Info": 0
    },
    "AdvisoryInfo": [],
    "AlarmInfo": [],
    "BoardInfo": {
        "BoardId": 0,
        "CpuTypeController": "",
        "Dn": "sys/rack-unit-1/board",
        "Model": "UCSC-C240-M5SN",
        "Moid": "5fdf9c056176752d35e44930",
        "OperPowerState": "not-supported",
        "Serial": "WZP23400AJW",
        "Vendor": "Cisco Systems Inc",
        "EquipmentTpmsIds": [
            "5fdf9c186176752d35e4503a"
        ],
        "EquipmentTpmsCount": 1,
        "GraphicsCardsIds": [],
        "GraphicsCardsCount": 0,
        "MemoryArraysIds": [
            "5fdf9c416176752d35e45e6f"
        ],
        "MemoryArraysCount": 1,
        "PciCoprocessorCardsIds": [],
        "PciCoprocessorCardsCount": 0,
        "PciSwitchIds": [],
        "PciSwitchCount": 0,
        "ProcessorsIds": [
            "5fdf9c5a6176752d35e467d7",
            "5fdf9c5a6176752d35e467db"
        ],
        "ProcessorsCount": 2,
        "SecurityUnitsIds": [],
        "SecurityUnitsCount": 0,
        "StorageControllersIds": [
            "635840e076752d31399d9215",
            "636ddf1876752d3139c8d4f5"
        ],
        "StorageControllersCount": 2,
        "StorageFlexFlashControllersIds": [],
        "StorageFlexFlashControllersCount": 0,
        "StorageFlexUtilControllersIds": [
            "5fdf9c726176752d35e46f0c"
        ],
        "StorageFlexUtilControllersCount": 1
    },
    "BootInfo": {
        "ConfiguredBootMode": "Legacy",
        "ActualBootMode": "Legacy",
        "SecureBoot": "disabled",
        "Order": [
            {
                "Moid": "60000c0b6176752d35b76e3e",
                "Name": "localhdd",
                "Order": 1,
                "State": "Disabled",
                "Type": "LOCALHDD"
            },
            {
                "Moid": "60000c046176752d35b76bb3",
                "Name": "pxeboot",
                "Order": 2,
                "State": "Disabled",
                "Type": "PXE"
            },
            {
                "Moid": "6013f1496176752d35458e49",
                "Name": "vmedia",
                "Order": 3,
                "State": "Disabled",
                "Type": "VMEDIA"
            }
        ]
    },
    "ConnectorInfo": {
        "__Output": {
            "ConnectionStatus": "Green"
        },
        "Moid": "5fdf9be76f72612d300a8d81",
        "ClaimedByUserName": "ttrabatt@cisco.com",
        "ClaimedTime": "2020-12-20T18:46:00.104Z",
        "PlatformType": "IMCM5",
        "ConnectorVersion": "1.0.11-2611",
        "ConnectionStatus": "Connected",
        "DeviceExternalIpAddress": "173.38.209.11",
        "ConnectionStatusLastChangeTime": "2022-12-21T09:54:28.112Z",
        "Connected": true
    },
    "ContractInfo": {
        "__Output": {
            "ContractStatus": "Red"
        },
        "Moid": "5fdf9be96265722d30188c77",
        "PurchaseOrderNumber": "6710008753",
        "SalesOrderNumber": "110208990",
        "ContractStatus": "Not Covered",
        "ContractNumber": "",
        "ContractUpdatedTime": "2023-01-04T15:04:47.634Z",
        "ServiceDescription": "UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS",
        "ServiceLevel": "",
        "ServiceSku": "",
        "ServiceStartDate": "0001-01-01T00:00:00Z",
        "ServiceEndDate": "0001-01-01T00:00:00Z",
        "IsValid": true
    },
    "NumCpus": 2,
    "NumCpuCores": 40,
    "NumThreads": 80,
    "Cpu": "2S 40C 80T",
    "CpuInfo": [
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "Architecture": "Xeon",
            "Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
            "NumCores": 20,
            "NumCoresEnabled": "20",
            "NumThreads": "40",
            "OperState": "operable",
            "Presence": "equipped",
            "ProcessorId": 1,
            "SocketDesignation": "CPU1",
            "Speed": 2.5,
            "Stepping": "7",
            "Vendor": "Intel(R) Corporation",
            "Thermal": "",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "Architecture": "Xeon",
            "Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
            "NumCores": 20,
            "NumCoresEnabled": "20",
            "NumThreads": "40",
            "OperState": "operable",
            "Presence": "equipped",
            "ProcessorId": 2,
            "SocketDesignation": "CPU2",
            "Speed": 2.5,
            "Stepping": "7",
            "Vendor": "Intel(R) Corporation",
            "Thermal": "",
            "StateTick": "\u2713"
        }
    ],
    "FanInfo": [
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "On": "Green",
                "StateTick": "Green"
            },
            "Moid": "5fdf9c106176752d35e44d77",
            "ModuleId": 1,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-1",
            "On": true,
            "Name": "Fan Module 1",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e57",
                "5fdf9c126176752d35e44e6d"
            ],
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "On": "Green",
                "StateTick": "Green"
            },
            "Moid": "5fdf9c106176752d35e44d79",
            "ModuleId": 2,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-2",
            "On": true,
            "Name": "Fan Module 2",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e59",
                "5fdf9c126176752d35e44e65"
            ],
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "On": "Green",
                "StateTick": "Green"
            },
            "Moid": "5fdf9c106176752d35e44d7b",
            "ModuleId": 3,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-3",
            "On": true,
            "Name": "Fan Module 3",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e5f",
                "5fdf9c126176752d35e44e6f"
            ],
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "On": "Green",
                "StateTick": "Green"
            },
            "Moid": "5fdf9c106176752d35e44d7d",
            "ModuleId": 4,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-4",
            "On": true,
            "Name": "Fan Module 4",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e5b",
                "5fdf9c126176752d35e44e67"
            ],
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "On": "Green",
                "StateTick": "Green"
            },
            "Moid": "5fdf9c106176752d35e44d71",
            "ModuleId": 5,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-5",
            "On": true,
            "Name": "Fan Module 5",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e61",
                "5fdf9c126176752d35e44e69"
            ],
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "On": "Green",
                "StateTick": "Green"
            },
            "Moid": "5fdf9c106176752d35e44d73",
            "ModuleId": 6,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-6",
            "On": true,
            "Name": "Fan Module 6",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e5d",
                "5fdf9c126176752d35e44e63"
            ],
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "On": "Red",
                "StateTick": "Red"
            },
            "Moid": "5fdf9c106176752d35e44d75",
            "ModuleId": 7,
            "OperState": "unknown",
            "Presence": "missing",
            "Dn": "sys/rack-unit-1/fan-module-1-7",
            "On": false,
            "Name": "Fan Module 7",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e6b",
                "5fdf9c126176752d35e44e71"
            ],
            "StateTick": "\u2717"
        }
    ],
    "FanOn": 6,
    "FanCount": 7,
    "FanSummary": "6/7",
    "FanHealthy": false,
    "FirmwarewComponents": [
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/mgmt/fw-system",
            "Type": "adaptor",
            "PackageVersion": "",
            "Version": "5.2(2b)",
            "Name": "Adapter"
        },
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/network-adapter-3/mgmt/fw-system",
            "Type": "adaptor",
            "PackageVersion": "",
            "Version": "0x8000B900-1.826.0",
            "Name": "Adapter"
        },
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/network-adapter-6/mgmt/fw-system",
            "Type": "adaptor",
            "PackageVersion": "",
            "Version": "0x8000B900-1.826.0",
            "Name": "Adapter"
        },
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/network-adapter-L/mgmt/fw-system",
            "Type": "adaptor",
            "PackageVersion": "",
            "Version": "0x800016F9-1.826.0",
            "Name": "Adapter"
        },
        {
            "Component": "boot-loader",
            "Dn": "sys/rack-unit-1/bios/fw-boot-loader",
            "Type": "blade-bios",
            "PackageVersion": "",
            "Version": "C240M5.4.2.2b.0.0613220203",
            "Name": "BIOS"
        },
        {
            "Component": "boot-loader",
            "Dn": "sys/rack-unit-1/mgmt/fw-boot-loader",
            "Type": "blade-controller",
            "PackageVersion": "",
            "Version": "4.2(2a)",
            "Name": "Board Controller"
        },
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/mgmt/fw-system",
            "Type": "blade-controller",
            "PackageVersion": "",
            "Version": "4.2(2a)",
            "Name": "CIMC Controller"
        },
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/board/storage-NVMe-PCIe-Switch/fw-system",
            "Type": "storage-controller",
            "PackageVersion": "",
            "Version": "1.8.0.58-24b3",
            "Name": "Storage Controller"
        },
        {
            "Component": "boot-loader",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-boot-loader",
            "Type": "storage-controller",
            "PackageVersion": "",
            "Version": "7.19.00.0_0x07130200",
            "Name": "Storage Controller"
        },
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-system",
            "Type": "storage-controller",
            "PackageVersion": "",
            "Version": "51.19.0-4296",
            "Name": "Storage Controller"
        }
    ],
    "FirmwareVersion": "4.2(2a)",
    "Groups": "p2b,pod2b,power",
    "AlarmSummary": {
        "__Output": {
            "Critical": "Red",
            "Warning": "Yellow",
            "Info": "Blue",
            "Cleared": "Green"
        },
        "Critical": 0,
        "Warning": 0,
        "Info": 0
    },
    "Health": "Healthy",
    "HclInfo": {
        "__Output": {
            "Status": "Yellow",
            "SoftwareStatus": "Green",
            "HardwareStatus": "Green",
            "ComponentStatus": "Yellow"
        },
        "ComponentStatus": "Not-Listed",
        "HardwareStatus": "Validated",
        "HclFirmwareVersion": "4.2(2)",
        "HclModel": "UCSC-C240-M5SN",
        "HclOsVendor": "VMware",
        "HclOsVersion": "ESXi 7.0 U3",
        "HclProcessor": "Intel Xeon Processor Scalable Family",
        "Moid": "5fdf9c0673736f2d31c2a581",
        "Reason": "Incompatible-Components",
        "ServerReason": "Incompatible-Components",
        "SoftwareStatus": "Validated",
        "Status": "Not-Listed",
        "Details": [
            {
                "__Output": {
                    "Status": "Yellow"
                },
                "HardwareStatus": "Compatible",
                "HclCimcVersion": "4.2(2)",
                "HclDriverName": "i40en",
                "HclDriverVersion": "2.2.7.0",
                "HclFirmwareVersion": "0x8000B900-1.826.0",
                "HclModel": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
                "Reason": "Incompatible-Driver",
                "SoftwareStatus": "Incompatible-Driver",
                "Status": "Not-Listed",
                "Moid": "6396f6ec73736f2d318a9a3f"
            },
            {
                "__Output": {
                    "Status": "Yellow"
                },
                "HardwareStatus": "Compatible",
                "HclCimcVersion": "4.2(2)",
                "HclDriverName": "ixgben",
                "HclDriverVersion": "1.12.3.0",
                "HclFirmwareVersion": "0x800016F9-1.826.0",
                "HclModel": "Cisco(R) LOM X550-T2",
                "Reason": "Incompatible-Driver",
                "SoftwareStatus": "Incompatible-Driver",
                "Status": "Not-Listed",
                "Moid": "6396f6ec73736f2d318a9a40"
            },
            {
                "__Output": {
                    "Status": "Green"
                },
                "HardwareStatus": "Compatible",
                "HclCimcVersion": "4.2(2)",
                "HclDriverName": "lsi_mr3",
                "HclDriverVersion": "7.718.02.00",
                "HclFirmwareVersion": "51.19.0-4296",
                "HclModel": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
                "Reason": "Compatible",
                "SoftwareStatus": "Compatible",
                "Status": "Validated",
                "Moid": "6396f6ec73736f2d318a9a41"
            },
            {
                "__Output": {
                    "Status": "Green"
                },
                "HardwareStatus": "Compatible",
                "HclCimcVersion": "4.2(2)",
                "HclDriverName": "nenic",
                "HclDriverVersion": "1.0.42.0",
                "HclFirmwareVersion": "5.2(2)",
                "HclModel": "UCSC-MLOM-C25Q-04",
                "Reason": "Compatible",
                "SoftwareStatus": "Compatible",
                "Status": "Validated",
                "Moid": "6396f6ec73736f2d318a9a3d"
            },
            {
                "__Output": {
                    "Status": "Yellow"
                },
                "HardwareStatus": "Compatible",
                "HclCimcVersion": "4.2(2)",
                "HclDriverName": "i40en",
                "HclDriverVersion": "2.2.7.0",
                "HclFirmwareVersion": "0x8000B900-1.826.0",
                "HclModel": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
                "Reason": "Incompatible-Driver",
                "SoftwareStatus": "Incompatible-Driver",
                "Status": "Not-Listed",
                "Moid": "6396f6ec73736f2d318a9a3e"
            }
        ]
    },
    "KvmInfo": {
        "KvmIpAddresses": [
            {
                "Address": "10.58.50.41",
                "Category": "Equipment",
                "ClassId": "compute.IpAddress",
                "DefaultGateway": "10.58.50.62",
                "Dn": "sys/rack-unit-1/mgmt/if-1",
                "HttpPort": 80,
                "HttpsPort": 443,
                "KvmPort": 2068,
                "KvmVlan": 1,
                "Name": "Outband",
                "ObjectType": "compute.IpAddress",
                "Subnet": "255.255.255.224",
                "Type": "MgmtInterface"
            }
        ],
        "KvmServerStateEnabled": false,
        "KvmVendor": "Avocent",
        "TunneledKvm": false
    },
    "LicenseInfo": {
        "Tier": "Premier"
    },
    "LocatorLedOn": false,
    "ManagementIp": "10.58.50.41",
    "Redfish": {
        "Capable": true,
        "Enabled": true
    },
    "UCSM": {
        "Capable": false,
        "Enabled": false
    },
    "IMC": {
        "Capable": true,
        "Enabled": false
    },
    "AvailableMemory": 393216,
    "TotalMemory": 393216,
    "UsedMemory": 0,
    "TotalMemoryUnit": "384 [GiB]",
    "TotalMemoryGB": 384,
    "AvailableMemoryUnit": "384 [GiB]",
    "AvailableMemoryGB": 384,
    "UsedMemoryUnit": "0 [KiB]",
    "UsedMemoryGB": 0,
    "UsedMemoryPct": 0,
    "UsedMemoryPctUnit": "0%",
    "MemoryInfo": [
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-1",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_A1",
            "MemoryId": 1,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73490",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-2",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_A2",
            "MemoryId": 2,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-3",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_B1",
            "MemoryId": 3,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F72CD9",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-4",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_B2",
            "MemoryId": 4,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-5",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_C1",
            "MemoryId": 5,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F7348D",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-6",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_C2",
            "MemoryId": 6,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-7",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_D1",
            "MemoryId": 7,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F734A7",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-8",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_D2",
            "MemoryId": 8,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-9",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_E1",
            "MemoryId": 9,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73492",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-10",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_E2",
            "MemoryId": 10,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-11",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_F1",
            "MemoryId": 11,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73498",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-12",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_F2",
            "MemoryId": 12,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-13",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_G1",
            "MemoryId": 13,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F7348E",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-14",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_G2",
            "MemoryId": 14,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-15",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_H1",
            "MemoryId": 15,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73495",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-16",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_H2",
            "MemoryId": 16,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-17",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_J1",
            "MemoryId": 17,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F72CCC",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-18",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_J2",
            "MemoryId": 18,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-19",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_K1",
            "MemoryId": 19,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73493",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-20",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_K2",
            "MemoryId": 20,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-21",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_L1",
            "MemoryId": 21,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73494",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-22",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_L2",
            "MemoryId": 22,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-23",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_M1",
            "MemoryId": 23,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F734AD",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-24",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_M2",
            "MemoryId": 24,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        }
    ],
    "PciDevicesInfo": [
        {
            "Model": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
            "Pid": "UCSC-PCIE-ID25GF",
            "SlotId": "3",
            "Vendor": "0x8086",
            "FirmwareVersion": "0x8000B900-1.826.0",
            "Dn": "sys/rack-unit-1/equipped-slot-3",
            "Serial": ""
        },
        {
            "Model": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
            "Pid": "UCSC-PCIE-ID25GF",
            "SlotId": "6",
            "Vendor": "0x8086",
            "FirmwareVersion": "0x8000B900-1.826.0",
            "Dn": "sys/rack-unit-1/equipped-slot-6",
            "Serial": ""
        },
        {
            "Model": "Intel X550 LOM",
            "Pid": "UNKNOWN",
            "SlotId": "L",
            "Vendor": "0x8086",
            "FirmwareVersion": "0x800016F9-1.826.0",
            "Dn": "sys/rack-unit-1/equipped-slot-L",
            "Serial": ""
        },
        {
            "Model": "Cisco UCS VIC 1457 MLOM",
            "Pid": "UCSC-MLOM-C25Q-04",
            "SlotId": "MLOM",
            "Vendor": "0x1137",
            "FirmwareVersion": "5.2(2b)",
            "Dn": "sys/rack-unit-1/equipped-slot-MLOM",
            "Serial": ""
        },
        {
            "Model": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
            "Pid": "UCSC-RAID-M5",
            "SlotId": "MRAID",
            "Vendor": "0x1000",
            "FirmwareVersion": "N/A",
            "Dn": "sys/rack-unit-1/equipped-slot-MRAID",
            "Serial": ""
        }
    ],
    "PciModels": [
        "UCSC-MLOM-C25Q-04",
        "UCSC-RAID-M5",
        "Intel X550 LOM",
        "UCSC-PCIE-ID25GF",
        "UCSC-PCIE-ID25GF"
    ],
    "GpuInfo": [],
    "AdaptersInfo": [
        {
            "Moid": "5fdf9c886176752d35e477ea",
            "Dn": "sys/rack-unit-1/network-adapter-3",
            "AdapterId": "3",
            "Name": "Adapter 3",
            "BaseMacAddress": "",
            "ComputeNodeMoid": "5fdf9c016176752d35e44795",
            "ExtEthIfsIds": [],
            "ExtEthIfsCount": 0,
            "HostEthIfsIds": [
                "5fdf9c8a6176752d35e478e5",
                "5fdf9c8a6176752d35e478f4"
            ],
            "HostEthIfsCount": 2,
            "HostFcIfsIds": [],
            "HostFcIfsCount": 0,
            "HostIscsiIfsIds": [],
            "HostIscsiIfsCount": 0,
            "Model": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
            "OperState": "",
            "PartNumber": "",
            "Presence": "equipped",
            "Healthy": false,
            "PciSlot": "3",
            "Thermal": "",
            "Serial": "",
            "Vendor": ""
        },
        {
            "Moid": "5fdf9c886176752d35e477e4",
            "Dn": "sys/rack-unit-1/network-adapter-6",
            "AdapterId": "6",
            "Name": "Adapter 6",
            "BaseMacAddress": "",
            "ComputeNodeMoid": "5fdf9c016176752d35e44795",
            "ExtEthIfsIds": [],
            "ExtEthIfsCount": 0,
            "HostEthIfsIds": [
                "5fdf9c8a6176752d35e478da",
                "5fdf9c8a6176752d35e478e1"
            ],
            "HostEthIfsCount": 2,
            "HostFcIfsIds": [],
            "HostFcIfsCount": 0,
            "HostIscsiIfsIds": [],
            "HostIscsiIfsCount": 0,
            "Model": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
            "OperState": "",
            "PartNumber": "",
            "Presence": "equipped",
            "Healthy": false,
            "PciSlot": "6",
            "Thermal": "",
            "Serial": "",
            "Vendor": ""
        },
        {
            "Moid": "5fdf9c886176752d35e477f0",
            "Dn": "sys/rack-unit-1/network-adapter-L",
            "AdapterId": "L",
            "Name": "Adapter L",
            "BaseMacAddress": "",
            "ComputeNodeMoid": "5fdf9c016176752d35e44795",
            "ExtEthIfsIds": [],
            "ExtEthIfsCount": 0,
            "HostEthIfsIds": [
                "5fdf9c8a6176752d35e478f6",
                "5fdf9c8a6176752d35e478fb"
            ],
            "HostEthIfsCount": 2,
            "HostFcIfsIds": [],
            "HostFcIfsCount": 0,
            "HostIscsiIfsIds": [],
            "HostIscsiIfsCount": 0,
            "Model": "Cisco(R) LOM X550-T2",
            "OperState": "",
            "PartNumber": "",
            "Presence": "equipped",
            "Healthy": false,
            "PciSlot": "L",
            "Thermal": "",
            "Serial": "",
            "Vendor": ""
        },
        {
            "Moid": "5fdf9bf46176752d35e4426e",
            "Dn": "sys/rack-unit-1/adaptor-MLOM",
            "AdapterId": "MLOM",
            "Name": "Adapter MLOM",
            "BaseMacAddress": "",
            "ComputeNodeMoid": "5fdf9c016176752d35e44795",
            "ExtEthIfsIds": [
                "5fff44fd6176752d3566f25c",
                "5fff44fd6176752d3566f25e",
                "5fff44fd6176752d3566f260",
                "5fff44fd6176752d3566f262"
            ],
            "ExtEthIfsCount": 4,
            "HostEthIfsIds": [
                "6358db4d76752d3139b6e4c9",
                "6358db5276752d3139b6e5c9",
                "6358db5276752d3139b6e5cb",
                "6358db5276752d3139b6e5cd"
            ],
            "HostEthIfsCount": 4,
            "HostFcIfsIds": [
                "6390087976752d313914f241",
                "6390087976752d313914f243",
                "6390087976752d313914f245",
                "6390087976752d313914f247"
            ],
            "HostFcIfsCount": 4,
            "HostIscsiIfsIds": [],
            "HostIscsiIfsCount": 0,
            "Model": "UCSC-MLOM-C25Q-04",
            "OperState": "",
            "PartNumber": "",
            "Presence": "equipped",
            "Healthy": false,
            "PciSlot": "MLOM",
            "Thermal": "",
            "Serial": "FCH24157D1V",
            "Vendor": "Cisco Systems Inc"
        }
    ],
    "ExtEthInfo": [
        {
            "Moid": "5fff44fd6176752d3566f25c",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/ext-eth-0",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "InterfaceId": "0",
            "MacAddress": "3C:57:31:CC:0E:3E",
            "SwitchId": "",
            "PeerHostPortId": null,
            "PeerAggrPortId": 0,
            "PeerDn": "",
            "PeerPortId": 0,
            "PeerSlotId": 0
        },
        {
            "Moid": "5fff44fd6176752d3566f25e",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/ext-eth-1",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "InterfaceId": "1",
            "MacAddress": "3C:57:31:CC:0E:40",
            "SwitchId": "",
            "PeerHostPortId": null,
            "PeerAggrPortId": 0,
            "PeerDn": "",
            "PeerPortId": 0,
            "PeerSlotId": 0
        },
        {
            "Moid": "5fff44fd6176752d3566f260",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/ext-eth-2",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "InterfaceId": "2",
            "MacAddress": "3C:57:31:CC:0E:3F",
            "SwitchId": "",
            "PeerHostPortId": null,
            "PeerAggrPortId": 0,
            "PeerDn": "",
            "PeerPortId": 0,
            "PeerSlotId": 0
        },
        {
            "Moid": "5fff44fd6176752d3566f262",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/ext-eth-3",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "InterfaceId": "3",
            "MacAddress": "3C:57:31:CC:0E:41",
            "SwitchId": "",
            "PeerHostPortId": null,
            "PeerAggrPortId": 0,
            "PeerDn": "",
            "PeerPortId": 0,
            "PeerSlotId": 0
        }
    ],
    "HostEthInfo": [
        {
            "Moid": "5fdf9c8a6176752d35e478e5",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/network-adapter-3/eth-1",
            "AdapterUnitId": "5fdf9c886176752d35e477ea",
            "AdminState": "",
            "HostEthInterfaceId": 1,
            "InterfaceType": "",
            "MacAddress": "3c:fd:fe:ee:2c:30",
            "Name": "eth-1",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter 3",
            "AdapterPciSlot": "3"
        },
        {
            "Moid": "5fdf9c8a6176752d35e478f4",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/network-adapter-3/eth-2",
            "AdapterUnitId": "5fdf9c886176752d35e477ea",
            "AdminState": "",
            "HostEthInterfaceId": 2,
            "InterfaceType": "",
            "MacAddress": "3c:fd:fe:ee:2c:31",
            "Name": "eth-2",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter 3",
            "AdapterPciSlot": "3"
        },
        {
            "Moid": "5fdf9c8a6176752d35e478da",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/network-adapter-6/eth-1",
            "AdapterUnitId": "5fdf9c886176752d35e477e4",
            "AdminState": "",
            "HostEthInterfaceId": 1,
            "InterfaceType": "",
            "MacAddress": "3c:fd:fe:ee:2d:60",
            "Name": "eth-1",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter 6",
            "AdapterPciSlot": "6"
        },
        {
            "Moid": "5fdf9c8a6176752d35e478e1",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/network-adapter-6/eth-2",
            "AdapterUnitId": "5fdf9c886176752d35e477e4",
            "AdminState": "",
            "HostEthInterfaceId": 2,
            "InterfaceType": "",
            "MacAddress": "3c:fd:fe:ee:2d:61",
            "Name": "eth-2",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter 6",
            "AdapterPciSlot": "6"
        },
        {
            "Moid": "5fdf9c8a6176752d35e478f6",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/network-adapter-L/eth-1",
            "AdapterUnitId": "5fdf9c886176752d35e477f0",
            "AdminState": "",
            "HostEthInterfaceId": 1,
            "InterfaceType": "",
            "MacAddress": "5c:71:0d:26:37:b2",
            "Name": "eth-1",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter L",
            "AdapterPciSlot": "L"
        },
        {
            "Moid": "5fdf9c8a6176752d35e478fb",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/network-adapter-L/eth-2",
            "AdapterUnitId": "5fdf9c886176752d35e477f0",
            "AdminState": "",
            "HostEthInterfaceId": 2,
            "InterfaceType": "",
            "MacAddress": "5c:71:0d:26:37:b3",
            "Name": "eth-2",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter L",
            "AdapterPciSlot": "L"
        },
        {
            "Moid": "6358db4d76752d3139b6e4c9",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-eth-eth0",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostEthInterfaceId": 0,
            "InterfaceType": "virtual",
            "MacAddress": "3C:57:31:CC:0E:46",
            "Name": "eth0",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        },
        {
            "Moid": "6358db5276752d3139b6e5c9",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-eth-eth1",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostEthInterfaceId": 0,
            "InterfaceType": "virtual",
            "MacAddress": "3C:57:31:CC:0E:47",
            "Name": "eth1",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        },
        {
            "Moid": "6358db5276752d3139b6e5cb",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-eth-eth2",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostEthInterfaceId": 0,
            "InterfaceType": "virtual",
            "MacAddress": "3C:57:31:CC:0E:48",
            "Name": "eth2",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        },
        {
            "Moid": "6358db5276752d3139b6e5cd",
            "Type": "HostEth",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-eth-eth3",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostEthInterfaceId": 0,
            "InterfaceType": "virtual",
            "MacAddress": "3C:57:31:CC:0E:49",
            "Name": "eth3",
            "OperState": "",
            "Operability": "",
            "PciAddr": "",
            "PeerDn": "",
            "PeerInterface": null,
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        }
    ],
    "HostFcInfo": [
        {
            "Moid": "6390087976752d313914f241",
            "Type": "HostFc",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-fc-fc0",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostFcInterfaceId": 0,
            "Name": "fc0",
            "OperState": "",
            "Operability": "",
            "Wwnn": "10:00:3C:57:31:CC:0E:4A",
            "Wwpn": "20:00:3C:57:31:CC:0E:4A",
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        },
        {
            "Moid": "6390087976752d313914f243",
            "Type": "HostFc",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-fc-fc1",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostFcInterfaceId": 0,
            "Name": "fc1",
            "OperState": "",
            "Operability": "",
            "Wwnn": "10:00:3C:57:31:CC:0E:4B",
            "Wwpn": "20:00:3C:57:31:CC:0E:4B",
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        },
        {
            "Moid": "6390087976752d313914f245",
            "Type": "HostFc",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-fc-fc2",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostFcInterfaceId": 0,
            "Name": "fc2",
            "OperState": "",
            "Operability": "",
            "Wwnn": "10:00:3C:57:31:CC:0E:4C",
            "Wwpn": "20:00:3C:57:31:CC:0E:4C",
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        },
        {
            "Moid": "6390087976752d313914f247",
            "Type": "HostFc",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/host-fc-fc3",
            "AdapterUnitId": "5fdf9bf46176752d35e4426e",
            "AdminState": "",
            "HostFcInterfaceId": 0,
            "Name": "fc3",
            "OperState": "",
            "Operability": "",
            "Wwnn": "10:00:3C:57:31:CC:0E:4D",
            "Wwpn": "20:00:3C:57:31:CC:0E:4D",
            "AdapterName": "Adapter MLOM",
            "AdapterPciSlot": "MLOM"
        }
    ],
    "Power": {
        "Data": {
            "PowerControl": {
                "PowerConsumedWatts": 324,
                "LimitException": "NoAction",
                "MinConsumedWatts": 177,
                "AverageConsumedWatts": 335,
                "MaxConsumedWatts": 490
            },
            "Voltage": [
                {
                    "Name": "PSU1_VOUT",
                    "ReadingVolts": 12.1,
                    "UpperThresholdCritical": 14,
                    "PhysicalContext": "PowerSupply",
                    "State": "Enabled",
                    "Health": "OK"
                },
                {
                    "Name": "PSU2_VOUT",
                    "ReadingVolts": 12.2,
                    "UpperThresholdCritical": 14,
                    "PhysicalContext": "PowerSupply",
                    "State": "Enabled",
                    "Health": "OK"
                },
                {
                    "Name": "P12V",
                    "ReadingVolts": 11.89,
                    "UpperThresholdCritical": 13.166,
                    "PhysicalContext": "PowerSupply",
                    "State": "Enabled",
                    "Health": "OK"
                },
                {
                    "Name": "P3V_BAT_SCALED",
                    "ReadingVolts": 3.026,
                    "UpperThresholdCritical": 3.588,
                    "PhysicalContext": "PowerSupply",
                    "State": "Enabled",
                    "Health": "OK"
                }
            ],
            "PowerSupply": [
                {
                    "Name": "PSU1",
                    "Model": "PS-2112-9S-LF",
                    "SerialNumber": "LIT241244MU",
                    "PartNumber": "341-0638-03",
                    "SparePartNumber": "341-0638-03",
                    "Manufacturer": "Cisco Systems Inc",
                    "FirmwareVersion": "10062019",
                    "PowerOutputWatts": 148,
                    "LastPowerOutputWatts": 148,
                    "PowerInputWatts": 165,
                    "PowerSupplyType": "AC",
                    "State": "Enabled",
                    "Health": "OK",
                    "MinimumVoltage": 180,
                    "OutputWattage": 1050,
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47
                },
                {
                    "Name": "PSU2",
                    "Model": "PS-2112-9S-LF",
                    "SerialNumber": "LIT241244Z5",
                    "PartNumber": "341-0638-03",
                    "SparePartNumber": "341-0638-03",
                    "Manufacturer": "Cisco Systems Inc",
                    "FirmwareVersion": "10062019",
                    "PowerOutputWatts": 149,
                    "LastPowerOutputWatts": 149,
                    "PowerInputWatts": 164,
                    "PowerSupplyType": "AC",
                    "State": "Enabled",
                    "Health": "OK",
                    "MinimumVoltage": 180,
                    "OutputWattage": 1050,
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47
                }
            ]
        },
        "Summary": {
            "Source": "Redfish",
            "PowerNow": 324,
            "PowerMin": 177,
            "PowerAvg": 335,
            "PowerMax": 490
        }
    },
    "PsuInfo": [
        {
            "__Output": {
                "On": "Green",
                "StateTick": "Green",
                "Voltage": "Green"
            },
            "Moid": "5fdf9c0d6176752d35e44cf7",
            "Name": "",
            "Model": "PS-2112-9S-LF",
            "Serial": "LIT241244MU",
            "Vendor": "Cisco Systems Inc",
            "Dn": "sys/rack-unit-1/psu-1",
            "On": true,
            "Voltage": "ok",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "On": "Green",
                "StateTick": "Green",
                "Voltage": "Green"
            },
            "Moid": "5fdf9c0d6176752d35e44cf9",
            "Name": "",
            "Model": "PS-2112-9S-LF",
            "Serial": "LIT241244Z5",
            "Vendor": "Cisco Systems Inc",
            "Dn": "sys/rack-unit-1/psu-2",
            "On": true,
            "Voltage": "ok",
            "StateTick": "\u2713"
        }
    ],
    "PsuOn": 2,
    "PsuCount": 2,
    "PsuSummary": "2/2",
    "PsuHealthy": true,
    "Connected": true,
    "StorageControllersInfo": [
        {
            "__Output": {
                "Presence": "Green"
            },
            "Model": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
            "Moid": "635840e076752d31399d9215",
            "Vendor": "LSI Logic",
            "Serial": "SK00188839",
            "Presence": "equipped",
            "ControllerStatus": "",
            "PciAddr": "",
            "PciSlot": "MRAID",
            "ControllerId": "MRAID",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID",
            "RaidSupport": "yes",
            "Name": "storage-SAS-MRAID",
            "PhysicalDiskCount": 10,
            "PhysicalDiskIds": [
                "635840e576752d31399d9373",
                "635840e576752d31399d9375",
                "635840e576752d31399d9377",
                "635840e576752d31399d9379",
                "635840e576752d31399d937b",
                "635840e676752d31399d937d",
                "635840e676752d31399d937f",
                "635840e676752d31399d9381",
                "635840e676752d31399d9383",
                "635840e676752d31399d9385"
            ],
            "VirtualDriveCount": 1,
            "VirtualDriveIds": [
                "638f666f76752d3139f6cc14"
            ]
        },
        {
            "__Output": {
                "Presence": "Green"
            },
            "Model": "",
            "Moid": "636ddf1876752d3139c8d4f5",
            "Vendor": "Cisco Systems Inc",
            "Serial": "",
            "Presence": "equipped",
            "ControllerStatus": "",
            "PciAddr": "",
            "PciSlot": "PCIe-Switch",
            "ControllerId": "PCIe-Switch",
            "Dn": "sys/rack-unit-1/board/storage-NVMe-PCIe-Switch",
            "RaidSupport": "N/A",
            "Name": "storage-NVMe-PCIe-Switch",
            "PhysicalDiskCount": 0,
            "PhysicalDiskIds": [],
            "VirtualDriveCount": 0,
            "VirtualDriveIds": []
        }
    ],
    "StorageControllersCount": 2,
    "VirtualDisks": [
        {
            "__Output": {
                "Presence": "Red",
                "Operability": "Red",
                "DriveState": "Green",
                "BootableTick": "Green",
                "StateTick": "Green"
            },
            "Moid": "638f666f76752d3139f6cc14",
            "Name": "vd-0",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/vd-0",
            "Size": "1143455 MB",
            "Type": "RAID 1",
            "VirtualDriveId": "0",
            "Bootable": "true",
            "DriveState": "Optimal",
            "Operability": "",
            "Presence": "",
            "ActualWriteCachePolicy": "write-through",
            "ConfiguredWriteCachePolicy": "write-through",
            "IoPolicy": "",
            "_VirtualDriveId": 0,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "PhysicalDiskCount": 2,
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2713",
            "StateTick": "\u2713",
            "PhysicalDiskIds": [
                "17",
                "18"
            ]
        }
    ],
    "VirtualDiskCount": 1,
    "VirtualDiskCapacity": 1198999470080,
    "VirtualDiskCapacityUnit": "1.2 [TB]",
    "HddDisks": [
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d937b",
            "Bootable": "",
            "DiskId": "13",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-13",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK654680000C024C6NE",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 13,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d937d",
            "Bootable": "",
            "DiskId": "14",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-14",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK65J9T0000C025976H",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 14,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d937f",
            "Bootable": "",
            "DiskId": "15",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-15",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK65HVV0000C024KK59",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 15,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d9381",
            "Bootable": "",
            "DiskId": "16",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-16",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK65M390000C024KKSN",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 16,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d9383",
            "Bootable": "",
            "DiskId": "17",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-17",
            "DriveFirmware": "CN03",
            "DriveState": "Online",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK654FJ0000C024KKCC",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 17,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": "638f666f76752d3139f6cc14",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d9385",
            "Bootable": "",
            "DiskId": "18",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-18",
            "DriveFirmware": "5703",
            "DriveState": "Online",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "AL15SEB120N",
            "Pid": "AL15SEB120N",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "Y9G0A06DFJMF",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "TOSHIBA",
            "_DiskId": 18,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": "638f666f76752d3139f6cc14",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        }
    ],
    "HddDiskCount": 6,
    "HddDiskCapacity": 7193996820480,
    "HddDiskCapacityUnit": "7.19 [TB]",
    "SsdDisks": [
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9373",
            "Bootable": "",
            "DiskId": "9",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-9",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS746002YU960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 9,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9375",
            "Bootable": "",
            "DiskId": "10",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-10",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS746002XE960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 10,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9377",
            "Bootable": "",
            "DiskId": "11",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-11",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS746002VN960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 11,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9379",
            "Bootable": "",
            "DiskId": "12",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-12",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS74610194960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 12,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        }
    ],
    "SsdDiskCount": 4,
    "SsdDiskCapacity": 3835997192192,
    "SsdDiskCapacityUnit": "3.84 [TB]",
    "PhysicalDisks": [
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9373",
            "Bootable": "",
            "DiskId": "9",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-9",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS746002YU960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 9,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9375",
            "Bootable": "",
            "DiskId": "10",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-10",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS746002XE960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 10,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9377",
            "Bootable": "",
            "DiskId": "11",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-11",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS746002VN960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 11,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9379",
            "Bootable": "",
            "DiskId": "12",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-12",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS74610194960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 12,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d937b",
            "Bootable": "",
            "DiskId": "13",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-13",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK654680000C024C6NE",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 13,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d937d",
            "Bootable": "",
            "DiskId": "14",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-14",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK65J9T0000C025976H",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 14,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d937f",
            "Bootable": "",
            "DiskId": "15",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-15",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK65HVV0000C024KK59",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 15,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d9381",
            "Bootable": "",
            "DiskId": "16",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-16",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK65M390000C024KKSN",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 16,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d9383",
            "Bootable": "",
            "DiskId": "17",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-17",
            "DriveFirmware": "CN03",
            "DriveState": "Online",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK654FJ0000C024KKCC",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 17,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": "638f666f76752d3139f6cc14",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d9385",
            "Bootable": "",
            "DiskId": "18",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-18",
            "DriveFirmware": "5703",
            "DriveState": "Online",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "AL15SEB120N",
            "Pid": "AL15SEB120N",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "Y9G0A06DFJMF",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "TOSHIBA",
            "_DiskId": 18,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": "638f666f76752d3139f6cc14",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        }
    ],
    "PhysicalDiskCount": 10,
    "PhysicalDiskCapacity": 11029994012672,
    "PhysicalDiskCapacityUnit": "11.03 [TB]",
    "StorageDrives": "2C 6H 4S 1VD",
    "StorageCapacity": "R 11.03 [TB] , VD 1.2 [TB]",
    "StorageSummary": "2C 6H 4S 1VD R11.03 [TB] L1.2 [TB]",
    "Thermal": {
        "Data": {
            "Temperature": [
                {
                    "Name": "DDR4_P1_A1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 114,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 29,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_B1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 120,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_C1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 126,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_D1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 132,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 29,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_E1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 138,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 29,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_F1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 144,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_G1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 150,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_H1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 156,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_J1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 162,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_K1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 168,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_L1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 174,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_M1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 180,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "MLOM_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 60,
                    "PhysicalContext": "NetworkingDevice",
                    "ReadingCelsius": 54,
                    "UpperThresholdCritical": 90
                },
                {
                    "Name": "P1_TEMP_SENS",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 196,
                    "PhysicalContext": "CPU",
                    "ReadingCelsius": 39.5,
                    "UpperThresholdCritical": 100
                },
                {
                    "Name": "P2_TEMP_SENS",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 197,
                    "PhysicalContext": "CPU",
                    "ReadingCelsius": 39.5,
                    "UpperThresholdCritical": 100
                },
                {
                    "Name": "PCH_TEMP_SENS",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 209,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 33,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "PCIE_SWITCH_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 239,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 39,
                    "UpperThresholdCritical": 100
                },
                {
                    "Name": "PSU1_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 207,
                    "PhysicalContext": "PowerSupply",
                    "ReadingCelsius": 21,
                    "UpperThresholdCritical": 65
                },
                {
                    "Name": "PSU2_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 208,
                    "PhysicalContext": "PowerSupply",
                    "ReadingCelsius": 19,
                    "UpperThresholdCritical": 65
                },
                {
                    "Name": "RISER1_INLET_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 250,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 32,
                    "UpperThresholdCritical": 70
                },
                {
                    "Name": "RISER1_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 245,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 24,
                    "UpperThresholdCritical": 70
                },
                {
                    "Name": "RISER2_INLET_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 249,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 31,
                    "UpperThresholdCritical": 70
                },
                {
                    "Name": "RISER2_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 246,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 70
                },
                {
                    "Name": "TEMP_SENS_FRONT",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 84,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 25,
                    "UpperThresholdCritical": 45
                }
            ],
            "Fan": [
                {
                    "Name": "MOD1_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD1_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD2_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7070,
                    "Value": "7070 RPM"
                },
                {
                    "Name": "MOD2_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7350,
                    "Value": "7350 RPM"
                },
                {
                    "Name": "MOD3_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD3_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD4_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD4_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7350,
                    "Value": "7350 RPM"
                },
                {
                    "Name": "MOD5_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD5_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD6_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD6_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7350,
                    "Value": "7350 RPM"
                },
                {
                    "Name": "MOD7_FAN1_SPEED",
                    "State": "Absent",
                    "Health": "",
                    "PhysicalContext": "",
                    "ReadingUnits": "",
                    "Reading": "",
                    "Value": " "
                }
            ]
        },
        "Summary": {
            "FanHealth": true,
            "SensorHealth": true,
            "HighestTemperature": 54,
            "SmallestGap": 20,
            "OverThreshold": 0
        }
    },
    "Workflow": {
        "Days": 7,
        "Running": null,
        "LatestMoid": "63b5c955696f6e2d30bd0bfb",
        "Last": [
            {
                "__Output": {
                    "Status": "Green"
                },
                "Moid": "63b5c955696f6e2d30bd0bfb",
                "Name": "Turn Off Locator",
                "Progress": 100,
                "CreateTime": "2023-01-04T18:45:41.509Z",
                "StartTime": "2023-01-04T18:45:41.741Z",
                "EndTime": "2023-01-04T18:45:45.353Z",
                "Status": "COMPLETED",
                "Type": "UserDefined",
                "CreateTimeEpoch": 1672854341509,
                "StartTimeEpoch": 1672854341741,
                "EndTimeEpoch": 1672854345353,
                "Running": false,
                "Completed": true,
                "Duration": "00:00:04"
            },
            {
                "__Output": {
                    "Status": "Green"
                },
                "Moid": "63b5c923696f6e2d30bd0b5d",
                "Name": "Turn On Locator",
                "Progress": 100,
                "CreateTime": "2023-01-04T18:44:51.803Z",
                "StartTime": "2023-01-04T18:44:52.467Z",
                "EndTime": "2023-01-04T18:44:57.964Z",
                "Status": "COMPLETED",
                "Type": "UserDefined",
                "CreateTimeEpoch": 1672854291803,
                "StartTimeEpoch": 1672854292467,
                "EndTimeEpoch": 1672854297964,
                "Running": false,
                "Completed": true,
                "Duration": "00:00:05"
            }
        ]
    },
    "TpmInfo": [
        {
            "__Output": {
                "ActivationStatus": "Yellow",
                "AdminState": "Yellow",
                "Presence": "Yellow"
            },
            "ActivationStatus": "unknown",
            "AdminState": "unknown",
            "FirmwareVersion": "",
            "Model": "NA",
            "Moid": "5fdf9c186176752d35e4503a",
            "Presence": "empty",
            "Serial": "NA",
            "TpmId": 0,
            "Vendor": "NA",
            "Version": "NA"
        }
    ],
    "FlagState": "P+ H",
    "FlagManagement": "CRi",
    "FlagWorkflow": "C2"
}
```

Developer output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --all

Developer output

{
    "duration": 71787,
    "isctl": {
        "read": true,
        "calls": 33,
        "success": 33,
        "failed": 0,
        "total_time": 52331
    },
    "redfish": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 4,
        "disconnect": 0,
        "path": 8,
        "connect_time": 4706,
        "disconnect_time": 0,
        "path_time": 2425,
        "total_time": 7131
    },
    "ucsm": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "mo": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "mo_time": 0,
        "total_time": 0
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": true,
        "lines": 466
    }
}

Log: isctl
-----------

2023-01-05 18:53:20.583477	True	2982	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:53:22.563844	True	1976	10	isctl get compute blade   -o json --top 100
2023-01-05 18:53:28.243509	True	1946	0	isctl get tam advisoryinstance --filter "AffectedObject/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:53:29.506090	True	1260	0	isctl get cond alarm --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:53:30.982427	True	1473	1	isctl get compute board --filter "ComputeRackUnit/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:53:32.569869	True	1585	1	isctl get boot devicebootmode --filter "ComputeRackUnit/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:53:34.120270	True	1548	1	isctl get bios bootmode --filter "ComputeRackUnit/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:53:35.637692	True	1514	1	isctl get boot devicebootsecurity --filter "ComputePhysical/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:53:37.132480	True	1492	1	isctl get boot hdddevice --filter "ComputePhysical/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:53:38.436794	True	1297	1	isctl get boot pxedevice --filter "ComputePhysical/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:53:39.809596	True	1369	1	isctl get boot vmediadevice --filter "ComputePhysical/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:53:41.277010	True	1463	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2023-01-05 18:53:42.813531	True	1533	1	isctl get asset devicecontractinformation --filter "DeviceId eq 'WZP23400AJW'"  -o json --top 100
2023-01-05 18:53:44.247466	True	1430	2	isctl get processor unit --filter "ComputeBoard/Moid eq '5fdf9c056176752d35e44930'"  -o json --top 100
2023-01-05 18:53:45.902936	True	1651	7	isctl get equipment fanmodule --filter "Parent/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:53:47.322345	True	1414	10	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:53:48.874510	True	1545	1	isctl get cond hclstatus --filter "ManagedObject/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:53:50.697683	True	1807	5	isctl get cond hclstatusdetail --filter "HclStatus/Moid eq '5fdf9c0673736f2d31c2a581'"  -o json --top 100
2023-01-05 18:53:52.151239	True	1448	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:53:53.854825	True	1695	24	isctl get memory unit --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:53:55.520450	True	1655	5	isctl get pci device --filter "Parent/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:53:56.770984	True	1235	4	isctl get adapter unit --filter "Moid in ('5fdf9bf46176752d35e4426e', '5fdf9c886176752d35e477e4', '5fdf9c886176752d35e477ea', '5fdf9c886176752d35e477f0')"  -o json --top 100
2023-01-05 18:53:58.244886	True	1439	4	isctl get adapter extethinterface --filter "AdapterUnit/Moid in ('5fdf9bf46176752d35e4426e', '5fdf9c886176752d35e477e4', '5fdf9c886176752d35e477ea', '5fdf9c886176752d35e477f0')"  -o json --top 100
2023-01-05 18:53:59.463796	True	1205	10	isctl get adapter hostethinterface --filter "AdapterUnit/Moid in ('5fdf9bf46176752d35e4426e', '5fdf9c886176752d35e477e4', '5fdf9c886176752d35e477ea', '5fdf9c886176752d35e477f0')"  -o json --top 100
2023-01-05 18:54:00.732177	True	1255	4	isctl get adapter hostfcinterface --filter "AdapterUnit/Moid in ('5fdf9bf46176752d35e4426e', '5fdf9c886176752d35e477e4', '5fdf9c886176752d35e477ea', '5fdf9c886176752d35e477f0')"  -o json --top 100
2023-01-05 18:54:05.263474	True	1585	0	isctl get server profile --filter "AssignedServer/Moid eq '5fdf9c016176752d35e44795'" --expand "ConfigChangeDetails" -o json --top 100
2023-01-05 18:54:06.768486	True	1488	2	isctl get equipment psu --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:54:08.360313	True	1564	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2023-01-05 18:54:10.017430	True	1640	2	isctl get storage controller --filter "Parent/Moid eq '5fdf9c056176752d35e44930'"  -o json --top 100
2023-01-05 18:54:11.654943	True	1619	1	isctl get storage virtualdrive --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:54:15.170961	True	1821	10	isctl get storage physicaldisk --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:54:20.102339	True	1751	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:54:18.000Z"  -o json --top 100
2023-01-05 18:54:22.699860	True	1646	1	isctl get equipment tpm --filter "Moid in ('5fdf9c186176752d35e4503a')"  -o json --top 100


Log: redfish
-------------

2023-01-05 18:54:02.625296	True	1875	connect 10.58.50.41
2023-01-05 18:54:02.693046	True	66	10.58.50.41:/redfish/v1/Systems
2023-01-05 18:54:02.773530	True	71	10.58.50.41:/redfish/v1/Chassis
2023-01-05 18:54:02.927542	True	144	10.58.50.41:/redfish/v1/Chassis/1
2023-01-05 18:54:03.666619	True	730	10.58.50.41:/redfish/v1/Chassis/1/Power
2023-01-05 18:54:16.877124	True	1685	connect 10.58.50.41
2023-01-05 18:54:16.940424	True	61	10.58.50.41:/redfish/v1/Systems
2023-01-05 18:54:17.028516	True	79	10.58.50.41:/redfish/v1/Chassis
2023-01-05 18:54:17.228868	True	188	10.58.50.41:/redfish/v1/Chassis/1
2023-01-05 18:54:18.329242	True	1086	10.58.50.41:/redfish/v1/Chassis/1/Thermal
2023-01-05 18:54:20.790153	True	682	disconnect 10.58.50.41
2023-01-05 18:54:25.813655	True	464	disconnect 10.58.50.41
```
