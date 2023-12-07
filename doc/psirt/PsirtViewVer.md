# Cisco PSIRT

## ver view

```
# iserver get psirt --prod *aci* --sev high -v ver

Advisory - Product Version [#2]
-------------------------------

+------+-------+------------------------------------------+------------+----------------+---------+--------------------------------------------------+------+--------+
| Sev  | Final | Title                                    | Bug        | CVE            | CWE     | Product                                          | Add  | Update |
+------+-------+------------------------------------------+------------+----------------+---------+--------------------------------------------------+------+--------+
| High | V     | Cisco ACI Multi-Site CloudSec            | CSCwf02544 | CVE-2023-20185 | CWE-330 | Cisco NX-OS System Software in ACI Mode 14.0(1h) | 155d | 152d   | 
|      |       | Encryption Information Disclosure        |            |                |         | Cisco NX-OS System Software in ACI Mode 14.0(2c) |      |        | 
|      |       | Vulnerability                            |            |                |         | Cisco NX-OS System Software in ACI Mode 14.0(3d) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.0(3c) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.1(1i) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.1(1j) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.1(1k) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.1(1l) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.1(2g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.1(2m) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.1(2o) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.1(2s) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.1(2u) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.1(2w) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.1(2x) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(1i) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(1j) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(1l) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(2e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(2f) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(2g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(3j) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(3l) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(3n) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(3q) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(4i) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(4k) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(4o) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(4p) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(5k) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(5l) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(5n) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(6d) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(6g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(6h) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(6l) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(7f) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(7l) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(6o) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(7q) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(7r) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(7s) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(7t) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(7u) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(7v) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 14.2(7w) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.0(1k) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.0(1l) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.0(2e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.0(2h) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.1(1h) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.1(2e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.1(3e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.1(4c) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(1g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(2e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(2f) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(2g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(2h) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(3e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(3f) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(3g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(4d) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(4e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(5c) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(5d) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(5e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(4f) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(6e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(6g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(7f) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(7g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(6h) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(8d) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(8e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(8f) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(8g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 16.0(1g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 16.0(1j) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 16.0(2h) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 16.0(2j) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 16.0(3d) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 16.0(3e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.3(1d) |      |        | 
+------+-------+------------------------------------------+------------+----------------+---------+--------------------------------------------------+------+--------+
| High | V     | Cisco Nexus 9000 Series Fabric Switches  | CSCwc23246 | CVE-2023-20089 | CWE-789 | Cisco NX-OS System Software in ACI Mode 15.2(1g) | 288d | 288d   | 
|      |       | in ACI Mode Link Layer Discovery         |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(2e) |      |        | 
|      |       | Protocol Memory Leak Denial of Service   |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(2f) |      |        | 
|      |       | Vulnerability                            |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(2g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(2h) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(3e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(3f) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(3g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(4d) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(4e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(5c) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(5d) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(5e) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 15.2(4f) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 16.0(1g) |      |        | 
|      |       |                                          |            |                |         | Cisco NX-OS System Software in ACI Mode 16.0(1j) |      |        | 
+------+-------+------------------------------------------+------------+----------------+---------+--------------------------------------------------+------+--------+

Filter: sev, bug, cve, cwe, prod, ver, added, updated
View:   list (def), url, sum, ver, all
```

[[Back]](./README.md)