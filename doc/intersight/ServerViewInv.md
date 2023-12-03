# Intersight Server

## inv view

```
# iserver get server --group test -v inv

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect chassis api objects...
Collect server api objects...


Server Inventory (R): comp-1-p2b-eu-spdc-WZP23400AJW
----------------------------------------------------

+--------------------+---------------------------------+------------------------------------------------------------------+----------------------+----------------------+-------------------+
| Type               | Name                            | Model                                                            | Vendor               | Serial               | Pid               |
+--------------------+---------------------------------+------------------------------------------------------------------+----------------------+----------------------+-------------------+
| Server             | Rack Server                     | UCSC-C240-M5SN                                                   | Cisco Systems Inc    | WZP23400AJW          | UCSC-C240-M5SN    | 
| Board              | Mother Board                    | UCSC-C240-M5SN                                                   | Cisco Systems Inc    | WZP23400AJW          | UCSC-C240-M5SN    | 
| CPU                | CPU #1                          | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz                         | Intel(R) Corporation |                      | UCS-CPU-I6248     | 
| CPU                | CPU #2                          | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz                         | Intel(R) Corporation |                      | UCS-CPU-I6248     | 
| Memory             | Memory #1                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F73490             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #3                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F72CD9             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #5                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F7348D             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #7                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F734A7             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #9                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F73492             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #11                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F73498             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #13                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F7348E             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #15                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F73495             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #17                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F72CCC             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #19                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F73493             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #21                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F73494             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #23                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F734AD             | UCS-MR-X32G2RT-H  | 
| Storage Controller | Storage Controller #MRAID       | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | LSI Logic            | SK00188839           | UCSC-RAID-M5      | 
| Storage Controller | Storage Controller #PCIe-Switch |                                                                  | Cisco Systems Inc    |                      |                   | 
| Disk               | Disk #10                        | SSDSC2KB960G7K                                                   | ATA                  | PHYS746002XE960CGN   | UCS-SD960G6I1X-EV | 
| Disk               | Disk #11                        | SSDSC2KB960G7K                                                   | ATA                  | PHYS746002VN960CGN   | UCS-SD960G6I1X-EV | 
| Disk               | Disk #12                        | SSDSC2KB960G7K                                                   | ATA                  | PHYS74610194960CGN   | UCS-SD960G6I1X-EV | 
| Disk               | Disk #13                        | ST1200MM0009                                                     | SEAGATE              | WFK654680000C024C6NE | UCS-HD12TB10K12N  | 
| Disk               | Disk #14                        | ST1200MM0009                                                     | SEAGATE              | WFK65J9T0000C025976H | UCS-HD12TB10K12N  | 
| Disk               | Disk #15                        | ST1200MM0009                                                     | SEAGATE              | WFK65HVV0000C024KK59 | UCS-HD12TB10K12N  | 
| Disk               | Disk #16                        | ST1200MM0009                                                     | SEAGATE              | WFK65M390000C024KKSN | UCS-HD12TB10K12N  | 
| Disk               | Disk #17                        | ST1200MM0009                                                     | SEAGATE              | WFK654FJ0000C024KKCC | UCS-HD12TB10K12N  | 
| Disk               | Disk #18                        | AL15SEB120N                                                      | TOSHIBA              | Y9G0A06DFJMF         | UCS-HD12TB10K12N  | 
| Disk               | Disk #9                         | SSDSC2KB960G7K                                                   | ATA                  | PHYS746002YU960CGN   | UCS-SD960G6I1X-EV | 
| PCI Adapter        | PCI Slot 3                      | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 0x8086               |                      | UCSC-PCIE-ID25GF  | 
| PCI Adapter        | PCI Slot 6                      | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 0x8086               |                      | UCSC-PCIE-ID25GF  | 
| PCI Adapter        | PCI Slot L                      | Intel X550 LOM                                                   | 0x8086               |                      |                   | 
| PCI Adapter        | PCI Slot MLOM                   | Cisco UCS VIC 1457 MLOM                                          | 0x1137               | FCH24157D1V          | UCSC-MLOM-C25Q-04 | 
| PCI Adapter        | PCI Slot MRAID                  | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 0x1000               | SK00188839           | UCSC-RAID-M5      | 
| Fan                | Fan Module 1 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 1 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 2 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 2 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 3 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 3 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 4 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 4 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 5 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 5 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 6 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 6 - Fan 2            |                                                                  |                      |                      |                   | 
| PSU                | PSU #1                          | PS-2112-9S-LF                                                    | Cisco Systems Inc    | LIT241244MU          | PS-2112-9S-LF     | 
| PSU                | PSU #2                          | PS-2112-9S-LF                                                    | Cisco Systems Inc    | LIT241244Z5          | PS-2112-9S-LF     | 
+--------------------+---------------------------------+------------------------------------------------------------------+----------------------+----------------------+-------------------+

Server Inventory (R): comp-2-p2b-eu-spdc-WZP23400AK4
----------------------------------------------------

+--------------------+---------------------------------+------------------------------------------------------------------+----------------------+----------------------+-------------------+
| Type               | Name                            | Model                                                            | Vendor               | Serial               | Pid               |
+--------------------+---------------------------------+------------------------------------------------------------------+----------------------+----------------------+-------------------+
| Server             | Rack Server                     | UCSC-C240-M5SN                                                   | Cisco Systems Inc    | WZP23400AK4          | UCSC-C240-M5SN    | 
| Board              | Mother Board                    | UCSC-C240-M5SN                                                   | Cisco Systems Inc    | WZP23400AK4          | UCSC-C240-M5SN    | 
| CPU                | CPU #1                          | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz                         | Intel(R) Corporation |                      | UCS-CPU-I6248     | 
| CPU                | CPU #2                          | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz                         | Intel(R) Corporation |                      | UCS-CPU-I6248     | 
| Memory             | Memory #1                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F736F1             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #3                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F7370D             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #5                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F736F9             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #7                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F73709             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #9                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F736F7             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #11                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F7370A             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #13                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F736F8             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #15                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F736ED             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #17                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F736F6             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #19                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0EFB85E             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #21                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F72BFA             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #23                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F72BFE             | UCS-MR-X32G2RT-H  | 
| Storage Controller | Storage Controller #MRAID       | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | LSI Logic            | SK00481450           | UCSC-RAID-M5      | 
| Storage Controller | Storage Controller #PCIe-Switch |                                                                  | Cisco Systems Inc    |                      |                   | 
| Disk               | Disk #10                        | SSDSC2KB960G7K                                                   | ATA                  | PHYS746002M1960CGN   | UCS-SD960G6I1X-EV | 
| Disk               | Disk #11                        | SSDSC2KB960G7K                                                   | ATA                  | PHYS746002ME960CGN   | UCS-SD960G6I1X-EV | 
| Disk               | Disk #12                        | SSDSC2KB960G7K                                                   | ATA                  | PHYS746003DM960CGN   | UCS-SD960G6I1X-EV | 
| Disk               | Disk #13                        | ST1200MM0009                                                     | SEAGATE              | WFK65JQF0000C0259760 | UCS-HD12TB10K12N  | 
| Disk               | Disk #14                        | ST1200MM0009                                                     | SEAGATE              | WFK65LZ70000C02597DN | UCS-HD12TB10K12N  | 
| Disk               | Disk #15                        | ST1200MM0009                                                     | SEAGATE              | WFK65LD10000C024KKJM | UCS-HD12TB10K12N  | 
| Disk               | Disk #16                        | ST1200MM0009                                                     | SEAGATE              | WFK64DPD0000C0244K8B | UCS-HD12TB10K12N  | 
| Disk               | Disk #17                        | ST1200MM0009                                                     | SEAGATE              | WFK64DX60000C025BW6X | UCS-HD12TB10K12N  | 
| Disk               | Disk #18                        | ST1200MM0088                                                     | SEAGATE              | Z4000FFD0000R616HPN9 | UCS-HD12TB10K12N  | 
| Disk               | Disk #9                         | SSDSC2KB960G7K                                                   | ATA                  | PHYS746100ZW960CGN   | UCS-SD960G6I1X-EV | 
| PCI Adapter        | PCI Slot 3                      | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 0x8086               |                      | UCSC-PCIE-ID25GF  | 
| PCI Adapter        | PCI Slot 6                      | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 0x8086               |                      | UCSC-PCIE-ID25GF  | 
| PCI Adapter        | PCI Slot L                      | Intel X550 LOM                                                   | 0x8086               |                      |                   | 
| PCI Adapter        | PCI Slot MLOM                   | Cisco UCS VIC 1457 MLOM                                          | 0x1137               | FCH24157DE1          | UCSC-MLOM-C25Q-04 | 
| PCI Adapter        | PCI Slot MRAID                  | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 0x1000               | SK00481450           | UCSC-RAID-M5      | 
| Fan                | Fan Module 1 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 1 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 2 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 2 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 3 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 3 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 4 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 4 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 5 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 5 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 6 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 6 - Fan 2            |                                                                  |                      |                      |                   | 
| PSU                | PSU #1                          | PS-2112-9S-LF                                                    | Cisco Systems Inc    | LIT241244RQ          | PS-2112-9S-LF     | 
| PSU                | PSU #2                          | PS-2112-9S-LF                                                    | Cisco Systems Inc    | LIT241242TS          | PS-2112-9S-LF     | 
+--------------------+---------------------------------+------------------------------------------------------------------+----------------------+----------------------+-------------------+

Server Inventory (R): comp-3-p2b-eu-spdc-WZP23400AKL
----------------------------------------------------

+--------------------+---------------------------------+------------------------------------------------------------------+----------------------+----------------------+-------------------+
| Type               | Name                            | Model                                                            | Vendor               | Serial               | Pid               |
+--------------------+---------------------------------+------------------------------------------------------------------+----------------------+----------------------+-------------------+
| Server             | Rack Server                     | UCSC-C240-M5SN                                                   | Cisco Systems Inc    | WZP23400AKL          | UCSC-C240-M5SN    | 
| Board              | Mother Board                    | UCSC-C240-M5SN                                                   | Cisco Systems Inc    | WZP23400AKL          | UCSC-C240-M5SN    | 
| CPU                | CPU #1                          | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz                         | Intel(R) Corporation |                      | UCS-CPU-I6248     | 
| CPU                | CPU #2                          | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz                         | Intel(R) Corporation |                      | UCS-CPU-I6248     | 
| Memory             | Memory #1                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F7348A             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #3                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F7348F             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #5                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F72D59             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #7                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F72D5A             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #9                       | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F734A6             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #11                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F72D73             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #13                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F734E5             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #15                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F72D5D             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #17                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F734C1             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #19                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F72D71             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #21                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F72D86             | UCS-MR-X32G2RT-H  | 
| Memory             | Memory #23                      | 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v (36ASF4G72PZ-2G9E2)           | 0x2C00               | F0F72D60             | UCS-MR-X32G2RT-H  | 
| Storage Controller | Storage Controller #MRAID       | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | LSI Logic            | SK00475134           | UCSC-RAID-M5      | 
| Storage Controller | Storage Controller #PCIe-Switch |                                                                  | Cisco Systems Inc    |                      |                   | 
| Disk               | Disk #10                        | SSDSC2KB960G7K                                                   | ATA                  | PHYS7461011Y960CGN   | UCS-SD960G6I1X-EV | 
| Disk               | Disk #11                        | SSDSC2KB960G7K                                                   | ATA                  | PHYS746002VC960CGN   | UCS-SD960G6I1X-EV | 
| Disk               | Disk #12                        | SSDSC2KB960G7K                                                   | ATA                  | PHYS7461011K960CGN   | UCS-SD960G6I1X-EV | 
| Disk               | Disk #13                        | ST1200MM0009                                                     | SEAGATE              | WFK65HXR0000C024KKBS | UCS-HD12TB10K12N  | 
| Disk               | Disk #14                        | ST1200MM0009                                                     | SEAGATE              | WFK65K2G0000C024C6NV | UCS-HD12TB10K12N  | 
| Disk               | Disk #15                        | ST1200MM0009                                                     | SEAGATE              | WFK654550000C024KM87 | UCS-HD12TB10K12N  | 
| Disk               | Disk #16                        | ST1200MM0009                                                     | SEAGATE              | WFK64DC40000C0244JS6 | UCS-HD12TB10K12N  | 
| Disk               | Disk #17                        | ST1200MM0009                                                     | SEAGATE              | WFK65JKQ0000C02597B5 | UCS-HD12TB10K12N  | 
| Disk               | Disk #18                        | AL15SEB120N                                                      | TOSHIBA              | Y9G0A066FJMF         | UCS-HD12TB10K12N  | 
| Disk               | Disk #9                         | SSDSC2KB960G7K                                                   | ATA                  | PHYS746002VL960CGN   | UCS-SD960G6I1X-EV | 
| PCI Adapter        | PCI Slot 3                      | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 0x8086               |                      | UCSC-PCIE-ID25GF  | 
| PCI Adapter        | PCI Slot 6                      | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 0x8086               |                      | UCSC-PCIE-ID25GF  | 
| PCI Adapter        | PCI Slot L                      | Intel X550 LOM                                                   | 0x8086               |                      | NA                | 
| PCI Adapter        | PCI Slot MLOM                   | Cisco UCS VIC 1457 MLOM                                          | 0x1137               | FCH24157D3D          | UCSC-MLOM-C25Q-04 | 
| PCI Adapter        | PCI Slot MRAID                  | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 0x1000               | SK00475134           | UCSC-RAID-M5      | 
| Fan                | Fan Module 1 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 1 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 2 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 2 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 3 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 3 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 4 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 4 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 5 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 5 - Fan 2            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 6 - Fan 1            |                                                                  |                      |                      |                   | 
| Fan                | Fan Module 6 - Fan 2            |                                                                  |                      |                      |                   | 
| PSU                | PSU #1                          | PS-2112-9S-LF                                                    | Cisco Systems Inc    | LIT241244NV          | PS-2112-9S-LF     | 
| PSU                | PSU #2                          | PS-2112-9S-LF                                                    | Cisco Systems Inc    | LIT241244UN          | PS-2112-9S-LF     | 
+--------------------+---------------------------------+------------------------------------------------------------------+----------------------+----------------------+-------------------+

Server Inventory (R): comp3-p4b-eu-spdc-WZP262207UM
---------------------------------------------------

+--------------------+--------------------------------+---------------------------------------------------------+------------------------------+--------------------+-------------------+
| Type               | Name                           | Model                                                   | Vendor                       | Serial             | Pid               |
+--------------------+--------------------------------+---------------------------------------------------------+------------------------------+--------------------+-------------------+
| Server             | Rack Server                    | UCSC-C225-M6S                                           | Cisco Systems Inc            | WZP262207UM        | UCSC-C225-M6S     | 
| Board              | Mother Board                   | UCSC-C225-M6S                                           | Cisco Systems Inc            | WZP262207UM        | UCSC-C225-M6S     | 
| CPU                | CPU #1                         | AMD EPYC 7763 64-Core Processor                         | Advanced Micro Devices, Inc. |                    | UCS-CPU-A7763     | 
| GPU                | GPU #3                         | NVIDIA T4 PCIe 16GB 70W                                 | 0x10de                       |                    | UCSC-GPU-T4-16    | 
| Memory             | Memory #2                      | 64GB RDIMM DRx4 3200 (16Gb) (M393A8G40AB2-CWE)          | 0xCE00                       | K00O00020713F09E6B | UCS-MR-X64G2RW    | 
| Memory             | Memory #4                      | 64GB RDIMM DRx4 3200 (16Gb) (M393A8G40AB2-CWE)          | 0xCE00                       | K00O00020713F09FB1 | UCS-MR-X64G2RW    | 
| Memory             | Memory #6                      | 64GB RDIMM DRx4 3200 (16Gb) (M393A8G40AB2-CWE)          | 0xCE00                       | K00O00020713F082FF | UCS-MR-X64G2RW    | 
| Memory             | Memory #8                      | 64GB RDIMM DRx4 3200 (16Gb) (M393A8G40AB2-CWE)          | 0xCE00                       | K00O00020713F083E5 | UCS-MR-X64G2RW    | 
| Memory             | Memory #10                     | 64GB RDIMM DRx4 3200 (16Gb) (M393A8G40AB2-CWE)          | 0xCE00                       | K00O00020713F0843C | UCS-MR-X64G2RW    | 
| Memory             | Memory #12                     | 64GB RDIMM DRx4 3200 (16Gb) (M393A8G40AB2-CWE)          | 0xCE00                       | K00O00020713F094EE | UCS-MR-X64G2RW    | 
| Memory             | Memory #14                     | 64GB RDIMM DRx4 3200 (16Gb) (M393A8G40AB2-CWE)          | 0xCE00                       | K00O00020713F0843D | UCS-MR-X64G2RW    | 
| Memory             | Memory #16                     | 64GB RDIMM DRx4 3200 (16Gb) (M393A8G40AB2-CWE)          | 0xCE00                       | K00O00020713F094EF | UCS-MR-X64G2RW    | 
| Storage Controller | Storage Controller #MRAID      | Cisco 12G SAS RAID Controller with 4GB FBWC (16 Drives) | LSI Logic                    | SKB4218819         | UCSC-RAID-M6T     | 
| Storage Controller | Storage Controller #MSTOR-RAID | Cisco Boot optimized M.2 Raid controller                | Marvell                      | FCH26237ESR        | UCS-M2-HWRAID     | 
| Disk               | Disk #1                        | SAMSUNG MZ7LH1T9HMLT-00003                              | ATA                          | S6MTNA0T204886     | UCS-SD19T61X-EV   | 
| Disk               | Disk #2                        | SAMSUNG MZ7LH1T9HMLT-00003                              | ATA                          | S6MTNA0T106186     | UCS-SD19T61X-EV   | 
| Disk               | Disk #253                      | Micron_5300_MTFDDAV240TDS                               | ATA                          | MSY26191X8W        | UCS-M2-240GB      | 
| Disk               | Disk #254                      | Micron_5300_MTFDDAV240TDS                               | ATA                          | MSY26191X8U        | UCS-M2-240GB      | 
| Disk               | Disk #3                        | SAMSUNG MZ7LH1T9HMLT-00003                              | ATA                          | S6MTNA0T106194     | UCS-SD19T61X-EV   | 
| Disk               | Disk #4                        | SAMSUNG MZ7LH1T9HMLT-00003                              | ATA                          | S6MTNA0T106181     | UCS-SD19T61X-EV   | 
| PCI Adapter        | PCI Slot 1                     | Cisco UCS VIC 1455                                      | 0x1137                       | FCH26277VDL        | UCSC-PCIE-C25Q-04 | 
| PCI Adapter        | PCI Slot 3                     | NVIDIA T4 PCIe 16GB 70W                                 | 0x10de                       |                    | UCSC-GPU-T4-16    | 
| PCI Adapter        | PCI Slot MLOM                  | Cisco UCS VIC 1477 MLOM                                 | 0x1137                       | FCH26147UW3        | UCSC-M-V100-04    | 
| PCI Adapter        | PCI Slot MRAID                 | Cisco 12G SAS RAID Controller with 4GB FBWC (16 Drives) | 0x1000                       | SKB4218819         | UCSC-RAID-M6T     | 
| PCI Adapter        | PCI Slot MSTOR-RAID            | Cisco Boot optimized M.2 Raid controller                | 0x1b4b                       | FCH26237ESR        | UCS-M2-HWRAID     | 
| Fan                | Fan Module 1 - Fan 1           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 1 - Fan 2           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 2 - Fan 1           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 2 - Fan 2           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 3 - Fan 1           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 3 - Fan 2           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 4 - Fan 1           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 4 - Fan 2           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 5 - Fan 1           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 5 - Fan 2           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 6 - Fan 1           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 6 - Fan 2           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 7 - Fan 1           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 7 - Fan 2           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 8 - Fan 1           |                                                         |                              |                    |                   | 
| Fan                | Fan Module 8 - Fan 2           |                                                         |                              |                    |                   | 
| PSU                | PSU #1                         | PS-2112-9S-LF                                           | Cisco Systems Inc            | LIT2625AJTW        | PS-2112-9S-LF     | 
| PSU                | PSU #2                         | PS-2112-9S-LF                                           | Cisco Systems Inc            | LIT2625AHMD        | PS-2112-9S-LF     | 
+--------------------+--------------------------------+---------------------------------------------------------+------------------------------+--------------------+-------------------+

Chassis Inventory: FI-ucsb1-eu-spdc-2
-------------------------------------

+---------+----------------------+-------------------------------+-------------------+-------------+-------------------------------+
| Type    | Name                 | Model                         | Vendor            | Serial      | Pid                           |
+---------+----------------------+-------------------------------+-------------------+-------------+-------------------------------+
| Chassis | FI-ucsb1-eu-spdc-2   | UCSB-5108-AC2                 | Cisco Systems Inc | FOX2403P2Z9 | UCSB-5108-AC2                 | 
| Node    | Server #1            | UCSB-B200-M5                  | Cisco Systems Inc | FLM241501FB | UCSB-B200-M5                  | 
| Node    | Server #2            | UCSB-B200-M5                  | Cisco Systems Inc | FLM24140BJB | UCSB-B200-M5                  | 
| Node    | Server #3            | UCSB-B200-M5                  | Cisco Systems Inc | FLM241501CT | UCSB-B200-M5                  | 
| Node    | Server #4            | UCSB-B200-M5                  | Cisco Systems Inc | FLM24140B0B | UCSB-B200-M5                  | 
| IO      | I/O #1 (left)        | UCS-IOM-2408                  | Cisco Systems Inc | FCH24107G7R | UCS-IOM-2408                  | 
| IO      | I/O #2 (right)       | UCS-IOM-2408                  | Cisco Systems Inc | FCH24107GJK | UCS-IOM-2408                  | 
| Fan     | Fan Module 1 - Fan 1 | N20-FAN5                      | Cisco Systems Inc | NWG235001XN | N20-FAN5                      | 
| Fan     | Fan Module 1 - Fan 2 | N20-FAN5                      | Cisco Systems Inc | NWG235001XN | N20-FAN5                      | 
| Fan     | Fan Module 2 - Fan 1 | N20-FAN5                      | Cisco Systems Inc | NWG235004LY | N20-FAN5                      | 
| Fan     | Fan Module 2 - Fan 2 | N20-FAN5                      | Cisco Systems Inc | NWG235004LY | N20-FAN5                      | 
| Fan     | Fan Module 3 - Fan 1 | N20-FAN5                      | Cisco Systems Inc | NWG235003PU | N20-FAN5                      | 
| Fan     | Fan Module 3 - Fan 2 | N20-FAN5                      | Cisco Systems Inc | NWG235003PU | N20-FAN5                      | 
| Fan     | Fan Module 4 - Fan 1 | N20-FAN5                      | Cisco Systems Inc | NWG235004LR | N20-FAN5                      | 
| Fan     | Fan Module 4 - Fan 2 | N20-FAN5                      | Cisco Systems Inc | NWG235004LR | N20-FAN5                      | 
| Fan     | Fan Module 5 - Fan 1 | N20-FAN5                      | Cisco Systems Inc | NWG235001QD | N20-FAN5                      | 
| Fan     | Fan Module 5 - Fan 2 | N20-FAN5                      | Cisco Systems Inc | NWG235001QD | N20-FAN5                      | 
| Fan     | Fan Module 6 - Fan 1 | N20-FAN5                      | Cisco Systems Inc | NWG2350046E | N20-FAN5                      | 
| Fan     | Fan Module 6 - Fan 2 | N20-FAN5                      | Cisco Systems Inc | NWG2350046E | N20-FAN5                      | 
| Fan     | Fan Module 7 - Fan 1 | N20-FAN5                      | Cisco Systems Inc | NWG235001QA | N20-FAN5                      | 
| Fan     | Fan Module 7 - Fan 2 | N20-FAN5                      | Cisco Systems Inc | NWG235001QA | N20-FAN5                      | 
| Fan     | Fan Module 8 - Fan 1 | N20-FAN5                      | Cisco Systems Inc | NWG235001N4 | N20-FAN5                      | 
| Fan     | Fan Module 8 - Fan 2 | N20-FAN5                      | Cisco Systems Inc | NWG235001N4 | N20-FAN5                      | 
| PSU     | PSU #1               | UCSB-PSU-2500ACDV-ECD15020029 | Cisco Systems Inc | DTM234502Y1 | UCSB-PSU-2500ACDV-ECD15020029 | 
| PSU     | PSU #2               | UCSB-PSU-2500ACDV-ECD15020029 | Cisco Systems Inc | DTM234502XY | UCSB-PSU-2500ACDV-ECD15020029 | 
| PSU     | PSU #3               | UCSB-PSU-2500ACDV-ECD15020029 | Cisco Systems Inc | DTM234502XG | UCSB-PSU-2500ACDV-ECD15020029 | 
| PSU     | PSU #4               | UCSB-PSU-2500ACDV-ECD15020029 | Cisco Systems Inc | DTM234502XL | UCSB-PSU-2500ACDV-ECD15020029 | 
+---------+----------------------+-------------------------------+-------------------+-------------+-------------------------------+

Server Inventory (B): FI-ucsb1-eu-spdc-2-1
------------------------------------------

+-------------+---------------------+------------------------------------------+----------------------+----------------------+------------------+
| Type        | Name                | Model                                    | Vendor               | Serial               | Pid              |
+-------------+---------------------+------------------------------------------+----------------------+----------------------+------------------+
| Server      | Blade Server        | UCSB-B200-M5                             | Cisco Systems Inc    | FLM241501FB          | UCSB-B200-M5     | 
| Board       | Mother Board        | UCSB-B200-M5                             | Cisco Systems Inc    | FLM241501FB          | UCSB-B200-M5     | 
| CPU         | CPU #1              | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | Intel(R) Corporation |                      | UCS-CPU-I6248    | 
| CPU         | CPU #2              | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | Intel(R) Corporation |                      | UCS-CPU-I6248    | 
| Memory      | Memory #1           | M393A4K40CB2-CVF                         | 0xCE00               | 14D204CB             |                  | 
| Memory      | Memory #2           | M393A4K40CB2-CVF                         | 0xCE00               | 14D1F4B3             |                  | 
| Memory      | Memory #3           | 36ASF4G72PZ-2G6E1                        | 0x2C00               | F09BA153             |                  | 
| Memory      | Memory #4           | HMA84GR7AFR4N-VK                         | 0xAD00               | 1222D1FE             |                  | 
| Memory      | Memory #7           | HMA84GR7CJR4N-VK                         | 0xAD00               | 834C103C             |                  | 
| Memory      | Memory #8           | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E43D             |                  | 
| Memory      | Memory #9           | HMA84GR7AFR4N-VK                         | 0xAD00               | 1222D090             |                  | 
| Memory      | Memory #10          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76DB55             |                  | 
| Memory      | Memory #13          | M393A4K40CB2-CVF                         | 0xCE00               | 14D1ECF4             |                  | 
| Memory      | Memory #14          | HMA84GR7AFR4N-VK                         | 0xAD00               | 1222D046             |                  | 
| Memory      | Memory #15          | M393A4K40CB2-CVF                         | 0xCE00               | 14D1F981             |                  | 
| Memory      | Memory #16          | HMA84GR7CJR4N-VK                         | 0xAD00               | 834C0F60             |                  | 
| Memory      | Memory #19          | HMA84GR7AFR4N-VK                         | 0xAD00               | 1222D19C             |                  | 
| Memory      | Memory #20          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E225             |                  | 
| Memory      | Memory #21          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | F09BA156             |                  | 
| Memory      | Memory #22          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E1C4             |                  | 
| Disk        | Disk #1             | ST300MM0048                              | SEAGATE              | W0K3N28E0000K03371D4 | UCS-HD300G10K12G | 
| Disk        | Disk #2             | ST300MM0048                              | SEAGATE              | W0K3N2DZ0000K0334YW3 | UCS-HD300G10K12G | 
| PCI Adapter | PCI Slot FMEZZ1-SAS | UCSB-MRAID12G-HE                         | Cisco Systems Inc    | LSK23300055          | UCSB-MRAID12G-HE | 
+-------------+---------------------+------------------------------------------+----------------------+----------------------+------------------+

Server Inventory (B): FI-ucsb1-eu-spdc-2-2
------------------------------------------

+-------------+---------------------+------------------------------------------+----------------------+----------------------+------------------+
| Type        | Name                | Model                                    | Vendor               | Serial               | Pid              |
+-------------+---------------------+------------------------------------------+----------------------+----------------------+------------------+
| Server      | Blade Server        | UCSB-B200-M5                             | Cisco Systems Inc    | FLM24140BJB          | UCSB-B200-M5     | 
| Board       | Mother Board        | UCSB-B200-M5                             | Cisco Systems Inc    | FLM24140BJB          | UCSB-B200-M5     | 
| CPU         | CPU #1              | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | Intel(R) Corporation |                      | UCS-CPU-I6248    | 
| CPU         | CPU #2              | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | Intel(R) Corporation |                      | UCS-CPU-I6248    | 
| Memory      | Memory #1           | M393A4K40CB2-CVF                         | 0xCE00               | 14D1EA35             |                  | 
| Memory      | Memory #2           | HMA84GR7CJR4N-VK                         | 0xAD00               | 834C0F86             |                  | 
| Memory      | Memory #3           | M393A4K40CB2-CVF                         | 0xCE00               | 14D1E9DA             |                  | 
| Memory      | Memory #4           | 36ASF4G72PZ-2G6E1                        | 0x2C00               | F09BA16A             |                  | 
| Memory      | Memory #7           | HMA84GR7AFR4N-VK                         | 0xAD00               | 1222D186             |                  | 
| Memory      | Memory #8           | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76DB7D             |                  | 
| Memory      | Memory #9           | HMA84GR7AFR4N-VK                         | 0xAD00               | 1222D044             |                  | 
| Memory      | Memory #10          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E5B4             |                  | 
| Memory      | Memory #13          | M393A4K40CB2-CVF                         | 0xCE00               | 14D1EA7F             |                  | 
| Memory      | Memory #14          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | F09BA170             |                  | 
| Memory      | Memory #15          | M393A4K40CB2-CVF                         | 0xCE00               | 14D1E9DE             |                  | 
| Memory      | Memory #16          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76DBDC             |                  | 
| Memory      | Memory #19          | HMA84GR7AFR4N-VK                         | 0xAD00               | 1222CFFB             |                  | 
| Memory      | Memory #20          | HMA84GR7CJR4N-VK                         | 0xAD00               | 834C0FBE             |                  | 
| Memory      | Memory #21          | HMA84GR7AFR4N-VK                         | 0xAD00               | 1222D0E2             |                  | 
| Memory      | Memory #22          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E49B             |                  | 
| Disk        | Disk #1             | ST300MM0048                              | SEAGATE              | W0K3LKAJ0000K03394BQ | UCS-HD300G10K12G | 
| Disk        | Disk #2             | ST300MM0048                              | SEAGATE              | W0K3LK8X0000K03394EE | UCS-HD300G10K12G | 
| PCI Adapter | PCI Slot FMEZZ1-SAS | UCSB-MRAID12G-HE                         | Cisco Systems Inc    | LSK2328027N          | UCSB-MRAID12G-HE | 
+-------------+---------------------+------------------------------------------+----------------------+----------------------+------------------+

Server Inventory (B): FI-ucsb1-eu-spdc-2-3
------------------------------------------

+-------------+---------------------+------------------------------------------+----------------------+----------------------+------------------+
| Type        | Name                | Model                                    | Vendor               | Serial               | Pid              |
+-------------+---------------------+------------------------------------------+----------------------+----------------------+------------------+
| Server      | Blade Server        | UCSB-B200-M5                             | Cisco Systems Inc    | FLM241501CT          | UCSB-B200-M5     | 
| Board       | Mother Board        | UCSB-B200-M5                             | Cisco Systems Inc    | FLM241501CT          | UCSB-B200-M5     | 
| CPU         | CPU #1              | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | Intel(R) Corporation |                      | UCS-CPU-I6248    | 
| CPU         | CPU #2              | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | Intel(R) Corporation |                      | UCS-CPU-I6248    | 
| Memory      | Memory #1           | M393A4K40CB2-CVF                         | 0xCE00               | 14D1EA76             |                  | 
| Memory      | Memory #2           | HMA84GR7CJR4N-VK                         | 0xAD00               | 834C1058             |                  | 
| Memory      | Memory #3           | M393A4K40CB2-CVF                         | 0xCE00               | 14D1EA78             |                  | 
| Memory      | Memory #4           | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E4EC             |                  | 
| Memory      | Memory #7           | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76D6F2             |                  | 
| Memory      | Memory #8           | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E525             |                  | 
| Memory      | Memory #9           | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E38B             |                  | 
| Memory      | Memory #10          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E4CD             |                  | 
| Memory      | Memory #13          | M393A4K40CB2-CVF                         | 0xCE00               | 14D204C6             |                  | 
| Memory      | Memory #14          | HMA84GR7CJR4N-VK                         | 0xAD00               | 834C100D             |                  | 
| Memory      | Memory #15          | M393A4K40CB2-CVF                         | 0xCE00               | 14D204C5             |                  | 
| Memory      | Memory #16          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76DBCB             |                  | 
| Memory      | Memory #19          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76DC03             |                  | 
| Memory      | Memory #20          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E25A             |                  | 
| Memory      | Memory #21          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E26D             |                  | 
| Memory      | Memory #22          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76DB69             |                  | 
| Disk        | Disk #1             | ST300MM0048                              | SEAGATE              | W0K3N2EV0000K03371BT | UCS-HD300G10K12G | 
| Disk        | Disk #2             | ST300MM0048                              | SEAGATE              | W0K3N2FL0000K0334XTB | UCS-HD300G10K12G | 
| PCI Adapter | PCI Slot FMEZZ1-SAS | UCSB-MRAID12G-HE                         | Cisco Systems Inc    | LSK232903L8          | UCSB-MRAID12G-HE | 
+-------------+---------------------+------------------------------------------+----------------------+----------------------+------------------+

Server Inventory (B): FI-ucsb1-eu-spdc-2-4
------------------------------------------

+-------------+---------------------+------------------------------------------+----------------------+----------------------+------------------+
| Type        | Name                | Model                                    | Vendor               | Serial               | Pid              |
+-------------+---------------------+------------------------------------------+----------------------+----------------------+------------------+
| Server      | Blade Server        | UCSB-B200-M5                             | Cisco Systems Inc    | FLM24140B0B          | UCSB-B200-M5     | 
| Board       | Mother Board        | UCSB-B200-M5                             | Cisco Systems Inc    | FLM24140B0B          | UCSB-B200-M5     | 
| CPU         | CPU #1              | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | Intel(R) Corporation |                      | UCS-CPU-I6248    | 
| CPU         | CPU #2              | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | Intel(R) Corporation |                      | UCS-CPU-I6248    | 
| Memory      | Memory #1           | M393A4K40CB2-CVF                         | 0xCE00               | 14D204CD             |                  | 
| Memory      | Memory #2           | HMA84GR7CJR4N-VK                         | 0xAD00               | 834C0F1E             |                  | 
| Memory      | Memory #3           | M393A4K40CB2-CVF                         | 0xCE00               | 14D1FA05             |                  | 
| Memory      | Memory #4           | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76DBCA             |                  | 
| Memory      | Memory #7           | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76D9A6             |                  | 
| Memory      | Memory #8           | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E264             |                  | 
| Memory      | Memory #9           | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E24D             |                  | 
| Memory      | Memory #10          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E26F             |                  | 
| Memory      | Memory #13          | M393A4K40CB2-CVF                         | 0xCE00               | 14D204CA             |                  | 
| Memory      | Memory #14          | HMA84GR7CJR4N-VK                         | 0xAD00               | 834C0F25             |                  | 
| Memory      | Memory #15          | M393A4K40CB2-CVF                         | 0xCE00               | 14D203DF             |                  | 
| Memory      | Memory #16          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E535             |                  | 
| Memory      | Memory #19          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76DC22             |                  | 
| Memory      | Memory #20          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E036             |                  | 
| Memory      | Memory #21          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E28A             |                  | 
| Memory      | Memory #22          | 36ASF4G72PZ-2G6E1                        | 0x2C00               | 3C76E52E             |                  | 
| Disk        | Disk #1             | ST300MM0048                              | SEAGATE              | W0K3LKCV0000K0336Y6S | UCS-HD300G10K12G | 
| Disk        | Disk #2             | ST300MM0048                              | SEAGATE              | W0K3LG700000K03394KH | UCS-HD300G10K12G | 
| PCI Adapter | PCI Slot FMEZZ1-SAS | UCSB-MRAID12G-HE                         | Cisco Systems Inc    | LSK232903Q4          | UCSB-MRAID12G-HE | 
+-------------+---------------------+------------------------------------------+----------------------+----------------------+------------------+
```

