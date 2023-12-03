# Intersight Server

## mem view

```
# iserver get server --group test -v mem

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


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

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v mem

{
    "duration": 24648,
    "isctl": {
        "read": true,
        "calls": 8,
        "success": 8,
        "failed": 0,
        "total_time": 22242
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
        "lines": 26
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:25:56.952278	True	2829	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:26:00.362170	True	3407	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:26:04.245581	True	3742	12	isctl get compute blade   -o json --top 100
2023-12-03 15:26:07.898736	True	3613	4	isctl get compute board --filter "ComputeRackUnit/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5')"  -o json --top 100
2023-12-03 15:26:10.249158	True	2337	4	isctl get compute board --filter "ComputeBlade/Moid in ('6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
2023-12-03 15:26:12.176222	True	1910	100	isctl get memory unit --filter "MemoryArray/Moid in ('5fdf9c416176752d35e45e6f', '5fdf9cb86176752d35e48ede', '5fdf9d436176752d35e4c6a5', '638501f276752d313964c605', '6501db4c76752d3901eb3945', '6501db4c76752d3901eb3833', '6501db4d76752d3901eb39a9', '6501db4d76752d3901eb3993')"  -o json --top 100
2023-12-03 15:26:14.551900	True	2350	100	isctl get memory unit --filter "MemoryArray/Moid in ('5fdf9c416176752d35e45e6f', '5fdf9cb86176752d35e48ede', '5fdf9d436176752d35e4c6a5', '638501f276752d313964c605', '6501db4c76752d3901eb3945', '6501db4c76752d3901eb3833', '6501db4d76752d3901eb39a9', '6501db4d76752d3901eb3993')"  -o json --top 100 --skip 100
2023-12-03 15:26:16.675047	True	2054	0	isctl get memory unit --filter "MemoryArray/Moid in ('5fdf9c416176752d35e45e6f', '5fdf9cb86176752d35e48ede', '5fdf9d436176752d35e4c6a5', '638501f276752d313964c605', '6501db4c76752d3901eb3945', '6501db4c76752d3901eb3833', '6501db4d76752d3901eb39a9', '6501db4d76752d3901eb3993')"  -o json --top 100 --skip 200
```

[[Back]](./ServerInventory.md)