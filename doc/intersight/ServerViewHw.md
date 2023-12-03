# Intersight Server

## hw view

```
# iserver get server --group test -v hw

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Motherboard Hardware Summary [#8]
---------------------------------

+--------------------------------+----------+-------------------+-----+--------+------------+------------------+----------+--------------+----------------+---------------+-----+-----+
| Server                         | Board Id | Vendor            | CPU | MemArr | PCI Switch | PCI Cooprocessor | Graphics | Storage Ctrl | FlexFlash Ctrl | FlexUtil Ctrl | Sec | TPM |
+--------------------------------+----------+-------------------+-----+--------+------------+------------------+----------+--------------+----------------+---------------+-----+-----+
| comp-1-p2b-eu-spdc-WZP23400AJW | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 1             | 0   | 1   | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 1             | 0   | 1   | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 1             | 0   | 1   | 
| comp3-p4b-eu-spdc-WZP262207UM  | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 1        | 2            | 0              | 0             | 0   | 1   | 
| FI-ucsb1-eu-spdc-2-1           | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   | 
| FI-ucsb1-eu-spdc-2-2           | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   | 
| FI-ucsb1-eu-spdc-2-3           | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   | 
| FI-ucsb1-eu-spdc-2-4           | 0        | Cisco Systems Inc | 2   | 1      | 0          | 0                | 0        | 2            | 0              | 0             | 0   | 0   | 
+--------------------------------+----------+-------------------+-----+--------+------------+------------------+----------+--------------+----------------+---------------+-----+-----+

CPU [#16]
---------

+--------------------------------+-------+--------+--------+------------------------------+------+-------------------------------------------------+-------+-------------+-------------+-------------+-------------+----------+-----------+---------+
| Server                         | State | CPU Id | Socket | Vendor                       | Arch | Model                                           | Cores | Enabled     | Threads     | Speed [GHz] | Stepping    | Presence | OperState | Thermal |
+--------------------------------+-------+--------+--------+------------------------------+------+-------------------------------------------------+-------+-------------+-------------+-------------+-------------+----------+-----------+---------+
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | 1      | CPU1   | Advanced Micro Devices, Inc. | Zen  | AMD EPYC 7763 64-Core Processor                 | 64    | 64          | 128         | 2.45        | 1           | equipped | operable  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 2      | CPU2   |                              | any  |                                                 | 0     | unspecified | unspecified | 0           | unspecified | missing  | removed   |         | 
| FI-ucsb1-eu-spdc-2-1           | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 1      | CPU1   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 2      | CPU2   | Intel(R) Corporation         | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz        | 20    | 20          | 40          | 2.5         | 7           | equipped | operable  | ok      | 
+--------------------------------+-------+--------+--------+------------------------------+------+-------------------------------------------------+-------+-------------+-------------+-------------+-------------+----------+-----------+---------+

GPU [#1]
--------

+-------------------------------+-------------------------+----------------+--------+--------+----------+---------------------------------+
| Server                        | GPU Device Model        | Pid            | SlotId | Vendor | Firmware | Dn                              |
+-------------------------------+-------------------------+----------------+--------+--------+----------+---------------------------------+
| comp3-p4b-eu-spdc-WZP262207UM | NVIDIA T4 PCIe 16GB 70W | UCSC-GPU-T4-16 | 3      | 0x10de | N/A      | sys/rack-unit-1/equipped-slot-3 | 
+-------------------------------+-------------------------+----------------+--------+--------+----------+---------------------------------+

Memory [#200]
-------------

+--------------------------------+-------+-----------+-------+------+------------+----------+-------------+---------+--------------+--------------+----------------------+--------------------+------------+----------+---------+
| Server                         | State | Memory Id | Array | Bank | Location   | Capacity | Clock       | Latency | Form Factor  | Type         | Model                | Serial             | Oper State | Presence | Thermal |
+--------------------------------+-------+-----------+-------+------+------------+----------+-------------+---------+--------------+--------------+----------------------+--------------------+------------+----------+---------+
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 1         | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73490           | operable   | equipped |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | 2         | 1     | 0    | DIMM_A2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 3         | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72CD9           | operable   | equipped |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | 4         | 1     | 0    | DIMM_B2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 5         | 1     | 0    | DIMM_C1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F7348D           | operable   | equipped |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | 6         | 1     | 0    | DIMM_C2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 7         | 1     | 0    | DIMM_D1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F734A7           | operable   | equipped |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | 8         | 1     | 0    | DIMM_D2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 9         | 1     | 0    | DIMM_E1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73492           | operable   | equipped |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | 10        | 1     | 0    | DIMM_E2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 11        | 1     | 0    | DIMM_F1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73498           | operable   | equipped |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | 12        | 1     | 0    | DIMM_F2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 13        | 1     | 0    | DIMM_G1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F7348E           | operable   | equipped |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | 14        | 1     | 0    | DIMM_G2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 15        | 1     | 0    | DIMM_H1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73495           | operable   | equipped |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | 16        | 1     | 0    | DIMM_H2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 17        | 1     | 0    | DIMM_J1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72CCC           | operable   | equipped |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | 18        | 1     | 0    | DIMM_J2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 19        | 1     | 0    | DIMM_K1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73493           | operable   | equipped |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | 20        | 1     | 0    | DIMM_K2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 21        | 1     | 0    | DIMM_L1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73494           | operable   | equipped |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | 22        | 1     | 0    | DIMM_L2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | 23        | 1     | 0    | DIMM_M1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F734AD           | operable   | equipped |         | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | 24        | 1     | 0    | DIMM_M2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 1         | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F736F1           | operable   | equipped |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | 2         | 1     | 0    | DIMM_A2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 3         | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F7370D           | operable   | equipped |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | 4         | 1     | 0    | DIMM_B2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 5         | 1     | 0    | DIMM_C1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F736F9           | operable   | equipped |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | 6         | 1     | 0    | DIMM_C2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 7         | 1     | 0    | DIMM_D1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73709           | operable   | equipped |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | 8         | 1     | 0    | DIMM_D2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 9         | 1     | 0    | DIMM_E1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F736F7           | operable   | equipped |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | 10        | 1     | 0    | DIMM_E2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 11        | 1     | 0    | DIMM_F1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F7370A           | operable   | equipped |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | 12        | 1     | 0    | DIMM_F2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 13        | 1     | 0    | DIMM_G1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F736F8           | operable   | equipped |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | 14        | 1     | 0    | DIMM_G2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 15        | 1     | 0    | DIMM_H1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F736ED           | operable   | equipped |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | 16        | 1     | 0    | DIMM_H2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 17        | 1     | 0    | DIMM_J1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F736F6           | operable   | equipped |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | 18        | 1     | 0    | DIMM_J2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 19        | 1     | 0    | DIMM_K1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0EFB85E           | operable   | equipped |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | 20        | 1     | 0    | DIMM_K2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 21        | 1     | 0    | DIMM_L1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72BFA           | operable   | equipped |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | 22        | 1     | 0    | DIMM_L2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | 23        | 1     | 0    | DIMM_M1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72BFE           | operable   | equipped |         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | 24        | 1     | 0    | DIMM_M2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 1         | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F7348A           | operable   | equipped |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | 2         | 1     | 0    | DIMM_A2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 3         | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F7348F           | operable   | equipped |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | 4         | 1     | 0    | DIMM_B2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 5         | 1     | 0    | DIMM_C1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72D59           | operable   | equipped |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | 6         | 1     | 0    | DIMM_C2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 7         | 1     | 0    | DIMM_D1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72D5A           | operable   | equipped |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | 8         | 1     | 0    | DIMM_D2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 9         | 1     | 0    | DIMM_E1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F734A6           | operable   | equipped |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | 10        | 1     | 0    | DIMM_E2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 11        | 1     | 0    | DIMM_F1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72D73           | operable   | equipped |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | 12        | 1     | 0    | DIMM_F2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 13        | 1     | 0    | DIMM_G1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F734E5           | operable   | equipped |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | 14        | 1     | 0    | DIMM_G2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 15        | 1     | 0    | DIMM_H1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72D5D           | operable   | equipped |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | 16        | 1     | 0    | DIMM_H2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 17        | 1     | 0    | DIMM_J1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F734C1           | operable   | equipped |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | 18        | 1     | 0    | DIMM_J2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 19        | 1     | 0    | DIMM_K1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72D71           | operable   | equipped |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | 20        | 1     | 0    | DIMM_K2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 21        | 1     | 0    | DIMM_L1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72D86           | operable   | equipped |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | 22        | 1     | 0    | DIMM_L2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | 23        | 1     | 0    | DIMM_M1    | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72D60           | operable   | equipped |         | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | 24        | 1     | 0    | DIMM_M2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 1         | 1     | 0    | DIMM_P1_A1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | 2         | 1     | 0    | DIMM_P1_A2 | 64 [GiB] | 3200        |         | DIMM         | DDR4         | M393A8G40AB2-CWE     | K00O00020713F09E6B | operable   | equipped |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 3         | 1     | 0    | DIMM_P1_B1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | 4         | 1     | 0    | DIMM_P1_B2 | 64 [GiB] | 3200        |         | DIMM         | DDR4         | M393A8G40AB2-CWE     | K00O00020713F09FB1 | operable   | equipped |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 5         | 1     | 0    | DIMM_P1_C1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | 6         | 1     | 0    | DIMM_P1_C2 | 64 [GiB] | 3200        |         | DIMM         | DDR4         | M393A8G40AB2-CWE     | K00O00020713F082FF | operable   | equipped |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 7         | 1     | 0    | DIMM_P1_D1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | 8         | 1     | 0    | DIMM_P1_D2 | 64 [GiB] | 3200        |         | DIMM         | DDR4         | M393A8G40AB2-CWE     | K00O00020713F083E5 | operable   | equipped |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 9         | 1     | 0    | DIMM_P1_E1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | 10        | 1     | 0    | DIMM_P1_E2 | 64 [GiB] | 3200        |         | DIMM         | DDR4         | M393A8G40AB2-CWE     | K00O00020713F0843C | operable   | equipped |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 11        | 1     | 0    | DIMM_P1_F1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | 12        | 1     | 0    | DIMM_P1_F2 | 64 [GiB] | 3200        |         | DIMM         | DDR4         | M393A8G40AB2-CWE     | K00O00020713F094EE | operable   | equipped |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 13        | 1     | 0    | DIMM_P1_G1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | 14        | 1     | 0    | DIMM_P1_G2 | 64 [GiB] | 3200        |         | DIMM         | DDR4         | M393A8G40AB2-CWE     | K00O00020713F0843D | operable   | equipped |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 15        | 1     | 0    | DIMM_P1_H1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | 16        | 1     | 0    | DIMM_P1_H2 | 64 [GiB] | 3200        |         | DIMM         | DDR4         | M393A8G40AB2-CWE     | K00O00020713F094EF | operable   | equipped |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 17        | 1     | 0    | DIMM_P2_A1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 18        | 1     | 0    | DIMM_P2_A2 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 19        | 1     | 0    | DIMM_P2_B1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 20        | 1     | 0    | DIMM_P2_B2 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 21        | 1     | 0    | DIMM_P2_C1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 22        | 1     | 0    | DIMM_P2_C2 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 23        | 1     | 0    | DIMM_P2_D1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 24        | 1     | 0    | DIMM_P2_D2 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 25        | 1     | 0    | DIMM_P2_E1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 26        | 1     | 0    | DIMM_P2_E2 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 27        | 1     | 0    | DIMM_P2_F1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 28        | 1     | 0    | DIMM_P2_F2 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 29        | 1     | 0    | DIMM_P2_G1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 30        | 1     | 0    | DIMM_P2_G2 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 31        | 1     | 0    | DIMM_P2_H1 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | 32        | 1     | 0    | DIMM_P2_H2 |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  |         | 
| FI-ucsb1-eu-spdc-2-1           | V     | 1         | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D204CB           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 2         | 1     | 0    | DIMM_A2    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D1F4B3           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 3         | 1     | 0    | DIMM_B1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | F09BA153           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 4         | 1     | 0    | DIMM_B2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7AFR4N-VK     | 1222D1FE           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | X     | 5         | 1     | 0    | DIMM_C1    |          | unspecified |         | undiscovered | undiscovered | 36ASF4G72PZ-2G6E1    | F09BA153           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-1           | X     | 6         | 1     | 0    | DIMM_C2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-1           | V     | 7         | 1     | 0    | DIMM_D1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7CJR4N-VK     | 834C103C           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 8         | 1     | 0    | DIMM_D2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E43D           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 9         | 1     | 0    | DIMM_E1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7AFR4N-VK     | 1222D090           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 10        | 1     | 0    | DIMM_E2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76DB55           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | X     | 11        | 1     | 0    | DIMM_F1    |          | unspecified |         | undiscovered | undiscovered | HMA84GR7AFR4N-VK     | 1222D1FE           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-1           | X     | 12        | 1     | 0    | DIMM_F2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-1           | V     | 13        | 1     | 1    | DIMM_G1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D1ECF4           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 14        | 1     | 1    | DIMM_G2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7AFR4N-VK     | 1222D046           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 15        | 1     | 1    | DIMM_H1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D1F981           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 16        | 1     | 1    | DIMM_H2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7CJR4N-VK     | 834C0F60           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | X     | 17        | 1     | 0    | DIMM_J1    |          | unspecified |         | undiscovered | undiscovered | 36ASF4G72PZ-2G6E1    | F09BA156           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-1           | X     | 18        | 1     | 0    | DIMM_J2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-1           | V     | 19        | 1     | 1    | DIMM_K1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7AFR4N-VK     | 1222D19C           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 20        | 1     | 1    | DIMM_K2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E225           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 21        | 1     | 1    | DIMM_L1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | F09BA156           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | V     | 22        | 1     | 1    | DIMM_L2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E1C4           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-1           | X     | 23        | 1     | 0    | DIMM_M1    |          | unspecified |         | undiscovered | undiscovered | HMA84GR7AFR4N-VK     | 1222D046           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-1           | X     | 24        | 1     | 0    | DIMM_M2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-2           | V     | 1         | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D1EA35           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 2         | 1     | 0    | DIMM_A2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7CJR4N-VK     | 834C0F86           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 3         | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D1E9DA           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 4         | 1     | 0    | DIMM_B2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | F09BA16A           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | X     | 5         | 1     | 0    | DIMM_C1    |          | unspecified |         | undiscovered | undiscovered | 36ASF4G72PZ-2G6E1    | F09BA16A           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-2           | X     | 6         | 1     | 0    | DIMM_C2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-2           | V     | 7         | 1     | 0    | DIMM_D1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7AFR4N-VK     | 1222D186           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 8         | 1     | 0    | DIMM_D2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76DB7D           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 9         | 1     | 0    | DIMM_E1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7AFR4N-VK     | 1222D044           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 10        | 1     | 0    | DIMM_E2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E5B4           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | X     | 11        | 1     | 0    | DIMM_F1    |          | unspecified |         | undiscovered | undiscovered | HMA84GR7CJR4N-VK     | 834C0F86           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-2           | X     | 12        | 1     | 0    | DIMM_F2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-2           | V     | 13        | 1     | 1    | DIMM_G1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D1EA7F           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 14        | 1     | 1    | DIMM_G2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | F09BA170           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 15        | 1     | 1    | DIMM_H1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D1E9DE           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 16        | 1     | 1    | DIMM_H2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76DBDC           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | X     | 17        | 1     | 0    | DIMM_J1    |          | unspecified |         | undiscovered | undiscovered | 36ASF4G72PZ-2G6E1    | F09BA170           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-2           | X     | 18        | 1     | 0    | DIMM_J2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-2           | V     | 19        | 1     | 1    | DIMM_K1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7AFR4N-VK     | 1222CFFB           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 20        | 1     | 1    | DIMM_K2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7CJR4N-VK     | 834C0FBE           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 21        | 1     | 1    | DIMM_L1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7AFR4N-VK     | 1222D0E2           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | V     | 22        | 1     | 1    | DIMM_L2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E49B           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-2           | X     | 23        | 1     | 0    | DIMM_M1    |          | unspecified |         | undiscovered | undiscovered | HMA84GR7CJR4N-VK     | 834C0FBE           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-2           | X     | 24        | 1     | 0    | DIMM_M2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-3           | V     | 1         | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D1EA76           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 2         | 1     | 0    | DIMM_A2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7CJR4N-VK     | 834C1058           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 3         | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D1EA78           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 4         | 1     | 0    | DIMM_B2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E4EC           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | X     | 5         | 1     | 0    | DIMM_C1    |          | unspecified |         | undiscovered | undiscovered | HMA84GR7CJR4N-VK     | 834C1058           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-3           | X     | 6         | 1     | 0    | DIMM_C2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-3           | V     | 7         | 1     | 0    | DIMM_D1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76D6F2           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 8         | 1     | 0    | DIMM_D2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E525           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 9         | 1     | 0    | DIMM_E1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E38B           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 10        | 1     | 0    | DIMM_E2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E4CD           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | X     | 11        | 1     | 0    | DIMM_F1    |          | unspecified |         | undiscovered | undiscovered | 36ASF4G72PZ-2G6E1    | 3C76E26F           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-3           | X     | 12        | 1     | 0    | DIMM_F2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-3           | V     | 13        | 1     | 1    | DIMM_G1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D204C6           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 14        | 1     | 1    | DIMM_G2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7CJR4N-VK     | 834C100D           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 15        | 1     | 1    | DIMM_H1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D204C5           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 16        | 1     | 1    | DIMM_H2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76DBCB           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | X     | 17        | 1     | 0    | DIMM_J1    |          | unspecified |         | undiscovered | undiscovered | HMA84GR7CJR4N-VK     | 834C100D           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-3           | X     | 18        | 1     | 0    | DIMM_J2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-3           | V     | 19        | 1     | 1    | DIMM_K1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76DC03           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 20        | 1     | 1    | DIMM_K2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E25A           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 21        | 1     | 1    | DIMM_L1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E26D           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | V     | 22        | 1     | 1    | DIMM_L2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76DB69           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-3           | X     | 23        | 1     | 0    | DIMM_M1    |          | unspecified |         | undiscovered | undiscovered | 36ASF4G72PZ-2G6E1    | 3C76E25A           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-3           | X     | 24        | 1     | 0    | DIMM_M2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-4           | V     | 1         | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D204CD           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 2         | 1     | 0    | DIMM_A2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7CJR4N-VK     | 834C0F1E           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 3         | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D1FA05           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 4         | 1     | 0    | DIMM_B2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76DBCA           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | X     | 5         | 1     | 0    | DIMM_C1    |          | unspecified |         | undiscovered | undiscovered | HMA84GR7CJR4N-VK     | 834C0F1E           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-4           | X     | 6         | 1     | 0    | DIMM_C2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-4           | V     | 7         | 1     | 0    | DIMM_D1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76D9A6           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 8         | 1     | 0    | DIMM_D2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E264           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 9         | 1     | 0    | DIMM_E1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E24D           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 10        | 1     | 0    | DIMM_E2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E26F           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | X     | 11        | 1     | 0    | DIMM_F1    |          | unspecified |         | undiscovered | undiscovered | 36ASF4G72PZ-2G6E1    | 3C76E264           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-4           | X     | 12        | 1     | 0    | DIMM_F2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-4           | V     | 13        | 1     | 1    | DIMM_G1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D204CA           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 14        | 1     | 1    | DIMM_G2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | HMA84GR7CJR4N-VK     | 834C0F25           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 15        | 1     | 1    | DIMM_H1    | 32 [GiB] | 2933        | 0.3 ns  | DIMM         | DDR4         | M393A4K40CB2-CVF     | 14D203DF           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 16        | 1     | 1    | DIMM_H2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E535           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | X     | 17        | 1     | 0    | DIMM_J1    |          | unspecified |         | undiscovered | undiscovered | HMA84GR7CJR4N-VK     | 834C0F25           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-4           | X     | 18        | 1     | 0    | DIMM_J2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-4           | V     | 19        | 1     | 1    | DIMM_K1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76DC22           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 20        | 1     | 1    | DIMM_K2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E036           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 21        | 1     | 1    | DIMM_L1    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E28A           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | V     | 22        | 1     | 1    | DIMM_L2    | 32 [GiB] | 2666        | 0.4 ns  | DIMM         | DDR4         | 36ASF4G72PZ-2G6E1    | 3C76E52E           | operable   | equipped | ok      | 
| FI-ucsb1-eu-spdc-2-4           | X     | 23        | 1     | 0    | DIMM_M1    |          | unspecified |         | undiscovered | undiscovered | 36ASF4G72PZ-2G6E1    | 3C76E036           | removed    | missing  | unknown | 
| FI-ucsb1-eu-spdc-2-4           | X     | 24        | 1     | 0    | DIMM_M2    |          | unspecified |         | undiscovered | undiscovered |                      |                    | removed    | missing  | unknown | 
+--------------------------------+-------+-----------+-------+------+------------+----------+-------------+---------+--------------+--------------+----------------------+--------------------+------------+----------+---------+

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

Network Adapters [#0]
---------------------
None

External Ethernet (MLOM) [#50]
------------------------------

+----------------------+-------------------------------------------+--------------+-------------------+
| Server               | Adapter Dn                                | Interface ID | MAC Address       |
+----------------------+-------------------------------------------+--------------+-------------------+
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-1/ext-eth-1 | 1            | 3c:57:31:a0:e1:94 | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-1/ext-eth-3 | 3            | 3c:57:31:a0:e1:97 | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-1/ext-eth-5 | 5            | 3c:57:31:a0:e1:95 | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-1/ext-eth-7 | 7            | 3c:57:31:a0:e1:9a | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-2/ext-eth-1 | 1            | 3c:57:31:35:bd:18 | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-2/ext-eth-3 | 3            | 3c:57:31:35:bd:1b | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-2/ext-eth-5 | 5            | 3c:57:31:35:bd:19 | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-2/ext-eth-7 | 7            | 3c:57:31:35:bd:1e | 
+----------------------+-------------------------------------------+--------------+-------------------+

Host Ethernet [#76]
-------------------

+--------------------------------+--------------+----------------+-------------------+
| Server                         | Adapter Name | Interface Name | MAC Address       |
+--------------------------------+--------------+----------------+-------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter 3    | eth-1          | 3c:fd:fe:ee:2c:30 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter 3    | eth-2          | 3c:fd:fe:ee:2c:31 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter 6    | eth-1          | 3c:fd:fe:ee:2d:60 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter 6    | eth-2          | 3c:fd:fe:ee:2d:61 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter L    | eth-1          | 5c:71:0d:26:37:b2 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter L    | eth-2          | 5c:71:0d:26:37:b3 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | eth0           | 3C:57:31:CC:0E:46 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | eth1           | 3C:57:31:CC:0E:47 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | eth2           | 3C:57:31:CC:0E:48 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | eth3           | 3C:57:31:CC:0E:49 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter 3    | eth-1          | 3c:fd:fe:ee:2a:4c | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter 3    | eth-2          | 3c:fd:fe:ee:2a:4d | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter 6    | eth-1          | 3c:fd:fe:ee:2d:24 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter 6    | eth-2          | 3c:fd:fe:ee:2d:25 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter L    | eth-1          | 5c:71:0d:26:2b:d2 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter L    | eth-2          | 5c:71:0d:26:2b:d3 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | eth0           | 3C:57:31:CC:14:0A | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | eth1           | 3C:57:31:CC:14:0B | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | eth2           | 3C:57:31:CC:14:0C | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | eth3           | 3C:57:31:CC:14:0D | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter 3    | eth-1          | 3c:fd:fe:ee:2d:28 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter 3    | eth-2          | 3c:fd:fe:ee:2d:29 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter 6    | eth-1          | 3c:fd:fe:ee:2a:dc | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter 6    | eth-2          | 3c:fd:fe:ee:2a:dd | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter L    | eth-1          | 5c:71:0d:26:3b:fe | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter L    | eth-2          | 5c:71:0d:26:3b:ff | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | eth0           | 3C:57:31:CC:0E:6A | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | eth1           | 3C:57:31:CC:0E:6B | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | eth2           | 3C:57:31:CC:0E:6C | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | eth3           | 3C:57:31:CC:0E:6D | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | eth0           | 88:FC:5D:45:4E:BC | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | eth1           | 88:FC:5D:45:4E:BD | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | eth2           | 88:FC:5D:45:4E:BE | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | eth3           | 88:FC:5D:45:4E:BF | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | vic1-i0        | 88:FC:5D:45:4E:C6 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | vic1-i1        | 88:FC:5D:45:4E:C7 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | vic1-vs0       | 88:FC:5D:45:4E:C4 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | vic1-vs1       | 88:FC:5D:45:4E:C5 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | eth0           | 04:BD:97:23:32:90 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | eth1           | 04:BD:97:23:32:91 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | i0             | 04:BD:97:23:32:96 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | i1             | 04:BD:97:23:32:97 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | vs0            | 04:BD:97:23:32:94 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | vs1            | 04:BD:97:23:32:95 | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 1    | ESXi-vSwitch0  | 00:25:B5:00:00:04 | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 1    | EU-SPDC-CDC    | 00:25:B5:CD:03:4F | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 1    | EU-SPDC-CDC22  | 00:25:B5:C2:01:CF | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 1    | Infra_DVS      | 00:25:B5:AA:00:4F | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 2    | EU-SPDC-CDC66  | 00:25:B5:6C:01:DF | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 2    | EU-SPDC-R3DC   | 00:25:B5:3D:02:8F | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 2    | EU-SPDC-R4DC   | 00:25:B5:4D:00:DF | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 2    | EU-SPDC-R7DC   | 00:25:B5:7D:03:BF | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 1    | ESXi-vSwitch0  | 00:25:B5:00:00:05 | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 1    | EU-SPDC-CDC    | 00:25:B5:CD:03:5F | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 1    | EU-SPDC-CDC22  | 00:25:B5:C2:01:AF | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 1    | Infra_DVS      | 00:25:B5:AA:00:5F | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 2    | EU-SPDC-CDC66  | 00:25:B5:6C:01:CF | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 2    | EU-SPDC-R3DC   | 00:25:B5:3D:02:9F | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 2    | EU-SPDC-R4DC   | 00:25:B5:4D:00:CF | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 2    | EU-SPDC-R7DC   | 00:25:B5:7D:02:8F | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 1    | ESXi-vSwitch0  | 00:25:B5:00:00:06 | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 1    | EU-SPDC-CDC    | 00:25:B5:CD:03:2F | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 1    | EU-SPDC-CDC22  | 00:25:B5:C2:00:8F | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 1    | Infra_DVS      | 00:25:B5:AA:00:2F | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 2    | EU-SPDC-CDC66  | 00:25:B5:6C:01:AF | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 2    | EU-SPDC-R3DC   | 00:25:B5:3D:02:6F | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 2    | EU-SPDC-R4DC   | 00:25:B5:4D:00:AF | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 2    | EU-SPDC-R7DC   | 00:25:B5:7D:02:9F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 1    | ESXi-vSwitch0  | 00:25:B5:00:00:07 | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 1    | EU-SPDC-CDC    | 00:25:B5:CD:03:3F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 1    | EU-SPDC-CDC22  | 00:25:B5:C2:00:9F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 1    | Infra_DVS      | 00:25:B5:AA:00:3F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 2    | EU-SPDC-CDC66  | 00:25:B5:6C:00:8F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 2    | EU-SPDC-R3DC   | 00:25:B5:3D:02:7F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 2    | EU-SPDC-R4DC   | 00:25:B5:4D:01:8F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 2    | EU-SPDC-R7DC   | 00:25:B5:7D:02:6F | 
+--------------------------------+--------------+----------------+-------------------+

Host FC [#18]
-------------

+--------------------------------+--------------+----------------+-------------------------+-------------------------+
| Server                         | Adapter Name | Interface Name | WWNN                    | WWPN                    |
+--------------------------------+--------------+----------------+-------------------------+-------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | fc0            | 10:00:3C:57:31:CC:0E:4A | 20:00:3C:57:31:CC:0E:4A | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | fc1            | 10:00:3C:57:31:CC:0E:4B | 20:00:3C:57:31:CC:0E:4B | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | fc2            | 10:00:3C:57:31:CC:0E:4C | 20:00:3C:57:31:CC:0E:4C | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | fc3            | 10:00:3C:57:31:CC:0E:4D | 20:00:3C:57:31:CC:0E:4D | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | fc0            | 10:00:3C:57:31:CC:14:0E | 20:00:3C:57:31:CC:14:0E | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | fc1            | 10:00:3C:57:31:CC:14:0F | 20:00:3C:57:31:CC:14:0F | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | fc2            | 10:00:3C:57:31:CC:14:10 | 20:00:3C:57:31:CC:14:10 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | fc3            | 10:00:3C:57:31:CC:14:11 | 20:00:3C:57:31:CC:14:11 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | fc0            | 10:00:3C:57:31:CC:0E:6E | 20:00:3C:57:31:CC:0E:6E | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | fc1            | 10:00:3C:57:31:CC:0E:6F | 20:00:3C:57:31:CC:0E:6F | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | fc2            | 10:00:3C:57:31:CC:0E:70 | 20:00:3C:57:31:CC:0E:70 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | fc3            | 10:00:3C:57:31:CC:0E:71 | 20:00:3C:57:31:CC:0E:71 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | fc0            | 10:00:88:FC:5D:45:4E:C0 | 20:00:88:FC:5D:45:4E:C0 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | fc1            | 10:00:88:FC:5D:45:4E:C1 | 20:00:88:FC:5D:45:4E:C1 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | fc2            | 10:00:88:FC:5D:45:4E:C2 | 20:00:88:FC:5D:45:4E:C2 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | fc3            | 10:00:88:FC:5D:45:4E:C3 | 20:00:88:FC:5D:45:4E:C3 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | fc0            | 10:00:04:BD:97:23:32:92 | 20:00:04:BD:97:23:32:92 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | fc1            | 10:00:04:BD:97:23:32:93 | 20:00:04:BD:97:23:32:93 | 
+--------------------------------+--------------+----------------+-------------------------+-------------------------+

PCI [#24]
---------

+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| Server                         | PCI Device Model                        | Pid               | Serial      | SlotId     | Vendor            | Firmware                  |
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  |             | 3          | 0x8086            | 0x8000B900-1.826.0        | 
|                                | XXV710-DA2                              |                   |             |            |                   |                           | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  |             | 6          | 0x8086            | 0x8000B900-1.826.0        | 
|                                | XXV710-DA2                              |                   |             |            |                   |                           | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Intel X550 LOM                          | None              |             | L          | 0x8086            | 0x800016F9-1.826.0        | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Cisco UCS VIC 1457 MLOM                 | UCSC-MLOM-C25Q-04 |             | MLOM       | 0x1137            | 5.2(2b)                   | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Cisco 12G Modular Raid Controller with  | UCSC-RAID-M5      |             | MRAID      | 0x1000            | N/A                       | 
|                                | 2GB cache (max 16 drives)               |                   |             |            |                   |                           | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-2-p2b-eu-spdc-WZP23400AK4 | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  |             | 3          | 0x8086            | 0x8000B900-1.826.0        | 
|                                | XXV710-DA2                              |                   |             |            |                   |                           | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-2-p2b-eu-spdc-WZP23400AK4 | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  |             | 6          | 0x8086            | 0x8000B900-1.826.0        | 
|                                | XXV710-DA2                              |                   |             |            |                   |                           | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-2-p2b-eu-spdc-WZP23400AK4 | Intel X550 LOM                          | None              |             | L          | 0x8086            | 0x800016F9-1.826.0        | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-2-p2b-eu-spdc-WZP23400AK4 | Cisco UCS VIC 1457 MLOM                 | UCSC-MLOM-C25Q-04 |             | MLOM       | 0x1137            | 5.2(2b)                   | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-2-p2b-eu-spdc-WZP23400AK4 | Cisco 12G Modular Raid Controller with  | UCSC-RAID-M5      |             | MRAID      | 0x1000            | 51.19.0-4296              | 
|                                | 2GB cache (max 16 drives)               |                   |             |            |                   |                           | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-3-p2b-eu-spdc-WZP23400AKL | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  |             | 3          | 0x8086            | 0x8000CC0F-1.826.0        | 
|                                | XXV710-DA2                              |                   |             |            |                   |                           | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-3-p2b-eu-spdc-WZP23400AKL | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  |             | 6          | 0x8086            | 0x8000CC0F-1.826.0        | 
|                                | XXV710-DA2                              |                   |             |            |                   |                           | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-3-p2b-eu-spdc-WZP23400AKL | Intel X550 LOM                          | NA                |             | L          | 0x8086            | 0x800016F9-1.826.0        | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-3-p2b-eu-spdc-WZP23400AKL | Cisco UCS VIC 1457 MLOM                 | UCSC-MLOM-C25Q-04 |             | MLOM       | 0x1137            | 5.2(3d)                   | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp-3-p2b-eu-spdc-WZP23400AKL | Cisco 12G Modular Raid Controller with  | UCSC-RAID-M5      |             | MRAID      | 0x1000            | 51.19.0-4532              | 
|                                | 2GB cache (max 16 drives)               |                   |             |            |                   |                           | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp3-p4b-eu-spdc-WZP262207UM  | Cisco UCS VIC 1455                      | UCSC-PCIE-C25Q-04 |             | 1          | 0x1137            | 5.2(3f)                   | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp3-p4b-eu-spdc-WZP262207UM  | NVIDIA T4 PCIe 16GB 70W                 | UCSC-GPU-T4-16    |             | 3          | 0x10de            | N/A                       | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp3-p4b-eu-spdc-WZP262207UM  | Cisco UCS VIC 1477 MLOM                 | UCSC-M-V100-04    |             | MLOM       | 0x1137            | 5.2(3f)                   | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp3-p4b-eu-spdc-WZP262207UM  | Cisco 12G SAS RAID Controller with 4GB  | UCSC-RAID-M6T     |             | MRAID      | 0x1000            | 52.20.0-4523              | 
|                                | FBWC (16 Drives)                        |                   |             |            |                   |                           | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| comp3-p4b-eu-spdc-WZP262207UM  | Cisco Boot optimized M.2 Raid           | UCS-M2-HWRAID     |             | MSTOR-RAID | 0x1b4b            | N/A                       | 
|                                | controller                              |                   |             |            |                   |                           | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| FI-ucsb1-eu-spdc-2-1           | UCSB-MRAID12G-HE                        | UCSB-MRAID12G-HE  | LSK23300055 | FMEZZ1-SAS | Cisco Systems Inc | 24.21.0-0156|6.36.00.3|NA | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| FI-ucsb1-eu-spdc-2-2           | UCSB-MRAID12G-HE                        | UCSB-MRAID12G-HE  | LSK2328027N | FMEZZ1-SAS | Cisco Systems Inc | 24.21.0-0156|6.36.00.3|NA | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| FI-ucsb1-eu-spdc-2-3           | UCSB-MRAID12G-HE                        | UCSB-MRAID12G-HE  | LSK232903L8 | FMEZZ1-SAS | Cisco Systems Inc | 24.21.0-0156|6.36.00.3|NA | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+
| FI-ucsb1-eu-spdc-2-4           | UCSB-MRAID12G-HE                        | UCSB-MRAID12G-HE  | LSK232903Q4 | FMEZZ1-SAS | Cisco Systems Inc | 24.21.0-0156|6.36.00.3|NA | 
+--------------------------------+-----------------------------------------+-------------------+-------------+------------+-------------------+---------------------------+

Fan Module [#29]
----------------

+--------------------------------+-------+--------------+-----------+----------+
| Server                         | State | Fan Module   | OperState | Presence |
+--------------------------------+-------+--------------+-----------+----------+
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 3 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 4 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 5 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 6 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | Fan Module 7 | unknown   | missing  | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 3 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 4 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 5 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 6 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | Fan Module 7 | unknown   | missing  | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 3 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 4 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 5 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 6 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | Fan Module 7 | unknown   | missing  | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 3 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 4 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 5 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 6 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | Fan Module 7 | unknown   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | Fan Module 8 | unknown   | equipped | 
+--------------------------------+-------+--------------+-----------+----------+

Fan [#58]
---------

+--------------------------------+-------+----------------------+-----------+----------+
| Server                         | State | Fan                  | OperState | Presence |
+--------------------------------+-------+----------------------+-----------+----------+
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 1 - Fan 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 1 - Fan 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 2 - Fan 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 2 - Fan 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 3 - Fan 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 3 - Fan 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 4 - Fan 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 4 - Fan 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 5 - Fan 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 5 - Fan 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 6 - Fan 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 6 - Fan 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | Fan Module 7 - Fan 1 | unknown   | missing  | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | Fan Module 7 - Fan 2 | unknown   | missing  | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 1 - Fan 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 1 - Fan 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 2 - Fan 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 2 - Fan 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 3 - Fan 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 3 - Fan 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 4 - Fan 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 4 - Fan 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 5 - Fan 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 5 - Fan 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 6 - Fan 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 6 - Fan 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | Fan Module 7 - Fan 1 | unknown   | missing  | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | Fan Module 7 - Fan 2 | unknown   | missing  | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 1 - Fan 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 1 - Fan 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 2 - Fan 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 2 - Fan 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 3 - Fan 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 3 - Fan 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 4 - Fan 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 4 - Fan 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 5 - Fan 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 5 - Fan 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 6 - Fan 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 6 - Fan 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | Fan Module 7 - Fan 1 | unknown   | missing  | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | Fan Module 7 - Fan 2 | unknown   | missing  | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 1 - Fan 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 1 - Fan 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 2 - Fan 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 2 - Fan 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 3 - Fan 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 3 - Fan 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 4 - Fan 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 4 - Fan 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 5 - Fan 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 5 - Fan 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 6 - Fan 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 6 - Fan 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | Fan Module 7 - Fan 1 | unknown   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | Fan Module 7 - Fan 2 | unknown   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | Fan Module 8 - Fan 1 | unknown   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | Fan Module 8 - Fan 2 | unknown   | equipped | 
+--------------------------------+-------+----------------------+-----------+----------+

PSU [#8]
--------

+--------------------------------+--------+-------+---------+---------+---------------+-------------+-------------------+
| Server                         | Name   | State | Present | Voltage | Model         | Serial      | Vendor            |
+--------------------------------+--------+-------+---------+---------+---------------+-------------+-------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | LIT241244MU | Cisco Systems Inc | 
| comp-1-p2b-eu-spdc-WZP23400AJW | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | LIT241244Z5 | Cisco Systems Inc | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | LIT241244RQ | Cisco Systems Inc | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | LIT241242TS | Cisco Systems Inc | 
| comp-3-p2b-eu-spdc-WZP23400AKL | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | LIT241244NV | Cisco Systems Inc | 
| comp-3-p2b-eu-spdc-WZP23400AKL | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | LIT241244UN | Cisco Systems Inc | 
| comp3-p4b-eu-spdc-WZP262207UM  | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | LIT2625AJTW | Cisco Systems Inc | 
| comp3-p4b-eu-spdc-WZP262207UM  | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | LIT2625AHMD | Cisco Systems Inc | 
+--------------------------------+--------+-------+---------+---------+---------------+-------------+-------------------+

Trusted Platform Module [#4]
----------------------------

+--------------------------------+----------+-------------------+-------------+---------+------------------+-------------------+-------------+------------------+
| Server                         | TPM      | Activation Status | Admin State | Version | Model            | Vendor            | Serial      | Firmware Version |
+--------------------------------+----------+-------------------+-------------+---------+------------------+-------------------+-------------+------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | empty    | unknown           | unknown     | NA      | NA               | NA                | NA          | NA               | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | empty    | unknown           | unknown     | NA      | NA               | NA                | NA          | NA               | 
| comp-3-p2b-eu-spdc-WZP23400AKL | empty    | unknown           | unknown     | NA      | NA               | NA                | NA          | NA               | 
| comp3-p4b-eu-spdc-WZP262207UM  | equipped | activated         | enabled     | 2.0     | UCSX-TPM2-002B-C | Cisco Systems Inc | FCH262076M1 | 7.85             | 
+--------------------------------+----------+-------------------+-------------+---------+------------------+-------------------+-------------+------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v hw

{
    "duration": 32677,
    "isctl": {
        "read": true,
        "calls": 15,
        "success": 15,
        "failed": 0,
        "total_time": 28767
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
        "lines": 135
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:23:03.857129	True	5510	100	isctl get compute rackunit  --expand "PciDevices,Psus,Fanmodules" -o json --top 100
2023-12-03 15:23:05.690355	True	1826	9	isctl get compute rackunit  --expand "PciDevices,Psus,Fanmodules" -o json --top 100 --skip 100
2023-12-03 15:23:07.411805	True	1438	12	isctl get compute blade  --expand "PciDevices" -o json --top 100
2023-12-03 15:23:09.141010	True	1693	4	isctl get compute board --filter "ComputeRackUnit/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5')" --expand "Processors" -o json --top 100
2023-12-03 15:23:10.810044	True	1650	4	isctl get compute board --filter "ComputeBlade/Moid in ('6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')" --expand "Processors" -o json --top 100
2023-12-03 15:23:12.542498	True	1694	40	isctl get equipment fan --filter "Parent/Moid in ('5fdf9c106176752d35e44d71', '5fdf9c106176752d35e44d73', '5fdf9c106176752d35e44d75', '5fdf9c106176752d35e44d77', '5fdf9c106176752d35e44d79', '5fdf9c106176752d35e44d7b', '5fdf9c106176752d35e44d7d', '5fdf9c876176752d35e4777c', '5fdf9c876176752d35e4777e', '5fdf9c876176752d35e47780', '5fdf9c876176752d35e47782', '5fdf9c876176752d35e47784', '5fdf9c876176752d35e47786', '5fdf9c876176752d35e47788', '5fdf9d116176752d35e4b355', '5fdf9d116176752d35e4b357', '5fdf9d116176752d35e4b359', '5fdf9d116176752d35e4b35b', '5fdf9d116176752d35e4b35d', '5fdf9d116176752d35e4b35f')"  -o json --top 100
2023-12-03 15:23:14.000388	True	1444	18	isctl get equipment fan --filter "Parent/Moid in ('5fdf9d116176752d35e4b361', '638501f176752d313964c5c6', '638501f176752d313964c5c8', '638501f176752d313964c5ca', '638501f176752d313964c5cc', '638501f176752d313964c5ce', '638501f176752d313964c5d0', '638501f176752d313964c5d2', '638501f176752d313964c5d4')"  -o json --top 100
2023-12-03 15:23:15.902026	True	1869	100	isctl get memory unit --filter "MemoryArray/Moid in ('5fdf9c416176752d35e45e6f', '5fdf9cb86176752d35e48ede', '5fdf9d436176752d35e4c6a5', '638501f276752d313964c605', '6501db4c76752d3901eb3945', '6501db4c76752d3901eb3833', '6501db4d76752d3901eb39a9', '6501db4d76752d3901eb3993')"  -o json --top 100
2023-12-03 15:23:17.553247	True	1617	100	isctl get memory unit --filter "MemoryArray/Moid in ('5fdf9c416176752d35e45e6f', '5fdf9cb86176752d35e48ede', '5fdf9d436176752d35e4c6a5', '638501f276752d313964c605', '6501db4c76752d3901eb3945', '6501db4c76752d3901eb3833', '6501db4d76752d3901eb39a9', '6501db4d76752d3901eb3993')"  -o json --top 100 --skip 100
2023-12-03 15:23:19.024872	True	1424	0	isctl get memory unit --filter "MemoryArray/Moid in ('5fdf9c416176752d35e45e6f', '5fdf9cb86176752d35e48ede', '5fdf9d436176752d35e4c6a5', '638501f276752d313964c605', '6501db4c76752d3901eb3945', '6501db4c76752d3901eb3833', '6501db4d76752d3901eb39a9', '6501db4d76752d3901eb3993')"  -o json --top 100 --skip 200
2023-12-03 15:23:21.021415	True	1904	20	isctl get adapter unit --filter "Moid in ('5fdf9bf46176752d35e4426e', '5fdf9c886176752d35e477e4', '5fdf9c886176752d35e477ea', '5fdf9c886176752d35e477f0', '5fdf9c6b6176752d35e46d1c', '5fdf9cfe6176752d35e4aa7f', '5fdf9cfe6176752d35e4aa85', '5fdf9cfe6176752d35e4aa8b', '5fdf9cf56176752d35e4a70f', '5fdf9d896176752d35e4e0b6', '5fdf9d896176752d35e4e0bc', '5fdf9d896176752d35e4e0c2', '6385018c76752d313964b35d', '6385018c76752d313964b35f', '6501db4c76752d3901eb3813', '6501db4c76752d3901eb3864', '6501db4c76752d3901eb381b', '6501db4d76752d3901eb3976', '6501db4e76752d3901eb3b32', '6501db4e76752d3901eb3b59')" --expand "ExtEthIfs,HostEthIfs,HostFcIfs" -o json --top 100
2023-12-03 15:23:22.777410	True	1675	2	isctl get adapter unit --filter "Moid in ('6501db4d76752d3901eb3972', '6501db4f76752d3901eb3c71')" --expand "ExtEthIfs,HostEthIfs,HostFcIfs" -o json --top 100
2023-12-03 15:23:24.897378	True	1939	16	isctl get storage controller --filter "Parent/Moid in ('5fdf9c056176752d35e44930', '5fdf9c7c6176752d35e472bd', '5fdf9d066176752d35e4aebe', '6385021176752d313964cbe0', '6501db4c76752d3901eb3890', '6501db4c76752d3901eb381d', '6501db4c76752d3901eb3882', '6501db4c76752d3901eb38a9')" --expand "PhysicalDisks,VirtualDrives" -o json --top 100
2023-12-03 15:23:26.585791	True	1507	8	isctl get storage physicaldiskusage --filter "StorageVirtualDrive/Moid in ('638f666f76752d3139f6cc14', '638fcd2976752d313909b32e', '617917b976752d3139754146', '65438f6a76752d3901322928', '6501db5276752d3901eb4051', '6501db5076752d3901eb3e4a', '6501db4f76752d3901eb3cee', '6501db5176752d3901eb3f14')"  -o json --top 100
2023-12-03 15:23:28.292258	True	1577	4	isctl get equipment tpm --filter "Moid in ('5fdf9c186176752d35e4503a', '5fdf9c8f6176752d35e47b82', '5fdf9d196176752d35e4b797', '638501fa76752d313964c6f7')"  -o json --top 100
```

[[Back]](./ServerInventory.md)