Developer

```
# iserver get server --group test -v inv

{
    "duration": 45014,
    "isctl": {
        "read": true,
        "calls": 23,
        "success": 23,
        "failed": 0,
        "total_time": 41346
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
        "lines": 144
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:23:41.443770	True	5344	100	isctl get compute rackunit  --expand "PciDevices,Psus,Fanmodules" -o json --top 100
2023-12-03 15:23:43.323560	True	1868	9	isctl get compute rackunit  --expand "PciDevices,Psus,Fanmodules" -o json --top 100 --skip 100
2023-12-03 15:23:45.210648	True	1593	12	isctl get compute blade  --expand "PciDevices" -o json --top 100
2023-12-03 15:23:46.816626	True	1581	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 15:23:48.281295	True	1454	4	isctl get compute blade --filter "EquipmentChassis/Moid in ('6501db4b76752d3901eb37c1')"  -o json --top 100
2023-12-03 15:23:49.863191	True	1570	2	isctl get equipment iocard --filter "EquipmentChassis/Moid in ('6501db4b76752d3901eb37c1')"  -o json --top 100
2023-12-03 15:23:51.508148	True	1638	0	isctl get equipment expandermodule --filter "EquipmentChassis/Moid in ('6501db4b76752d3901eb37c1')"  -o json --top 100
2023-12-03 15:23:53.157658	True	1639	1	isctl get equipment fancontrol --filter "Parent/Moid in ('6501db4b76752d3901eb37c1')"  -o json --top 100
2023-12-03 15:23:54.667933	True	1503	8	isctl get equipment fanmodule --filter "EquipmentChassis/Moid in ('6501db4b76752d3901eb37c1')"  -o json --top 100
2023-12-03 15:23:56.168096	True	1486	16	isctl get equipment fan --filter "Parent/Moid in ('6501db4c76752d3901eb3819', '6501db4c76752d3901eb381f', '6501db4c76752d3901eb3876', '6501db4c76752d3901eb389c', '6501db4c76752d3901eb389e', '6501db4d76752d3901eb399d', '6501db4d76752d3901eb39dd', '6501db4d76752d3901eb3a56')"  -o json --top 100
2023-12-03 15:23:57.745332	True	1560	4	isctl get equipment psu --filter "Parent/Moid in ('6501db4b76752d3901eb37c1')"  -o json --top 100
2023-12-03 15:23:59.905970	True	2096	4	isctl get compute board --filter "ComputeRackUnit/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5')" --expand "Processors" -o json --top 100
2023-12-03 15:24:01.374926	True	1443	4	isctl get compute board --filter "ComputeBlade/Moid in ('6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')" --expand "Processors" -o json --top 100
2023-12-03 15:24:02.929539	True	1521	40	isctl get equipment fan --filter "Parent/Moid in ('5fdf9c106176752d35e44d71', '5fdf9c106176752d35e44d73', '5fdf9c106176752d35e44d75', '5fdf9c106176752d35e44d77', '5fdf9c106176752d35e44d79', '5fdf9c106176752d35e44d7b', '5fdf9c106176752d35e44d7d', '5fdf9c876176752d35e4777c', '5fdf9c876176752d35e4777e', '5fdf9c876176752d35e47780', '5fdf9c876176752d35e47782', '5fdf9c876176752d35e47784', '5fdf9c876176752d35e47786', '5fdf9c876176752d35e47788', '5fdf9d116176752d35e4b355', '5fdf9d116176752d35e4b357', '5fdf9d116176752d35e4b359', '5fdf9d116176752d35e4b35b', '5fdf9d116176752d35e4b35d', '5fdf9d116176752d35e4b35f')"  -o json --top 100
2023-12-03 15:24:04.435333	True	1479	18	isctl get equipment fan --filter "Parent/Moid in ('5fdf9d116176752d35e4b361', '638501f176752d313964c5c6', '638501f176752d313964c5c8', '638501f176752d313964c5ca', '638501f176752d313964c5cc', '638501f176752d313964c5ce', '638501f176752d313964c5d0', '638501f176752d313964c5d2', '638501f176752d313964c5d4')"  -o json --top 100
2023-12-03 15:24:06.159523	True	1688	100	isctl get memory unit --filter "MemoryArray/Moid in ('5fdf9c416176752d35e45e6f', '5fdf9cb86176752d35e48ede', '5fdf9d436176752d35e4c6a5', '638501f276752d313964c605', '6501db4c76752d3901eb3945', '6501db4c76752d3901eb3833', '6501db4d76752d3901eb39a9', '6501db4d76752d3901eb3993')"  -o json --top 100
2023-12-03 15:24:07.865917	True	1658	100	isctl get memory unit --filter "MemoryArray/Moid in ('5fdf9c416176752d35e45e6f', '5fdf9cb86176752d35e48ede', '5fdf9d436176752d35e4c6a5', '638501f276752d313964c605', '6501db4c76752d3901eb3945', '6501db4c76752d3901eb3833', '6501db4d76752d3901eb39a9', '6501db4d76752d3901eb3993')"  -o json --top 100 --skip 100
2023-12-03 15:24:09.474455	True	1546	0	isctl get memory unit --filter "MemoryArray/Moid in ('5fdf9c416176752d35e45e6f', '5fdf9cb86176752d35e48ede', '5fdf9d436176752d35e4c6a5', '638501f276752d313964c605', '6501db4c76752d3901eb3945', '6501db4c76752d3901eb3833', '6501db4d76752d3901eb39a9', '6501db4d76752d3901eb3993')"  -o json --top 100 --skip 200
2023-12-03 15:24:11.686540	True	2112	20	isctl get adapter unit --filter "Moid in ('5fdf9bf46176752d35e4426e', '5fdf9c886176752d35e477e4', '5fdf9c886176752d35e477ea', '5fdf9c886176752d35e477f0', '5fdf9c6b6176752d35e46d1c', '5fdf9cfe6176752d35e4aa7f', '5fdf9cfe6176752d35e4aa85', '5fdf9cfe6176752d35e4aa8b', '5fdf9cf56176752d35e4a70f', '5fdf9d896176752d35e4e0b6', '5fdf9d896176752d35e4e0bc', '5fdf9d896176752d35e4e0c2', '6385018c76752d313964b35d', '6385018c76752d313964b35f', '6501db4c76752d3901eb3813', '6501db4c76752d3901eb3864', '6501db4c76752d3901eb381b', '6501db4d76752d3901eb3976', '6501db4e76752d3901eb3b32', '6501db4e76752d3901eb3b59')" --expand "ExtEthIfs,HostEthIfs,HostFcIfs" -o json --top 100
2023-12-03 15:24:13.288724	True	1505	2	isctl get adapter unit --filter "Moid in ('6501db4d76752d3901eb3972', '6501db4f76752d3901eb3c71')" --expand "ExtEthIfs,HostEthIfs,HostFcIfs" -o json --top 100
2023-12-03 15:24:15.562329	True	2059	16	isctl get storage controller --filter "Parent/Moid in ('5fdf9c056176752d35e44930', '5fdf9c7c6176752d35e472bd', '5fdf9d066176752d35e4aebe', '6385021176752d313964cbe0', '6501db4c76752d3901eb3890', '6501db4c76752d3901eb381d', '6501db4c76752d3901eb3882', '6501db4c76752d3901eb38a9')" --expand "PhysicalDisks,VirtualDrives" -o json --top 100
2023-12-03 15:24:17.182531	True	1457	8	isctl get storage physicaldiskusage --filter "StorageVirtualDrive/Moid in ('638f666f76752d3139f6cc14', '638fcd2976752d313909b32e', '617917b976752d3139754146', '65438f6a76752d3901322928', '6501db5276752d3901eb4051', '6501db5076752d3901eb3e4a', '6501db4f76752d3901eb3cee', '6501db5176752d3901eb3f14')"  -o json --top 100
2023-12-03 15:24:18.864401	True	1546	4	isctl get equipment tpm --filter "Moid in ('5fdf9c186176752d35e4503a', '5fdf9c8f6176752d35e47b82', '5fdf9d196176752d35e4b797', '638501fa76752d313964c6f7')"  -o json --top 100
```

[[Back]](./ServerInventory.md)