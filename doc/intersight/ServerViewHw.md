# Intersight Server

## hw view

```
# iserver get server --group test -v hw

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Server Summary [#8]
-------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU         | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+
| P+ H    | CRi | Server874 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-94  | 10.137.247.133 | 2S 40C 80T  | 384 [GiB] |
| P+ H    | CRi | Server449 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-10  | 10.8.228.146   | 2S 40C 80T  | 384 [GiB] |
| P+ H    | CRi | Server731 | Moid-value | --  | (R) UCSC-C240-M5SN | SN-12  | 10.203.27.148  | 2S 40C 80T  | 384 [GiB] |
| P+ C(1) | CRi | Server583 | Moid-value | --  | (R) UCSC-C225-M6S  | SN-61  | 10.177.17.43   | 1S 64C 128T | 512 [GiB] |
| P+ H    | Cu  | Server378 | Moid-value | --  | (B) UCSB-B200-M5   | SN-27  | 10.61.5.213    | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu  | Server300 | Moid-value | --  | (B) UCSB-B200-M5   | SN-62  | 10.91.196.215  | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu  | Server941 | Moid-value | --  | (B) UCSB-B200-M5   | SN-68  | 10.69.152.250  | 2S 40C 80T  | 512 [GiB] |
| P+ H    | Cu  | Server851 | Moid-value | --  | (B) UCSB-B200-M5   | SN-48  | 10.250.181.57  | 2S 40C 80T  | 512 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+-------------+-----------+

Motherboard Hardware Summary [#8]
---------------------------------

+-----------+----------+-------------------+-----+--------+------------+------------------+----------+--------------+----------------+---------------+-----+-----+
| Server    | Board Id | Vendor            | CPU | MemArr | PCI Switch | PCI Cooprocessor | Graphics | Storage Ctrl | FlexFlash Ctrl | FlexUtil Ctrl | Sec | TPM |
+-----------+----------+-------------------+-----+--------+------------+------------------+----------+--------------+----------------+---------------+-----+-----+
| Server874 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 1             | 0   | 1   |
| Server449 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 1             | 0   | 1   |
| Server731 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 1             | 0   | 1   |
| Server583 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 1        | 2            | 0              | 0             | 0   | 1   |
| Server378 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   |
| Server300 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   |
| Server941 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   |
| Server851 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   |
+-----------+----------+-------------------+-----+--------+------------+------------------+----------+--------------+----------------+---------------+-----+-----+

CPU [#15]
---------

+-----------+-------+--------+--------+----------------------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+---------+
| Server    | State | CPU Id | Socket | Vendor               | Arch | Model                                           | Cores | Enabled | Threads | Speed [GHz] | Stepping | Presence | OperState | Thermal |
+-----------+-------+--------+--------+----------------------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+---------+
| Server874 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  |         |
| Server874 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  |         |
| Server449 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  |         |
| Server449 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  |         |
| Server731 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  |         |
| Server731 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  |         |
| Server583 | V     | 1      | CPU1   | AMD                  | Zen  | AMD EPYC 7763 64-Core Processor                 | 64    | 64      | 128     | 2.45        | 1        | equipped | operable  |         |
| Server378 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server378 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server300 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server300 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server941 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server941 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server851 | V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
| Server851 | V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | ok      |
+-----------+-------+--------+--------+----------------------+------+-------------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+---------+

GPU [#1]
--------

+-----------+-------------------------+----------------+--------+--------+--------+----------+
| Server    | GPU Device Model        | Pid            | Serial | SlotId | Vendor | Firmware |
+-----------+-------------------------+----------------+--------+--------+--------+----------+
| Server583 | NVIDIA T4 PCIe 16GB 70W | UCSC-GPU-T4-16 | SN-67  | 3      | 0x10de | 1.0(1a)  |
+-----------+-------------------------+----------------+--------+--------+--------+----------+

Memory [#108]
-------------

+-----------+----------+----------+----+-------+------+------------+----------+-------+-------------+------+----------+--------+
| Server    | Oper     | Presence | Id | Array | Bank | Location   | Capacity | Clock | Form Factor | Type | Model    | Serial |
+-----------+----------+----------+----+-------+------+------------+----------+-------+-------------+------+----------+--------+
| Server874 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-25 | SN-35  |
| Server874 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-66 | SN-25  |
| Server874 | operable | equipped | 5  | 1     | 0    | DIMM_C1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-36 | SN-83  |
| Server874 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-36 | SN-55  |
| Server874 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-78 | SN-35  |
| Server874 | operable | equipped | 11 | 1     | 0    | DIMM_F1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-27 | SN-28  |
| Server874 | operable | equipped | 13 | 1     | 0    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-98 | SN-33  |
| Server874 | operable | equipped | 15 | 1     | 0    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-27 | SN-51  |
| Server874 | operable | equipped | 17 | 1     | 0    | DIMM_J1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-32 | SN-58  |
| Server874 | operable | equipped | 19 | 1     | 0    | DIMM_K1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-14 | SN-56  |
| Server874 | operable | equipped | 21 | 1     | 0    | DIMM_L1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-33 | SN-76  |
| Server874 | operable | equipped | 23 | 1     | 0    | DIMM_M1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-17 | SN-39  |
| Server449 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-74 | SN-89  |
| Server449 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-89 | SN-44  |
| Server449 | operable | equipped | 5  | 1     | 0    | DIMM_C1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-64 | SN-70  |
| Server449 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-21 | SN-77  |
| Server449 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-28 | SN-24  |
| Server449 | operable | equipped | 11 | 1     | 0    | DIMM_F1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-48 | SN-92  |
| Server449 | operable | equipped | 13 | 1     | 0    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-46 | SN-26  |
| Server449 | operable | equipped | 15 | 1     | 0    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-10 | SN-83  |
| Server449 | operable | equipped | 17 | 1     | 0    | DIMM_J1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-96 | SN-44  |
| Server449 | operable | equipped | 19 | 1     | 0    | DIMM_K1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-87 | SN-13  |
| Server449 | operable | equipped | 21 | 1     | 0    | DIMM_L1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-50 | SN-82  |
| Server449 | operable | equipped | 23 | 1     | 0    | DIMM_M1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-77 | SN-43  |
| Server731 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-96 | SN-80  |
| Server731 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-98 | SN-18  |
| Server731 | operable | equipped | 5  | 1     | 0    | DIMM_C1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-22 | SN-95  |
| Server731 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-46 | SN-99  |
| Server731 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-65 | SN-62  |
| Server731 | operable | equipped | 11 | 1     | 0    | DIMM_F1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-67 | SN-66  |
| Server731 | operable | equipped | 13 | 1     | 0    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-71 | SN-99  |
| Server731 | operable | equipped | 15 | 1     | 0    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-80 | SN-40  |
| Server731 | operable | equipped | 17 | 1     | 0    | DIMM_J1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-80 | SN-88  |
| Server731 | operable | equipped | 19 | 1     | 0    | DIMM_K1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-91 | SN-23  |
| Server731 | operable | equipped | 21 | 1     | 0    | DIMM_L1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-96 | SN-60  |
| Server731 | operable | equipped | 23 | 1     | 0    | DIMM_M1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-20 | SN-25  |
| Server583 | operable | equipped | 2  | 1     | 0    | DIMM_P1_A2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-66 | SN-30  |
| Server583 | operable | equipped | 4  | 1     | 0    | DIMM_P1_B2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-70 | SN-22  |
| Server583 | operable | equipped | 6  | 1     | 0    | DIMM_P1_C2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-27 | SN-21  |
| Server583 | operable | equipped | 8  | 1     | 0    | DIMM_P1_D2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-49 | SN-86  |
| Server583 | operable | equipped | 10 | 1     | 0    | DIMM_P1_E2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-63 | SN-46  |
| Server583 | operable | equipped | 12 | 1     | 0    | DIMM_P1_F2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-91 | SN-51  |
| Server583 | operable | equipped | 14 | 1     | 0    | DIMM_P1_G2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-17 | SN-85  |
| Server583 | operable | equipped | 16 | 1     | 0    | DIMM_P1_H2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-34 | SN-94  |
| Server378 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-96 | SN-58  |
| Server378 | operable | equipped | 2  | 1     | 0    | DIMM_A2    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-65 | SN-84  |
| Server378 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-23 | SN-12  |
| Server378 | operable | equipped | 4  | 1     | 0    | DIMM_B2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-40 | SN-21  |
| Server378 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-78 | SN-27  |
| Server378 | operable | equipped | 8  | 1     | 0    | DIMM_D2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-60 | SN-74  |
| Server378 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-83 | SN-72  |
| Server378 | operable | equipped | 10 | 1     | 0    | DIMM_E2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-44 | SN-36  |
| Server378 | operable | equipped | 13 | 1     | 1    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-16 | SN-58  |
| Server378 | operable | equipped | 14 | 1     | 1    | DIMM_G2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-46 | SN-71  |
| Server378 | operable | equipped | 15 | 1     | 1    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-50 | SN-76  |
| Server378 | operable | equipped | 16 | 1     | 1    | DIMM_H2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-53 | SN-51  |
| Server378 | operable | equipped | 19 | 1     | 1    | DIMM_K1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-99 | SN-27  |
| Server378 | operable | equipped | 20 | 1     | 1    | DIMM_K2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-18 | SN-49  |
| Server378 | operable | equipped | 21 | 1     | 1    | DIMM_L1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-55 | SN-39  |
| Server378 | operable | equipped | 22 | 1     | 1    | DIMM_L2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-78 | SN-31  |
| Server300 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-27 | SN-52  |
| Server300 | operable | equipped | 2  | 1     | 0    | DIMM_A2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-79 | SN-64  |
| Server300 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-48 | SN-75  |
| Server300 | operable | equipped | 4  | 1     | 0    | DIMM_B2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-55 | SN-18  |
| Server300 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-92 | SN-32  |
| Server300 | operable | equipped | 8  | 1     | 0    | DIMM_D2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-97 | SN-12  |
| Server300 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-82 | SN-27  |
| Server300 | operable | equipped | 10 | 1     | 0    | DIMM_E2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-26 | SN-78  |
| Server300 | operable | equipped | 13 | 1     | 1    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-16 | SN-19  |
| Server300 | operable | equipped | 14 | 1     | 1    | DIMM_G2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-92 | SN-41  |
| Server300 | operable | equipped | 15 | 1     | 1    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-88 | SN-62  |
| Server300 | operable | equipped | 16 | 1     | 1    | DIMM_H2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-19 | SN-18  |
| Server300 | operable | equipped | 19 | 1     | 1    | DIMM_K1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-93 | SN-69  |
| Server300 | operable | equipped | 20 | 1     | 1    | DIMM_K2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-63 | SN-22  |
| Server300 | operable | equipped | 21 | 1     | 1    | DIMM_L1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-42 | SN-67  |
| Server300 | operable | equipped | 22 | 1     | 1    | DIMM_L2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-79 | SN-43  |
| Server941 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-92 | SN-73  |
| Server941 | operable | equipped | 2  | 1     | 0    | DIMM_A2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-90 | SN-66  |
| Server941 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-86 | SN-13  |
| Server941 | operable | equipped | 4  | 1     | 0    | DIMM_B2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-23 | SN-57  |
| Server941 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-86 | SN-53  |
| Server941 | operable | equipped | 8  | 1     | 0    | DIMM_D2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-48 | SN-14  |
| Server941 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-83 | SN-19  |
| Server941 | operable | equipped | 10 | 1     | 0    | DIMM_E2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-39 | SN-21  |
| Server941 | operable | equipped | 13 | 1     | 1    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-92 | SN-79  |
| Server941 | operable | equipped | 14 | 1     | 1    | DIMM_G2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-83 | SN-87  |
| Server941 | operable | equipped | 15 | 1     | 1    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-31 | SN-25  |
| Server941 | operable | equipped | 16 | 1     | 1    | DIMM_H2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-82 | SN-22  |
| Server941 | operable | equipped | 19 | 1     | 1    | DIMM_K1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-59 | SN-75  |
| Server941 | operable | equipped | 20 | 1     | 1    | DIMM_K2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-24 | SN-68  |
| Server941 | operable | equipped | 21 | 1     | 1    | DIMM_L1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-69 | SN-49  |
| Server941 | operable | equipped | 22 | 1     | 1    | DIMM_L2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-51 | SN-93  |
| Server851 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-79 | SN-39  |
| Server851 | operable | equipped | 2  | 1     | 0    | DIMM_A2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-98 | SN-15  |
| Server851 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-48 | SN-28  |
| Server851 | operable | equipped | 4  | 1     | 0    | DIMM_B2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-23 | SN-43  |
| Server851 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-73 | SN-60  |
| Server851 | operable | equipped | 8  | 1     | 0    | DIMM_D2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-51 | SN-39  |
| Server851 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-51 | SN-58  |
| Server851 | operable | equipped | 10 | 1     | 0    | DIMM_E2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-55 | SN-53  |
| Server851 | operable | equipped | 13 | 1     | 1    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-63 | SN-57  |
| Server851 | operable | equipped | 14 | 1     | 1    | DIMM_G2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-28 | SN-72  |
| Server851 | operable | equipped | 15 | 1     | 1    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-14 | SN-70  |
| Server851 | operable | equipped | 16 | 1     | 1    | DIMM_H2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-71 | SN-72  |
| Server851 | operable | equipped | 19 | 1     | 1    | DIMM_K1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-42 | SN-39  |
| Server851 | operable | equipped | 20 | 1     | 1    | DIMM_K2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-30 | SN-44  |
| Server851 | operable | equipped | 21 | 1     | 1    | DIMM_L1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-35 | SN-80  |
| Server851 | operable | equipped | 22 | 1     | 1    | DIMM_L2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-64 | SN-20  |
+-----------+----------+----------+----+-------+------+------------+----------+-------+-------------+------+----------+--------+

Storage Controller [#16]
------------------------

+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server    | Controller  | Model                          | Vendor            | Serial | Presence | PCI Slot    | Raid Support | PD | VD |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server874 | MRAID       | Cisco 12G Modular Raid         | LSI Logic         | SN-12  | equipped | MRAID       | yes          | 10 | 1  |
|           |             | Controller with 2GB cache      |                   |        |          |             |              |    |    |
|           |             | (max 16 drives)                |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server874 | PCIe-Switch | --                             | Cisco Systems Inc | SN-59  | equipped | PCIe-Switch | N/A          | 0  | 0  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server449 | MRAID       | Cisco 12G Modular Raid         | LSI Logic         | SN-15  | equipped | MRAID       | yes          | 10 | 1  |
|           |             | Controller with 2GB cache      |                   |        |          |             |              |    |    |
|           |             | (max 16 drives)                |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server449 | PCIe-Switch | --                             | Cisco Systems Inc | SN-68  | equipped | PCIe-Switch | N/A          | 0  | 0  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server731 | MRAID       | Cisco 12G Modular Raid         | LSI Logic         | SN-23  | equipped | MRAID       | yes          | 10 | 1  |
|           |             | Controller with 2GB cache      |                   |        |          |             |              |    |    |
|           |             | (max 16 drives)                |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server731 | PCIe-Switch | --                             | Cisco Systems Inc | SN-15  | equipped | PCIe-Switch | N/A          | 0  | 0  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server583 | MSTOR-RAID  | Cisco Boot optimized M.2 Raid  | Marvell           | SN-25  | equipped | MSTOR-RAID  | yes          | 2  | 1  |
|           |             | controller                     |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server583 | MRAID       | Cisco 12G SAS RAID Controller  | LSI Logic         | SN-15  | equipped | MRAID       | yes          | 4  | 0  |
|           |             | with 4GB FBWC (16 Drives)      |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server378 | 1           | UCSB-MRAID12G-HE               | Cisco Systems Inc | SN-40  | equipped | FMEZZ1-SAS  | RAID0, RAID1 | 2  | 1  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server378 | 1           | Lewisburg SSATA Controller     | Intel Corp.       | SN-35  | equipped |             | RAID0, RAID1 | 0  | 0  |
|           |             | [AHCI mode]                    |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server300 | 1           | Lewisburg SSATA Controller     | Intel Corp.       | SN-35  | equipped |             | RAID0, RAID1 | 0  | 0  |
|           |             | [AHCI mode]                    |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server300 | 1           | UCSB-MRAID12G-HE               | Cisco Systems Inc | SN-82  | equipped | FMEZZ1-SAS  | RAID0, RAID1 | 2  | 1  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server941 | 1           | UCSB-MRAID12G-HE               | Cisco Systems Inc | SN-19  | equipped | FMEZZ1-SAS  | RAID0, RAID1 | 2  | 1  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server941 | 1           | Lewisburg SSATA Controller     | Intel Corp.       | SN-42  | equipped |             | RAID0, RAID1 | 0  | 0  |
|           |             | [AHCI mode]                    |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server851 | 1           | UCSB-MRAID12G-HE               | Cisco Systems Inc | SN-69  | equipped | FMEZZ1-SAS  | RAID0, RAID1 | 2  | 1  |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+
| Server851 | 1           | Lewisburg SSATA Controller     | Intel Corp.       | SN-48  | equipped |             | RAID0, RAID1 | 0  | 0  |
|           |             | [AHCI mode]                    |                   |        |          |             |              |    |    |
+-----------+-------------+--------------------------------+-------------------+--------+----------+-------------+--------------+----+----+

Physical Disk - State [#44]
---------------------------

+-----------+-------+------------+---------+----+-------------+------+----------+----------+------------+---------+--------+----------+
| Server    | State | Controller | Disk Id | VD | Size        | Type | Protocol | Bootable | Link Speed | Fw      | State  | Presence |
+-----------+-------+------------+---------+----+-------------+------+----------+----------+------------+---------+--------+----------+
| Server874 | V     | MRAID      | 9       | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server874 | V     | MRAID      | 10      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server874 | V     | MRAID      | 11      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server874 | V     | MRAID      | 12      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server874 | V     | MRAID      | 13      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server874 | V     | MRAID      | 14      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server874 | V     | MRAID      | 15      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server874 | V     | MRAID      | 16      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server874 | V     | MRAID      | 17      | 0  | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server874 | V     | MRAID      | 18      | 0  | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server449 | V     | MRAID      | 9       | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server449 | V     | MRAID      | 10      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server449 | V     | MRAID      | 11      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server449 | V     | MRAID      | 12      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server449 | V     | MRAID      | 13      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server449 | V     | MRAID      | 14      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server449 | V     | MRAID      | 15      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server449 | V     | MRAID      | 16      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server449 | V     | MRAID      | 17      | 0  | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server449 | V     | MRAID      | 18      | 0  | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server731 | V     | MRAID      | 9       | 0  | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server731 | V     | MRAID      | 10      | 0  | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server731 | V     | MRAID      | 11      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server731 | V     | MRAID      | 12      | -- | 959.0 [GB]  | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server731 | V     | MRAID      | 13      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server731 | V     | MRAID      | 14      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server731 | V     | MRAID      | 15      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server731 | V     | MRAID      | 16      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server731 | V     | MRAID      | 17      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server731 | V     | MRAID      | 18      | -- | 1.2 [TB]    | HDD  | SAS      | X        | 12.0 Gb/s  | 1.0(1a) | Good   | equipped |
| Server583 | V     | MRAID      | 1       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server583 | V     | MRAID      | 2       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server583 | V     | MRAID      | 3       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server583 | V     | MRAID      | 4       | -- | 1.92 [TB]   | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server583 | V     | MSTOR-RAID | 253     | 0  | 240.06 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server583 | V     | MSTOR-RAID | 254     | 0  | 240.06 [GB] | SSD  | SATA     | X        | 6.0 Gb/s   | 1.0(1a) | Good   | equipped |
| Server378 | V     | 1          | 1       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server378 | V     | 1          | 2       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server300 | V     | 1          | 1       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server300 | V     | 1          | 2       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server941 | V     | 1          | 1       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server941 | V     | 1          | 2       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server851 | V     | 1          | 1       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
| Server851 | V     | 1          | 2       | -- | 299.0 [GB]  | HDD  | SAS      | X        | 12-gbps    | 1.0(1a) | online | equipped |
+-----------+-------+------------+---------+----+-------------+------+----------+----------+------------+---------+--------+----------+

Physical Disk - Inventory [#44]
-------------------------------

+-----------+---------+--------+-----------+-------+---------+--------+
| Server    | Disk Id | Pid    | Model     | PN    | Vendor  | Serial |
+-----------+---------+--------+-----------+-------+---------+--------+
| Server874 | 9       | PID-55 | Model-XYZ | PN-48 | ATA     | SN-12  |
| Server874 | 10      | PID-13 | Model-XYZ | PN-97 | ATA     | SN-79  |
| Server874 | 11      | PID-34 | Model-XYZ | PN-99 | ATA     | SN-88  |
| Server874 | 12      | PID-24 | Model-XYZ | PN-95 | ATA     | SN-25  |
| Server874 | 13      | PID-73 | Model-XYZ | PN-30 | SEAGATE | SN-74  |
| Server874 | 14      | PID-93 | Model-XYZ | PN-30 | SEAGATE | SN-50  |
| Server874 | 15      | PID-23 | Model-XYZ | PN-26 | SEAGATE | SN-68  |
| Server874 | 16      | PID-18 | Model-XYZ | PN-13 | SEAGATE | SN-95  |
| Server874 | 17      | PID-36 | Model-XYZ | PN-76 | SEAGATE | SN-44  |
| Server874 | 18      | PID-23 | Model-XYZ | PN-46 | TOSHIBA | SN-30  |
| Server449 | 9       | PID-64 | Model-XYZ | PN-24 | ATA     | SN-80  |
| Server449 | 10      | PID-89 | Model-XYZ | PN-95 | ATA     | SN-57  |
| Server449 | 11      | PID-81 | Model-XYZ | PN-46 | ATA     | SN-57  |
| Server449 | 12      | PID-12 | Model-XYZ | PN-11 | ATA     | SN-91  |
| Server449 | 13      | PID-24 | Model-XYZ | PN-62 | SEAGATE | SN-12  |
| Server449 | 14      | PID-90 | Model-XYZ | PN-20 | SEAGATE | SN-48  |
| Server449 | 15      | PID-23 | Model-XYZ | PN-13 | SEAGATE | SN-97  |
| Server449 | 16      | PID-88 | Model-XYZ | PN-37 | SEAGATE | SN-88  |
| Server449 | 17      | PID-78 | Model-XYZ | PN-27 | SEAGATE | SN-84  |
| Server449 | 18      | PID-36 | Model-XYZ | PN-44 | SEAGATE | SN-86  |
| Server731 | 9       | PID-47 | Model-XYZ | PN-44 | ATA     | SN-53  |
| Server731 | 10      | PID-99 | Model-XYZ | PN-53 | ATA     | SN-78  |
| Server731 | 11      | PID-73 | Model-XYZ | PN-12 | ATA     | SN-35  |
| Server731 | 12      | PID-71 | Model-XYZ | PN-31 | ATA     | SN-20  |
| Server731 | 13      | PID-17 | Model-XYZ | PN-72 | SEAGATE | SN-14  |
| Server731 | 14      | PID-33 | Model-XYZ | PN-38 | SEAGATE | SN-93  |
| Server731 | 15      | PID-15 | Model-XYZ | PN-53 | SEAGATE | SN-64  |
| Server731 | 16      | PID-93 | Model-XYZ | PN-10 | SEAGATE | SN-44  |
| Server731 | 17      | PID-91 | Model-XYZ | PN-31 | SEAGATE | SN-17  |
| Server731 | 18      | PID-20 | Model-XYZ | PN-85 | TOSHIBA | SN-58  |
| Server583 | 1       | PID-20 | Model-XYZ | PN-41 | ATA     | SN-19  |
| Server583 | 2       | PID-72 | Model-XYZ | PN-96 | ATA     | SN-38  |
| Server583 | 3       | PID-23 | Model-XYZ | PN-78 | ATA     | SN-33  |
| Server583 | 4       | PID-73 | Model-XYZ | PN-44 | ATA     | SN-76  |
| Server583 | 253     | PID-54 | Model-XYZ | PN-36 | ATA     | SN-32  |
| Server583 | 254     | PID-59 | Model-XYZ | PN-49 | ATA     | SN-45  |
| Server378 | 1       | PID-19 | Model-XYZ | PN-47 | SEAGATE | SN-80  |
| Server378 | 2       | PID-26 | Model-XYZ | PN-89 | SEAGATE | SN-28  |
| Server300 | 1       | PID-85 | Model-XYZ | PN-58 | SEAGATE | SN-79  |
| Server300 | 2       | PID-31 | Model-XYZ | PN-92 | SEAGATE | SN-76  |
| Server941 | 1       | PID-66 | Model-XYZ | PN-50 | SEAGATE | SN-29  |
| Server941 | 2       | PID-92 | Model-XYZ | PN-61 | SEAGATE | SN-24  |
| Server851 | 1       | PID-18 | Model-XYZ | PN-25 | SEAGATE | SN-78  |
| Server851 | 2       | PID-66 | Model-XYZ | PN-42 | SEAGATE | SN-20  |
+-----------+---------+--------+-----------+-------+---------+--------+

Virtual Drive [#8]
------------------

+-----------+-------+------------+----------+-------------+-------+--------+-------------+----------+---------------+-------------+
| Server    | State | Controller | Drive Id | Size        | Disks | Type   | Name        | Bootable | Write Cache   | Drive State |
+-----------+-------+------------+----------+-------------+-------+--------+-------------+----------+---------------+-------------+
| Server874 | V     | MRAID      | 0        | 1.2 [TB]    | 2     | RAID 1 | vd-0        | V        | write-through | Optimal     |
| Server449 | V     | MRAID      | 0        | 1.2 [TB]    | 2     | RAID 1 | vd-0        | V        | write-through | Optimal     |
| Server731 | V     | MRAID      | 0        | 1.92 [TB]   | 2     | RAID 0 | RAID0_910   | V        | write-through | Optimal     |
| Server583 | V     | MSTOR-RAID | 0        | 239.99 [GB] | 2     | RAID 1 | MStorBootVd | V        | write-through | Optimal     |
| Server378 | V     | 1          | 0        | 299.0 [GB]  | 2     | mirror |             | V        | write-through | optimal     |
| Server300 | V     | 1          | 0        | 299.0 [GB]  | 2     | mirror |             | V        | write-through | optimal     |
| Server941 | V     | 1          | 0        | 299.0 [GB]  | 2     | mirror |             | V        | write-through | optimal     |
| Server851 | V     | 1          | 0        | 299.0 [GB]  | 2     | mirror |             | V        | write-through | optimal     |
+-----------+-------+------------+----------+-------------+-------+--------+-------------+----------+---------------+-------------+

MAC Addresses [#130]
--------------------

+-----------+----------------+-------------------+--------------------------------------------+---------------------------------------------+
| Server    | IP             | MAC               | Adapter                                    | Interface                                   |
+-----------+----------------+-------------------+--------------------------------------------+---------------------------------------------+
| Server874 | 10.137.247.133 | aa:bb:60:96:88:26 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/ext-eth-0      |
| Server874 | 10.137.247.133 | aa:bb:87:46:94:73 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/ext-eth-1      |
| Server874 | 10.137.247.133 | aa:bb:33:33:12:49 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/ext-eth-2      |
| Server874 | 10.137.247.133 | aa:bb:43:87:97:75 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/ext-eth-3      |
| Server874 | 10.137.247.133 | aa:bb:49:30:63:35 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/host-eth-eth0  |
| Server874 | 10.137.247.133 | aa:bb:87:92:35:51 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/host-eth-eth1  |
| Server874 | 10.137.247.133 | aa:bb:86:17:27:46 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/host-eth-eth2  |
| Server874 | 10.137.247.133 | aa:bb:31:35:97:19 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/host-eth-eth3  |
| Server874 | 10.137.247.133 | aa:bb:58:36:46:87 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | sys/rack-unit-1/network-adapter-6/eth-1     |
| Server874 | 10.137.247.133 | aa:bb:43:39:68:99 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | sys/rack-unit-1/network-adapter-6/eth-2     |
| Server874 | 10.137.247.133 | aa:bb:57:65:28:96 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | sys/rack-unit-1/network-adapter-3/eth-1     |
| Server874 | 10.137.247.133 | aa:bb:20:73:11:12 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | sys/rack-unit-1/network-adapter-3/eth-2     |
| Server874 | 10.137.247.133 | aa:bb:49:61:34:53 | Cisco(R) LOM X550-T2                       | sys/rack-unit-1/network-adapter-L/eth-1     |
| Server874 | 10.137.247.133 | aa:bb:34:47:75:23 | Cisco(R) LOM X550-T2                       | sys/rack-unit-1/network-adapter-L/eth-2     |
| Server874 | 10.137.247.133 | aa:bb:77:90:54:38 | Cisco IMC                                  | imc                                         |
| Server449 | 10.8.228.146   | aa:bb:12:15:28:74 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/ext-eth-0      |
| Server449 | 10.8.228.146   | aa:bb:31:56:37:99 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/ext-eth-1      |
| Server449 | 10.8.228.146   | aa:bb:31:41:92:63 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/ext-eth-2      |
| Server449 | 10.8.228.146   | aa:bb:86:68:70:37 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/ext-eth-3      |
| Server449 | 10.8.228.146   | aa:bb:62:83:60:87 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/host-eth-eth0  |
| Server449 | 10.8.228.146   | aa:bb:81:45:13:91 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/host-eth-eth1  |
| Server449 | 10.8.228.146   | aa:bb:11:52:12:17 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/host-eth-eth2  |
| Server449 | 10.8.228.146   | aa:bb:45:78:76:71 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/host-eth-eth3  |
| Server449 | 10.8.228.146   | aa:bb:61:64:28:20 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | sys/rack-unit-1/network-adapter-6/eth-1     |
| Server449 | 10.8.228.146   | aa:bb:79:34:54:81 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | sys/rack-unit-1/network-adapter-6/eth-2     |
| Server449 | 10.8.228.146   | aa:bb:88:56:86:62 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | sys/rack-unit-1/network-adapter-3/eth-1     |
| Server449 | 10.8.228.146   | aa:bb:88:79:73:71 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | sys/rack-unit-1/network-adapter-3/eth-2     |
| Server449 | 10.8.228.146   | aa:bb:44:65:63:48 | Cisco(R) LOM X550-T2                       | sys/rack-unit-1/network-adapter-L/eth-1     |
| Server449 | 10.8.228.146   | aa:bb:75:98:51:95 | Cisco(R) LOM X550-T2                       | sys/rack-unit-1/network-adapter-L/eth-2     |
| Server449 | 10.8.228.146   | aa:bb:58:92:94:27 | Cisco IMC                                  | imc                                         |
| Server731 | 10.203.27.148  | aa:bb:75:10:53:61 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/ext-eth-0      |
| Server731 | 10.203.27.148  | aa:bb:52:29:45:75 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/ext-eth-1      |
| Server731 | 10.203.27.148  | aa:bb:94:78:66:35 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/ext-eth-2      |
| Server731 | 10.203.27.148  | aa:bb:15:76:46:29 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/ext-eth-3      |
| Server731 | 10.203.27.148  | aa:bb:18:92:71:47 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/host-eth-eth0  |
| Server731 | 10.203.27.148  | aa:bb:57:59:65:25 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/host-eth-eth1  |
| Server731 | 10.203.27.148  | aa:bb:19:96:14:87 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/host-eth-eth2  |
| Server731 | 10.203.27.148  | aa:bb:98:24:77:26 | UCSC-MLOM-C25Q-04                          | sys/rack-unit-1/adaptor-MLOM/host-eth-eth3  |
| Server731 | 10.203.27.148  | aa:bb:10:90:93:76 | Cisco(R) LOM X550-T2                       | sys/rack-unit-1/network-adapter-L/eth-1     |
| Server731 | 10.203.27.148  | aa:bb:44:62:73:80 | Cisco(R) LOM X550-T2                       | sys/rack-unit-1/network-adapter-L/eth-2     |
| Server731 | 10.203.27.148  | aa:bb:23:18:12:54 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | sys/rack-unit-1/network-adapter-6/eth-1     |
| Server731 | 10.203.27.148  | aa:bb:46:50:91:31 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | sys/rack-unit-1/network-adapter-6/eth-2     |
| Server731 | 10.203.27.148  | aa:bb:61:62:13:17 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | sys/rack-unit-1/network-adapter-3/eth-2     |
| Server731 | 10.203.27.148  | aa:bb:87:95:33:91 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | sys/rack-unit-1/network-adapter-3/eth-1     |
| Server731 | 10.203.27.148  | aa:bb:32:64:73:81 | Cisco IMC                                  | imc                                         |
| Server583 | 10.177.17.43   | aa:bb:81:73:62:85 | UCSC-PCIE-C25Q-04                          | sys/rack-unit-1/adaptor-1/ext-eth-1         |
| Server583 | 10.177.17.43   | aa:bb:78:34:67:73 | UCSC-PCIE-C25Q-04                          | sys/rack-unit-1/adaptor-1/ext-eth-2         |
| Server583 | 10.177.17.43   | aa:bb:71:30:62:53 | UCSC-PCIE-C25Q-04                          | sys/rack-unit-1/adaptor-1/ext-eth-3         |
| Server583 | 10.177.17.43   | aa:bb:71:82:94:98 | UCSC-PCIE-C25Q-04                          | sys/rack-unit-1/adaptor-1/ext-eth-0         |
| Server583 | 10.177.17.43   | aa:bb:12:73:59:93 | UCSC-M-V100-04                             | sys/rack-unit-1/adaptor-MLOM/ext-eth-0      |
| Server583 | 10.177.17.43   | aa:bb:45:27:17:82 | UCSC-M-V100-04                             | sys/rack-unit-1/adaptor-MLOM/ext-eth-1      |
| Server583 | 10.177.17.43   | aa:bb:42:88:36:91 | UCSC-PCIE-C25Q-04                          | sys/rack-unit-1/adaptor-1/host-eth-eth0     |
| Server583 | 10.177.17.43   | aa:bb:89:90:11:95 | UCSC-PCIE-C25Q-04                          | sys/rack-unit-1/adaptor-1/host-eth-eth1     |
| Server583 | 10.177.17.43   | aa:bb:46:11:99:40 | UCSC-PCIE-C25Q-04                          | sys/rack-unit-1/adaptor-1/host-eth-eth2     |
| Server583 | 10.177.17.43   | aa:bb:50:54:15:63 | UCSC-PCIE-C25Q-04                          | sys/rack-unit-1/adaptor-1/host-eth-eth3     |
| Server583 | 10.177.17.43   | aa:bb:35:16:86:83 | UCSC-PCIE-C25Q-04                          | sys/rack-unit-1/adaptor-1/host-eth-vic1-vs0 |
| Server583 | 10.177.17.43   | aa:bb:64:37:20:26 | UCSC-PCIE-C25Q-04                          | sys/rack-unit-1/adaptor-1/host-eth-vic1-vs1 |
| Server583 | 10.177.17.43   | aa:bb:32:28:30:99 | UCSC-PCIE-C25Q-04                          | sys/rack-unit-1/adaptor-1/host-eth-vic1-i0  |
| Server583 | 10.177.17.43   | aa:bb:54:67:19:40 | UCSC-PCIE-C25Q-04                          | sys/rack-unit-1/adaptor-1/host-eth-vic1-i1  |
| Server583 | 10.177.17.43   | aa:bb:44:11:35:77 | UCSC-M-V100-04                             | sys/rack-unit-1/adaptor-MLOM/host-eth-eth0  |
| Server583 | 10.177.17.43   | aa:bb:23:68:16:50 | UCSC-M-V100-04                             | sys/rack-unit-1/adaptor-MLOM/host-eth-eth1  |
| Server583 | 10.177.17.43   | aa:bb:97:84:65:14 | UCSC-M-V100-04                             | sys/rack-unit-1/adaptor-MLOM/host-eth-vs0   |
| Server583 | 10.177.17.43   | aa:bb:76:47:84:77 | UCSC-M-V100-04                             | sys/rack-unit-1/adaptor-MLOM/host-eth-vs1   |
| Server583 | 10.177.17.43   | aa:bb:24:96:90:45 | UCSC-M-V100-04                             | sys/rack-unit-1/adaptor-MLOM/host-eth-i0    |
| Server583 | 10.177.17.43   | aa:bb:20:34:82:35 | UCSC-M-V100-04                             | sys/rack-unit-1/adaptor-MLOM/host-eth-i1    |
| Server583 | 10.177.17.43   | aa:bb:63:61:33:84 | Cisco IMC                                  | imc                                         |
| Server378 | 10.61.5.213    | aa:bb:95:55:83:64 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-1/adaptor-1/ext-eth-3   |
| Server378 | 10.61.5.213    | aa:bb:91:60:74:70 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-1/adaptor-1/ext-eth-1   |
| Server378 | 10.61.5.213    | aa:bb:16:24:24:75 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-1/adaptor-1/ext-eth-7   |
| Server378 | 10.61.5.213    | aa:bb:96:74:42:41 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-1/adaptor-1/ext-eth-5   |
| Server378 | 10.61.5.213    | aa:bb:10:11:97:60 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-1/adaptor-2/ext-eth-3   |
| Server378 | 10.61.5.213    | aa:bb:75:72:27:83 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-1/adaptor-2/ext-eth-7   |
| Server378 | 10.61.5.213    | aa:bb:30:10:56:20 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-1/adaptor-2/ext-eth-5   |
| Server378 | 10.61.5.213    | aa:bb:29:43:60:12 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-1/adaptor-2/ext-eth-1   |
| Server378 | 10.61.5.213    | aa:bb:15:34:61:42 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-1/adaptor-1/host-eth-1  |
| Server378 | 10.61.5.213    | aa:bb:25:50:84:94 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-1/adaptor-1/host-eth-4  |
| Server378 | 10.61.5.213    | aa:bb:87:84:60:70 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-1/adaptor-1/host-eth-2  |
| Server378 | 10.61.5.213    | aa:bb:78:25:50:22 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-1/adaptor-1/host-eth-3  |
| Server378 | 10.61.5.213    | aa:bb:14:45:64:93 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-1/adaptor-2/host-eth-4  |
| Server378 | 10.61.5.213    | aa:bb:13:12:17:86 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-1/adaptor-2/host-eth-3  |
| Server378 | 10.61.5.213    | aa:bb:14:84:58:53 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-1/adaptor-2/host-eth-2  |
| Server378 | 10.61.5.213    | aa:bb:97:56:14:95 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-1/adaptor-2/host-eth-1  |
| Server300 | 10.91.196.215  | aa:bb:96:18:76:75 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-2/adaptor-1/ext-eth-7   |
| Server300 | 10.91.196.215  | aa:bb:15:51:73:98 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-2/adaptor-1/ext-eth-3   |
| Server300 | 10.91.196.215  | aa:bb:89:30:27:28 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-2/adaptor-1/ext-eth-1   |
| Server300 | 10.91.196.215  | aa:bb:53:66:76:52 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-2/adaptor-1/ext-eth-5   |
| Server300 | 10.91.196.215  | aa:bb:40:73:27:31 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-2/adaptor-2/ext-eth-7   |
| Server300 | 10.91.196.215  | aa:bb:38:64:13:19 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-2/adaptor-2/ext-eth-3   |
| Server300 | 10.91.196.215  | aa:bb:23:12:94:19 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-2/adaptor-2/ext-eth-1   |
| Server300 | 10.91.196.215  | aa:bb:55:55:70:70 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-2/adaptor-2/ext-eth-5   |
| Server300 | 10.91.196.215  | aa:bb:27:85:37:72 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-2/adaptor-1/host-eth-1  |
| Server300 | 10.91.196.215  | aa:bb:85:96:50:93 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-2/adaptor-1/host-eth-3  |
| Server300 | 10.91.196.215  | aa:bb:32:31:31:57 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-2/adaptor-1/host-eth-4  |
| Server300 | 10.91.196.215  | aa:bb:32:31:82:29 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-2/adaptor-1/host-eth-2  |
| Server300 | 10.91.196.215  | aa:bb:18:59:62:72 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-2/adaptor-2/host-eth-3  |
| Server300 | 10.91.196.215  | aa:bb:91:59:89:10 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-2/adaptor-2/host-eth-2  |
| Server300 | 10.91.196.215  | aa:bb:99:55:47:19 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-2/adaptor-2/host-eth-4  |
| Server300 | 10.91.196.215  | aa:bb:22:48:57:38 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-2/adaptor-2/host-eth-1  |
| Server941 | 10.69.152.250  | aa:bb:46:14:69:37 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-3/adaptor-2/ext-eth-5   |
| Server941 | 10.69.152.250  | aa:bb:45:13:75:34 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-3/adaptor-2/ext-eth-7   |
| Server941 | 10.69.152.250  | aa:bb:12:49:71:32 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-3/adaptor-2/ext-eth-1   |
| Server941 | 10.69.152.250  | aa:bb:80:79:83:23 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-3/adaptor-2/ext-eth-3   |
| Server941 | 10.69.152.250  | aa:bb:14:56:18:80 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-3/adaptor-1/ext-eth-3   |
| Server941 | 10.69.152.250  | aa:bb:27:45:52:30 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-3/adaptor-1/ext-eth-5   |
| Server941 | 10.69.152.250  | aa:bb:59:47:11:18 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-3/adaptor-1/ext-eth-7   |
| Server941 | 10.69.152.250  | aa:bb:20:67:31:93 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-3/adaptor-1/ext-eth-1   |
| Server941 | 10.69.152.250  | aa:bb:65:26:35:37 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-3/adaptor-2/host-eth-3  |
| Server941 | 10.69.152.250  | aa:bb:76:63:99:80 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-3/adaptor-2/host-eth-2  |
| Server941 | 10.69.152.250  | aa:bb:40:41:11:68 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-3/adaptor-2/host-eth-1  |
| Server941 | 10.69.152.250  | aa:bb:29:80:94:75 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-3/adaptor-2/host-eth-4  |
| Server941 | 10.69.152.250  | aa:bb:97:17:27:71 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-3/adaptor-1/host-eth-1  |
| Server941 | 10.69.152.250  | aa:bb:95:54:31:29 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-3/adaptor-1/host-eth-2  |
| Server941 | 10.69.152.250  | aa:bb:48:27:34:21 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-3/adaptor-1/host-eth-3  |
| Server941 | 10.69.152.250  | aa:bb:80:10:86:62 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-3/adaptor-1/host-eth-4  |
| Server851 | 10.250.181.57  | aa:bb:17:96:43:84 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-4/adaptor-2/ext-eth-1   |
| Server851 | 10.250.181.57  | aa:bb:72:70:27:96 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-4/adaptor-2/ext-eth-7   |
| Server851 | 10.250.181.57  | aa:bb:10:29:99:80 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-4/adaptor-2/ext-eth-3   |
| Server851 | 10.250.181.57  | aa:bb:68:77:85:16 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-4/adaptor-2/ext-eth-5   |
| Server851 | 10.250.181.57  | aa:bb:97:11:59:51 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-4/adaptor-1/ext-eth-3   |
| Server851 | 10.250.181.57  | aa:bb:41:78:28:68 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-4/adaptor-1/ext-eth-1   |
| Server851 | 10.250.181.57  | aa:bb:47:13:26:29 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-4/adaptor-1/ext-eth-5   |
| Server851 | 10.250.181.57  | aa:bb:98:28:79:51 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-4/adaptor-1/ext-eth-7   |
| Server851 | 10.250.181.57  | aa:bb:75:81:26:94 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-4/adaptor-2/host-eth-3  |
| Server851 | 10.250.181.57  | aa:bb:30:95:27:69 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-4/adaptor-2/host-eth-2  |
| Server851 | 10.250.181.57  | aa:bb:77:81:81:27 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-4/adaptor-2/host-eth-4  |
| Server851 | 10.250.181.57  | aa:bb:64:95:60:19 | UCSB-VIC-M84-4P                            | sys/chassis-2/blade-4/adaptor-2/host-eth-1  |
| Server851 | 10.250.181.57  | aa:bb:15:65:97:44 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-4/adaptor-1/host-eth-1  |
| Server851 | 10.250.181.57  | aa:bb:77:72:57:63 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-4/adaptor-1/host-eth-2  |
| Server851 | 10.250.181.57  | aa:bb:40:59:14:80 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-4/adaptor-1/host-eth-4  |
| Server851 | 10.250.181.57  | aa:bb:12:45:70:67 | UCSB-MLOM-40G-04                           | sys/chassis-2/blade-4/adaptor-1/host-eth-3  |
+-----------+----------------+-------------------+--------------------------------------------+---------------------------------------------+

IMC [#4]
--------

+-----------+------------+---------------+------------+-------------------+
| Server    | IP         | Mask          | Gateway    | MAC               |
+-----------+------------+---------------+------------+-------------------+
| Server874 | 10.1.1.149 | 255.255.255.0 | 10.1.1.254 | aa:bb:58:18:85:60 |
| Server449 | 10.1.1.86  | 255.255.255.0 | 10.1.1.254 | aa:bb:85:91:56:42 |
| Server731 | 10.1.1.151 | 255.255.255.0 | 10.1.1.254 | aa:bb:97:91:89:96 |
| Server583 | 10.1.1.184 | 255.255.255.0 | 10.1.1.254 | aa:bb:17:69:56:39 |
+-----------+------------+---------------+------------+-------------------+

Network Adapters [#22]
----------------------

+-----------+--------------+---------+--------------------------------------------+-------------------+--------+-------------------+-----+-----+-----+
| Server    | Name         | PciSlot | Model                                      | PID               | Serial | Vendor            | Eth | HBA | DCE |
+-----------+--------------+---------+--------------------------------------------+-------------------+--------+-------------------+-----+-----+-----+
| Server874 | Adapter 3    | 3       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | UCSC-PCIE-ID25GF  | SN-54  | 0x8086            | 2   | 0   | 0   |
| Server874 | Adapter 6    | 6       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | UCSC-PCIE-ID25GF  | SN-53  | 0x8086            | 2   | 0   | 0   |
| Server874 | Adapter L    | L       | Cisco(R) LOM X550-T2                       | --                | SN-92  | 0x8086            | 2   | 0   | 0   |
| Server874 | Adapter MLOM | MLOM    | UCSC-MLOM-C25Q-04                          | UCSC-MLOM-C25Q-04 | SN-13  | Cisco Systems Inc | 4   | 4   | 4   |
| Server449 | Adapter 3    | 3       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | UCSC-PCIE-ID25GF  | SN-52  | 0x8086            | 2   | 0   | 0   |
| Server449 | Adapter 6    | 6       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | UCSC-PCIE-ID25GF  | SN-58  | 0x8086            | 2   | 0   | 0   |
| Server449 | Adapter L    | L       | Cisco(R) LOM X550-T2                       | --                | SN-59  | 0x8086            | 2   | 0   | 0   |
| Server449 | Adapter MLOM | MLOM    | UCSC-MLOM-C25Q-04                          | UCSC-MLOM-C25Q-04 | SN-48  | Cisco Systems Inc | 4   | 4   | 4   |
| Server731 | Adapter 3    | 3       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | UCSC-PCIE-ID25GF  | SN-60  | 0x8086            | 2   | 0   | 0   |
| Server731 | Adapter 6    | 6       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | UCSC-PCIE-ID25GF  | SN-13  | 0x8086            | 2   | 0   | 0   |
| Server731 | Adapter L    | L       | Cisco(R) LOM X550-T2                       | NA                | SN-27  | 0x8086            | 2   | 0   | 0   |
| Server731 | Adapter MLOM | MLOM    | UCSC-MLOM-C25Q-04                          | UCSC-MLOM-C25Q-04 | SN-40  | Cisco Systems Inc | 4   | 4   | 4   |
| Server583 | Adapter 1    | 1       | UCSC-PCIE-C25Q-04                          | UCSC-PCIE-C25Q-04 | SN-56  | Cisco Systems Inc | 8   | 4   | 4   |
| Server583 | Adapter MLOM | MLOM    | UCSC-M-V100-04                             | UCSC-M-V100-04    | SN-39  | Cisco Systems Inc | 6   | 2   | 2   |
| Server378 | Adapter 1    | N/A     | UCSB-MLOM-40G-04                           | --                | SN-85  | Cisco Systems Inc | 4   | 0   | 4   |
| Server378 | Adapter 2    | N/A     | UCSB-VIC-M84-4P                            | --                | SN-36  | Cisco Systems Inc | 4   | 0   | 4   |
| Server300 | Adapter 1    | N/A     | UCSB-MLOM-40G-04                           | --                | SN-82  | Cisco Systems Inc | 4   | 0   | 4   |
| Server300 | Adapter 2    | N/A     | UCSB-VIC-M84-4P                            | --                | SN-70  | Cisco Systems Inc | 4   | 0   | 4   |
| Server941 | Adapter 1    | N/A     | UCSB-MLOM-40G-04                           | --                | SN-40  | Cisco Systems Inc | 4   | 0   | 4   |
| Server941 | Adapter 2    | N/A     | UCSB-VIC-M84-4P                            | --                | SN-93  | Cisco Systems Inc | 4   | 0   | 4   |
| Server851 | Adapter 1    | N/A     | UCSB-MLOM-40G-04                           | --                | SN-38  | Cisco Systems Inc | 4   | 0   | 4   |
| Server851 | Adapter 2    | N/A     | UCSB-VIC-M84-4P                            | --                | SN-67  | Cisco Systems Inc | 4   | 0   | 4   |
+-----------+--------------+---------+--------------------------------------------+-------------------+--------+-------------------+-----+-----+-----+

External Ethernet (MLOM) [#50]
------------------------------

+-----------+-------------------+--------------+-------------------+
| Server    | Adapter Model     | Interface ID | MAC Address       |
+-----------+-------------------+--------------+-------------------+
| Server874 | UCSC-MLOM-C25Q-04 | 0            | aa:bb:96:91:10:19 |
| Server874 | UCSC-MLOM-C25Q-04 | 1            | aa:bb:49:22:20:35 |
| Server874 | UCSC-MLOM-C25Q-04 | 2            | aa:bb:73:33:51:37 |
| Server874 | UCSC-MLOM-C25Q-04 | 3            | aa:bb:75:25:18:37 |
| Server449 | UCSC-MLOM-C25Q-04 | 0            | aa:bb:31:25:98:15 |
| Server449 | UCSC-MLOM-C25Q-04 | 1            | aa:bb:20:74:42:31 |
| Server449 | UCSC-MLOM-C25Q-04 | 2            | aa:bb:21:70:68:66 |
| Server449 | UCSC-MLOM-C25Q-04 | 3            | aa:bb:54:59:17:49 |
| Server731 | UCSC-MLOM-C25Q-04 | 0            | aa:bb:93:62:29:82 |
| Server731 | UCSC-MLOM-C25Q-04 | 1            | aa:bb:36:22:52:58 |
| Server731 | UCSC-MLOM-C25Q-04 | 2            | aa:bb:22:46:40:75 |
| Server731 | UCSC-MLOM-C25Q-04 | 3            | aa:bb:90:69:36:58 |
| Server583 | UCSC-PCIE-C25Q-04 | 0            | aa:bb:76:57:23:81 |
| Server583 | UCSC-PCIE-C25Q-04 | 1            | aa:bb:86:57:74:96 |
| Server583 | UCSC-PCIE-C25Q-04 | 2            | aa:bb:82:36:64:93 |
| Server583 | UCSC-PCIE-C25Q-04 | 3            | aa:bb:35:10:31:93 |
| Server583 | UCSC-M-V100-04    | 0            | aa:bb:37:27:14:35 |
| Server583 | UCSC-M-V100-04    | 1            | aa:bb:98:35:56:72 |
| Server378 | UCSB-MLOM-40G-04  | 1            | aa:bb:80:70:20:17 |
| Server378 | UCSB-MLOM-40G-04  | 3            | aa:bb:19:83:10:24 |
| Server378 | UCSB-MLOM-40G-04  | 5            | aa:bb:28:78:93:69 |
| Server378 | UCSB-MLOM-40G-04  | 7            | aa:bb:30:19:98:63 |
| Server378 | UCSB-VIC-M84-4P   | 1            | aa:bb:58:84:41:67 |
| Server378 | UCSB-VIC-M84-4P   | 3            | aa:bb:70:71:11:50 |
| Server378 | UCSB-VIC-M84-4P   | 5            | aa:bb:18:46:54:38 |
| Server378 | UCSB-VIC-M84-4P   | 7            | aa:bb:28:79:62:42 |
| Server300 | UCSB-MLOM-40G-04  | 1            | aa:bb:31:36:17:96 |
| Server300 | UCSB-MLOM-40G-04  | 3            | aa:bb:36:80:77:96 |
| Server300 | UCSB-MLOM-40G-04  | 5            | aa:bb:72:17:53:32 |
| Server300 | UCSB-MLOM-40G-04  | 7            | aa:bb:84:44:49:45 |
| Server300 | UCSB-VIC-M84-4P   | 1            | aa:bb:62:43:38:92 |
| Server300 | UCSB-VIC-M84-4P   | 3            | aa:bb:10:92:20:24 |
| Server300 | UCSB-VIC-M84-4P   | 5            | aa:bb:40:97:84:77 |
| Server300 | UCSB-VIC-M84-4P   | 7            | aa:bb:72:97:31:48 |
| Server941 | UCSB-MLOM-40G-04  | 1            | aa:bb:86:82:74:20 |
| Server941 | UCSB-MLOM-40G-04  | 3            | aa:bb:18:91:50:79 |
| Server941 | UCSB-MLOM-40G-04  | 5            | aa:bb:47:97:31:81 |
| Server941 | UCSB-MLOM-40G-04  | 7            | aa:bb:43:17:83:43 |
| Server941 | UCSB-VIC-M84-4P   | 1            | aa:bb:60:48:90:99 |
| Server941 | UCSB-VIC-M84-4P   | 3            | aa:bb:76:37:12:21 |
| Server941 | UCSB-VIC-M84-4P   | 5            | aa:bb:92:31:45:94 |
| Server941 | UCSB-VIC-M84-4P   | 7            | aa:bb:45:52:80:64 |
| Server851 | UCSB-MLOM-40G-04  | 1            | aa:bb:36:28:97:49 |
| Server851 | UCSB-MLOM-40G-04  | 3            | aa:bb:50:41:67:26 |
| Server851 | UCSB-MLOM-40G-04  | 5            | aa:bb:30:40:32:31 |
| Server851 | UCSB-MLOM-40G-04  | 7            | aa:bb:58:42:42:56 |
| Server851 | UCSB-VIC-M84-4P   | 1            | aa:bb:70:55:78:68 |
| Server851 | UCSB-VIC-M84-4P   | 3            | aa:bb:57:74:58:84 |
| Server851 | UCSB-VIC-M84-4P   | 5            | aa:bb:15:83:44:58 |
| Server851 | UCSB-VIC-M84-4P   | 7            | aa:bb:80:12:47:36 |
+-----------+-------------------+--------------+-------------------+

Host Ethernet [#76]
-------------------

+-----------+--------------+--------------------------------------------+----------------+-------------------+
| Server    | Adapter Name | Adapter Model                              | Interface Name | MAC Address       |
+-----------+--------------+--------------------------------------------+----------------+-------------------+
| Server874 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-74        | aa:bb:23:85:89:41 |
| Server874 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-46        | aa:bb:16:77:48:18 |
| Server874 | Adapter 6    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-68        | aa:bb:83:19:68:38 |
| Server874 | Adapter 6    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-97        | aa:bb:26:91:28:75 |
| Server874 | Adapter L    | Cisco(R) LOM X550-T2                       | Name-40        | aa:bb:32:83:92:47 |
| Server874 | Adapter L    | Cisco(R) LOM X550-T2                       | Name-24        | aa:bb:14:48:12:72 |
| Server874 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-89        | aa:bb:10:87:45:72 |
| Server874 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-28        | aa:bb:67:89:14:94 |
| Server874 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-50        | aa:bb:43:40:20:23 |
| Server874 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-21        | aa:bb:15:42:94:56 |
| Server449 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-75        | aa:bb:44:30:30:67 |
| Server449 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-22        | aa:bb:36:96:83:20 |
| Server449 | Adapter 6    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-13        | aa:bb:11:93:31:45 |
| Server449 | Adapter 6    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-10        | aa:bb:78:20:68:70 |
| Server449 | Adapter L    | Cisco(R) LOM X550-T2                       | Name-78        | aa:bb:96:45:89:89 |
| Server449 | Adapter L    | Cisco(R) LOM X550-T2                       | Name-23        | aa:bb:58:73:75:70 |
| Server449 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-35        | aa:bb:28:22:74:77 |
| Server449 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-94        | aa:bb:96:81:63:62 |
| Server449 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-81        | aa:bb:64:21:48:58 |
| Server449 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-71        | aa:bb:77:82:63:81 |
| Server731 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-51        | aa:bb:56:25:90:90 |
| Server731 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-22        | aa:bb:60:21:90:87 |
| Server731 | Adapter 6    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-44        | aa:bb:25:32:43:27 |
| Server731 | Adapter 6    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-84        | aa:bb:39:14:78:79 |
| Server731 | Adapter L    | Cisco(R) LOM X550-T2                       | Name-70        | aa:bb:73:61:30:13 |
| Server731 | Adapter L    | Cisco(R) LOM X550-T2                       | Name-65        | aa:bb:64:30:35:70 |
| Server731 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-77        | aa:bb:84:88:35:42 |
| Server731 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-11        | aa:bb:96:86:53:26 |
| Server731 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-32        | aa:bb:17:62:81:27 |
| Server731 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-71        | aa:bb:47:75:42:50 |
| Server583 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-37        | aa:bb:41:14:80:94 |
| Server583 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-47        | aa:bb:83:36:29:44 |
| Server583 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-95        | aa:bb:53:35:32:35 |
| Server583 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-25        | aa:bb:23:55:76:32 |
| Server583 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-20        | aa:bb:66:88:17:98 |
| Server583 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-35        | aa:bb:35:19:79:14 |
| Server583 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-84        | aa:bb:10:74:23:17 |
| Server583 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-10        | aa:bb:83:38:23:24 |
| Server583 | Adapter MLOM | UCSC-M-V100-04                             | Name-55        | aa:bb:44:71:66:90 |
| Server583 | Adapter MLOM | UCSC-M-V100-04                             | Name-32        | aa:bb:83:59:67:71 |
| Server583 | Adapter MLOM | UCSC-M-V100-04                             | Name-68        | aa:bb:25:15:99:14 |
| Server583 | Adapter MLOM | UCSC-M-V100-04                             | Name-72        | aa:bb:63:90:28:64 |
| Server583 | Adapter MLOM | UCSC-M-V100-04                             | Name-21        | aa:bb:78:96:52:14 |
| Server583 | Adapter MLOM | UCSC-M-V100-04                             | Name-19        | aa:bb:52:86:21:67 |
| Server378 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-99        | aa:bb:16:99:39:17 |
| Server378 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-73        | aa:bb:65:11:43:81 |
| Server378 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-20        | aa:bb:18:13:67:57 |
| Server378 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-57        | aa:bb:41:26:80:57 |
| Server378 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-10        | aa:bb:57:76:63:61 |
| Server378 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-33        | aa:bb:40:58:47:15 |
| Server378 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-99        | aa:bb:19:34:61:65 |
| Server378 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-67        | aa:bb:46:61:66:43 |
| Server300 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-77        | aa:bb:14:66:10:63 |
| Server300 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-81        | aa:bb:26:78:21:40 |
| Server300 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-10        | aa:bb:70:87:22:67 |
| Server300 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-14        | aa:bb:80:17:87:91 |
| Server300 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-88        | aa:bb:16:10:95:66 |
| Server300 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-51        | aa:bb:12:78:40:34 |
| Server300 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-88        | aa:bb:57:21:53:54 |
| Server300 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-95        | aa:bb:40:80:26:29 |
| Server941 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-91        | aa:bb:89:81:50:43 |
| Server941 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-47        | aa:bb:90:73:81:40 |
| Server941 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-16        | aa:bb:33:99:76:34 |
| Server941 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-63        | aa:bb:59:25:37:95 |
| Server941 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-23        | aa:bb:41:18:12:70 |
| Server941 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-79        | aa:bb:21:90:76:93 |
| Server941 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-54        | aa:bb:51:32:16:59 |
| Server941 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-94        | aa:bb:70:78:98:98 |
| Server851 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-97        | aa:bb:34:75:58:50 |
| Server851 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-97        | aa:bb:35:51:58:23 |
| Server851 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-38        | aa:bb:85:41:93:50 |
| Server851 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-98        | aa:bb:73:25:32:46 |
| Server851 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-98        | aa:bb:16:89:51:13 |
| Server851 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-39        | aa:bb:34:16:69:59 |
| Server851 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-59        | aa:bb:11:31:91:66 |
| Server851 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-41        | aa:bb:12:16:51:60 |
+-----------+--------------+--------------------------------------------+----------------+-------------------+

Host FC [#18]
-------------

+-----------+--------------+-------------------+----------------+-------------------------+-------------------------+
| Server    | Adapter Name | Adapter Model     | Interface Name | WWNN                    | WWPN                    |
+-----------+--------------+-------------------+----------------+-------------------------+-------------------------+
| Server874 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc0            | 10:10:aa:bb:61:16:20:23 | 20:20:aa:bb:59:16:15:52 |
| Server874 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc1            | 10:10:aa:bb:91:38:97:52 | 20:20:aa:bb:65:30:75:58 |
| Server874 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc2            | 10:10:aa:bb:50:19:72:76 | 20:20:aa:bb:73:81:54:52 |
| Server874 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc3            | 10:10:aa:bb:29:33:72:42 | 20:20:aa:bb:67:54:48:92 |
| Server449 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc0            | 10:10:aa:bb:50:29:16:36 | 20:20:aa:bb:90:95:20:98 |
| Server449 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc1            | 10:10:aa:bb:67:68:24:91 | 20:20:aa:bb:65:56:27:23 |
| Server449 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc2            | 10:10:aa:bb:33:73:58:32 | 20:20:aa:bb:23:19:72:74 |
| Server449 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc3            | 10:10:aa:bb:33:25:42:14 | 20:20:aa:bb:17:64:24:46 |
| Server731 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc0            | 10:10:aa:bb:26:88:70:85 | 20:20:aa:bb:66:35:99:50 |
| Server731 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc1            | 10:10:aa:bb:61:58:96:81 | 20:20:aa:bb:59:19:78:14 |
| Server731 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc2            | 10:10:aa:bb:48:98:99:13 | 20:20:aa:bb:75:25:42:39 |
| Server731 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc3            | 10:10:aa:bb:74:61:99:85 | 20:20:aa:bb:85:31:16:19 |
| Server583 | Adapter 1    | UCSC-PCIE-C25Q-04 | fc0            | 10:10:aa:bb:76:58:13:17 | 20:20:aa:bb:44:16:39:49 |
| Server583 | Adapter 1    | UCSC-PCIE-C25Q-04 | fc1            | 10:10:aa:bb:68:34:49:81 | 20:20:aa:bb:10:32:87:98 |
| Server583 | Adapter 1    | UCSC-PCIE-C25Q-04 | fc2            | 10:10:aa:bb:21:14:43:73 | 20:20:aa:bb:63:58:16:56 |
| Server583 | Adapter 1    | UCSC-PCIE-C25Q-04 | fc3            | 10:10:aa:bb:30:94:51:87 | 20:20:aa:bb:61:54:26:83 |
| Server583 | Adapter MLOM | UCSC-M-V100-04    | fc0            | 10:10:aa:bb:23:18:97:88 | 20:20:aa:bb:69:12:32:79 |
| Server583 | Adapter MLOM | UCSC-M-V100-04    | fc1            | 10:10:aa:bb:53:94:93:39 | 20:20:aa:bb:19:67:49:13 |
+-----------+--------------+-------------------+----------------+-------------------------+-------------------------+

PCI [#24]
---------

+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server    | PCI Device Model                        | Pid               | Serial | SlotId     | Vendor            | Firmware |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server874 | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  | SN-37  | 3          | 0x8086            | 1.0(1a)  |
|           | XXV710-DA2                              |                   |        |            |                   |          |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server874 | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  | SN-68  | 6          | 0x8086            | 1.0(1a)  |
|           | XXV710-DA2                              |                   |        |            |                   |          |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server874 | Intel X550 LOM                          | None              | SN-83  | L          | 0x8086            | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server874 | Cisco UCS VIC 1457 MLOM                 | UCSC-MLOM-C25Q-04 | SN-84  | MLOM       | 0x1137            | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server874 | Cisco 12G Modular Raid Controller with  | UCSC-RAID-M5      | SN-26  | MRAID      | 0x1000            | 1.0(1a)  |
|           | 2GB cache (max 16 drives)               |                   |        |            |                   |          |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server449 | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  | SN-40  | 3          | 0x8086            | 1.0(1a)  |
|           | XXV710-DA2                              |                   |        |            |                   |          |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server449 | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  | SN-44  | 6          | 0x8086            | 1.0(1a)  |
|           | XXV710-DA2                              |                   |        |            |                   |          |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server449 | Intel X550 LOM                          | None              | SN-15  | L          | 0x8086            | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server449 | Cisco UCS VIC 1457 MLOM                 | UCSC-MLOM-C25Q-04 | SN-42  | MLOM       | 0x1137            | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server449 | Cisco 12G Modular Raid Controller with  | UCSC-RAID-M5      | SN-41  | MRAID      | 0x1000            | 1.0(1a)  |
|           | 2GB cache (max 16 drives)               |                   |        |            |                   |          |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server731 | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  | SN-73  | 3          | 0x8086            | 1.0(1a)  |
|           | XXV710-DA2                              |                   |        |            |                   |          |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server731 | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  | SN-33  | 6          | 0x8086            | 1.0(1a)  |
|           | XXV710-DA2                              |                   |        |            |                   |          |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server731 | Intel X550 LOM                          | NA                | SN-41  | L          | 0x8086            | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server731 | Cisco UCS VIC 1457 MLOM                 | UCSC-MLOM-C25Q-04 | SN-87  | MLOM       | 0x1137            | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server731 | Cisco 12G Modular Raid Controller with  | UCSC-RAID-M5      | SN-52  | MRAID      | 0x1000            | 1.0(1a)  |
|           | 2GB cache (max 16 drives)               |                   |        |            |                   |          |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server583 | Cisco UCS VIC 1455                      | UCSC-PCIE-C25Q-04 | SN-57  | 1          | 0x1137            | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server583 | NVIDIA T4 PCIe 16GB 70W                 | UCSC-GPU-T4-16    | SN-67  | 3          | 0x10de            | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server583 | Cisco UCS VIC 1477 MLOM                 | UCSC-M-V100-04    | SN-51  | MLOM       | 0x1137            | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server583 | Cisco 12G SAS RAID Controller with 4GB  | UCSC-RAID-M6T     | SN-44  | MRAID      | 0x1000            | 1.0(1a)  |
|           | FBWC (16 Drives)                        |                   |        |            |                   |          |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server583 | Cisco Boot optimized M.2 Raid           | UCS-M2-HWRAID     | SN-80  | MSTOR-RAID | 0x1b4b            | 1.0(1a)  |
|           | controller                              |                   |        |            |                   |          |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server378 | UCSB-MRAID12G-HE                        | UCSB-MRAID12G-HE  | SN-50  | FMEZZ1-SAS | Cisco Systems Inc | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server300 | UCSB-MRAID12G-HE                        | UCSB-MRAID12G-HE  | SN-79  | FMEZZ1-SAS | Cisco Systems Inc | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server941 | UCSB-MRAID12G-HE                        | UCSB-MRAID12G-HE  | SN-99  | FMEZZ1-SAS | Cisco Systems Inc | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+
| Server851 | UCSB-MRAID12G-HE                        | UCSB-MRAID12G-HE  | SN-61  | FMEZZ1-SAS | Cisco Systems Inc | 1.0(1a)  |
+-----------+-----------------------------------------+-------------------+--------+------------+-------------------+----------+

PCI Node [#0]
-------------
None

Fan [#58]
---------

+-----------+-------+----------------------+-----------+----------+
| Server    | State | Fan                  | OperState | Presence |
+-----------+-------+----------------------+-----------+----------+
| Server874 | V     | Fan Module 1 - Fan 1 | operable  | equipped |
| Server874 | V     | Fan Module 1 - Fan 2 | operable  | equipped |
| Server874 | V     | Fan Module 2 - Fan 1 | operable  | equipped |
| Server874 | V     | Fan Module 2 - Fan 2 | operable  | equipped |
| Server874 | V     | Fan Module 3 - Fan 1 | operable  | equipped |
| Server874 | V     | Fan Module 3 - Fan 2 | operable  | equipped |
| Server874 | V     | Fan Module 4 - Fan 1 | operable  | equipped |
| Server874 | V     | Fan Module 4 - Fan 2 | operable  | equipped |
| Server874 | V     | Fan Module 5 - Fan 1 | operable  | equipped |
| Server874 | V     | Fan Module 5 - Fan 2 | operable  | equipped |
| Server874 | V     | Fan Module 6 - Fan 1 | operable  | equipped |
| Server874 | V     | Fan Module 6 - Fan 2 | operable  | equipped |
| Server874 | X     | Fan Module 7 - Fan 1 | unknown   | missing  |
| Server874 | X     | Fan Module 7 - Fan 2 | unknown   | missing  |
| Server449 | V     | Fan Module 1 - Fan 1 | operable  | equipped |
| Server449 | V     | Fan Module 1 - Fan 2 | operable  | equipped |
| Server449 | V     | Fan Module 2 - Fan 1 | operable  | equipped |
| Server449 | V     | Fan Module 2 - Fan 2 | operable  | equipped |
| Server449 | V     | Fan Module 3 - Fan 1 | operable  | equipped |
| Server449 | V     | Fan Module 3 - Fan 2 | operable  | equipped |
| Server449 | V     | Fan Module 4 - Fan 1 | operable  | equipped |
| Server449 | V     | Fan Module 4 - Fan 2 | operable  | equipped |
| Server449 | V     | Fan Module 5 - Fan 1 | operable  | equipped |
| Server449 | V     | Fan Module 5 - Fan 2 | operable  | equipped |
| Server449 | V     | Fan Module 6 - Fan 1 | operable  | equipped |
| Server449 | V     | Fan Module 6 - Fan 2 | operable  | equipped |
| Server449 | X     | Fan Module 7 - Fan 1 | unknown   | missing  |
| Server449 | X     | Fan Module 7 - Fan 2 | unknown   | missing  |
| Server731 | V     | Fan Module 1 - Fan 1 | operable  | equipped |
| Server731 | V     | Fan Module 1 - Fan 2 | operable  | equipped |
| Server731 | V     | Fan Module 2 - Fan 1 | operable  | equipped |
| Server731 | V     | Fan Module 2 - Fan 2 | operable  | equipped |
| Server731 | V     | Fan Module 3 - Fan 1 | operable  | equipped |
| Server731 | V     | Fan Module 3 - Fan 2 | operable  | equipped |
| Server731 | V     | Fan Module 4 - Fan 1 | operable  | equipped |
| Server731 | V     | Fan Module 4 - Fan 2 | operable  | equipped |
| Server731 | V     | Fan Module 5 - Fan 1 | operable  | equipped |
| Server731 | V     | Fan Module 5 - Fan 2 | operable  | equipped |
| Server731 | V     | Fan Module 6 - Fan 1 | operable  | equipped |
| Server731 | V     | Fan Module 6 - Fan 2 | operable  | equipped |
| Server731 | X     | Fan Module 7 - Fan 1 | unknown   | missing  |
| Server731 | X     | Fan Module 7 - Fan 2 | unknown   | missing  |
| Server583 | V     | Fan Module 1 - Fan 1 | operable  | equipped |
| Server583 | V     | Fan Module 1 - Fan 2 | operable  | equipped |
| Server583 | V     | Fan Module 2 - Fan 1 | operable  | equipped |
| Server583 | V     | Fan Module 2 - Fan 2 | operable  | equipped |
| Server583 | V     | Fan Module 3 - Fan 1 | operable  | equipped |
| Server583 | V     | Fan Module 3 - Fan 2 | operable  | equipped |
| Server583 | V     | Fan Module 4 - Fan 1 | operable  | equipped |
| Server583 | V     | Fan Module 4 - Fan 2 | operable  | equipped |
| Server583 | V     | Fan Module 5 - Fan 1 | operable  | equipped |
| Server583 | V     | Fan Module 5 - Fan 2 | operable  | equipped |
| Server583 | V     | Fan Module 6 - Fan 1 | operable  | equipped |
| Server583 | V     | Fan Module 6 - Fan 2 | operable  | equipped |
| Server583 | X     | Fan Module 7 - Fan 1 | unknown   | equipped |
| Server583 | X     | Fan Module 7 - Fan 2 | unknown   | equipped |
| Server583 | X     | Fan Module 8 - Fan 1 | unknown   | equipped |
| Server583 | X     | Fan Module 8 - Fan 2 | unknown   | equipped |
+-----------+-------+----------------------+-----------+----------+

PSU [#8]
--------

+-----------+--------+-------+---------+---------+---------------+--------+-------------------+
| Server    | Name   | State | Present | Voltage | Model         | Serial | Vendor            |
+-----------+--------+-------+---------+---------+---------------+--------+-------------------+
| Server874 | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | SN-22  | Cisco Systems Inc |
| Server874 | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | SN-99  | Cisco Systems Inc |
| Server449 | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | SN-58  | Cisco Systems Inc |
| Server449 | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | SN-88  | Cisco Systems Inc |
| Server731 | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | SN-17  | Cisco Systems Inc |
| Server731 | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | SN-55  | Cisco Systems Inc |
| Server583 | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | SN-39  | Cisco Systems Inc |
| Server583 | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | SN-16  | Cisco Systems Inc |
+-----------+--------+-------+---------+---------+---------------+--------+-------------------+

Trusted Platform Module [#4]
----------------------------

+-----------+----------+-------------------+-------------+------------+------------------+-------------------+--------+------------------+
| Server    | TPM      | Activation Status | Admin State | Version    | Model            | Vendor            | Serial | Firmware Version |
+-----------+----------+-------------------+-------------+------------+------------------+-------------------+--------+------------------+
| Server874 | empty    | unknown           | unknown     | Version-98 | NA               | NA                | SN-36  | Version-32       |
| Server449 | empty    | unknown           | unknown     | Version-72 | NA               | NA                | SN-28  | Version-33       |
| Server731 | empty    | unknown           | unknown     | Version-57 | NA               | NA                | SN-39  | Version-59       |
| Server583 | equipped | activated         | enabled     | Version-55 | UCSX-TPM2-002B-C | Cisco Systems Inc | SN-93  | Version-23       |
+-----------+----------+-------------------+-------------+------------+------------------+-------------------+--------+------------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)