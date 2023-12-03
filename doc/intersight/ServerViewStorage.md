# Intersight Server

## storage view

```
# iserver get server --group test -v storage

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Storage Controller [#16]
------------------------

+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| Server                         | Controller  | Model                          | Vendor            | Serial      | Presence | PCI Slot    | Raid Support | PD | VD |
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| comp-1-p2b-eu-spdc-WZP23400AJW | MRAID       | Cisco 12G Modular Raid         | LSI Logic         | SK00188839  | equipped | MRAID       | yes          | 10 | 1  | 
|                                |             | Controller with 2GB cache      |                   |             |          |             |              |    |    | 
|                                |             | (max 16 drives)                |                   |             |          |             |              |    |    | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| comp-1-p2b-eu-spdc-WZP23400AJW | PCIe-Switch |                                | Cisco Systems Inc |             | equipped | PCIe-Switch |              | 0  | 0  | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| comp-2-p2b-eu-spdc-WZP23400AK4 | MRAID       | Cisco 12G Modular Raid         | LSI Logic         | SK00481450  | equipped | MRAID       | yes          | 10 | 1  | 
|                                |             | Controller with 2GB cache      |                   |             |          |             |              |    |    | 
|                                |             | (max 16 drives)                |                   |             |          |             |              |    |    | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| comp-2-p2b-eu-spdc-WZP23400AK4 | PCIe-Switch |                                | Cisco Systems Inc |             | equipped | PCIe-Switch |              | 0  | 0  | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| comp-3-p2b-eu-spdc-WZP23400AKL | MRAID       | Cisco 12G Modular Raid         | LSI Logic         | SK00475134  | equipped | MRAID       | yes          | 10 | 1  | 
|                                |             | Controller with 2GB cache      |                   |             |          |             |              |    |    | 
|                                |             | (max 16 drives)                |                   |             |          |             |              |    |    | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| comp-3-p2b-eu-spdc-WZP23400AKL | PCIe-Switch |                                | Cisco Systems Inc |             | equipped | PCIe-Switch |              | 0  | 0  | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| comp3-p4b-eu-spdc-WZP262207UM  | MSTOR-RAID  | Cisco Boot optimized M.2 Raid  | Marvell           | FCH26237ESR | equipped | MSTOR-RAID  | yes          | 2  | 1  | 
|                                |             | controller                     |                   |             |          |             |              |    |    | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| comp3-p4b-eu-spdc-WZP262207UM  | MRAID       | Cisco 12G SAS RAID Controller  | LSI Logic         | SKB4218819  | equipped | MRAID       | yes          | 4  | 0  | 
|                                |             | with 4GB FBWC (16 Drives)      |                   |             |          |             |              |    |    | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| FI-ucsb1-eu-spdc-2-1           | 1           | UCSB-MRAID12G-HE               | Cisco Systems Inc | LSK23300055 | equipped | FMEZZ1-SAS  | RAID0, RAID1 | 2  | 1  | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| FI-ucsb1-eu-spdc-2-1           | 1           | Lewisburg SSATA Controller     | Intel Corp.       | LSIROMB-0   | equipped |             | RAID0, RAID1 | 0  | 0  | 
|                                |             | [AHCI mode]                    |                   |             |          |             |              |    |    | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| FI-ucsb1-eu-spdc-2-2           | 1           | Lewisburg SSATA Controller     | Intel Corp.       | LSIROMB-0   | equipped |             | RAID0, RAID1 | 0  | 0  | 
|                                |             | [AHCI mode]                    |                   |             |          |             |              |    |    | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| FI-ucsb1-eu-spdc-2-2           | 1           | UCSB-MRAID12G-HE               | Cisco Systems Inc | LSK2328027N | equipped | FMEZZ1-SAS  | RAID0, RAID1 | 2  | 1  | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| FI-ucsb1-eu-spdc-2-3           | 1           | UCSB-MRAID12G-HE               | Cisco Systems Inc | LSK232903L8 | equipped | FMEZZ1-SAS  | RAID0, RAID1 | 2  | 1  | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| FI-ucsb1-eu-spdc-2-3           | 1           | Lewisburg SSATA Controller     | Intel Corp.       | LSIROMB-0   | equipped |             | RAID0, RAID1 | 0  | 0  | 
|                                |             | [AHCI mode]                    |                   |             |          |             |              |    |    | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| FI-ucsb1-eu-spdc-2-4           | 1           | UCSB-MRAID12G-HE               | Cisco Systems Inc | LSK232903Q4 | equipped | FMEZZ1-SAS  | RAID0, RAID1 | 2  | 1  | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+
| FI-ucsb1-eu-spdc-2-4           | 1           | Lewisburg SSATA Controller     | Intel Corp.       | LSIROMB-0   | equipped |             | RAID0, RAID1 | 0  | 0  | 
|                                |             | [AHCI mode]                    |                   |             |          |             |              |    |    | 
+--------------------------------+-------------+--------------------------------+-------------------+-------------+----------+-------------+--------------+----+----+

Physical Disk - State [#44]
---------------------------

+--------------------------------+-------+------------+---------+----+-------------+------+----------+----------+------------+----------+--------+----------+
| Server                         | State | Controller | Disk Id | VD | Size        | Type | Protocol | Bootable | Link Speed | Fw       | State  | Presence |
+--------------------------------+-------+------------+---------+----+-------------+------+----------+----------+------------+----------+--------+----------+
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | MRAID      | 9       |    | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | SCV1CS08 | Good   | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | MRAID      | 10      |    | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | SCV1CS08 | Good   | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | MRAID      | 11      |    | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | SCV1CS08 | Good   | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | MRAID      | 12      |    | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | SCV1CS08 | Good   | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | MRAID      | 13      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | MRAID      | 14      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | MRAID      | 15      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | MRAID      | 16      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | MRAID      | 17      | 0  | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | MRAID      | 18      | 0  | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 5703     | Good   | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | MRAID      | 9       |    | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | SCV1CS08 | Good   | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | MRAID      | 10      |    | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | SCV1CS08 | Good   | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | MRAID      | 11      |    | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | SCV1CS08 | Good   | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | MRAID      | 12      |    | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | SCV1CS08 | Good   | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | MRAID      | 13      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | MRAID      | 14      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | MRAID      | 15      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | MRAID      | 16      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | MRAID      | 17      | 0  | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | MRAID      | 18      | 0  | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | N0A6     | Good   | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | MRAID      | 9       | 0  | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | SCV1CS08 | Good   | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | MRAID      | 10      | 0  | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | SCV1CS08 | Good   | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | MRAID      | 11      |    | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | SCV1CS08 | Good   | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | MRAID      | 12      |    | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | SCV1CS08 | Good   | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | MRAID      | 13      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | MRAID      | 14      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | MRAID      | 15      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | MRAID      | 16      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | MRAID      | 17      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | CN03     | Good   | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | MRAID      | 18      |    | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 5703     | Good   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | MRAID      | 1       |    | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | HXT79F3Q | Good   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | MRAID      | 2       |    | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | HXT79F3Q | Good   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | MRAID      | 3       |    | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | HXT79F3Q | Good   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | MRAID      | 4       |    | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | HXT79F3Q | Good   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | MSTOR-RAID | 253     | 0  | 240.06 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | D3MC000  | Good   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | MSTOR-RAID | 254     | 0  | 240.06 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | D3MC000  | Good   | equipped | 
| FI-ucsb1-eu-spdc-2-1           | V     | 1          | 1       |    | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    |          | online | equipped | 
| FI-ucsb1-eu-spdc-2-1           | V     | 1          | 2       |    | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    |          | online | equipped | 
| FI-ucsb1-eu-spdc-2-2           | V     | 1          | 1       |    | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    |          | online | equipped | 
| FI-ucsb1-eu-spdc-2-2           | V     | 1          | 2       |    | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    |          | online | equipped | 
| FI-ucsb1-eu-spdc-2-3           | V     | 1          | 1       |    | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    |          | online | equipped | 
| FI-ucsb1-eu-spdc-2-3           | V     | 1          | 2       |    | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    |          | online | equipped | 
| FI-ucsb1-eu-spdc-2-4           | V     | 1          | 1       |    | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    |          | online | equipped | 
| FI-ucsb1-eu-spdc-2-4           | V     | 1          | 2       |    | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    |          | online | equipped | 
+--------------------------------+-------+------------+---------+----+-------------+------+----------+----------+------------+----------+--------+----------+

Physical Disk - Inventory [#44]
-------------------------------

+--------------------------------+---------+-------------------+----------------------------+---------+----------------------+
| Server                         | Disk Id | Pid               | Model                      | Vendor  | Serial               |
+--------------------------------+---------+-------------------+----------------------------+---------+----------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | 9       | UCS-SD960G6I1X-EV | SSDSC2KB960G7K             | ATA     | PHYS746002YU960CGN   | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 10      | UCS-SD960G6I1X-EV | SSDSC2KB960G7K             | ATA     | PHYS746002XE960CGN   | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 11      | UCS-SD960G6I1X-EV | SSDSC2KB960G7K             | ATA     | PHYS746002VN960CGN   | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 12      | UCS-SD960G6I1X-EV | SSDSC2KB960G7K             | ATA     | PHYS74610194960CGN   | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 13      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK654680000C024C6NE | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 14      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK65J9T0000C025976H | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 15      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK65HVV0000C024KK59 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 16      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK65M390000C024KKSN | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 17      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK654FJ0000C024KKCC | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 18      | UCS-HD12TB10K12N  | AL15SEB120N                | TOSHIBA | Y9G0A06DFJMF         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 9       | UCS-SD960G6I1X-EV | SSDSC2KB960G7K             | ATA     | PHYS746100ZW960CGN   | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 10      | UCS-SD960G6I1X-EV | SSDSC2KB960G7K             | ATA     | PHYS746002M1960CGN   | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 11      | UCS-SD960G6I1X-EV | SSDSC2KB960G7K             | ATA     | PHYS746002ME960CGN   | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 12      | UCS-SD960G6I1X-EV | SSDSC2KB960G7K             | ATA     | PHYS746003DM960CGN   | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 13      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK65JQF0000C0259760 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 14      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK65LZ70000C02597DN | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 15      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK65LD10000C024KKJM | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 16      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK64DPD0000C0244K8B | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 17      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK64DX60000C025BW6X | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 18      | UCS-HD12TB10K12N  | ST1200MM0088               | SEAGATE | Z4000FFD0000R616HPN9 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 9       | UCS-SD960G6I1X-EV | SSDSC2KB960G7K             | ATA     | PHYS746002VL960CGN   | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 10      | UCS-SD960G6I1X-EV | SSDSC2KB960G7K             | ATA     | PHYS7461011Y960CGN   | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 11      | UCS-SD960G6I1X-EV | SSDSC2KB960G7K             | ATA     | PHYS746002VC960CGN   | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 12      | UCS-SD960G6I1X-EV | SSDSC2KB960G7K             | ATA     | PHYS7461011K960CGN   | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 13      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK65HXR0000C024KKBS | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 14      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK65K2G0000C024C6NV | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 15      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK654550000C024KM87 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 16      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK64DC40000C0244JS6 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 17      | UCS-HD12TB10K12N  | ST1200MM0009               | SEAGATE | WFK65JKQ0000C02597B5 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 18      | UCS-HD12TB10K12N  | AL15SEB120N                | TOSHIBA | Y9G0A066FJMF         | 
| comp3-p4b-eu-spdc-WZP262207UM  | 1       | UCS-SD19T61X-EV   | SAMSUNG MZ7LH1T9HMLT-00003 | ATA     | S6MTNA0T204886       | 
| comp3-p4b-eu-spdc-WZP262207UM  | 2       | UCS-SD19T61X-EV   | SAMSUNG MZ7LH1T9HMLT-00003 | ATA     | S6MTNA0T106186       | 
| comp3-p4b-eu-spdc-WZP262207UM  | 3       | UCS-SD19T61X-EV   | SAMSUNG MZ7LH1T9HMLT-00003 | ATA     | S6MTNA0T106194       | 
| comp3-p4b-eu-spdc-WZP262207UM  | 4       | UCS-SD19T61X-EV   | SAMSUNG MZ7LH1T9HMLT-00003 | ATA     | S6MTNA0T106181       | 
| comp3-p4b-eu-spdc-WZP262207UM  | 253     | UCS-M2-240GB      | Micron_5300_MTFDDAV240TDS  | ATA     | MSY26191X8W          | 
| comp3-p4b-eu-spdc-WZP262207UM  | 254     | UCS-M2-240GB      | Micron_5300_MTFDDAV240TDS  | ATA     | MSY26191X8U          | 
| FI-ucsb1-eu-spdc-2-1           | 1       | UCS-HD300G10K12G  | ST300MM0048                | SEAGATE | W0K3N28E0000K03371D4 | 
| FI-ucsb1-eu-spdc-2-1           | 2       | UCS-HD300G10K12G  | ST300MM0048                | SEAGATE | W0K3N2DZ0000K0334YW3 | 
| FI-ucsb1-eu-spdc-2-2           | 1       | UCS-HD300G10K12G  | ST300MM0048                | SEAGATE | W0K3LKAJ0000K03394BQ | 
| FI-ucsb1-eu-spdc-2-2           | 2       | UCS-HD300G10K12G  | ST300MM0048                | SEAGATE | W0K3LK8X0000K03394EE | 
| FI-ucsb1-eu-spdc-2-3           | 1       | UCS-HD300G10K12G  | ST300MM0048                | SEAGATE | W0K3N2EV0000K03371BT | 
| FI-ucsb1-eu-spdc-2-3           | 2       | UCS-HD300G10K12G  | ST300MM0048                | SEAGATE | W0K3N2FL0000K0334XTB | 
| FI-ucsb1-eu-spdc-2-4           | 1       | UCS-HD300G10K12G  | ST300MM0048                | SEAGATE | W0K3LKCV0000K0336Y6S | 
| FI-ucsb1-eu-spdc-2-4           | 2       | UCS-HD300G10K12G  | ST300MM0048                | SEAGATE | W0K3LG700000K03394KH | 
+--------------------------------+---------+-------------------+----------------------------+---------+----------------------+

Virtual Drive [#8]
------------------

+--------------------------------+-------+------------+----------+-------------+-------+--------+-------------+----------+---------------+-------------+
| Server                         | State | Controller | Drive Id | Size        | Disks | Type   | Name        | Bootable | Write Cache   | Drive State |
+--------------------------------+-------+------------+----------+-------------+-------+--------+-------------+----------+---------------+-------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | MRAID      | 0        | 1.2 [TB]    | 2     | RAID 1 | vd-0        | V        | write-through | Optimal     | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | MRAID      | 0        | 1.2 [TB]    | 2     | RAID 1 | vd-0        | V        | write-through | Optimal     | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | MRAID      | 0        | 1.92 [TB]   | 2     | RAID 0 | RAID0_910   | V        | write-through | Optimal     | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | MSTOR-RAID | 0        | 239.99 [GB] | 2     | RAID 1 | MStorBootVd | V        | write-through | Optimal     | 
| FI-ucsb1-eu-spdc-2-1           | V     | 1          | 0        | 299.0 [GB]  | 2     | mirror |             | V        | write-through | optimal     | 
| FI-ucsb1-eu-spdc-2-2           | V     | 1          | 0        | 299.0 [GB]  | 2     | mirror |             | V        | write-through | optimal     | 
| FI-ucsb1-eu-spdc-2-3           | V     | 1          | 0        | 299.0 [GB]  | 2     | mirror |             | V        | write-through | optimal     | 
| FI-ucsb1-eu-spdc-2-4           | V     | 1          | 0        | 299.0 [GB]  | 2     | mirror |             | V        | write-through | optimal     | 
+--------------------------------+-------+------------+----------+-------------+-------+--------+-------------+----------+---------------+-------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v storage

{
    "duration": 11745,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 9785
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
        "lines": 32
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:28:26.731446	True	2223	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:28:28.461477	True	1727	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:28:30.793257	True	2278	12	isctl get compute blade   -o json --top 100
2023-12-03 15:28:32.834149	True	2012	16	isctl get storage controller --filter "Parent/Moid in ('5fdf9c056176752d35e44930', '5fdf9c7c6176752d35e472bd', '5fdf9d066176752d35e4aebe', '6385021176752d313964cbe0', '6501db4c76752d3901eb3890', '6501db4c76752d3901eb381d', '6501db4c76752d3901eb3882', '6501db4c76752d3901eb38a9')" --expand "PhysicalDisks,VirtualDrives" -o json --top 100
2023-12-03 15:28:34.466750	True	1545	8	isctl get storage physicaldiskusage --filter "StorageVirtualDrive/Moid in ('638f666f76752d3139f6cc14', '638fcd2976752d313909b32e', '617917b976752d3139754146', '65438f6a76752d3901322928', '6501db5276752d3901eb4051', '6501db5076752d3901eb3e4a', '6501db4f76752d3901eb3cee', '6501db5176752d3901eb3f14')"  -o json --top 100
```

[[Back]](./ServerInventory.md)