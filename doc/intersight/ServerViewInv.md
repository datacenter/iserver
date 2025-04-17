# Intersight Server

## inv view

```
# iserver get server --group test -v inv

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect chassis api objects...
Collect server api objects...


Server Inventory (R): Server874
-------------------------------

+--------------------+---------------------------------+--------------------+----------------------+--------+-------------------+
| Type               | Name                            | Model              | Vendor               | Serial | Pid               |
+--------------------+---------------------------------+--------------------+----------------------+--------+-------------------+
| Server             | Rack Server                     | --- Anonymized --- | Cisco Systems Inc    | SN-54  | UCSC-C240-M5SN    |
| Board              | Mother Board                    | --- Anonymized --- | Cisco Systems Inc    | SN-44  | UCSC-C240-M5SN    |
| CPU                | CPU #1                          | --- Anonymized --- | Intel(R) Corporation | SN-22  | UCS-CPU-I6248     |
| CPU                | CPU #2                          | --- Anonymized --- | Intel(R) Corporation | SN-13  | UCS-CPU-I6248     |
| Memory             | Memory #1                       | --- Anonymized --- | 0x2C00               | SN-20  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #3                       | --- Anonymized --- | 0x2C00               | SN-51  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #5                       | --- Anonymized --- | 0x2C00               | SN-92  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #7                       | --- Anonymized --- | 0x2C00               | SN-72  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #9                       | --- Anonymized --- | 0x2C00               | SN-75  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #11                      | --- Anonymized --- | 0x2C00               | SN-66  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #13                      | --- Anonymized --- | 0x2C00               | SN-46  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #15                      | --- Anonymized --- | 0x2C00               | SN-57  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #17                      | --- Anonymized --- | 0x2C00               | SN-67  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #19                      | --- Anonymized --- | 0x2C00               | SN-40  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #21                      | --- Anonymized --- | 0x2C00               | SN-33  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #23                      | --- Anonymized --- | 0x2C00               | SN-87  | UCS-MR-X32G2RT-H  |
| Storage Controller | Storage Controller #MRAID       | --- Anonymized --- | LSI Logic            | SN-43  | UCSC-RAID-M5      |
| Storage Controller | Storage Controller #PCIe-Switch | --- Anonymized --- | Cisco Systems Inc    | SN-29  |                   |
| Disk               | Disk #10                        | --- Anonymized --- | ATA                  | SN-72  | UCS-SD960G6I1X-EV |
| Disk               | Disk #11                        | --- Anonymized --- | ATA                  | SN-78  | UCS-SD960G6I1X-EV |
| Disk               | Disk #12                        | --- Anonymized --- | ATA                  | SN-93  | UCS-SD960G6I1X-EV |
| Disk               | Disk #13                        | --- Anonymized --- | SEAGATE              | SN-87  | UCS-HD12TB10K12N  |
| Disk               | Disk #14                        | --- Anonymized --- | SEAGATE              | SN-43  | UCS-HD12TB10K12N  |
| Disk               | Disk #15                        | --- Anonymized --- | SEAGATE              | SN-25  | UCS-HD12TB10K12N  |
| Disk               | Disk #16                        | --- Anonymized --- | SEAGATE              | SN-15  | UCS-HD12TB10K12N  |
| Disk               | Disk #17                        | --- Anonymized --- | SEAGATE              | SN-49  | UCS-HD12TB10K12N  |
| Disk               | Disk #18                        | --- Anonymized --- | TOSHIBA              | SN-82  | UCS-HD12TB10K12N  |
| Disk               | Disk #9                         | --- Anonymized --- | ATA                  | SN-44  | UCS-SD960G6I1X-EV |
| PCI Adapter        | PCI Slot 3                      | --- Anonymized --- | 0x8086               | SN-45  | UCSC-PCIE-ID25GF  |
| PCI Adapter        | PCI Slot 6                      | --- Anonymized --- | 0x8086               | SN-77  | UCSC-PCIE-ID25GF  |
| PCI Adapter        | PCI Slot L                      | --- Anonymized --- | 0x8086               | SN-38  |                   |
| PCI Adapter        | PCI Slot MLOM                   | --- Anonymized --- | 0x1137               | SN-79  | UCSC-MLOM-C25Q-04 |
| PCI Adapter        | PCI Slot MRAID                  | --- Anonymized --- | 0x1000               | SN-20  | UCSC-RAID-M5      |
| Fan                | Fan Module 1 - Fan 1            | --- Anonymized --- |                      | SN-95  |                   |
| Fan                | Fan Module 1 - Fan 2            | --- Anonymized --- |                      | SN-74  |                   |
| Fan                | Fan Module 2 - Fan 1            | --- Anonymized --- |                      | SN-97  |                   |
| Fan                | Fan Module 2 - Fan 2            | --- Anonymized --- |                      | SN-93  |                   |
| Fan                | Fan Module 3 - Fan 1            | --- Anonymized --- |                      | SN-47  |                   |
| Fan                | Fan Module 3 - Fan 2            | --- Anonymized --- |                      | SN-82  |                   |
| Fan                | Fan Module 4 - Fan 1            | --- Anonymized --- |                      | SN-18  |                   |
| Fan                | Fan Module 4 - Fan 2            | --- Anonymized --- |                      | SN-69  |                   |
| Fan                | Fan Module 5 - Fan 1            | --- Anonymized --- |                      | SN-21  |                   |
| Fan                | Fan Module 5 - Fan 2            | --- Anonymized --- |                      | SN-61  |                   |
| Fan                | Fan Module 6 - Fan 1            | --- Anonymized --- |                      | SN-39  |                   |
| Fan                | Fan Module 6 - Fan 2            | --- Anonymized --- |                      | SN-15  |                   |
| PSU                | PSU #1                          | --- Anonymized --- | Cisco Systems Inc    | SN-17  | PS-2112-9S-LF     |
| PSU                | PSU #2                          | --- Anonymized --- | Cisco Systems Inc    | SN-55  | PS-2112-9S-LF     |
+--------------------+---------------------------------+--------------------+----------------------+--------+-------------------+

Server Inventory (R): Server182
-------------------------------

+--------------------+---------------------------------+--------------------+----------------------+--------+-------------------+
| Type               | Name                            | Model              | Vendor               | Serial | Pid               |
+--------------------+---------------------------------+--------------------+----------------------+--------+-------------------+
| Server             | Rack Server                     | --- Anonymized --- | Cisco Systems Inc    | SN-47  | UCSC-C240-M5SN    |
| Board              | Mother Board                    | --- Anonymized --- | Cisco Systems Inc    | SN-37  | UCSC-C240-M5SN    |
| CPU                | CPU #1                          | --- Anonymized --- | Intel(R) Corporation | SN-47  | UCS-CPU-I6248     |
| CPU                | CPU #2                          | --- Anonymized --- | Intel(R) Corporation | SN-20  | UCS-CPU-I6248     |
| Memory             | Memory #1                       | --- Anonymized --- | 0x2C00               | SN-17  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #3                       | --- Anonymized --- | 0x2C00               | SN-84  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #5                       | --- Anonymized --- | 0x2C00               | SN-44  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #7                       | --- Anonymized --- | 0x2C00               | SN-95  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #9                       | --- Anonymized --- | 0x2C00               | SN-69  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #11                      | --- Anonymized --- | 0x2C00               | SN-25  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #13                      | --- Anonymized --- | 0x2C00               | SN-53  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #15                      | --- Anonymized --- | 0x2C00               | SN-30  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #17                      | --- Anonymized --- | 0x2C00               | SN-14  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #19                      | --- Anonymized --- | 0x2C00               | SN-57  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #21                      | --- Anonymized --- | 0x2C00               | SN-28  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #23                      | --- Anonymized --- | 0x2C00               | SN-53  | UCS-MR-X32G2RT-H  |
| Storage Controller | Storage Controller #MRAID       | --- Anonymized --- | LSI Logic            | SN-60  | UCSC-RAID-M5      |
| Storage Controller | Storage Controller #PCIe-Switch | --- Anonymized --- | Cisco Systems Inc    | SN-69  |                   |
| Disk               | Disk #10                        | --- Anonymized --- | ATA                  | SN-97  | UCS-SD960G6I1X-EV |
| Disk               | Disk #11                        | --- Anonymized --- | ATA                  | SN-21  | UCS-SD960G6I1X-EV |
| Disk               | Disk #12                        | --- Anonymized --- | ATA                  | SN-71  | UCS-SD960G6I1X-EV |
| Disk               | Disk #13                        | --- Anonymized --- | SEAGATE              | SN-80  | UCS-HD12TB10K12N  |
| Disk               | Disk #14                        | --- Anonymized --- | SEAGATE              | SN-34  | UCS-HD12TB10K12N  |
| Disk               | Disk #15                        | --- Anonymized --- | SEAGATE              | SN-22  | UCS-HD12TB10K12N  |
| Disk               | Disk #16                        | --- Anonymized --- | SEAGATE              | SN-85  | UCS-HD12TB10K12N  |
| Disk               | Disk #17                        | --- Anonymized --- | SEAGATE              | SN-67  | UCS-HD12TB10K12N  |
| Disk               | Disk #18                        | --- Anonymized --- | SEAGATE              | SN-45  | UCS-HD12TB10K12N  |
| Disk               | Disk #9                         | --- Anonymized --- | ATA                  | SN-52  | UCS-SD960G6I1X-EV |
| PCI Adapter        | PCI Slot 3                      | --- Anonymized --- | 0x8086               | SN-31  | UCSC-PCIE-ID25GF  |
| PCI Adapter        | PCI Slot 6                      | --- Anonymized --- | 0x8086               | SN-95  | UCSC-PCIE-ID25GF  |
| PCI Adapter        | PCI Slot L                      | --- Anonymized --- | 0x8086               | SN-20  |                   |
| PCI Adapter        | PCI Slot MLOM                   | --- Anonymized --- | 0x1137               | SN-52  | UCSC-MLOM-C25Q-04 |
| PCI Adapter        | PCI Slot MRAID                  | --- Anonymized --- | 0x1000               | SN-31  | UCSC-RAID-M5      |
| Fan                | Fan Module 1 - Fan 1            | --- Anonymized --- |                      | SN-69  |                   |
| Fan                | Fan Module 1 - Fan 2            | --- Anonymized --- |                      | SN-65  |                   |
| Fan                | Fan Module 2 - Fan 1            | --- Anonymized --- |                      | SN-93  |                   |
| Fan                | Fan Module 2 - Fan 2            | --- Anonymized --- |                      | SN-26  |                   |
| Fan                | Fan Module 3 - Fan 1            | --- Anonymized --- |                      | SN-57  |                   |
| Fan                | Fan Module 3 - Fan 2            | --- Anonymized --- |                      | SN-47  |                   |
| Fan                | Fan Module 4 - Fan 1            | --- Anonymized --- |                      | SN-63  |                   |
| Fan                | Fan Module 4 - Fan 2            | --- Anonymized --- |                      | SN-88  |                   |
| Fan                | Fan Module 5 - Fan 1            | --- Anonymized --- |                      | SN-11  |                   |
| Fan                | Fan Module 5 - Fan 2            | --- Anonymized --- |                      | SN-95  |                   |
| Fan                | Fan Module 6 - Fan 1            | --- Anonymized --- |                      | SN-38  |                   |
| Fan                | Fan Module 6 - Fan 2            | --- Anonymized --- |                      | SN-93  |                   |
| PSU                | PSU #1                          | --- Anonymized --- | Cisco Systems Inc    | SN-26  | PS-2112-9S-LF     |
| PSU                | PSU #2                          | --- Anonymized --- | Cisco Systems Inc    | SN-12  | PS-2112-9S-LF     |
+--------------------+---------------------------------+--------------------+----------------------+--------+-------------------+

Server Inventory (R): Server552
-------------------------------

+--------------------+---------------------------------+--------------------+----------------------+--------+-------------------+
| Type               | Name                            | Model              | Vendor               | Serial | Pid               |
+--------------------+---------------------------------+--------------------+----------------------+--------+-------------------+
| Server             | Rack Server                     | --- Anonymized --- | Cisco Systems Inc    | SN-47  | UCSC-C240-M5SN    |
| Board              | Mother Board                    | --- Anonymized --- | Cisco Systems Inc    | SN-63  | UCSC-C240-M5SN    |
| CPU                | CPU #1                          | --- Anonymized --- | Intel(R) Corporation | SN-43  | UCS-CPU-I6248     |
| CPU                | CPU #2                          | --- Anonymized --- | Intel(R) Corporation | SN-29  | UCS-CPU-I6248     |
| Memory             | Memory #1                       | --- Anonymized --- | 0x2C00               | SN-30  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #3                       | --- Anonymized --- | 0x2C00               | SN-73  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #5                       | --- Anonymized --- | 0x2C00               | SN-69  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #7                       | --- Anonymized --- | 0x2C00               | SN-83  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #9                       | --- Anonymized --- | 0x2C00               | SN-76  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #11                      | --- Anonymized --- | 0x2C00               | SN-46  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #13                      | --- Anonymized --- | 0x2C00               | SN-95  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #15                      | --- Anonymized --- | 0x2C00               | SN-35  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #17                      | --- Anonymized --- | 0x2C00               | SN-21  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #19                      | --- Anonymized --- | 0x2C00               | SN-22  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #21                      | --- Anonymized --- | 0x2C00               | SN-51  | UCS-MR-X32G2RT-H  |
| Memory             | Memory #23                      | --- Anonymized --- | 0x2C00               | SN-67  | UCS-MR-X32G2RT-H  |
| Storage Controller | Storage Controller #MRAID       | --- Anonymized --- | LSI Logic            | SN-67  | UCSC-RAID-M5      |
| Storage Controller | Storage Controller #PCIe-Switch | --- Anonymized --- | Cisco Systems Inc    | SN-16  |                   |
| Disk               | Disk #10                        | --- Anonymized --- | ATA                  | SN-77  | UCS-SD960G6I1X-EV |
| Disk               | Disk #11                        | --- Anonymized --- | ATA                  | SN-89  | UCS-SD960G6I1X-EV |
| Disk               | Disk #12                        | --- Anonymized --- | ATA                  | SN-51  | UCS-SD960G6I1X-EV |
| Disk               | Disk #13                        | --- Anonymized --- | SEAGATE              | SN-53  | UCS-HD12TB10K12N  |
| Disk               | Disk #14                        | --- Anonymized --- | SEAGATE              | SN-77  | UCS-HD12TB10K12N  |
| Disk               | Disk #15                        | --- Anonymized --- | SEAGATE              | SN-63  | UCS-HD12TB10K12N  |
| Disk               | Disk #16                        | --- Anonymized --- | SEAGATE              | SN-41  | UCS-HD12TB10K12N  |
| Disk               | Disk #17                        | --- Anonymized --- | SEAGATE              | SN-33  | UCS-HD12TB10K12N  |
| Disk               | Disk #18                        | --- Anonymized --- | TOSHIBA              | SN-64  | UCS-HD12TB10K12N  |
| Disk               | Disk #9                         | --- Anonymized --- | ATA                  | SN-89  | UCS-SD960G6I1X-EV |
| PCI Adapter        | PCI Slot 3                      | --- Anonymized --- | 0x8086               | SN-54  | UCSC-PCIE-ID25GF  |
| PCI Adapter        | PCI Slot 6                      | --- Anonymized --- | 0x8086               | SN-35  | UCSC-PCIE-ID25GF  |
| PCI Adapter        | PCI Slot L                      | --- Anonymized --- | 0x8086               | SN-38  | NA                |
| PCI Adapter        | PCI Slot MLOM                   | --- Anonymized --- | 0x1137               | SN-28  | UCSC-MLOM-C25Q-04 |
| PCI Adapter        | PCI Slot MRAID                  | --- Anonymized --- | 0x1000               | SN-69  | UCSC-RAID-M5      |
| Fan                | Fan Module 1 - Fan 1            | --- Anonymized --- |                      | SN-57  |                   |
| Fan                | Fan Module 1 - Fan 2            | --- Anonymized --- |                      | SN-44  |                   |
| Fan                | Fan Module 2 - Fan 1            | --- Anonymized --- |                      | SN-21  |                   |
| Fan                | Fan Module 2 - Fan 2            | --- Anonymized --- |                      | SN-60  |                   |
| Fan                | Fan Module 3 - Fan 1            | --- Anonymized --- |                      | SN-12  |                   |
| Fan                | Fan Module 3 - Fan 2            | --- Anonymized --- |                      | SN-89  |                   |
| Fan                | Fan Module 4 - Fan 1            | --- Anonymized --- |                      | SN-66  |                   |
| Fan                | Fan Module 4 - Fan 2            | --- Anonymized --- |                      | SN-75  |                   |
| Fan                | Fan Module 5 - Fan 1            | --- Anonymized --- |                      | SN-37  |                   |
| Fan                | Fan Module 5 - Fan 2            | --- Anonymized --- |                      | SN-29  |                   |
| Fan                | Fan Module 6 - Fan 1            | --- Anonymized --- |                      | SN-78  |                   |
| Fan                | Fan Module 6 - Fan 2            | --- Anonymized --- |                      | SN-24  |                   |
| PSU                | PSU #1                          | --- Anonymized --- | Cisco Systems Inc    | SN-59  | PS-2112-9S-LF     |
| PSU                | PSU #2                          | --- Anonymized --- | Cisco Systems Inc    | SN-17  | PS-2112-9S-LF     |
+--------------------+---------------------------------+--------------------+----------------------+--------+-------------------+

Server Inventory (R): Server288
-------------------------------

+--------------------+--------------------------------+--------------------+-------------------+--------+-------------------+
| Type               | Name                           | Model              | Vendor            | Serial | Pid               |
+--------------------+--------------------------------+--------------------+-------------------+--------+-------------------+
| Server             | Rack Server                    | --- Anonymized --- | Cisco Systems Inc | SN-33  | UCSC-C225-M6S     |
| Board              | Mother Board                   | --- Anonymized --- | Cisco Systems Inc | SN-38  | UCSC-C225-M6S     |
| CPU                | CPU #1                         | --- Anonymized --- | AMD               | SN-14  | UCS-CPU-A7763     |
| GPU                | GPU #3                         | --- Anonymized --- | 0x10de            | SN-71  | UCSC-GPU-T4-16    |
| Memory             | Memory #2                      | --- Anonymized --- | 0xCE00            | SN-98  | UCS-MR-X64G2RW    |
| Memory             | Memory #4                      | --- Anonymized --- | 0xCE00            | SN-21  | UCS-MR-X64G2RW    |
| Memory             | Memory #6                      | --- Anonymized --- | 0xCE00            | SN-92  | UCS-MR-X64G2RW    |
| Memory             | Memory #8                      | --- Anonymized --- | 0xCE00            | SN-22  | UCS-MR-X64G2RW    |
| Memory             | Memory #10                     | --- Anonymized --- | 0xCE00            | SN-77  | UCS-MR-X64G2RW    |
| Memory             | Memory #12                     | --- Anonymized --- | 0xCE00            | SN-98  | UCS-MR-X64G2RW    |
| Memory             | Memory #14                     | --- Anonymized --- | 0xCE00            | SN-96  | UCS-MR-X64G2RW    |
| Memory             | Memory #16                     | --- Anonymized --- | 0xCE00            | SN-22  | UCS-MR-X64G2RW    |
| Storage Controller | Storage Controller #MRAID      | --- Anonymized --- | LSI Logic         | SN-97  | UCSC-RAID-M6T     |
| Storage Controller | Storage Controller #MSTOR-RAID | --- Anonymized --- | Marvell           | SN-86  | UCS-M2-HWRAID     |
| Disk               | Disk #1                        | --- Anonymized --- | ATA               | SN-39  | UCS-SD19T61X-EV   |
| Disk               | Disk #2                        | --- Anonymized --- | ATA               | SN-44  | UCS-SD19T61X-EV   |
| Disk               | Disk #253                      | --- Anonymized --- | ATA               | SN-20  | UCS-M2-240GB      |
| Disk               | Disk #254                      | --- Anonymized --- | ATA               | SN-40  | UCS-M2-240GB      |
| Disk               | Disk #3                        | --- Anonymized --- | ATA               | SN-81  | UCS-SD19T61X-EV   |
| Disk               | Disk #4                        | --- Anonymized --- | ATA               | SN-98  | UCS-SD19T61X-EV   |
| PCI Adapter        | PCI Slot 1                     | --- Anonymized --- | 0x1137            | SN-83  | UCSC-PCIE-C25Q-04 |
| PCI Adapter        | PCI Slot 3                     | --- Anonymized --- | 0x10de            | SN-73  | UCSC-GPU-T4-16    |
| PCI Adapter        | PCI Slot MLOM                  | --- Anonymized --- | 0x1137            | SN-50  | UCSC-M-V100-04    |
| PCI Adapter        | PCI Slot MRAID                 | --- Anonymized --- | 0x1000            | SN-75  | UCSC-RAID-M6T     |
| PCI Adapter        | PCI Slot MSTOR-RAID            | --- Anonymized --- | 0x1b4b            | SN-50  | UCS-M2-HWRAID     |
| Fan                | Fan Module 1 - Fan 1           | --- Anonymized --- |                   | SN-12  |                   |
| Fan                | Fan Module 1 - Fan 2           | --- Anonymized --- |                   | SN-97  |                   |
| Fan                | Fan Module 2 - Fan 1           | --- Anonymized --- |                   | SN-58  |                   |
| Fan                | Fan Module 2 - Fan 2           | --- Anonymized --- |                   | SN-28  |                   |
| Fan                | Fan Module 3 - Fan 1           | --- Anonymized --- |                   | SN-64  |                   |
| Fan                | Fan Module 3 - Fan 2           | --- Anonymized --- |                   | SN-50  |                   |
| Fan                | Fan Module 4 - Fan 1           | --- Anonymized --- |                   | SN-31  |                   |
| Fan                | Fan Module 4 - Fan 2           | --- Anonymized --- |                   | SN-65  |                   |
| Fan                | Fan Module 5 - Fan 1           | --- Anonymized --- |                   | SN-53  |                   |
| Fan                | Fan Module 5 - Fan 2           | --- Anonymized --- |                   | SN-19  |                   |
| Fan                | Fan Module 6 - Fan 1           | --- Anonymized --- |                   | SN-55  |                   |
| Fan                | Fan Module 6 - Fan 2           | --- Anonymized --- |                   | SN-68  |                   |
| Fan                | Fan Module 7 - Fan 1           | --- Anonymized --- |                   | SN-53  |                   |
| Fan                | Fan Module 7 - Fan 2           | --- Anonymized --- |                   | SN-51  |                   |
| Fan                | Fan Module 8 - Fan 1           | --- Anonymized --- |                   | SN-80  |                   |
| Fan                | Fan Module 8 - Fan 2           | --- Anonymized --- |                   | SN-19  |                   |
| PSU                | PSU #1                         | --- Anonymized --- | Cisco Systems Inc | SN-15  | PS-2112-9S-LF     |
| PSU                | PSU #2                         | --- Anonymized --- | Cisco Systems Inc | SN-10  | PS-2112-9S-LF     |
+--------------------+--------------------------------+--------------------+-------------------+--------+-------------------+

[[Back]](./ServerInventory.md)