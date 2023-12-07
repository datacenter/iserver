# Cisco PSIRT

## Filter by prod

```
# iserver get psirt --prod *aci* --sev high --updated 700

Advisory [#6]
-------------

+------+-------+------------------------------------------+------------+----------------+---------+---------------------------------------------+--------+--------+
| Sev  | Final | Title                                    | Bug        | CVE            | CWE     | Product                                     | Add    | Update |
+------+-------+------------------------------------------+------------+----------------+---------+---------------------------------------------+--------+--------+
| High | V     | Cisco ACI Multi-Site CloudSec            | CSCwf02544 | CVE-2023-20185 | CWE-330 | Cisco NX-OS System Software in ACI Mode     | 155d   | 152d   | 
|      |       | Encryption Information Disclosure        |            |                |         |                                             |        |        | 
|      |       | Vulnerability                            |            |                |         |                                             |        |        | 
+------+-------+------------------------------------------+------------+----------------+---------+---------------------------------------------+--------+--------+
| High | V     | Cisco Nexus 9000 Series Fabric Switches  | CSCwc23246 | CVE-2023-20089 | CWE-789 | Cisco NX-OS System Software in ACI Mode     | 288d   | 288d   | 
|      |       | in ACI Mode Link Layer Discovery         |            |                |         |                                             |        |        | 
|      |       | Protocol Memory Leak Denial of Service   |            |                |         |                                             |        |        | 
|      |       | Vulnerability                            |            |                |         |                                             |        |        | 
+------+-------+------------------------------------------+------------+----------------+---------+---------------------------------------------+--------+--------+
| High | V     | Cisco NX-OS Software OSPFv3 Denial of    | CSCvz68748 | CVE-2022-20823 | CWE-126 | Cisco NX-OS System Software in ACI Mode     | 1y105d | 1y105d | 
|      |       | Service Vulnerability                    | CSCwb50012 |                |         |                                             |        |        | 
|      |       |                                          | CSCwb50013 |                |         |                                             |        |        | 
|      |       |                                          | CSCwb50015 |                |         |                                             |        |        | 
+------+-------+------------------------------------------+------------+----------------+---------+---------------------------------------------+--------+--------+
| High | V     | Cisco FXOS and NX-OS Software Cisco      | CSCwb70210 | CVE-2022-20824 | CWE-121 | Cisco NX-OS System Software in ACI Mode     | 1y105d | 1y105d | 
|      |       | Discovery Protocol Denial of Service     | CSCwb74493 |                |         |                                             |        |        | 
|      |       | and Arbitrary Code Execution             | CSCwb74494 |                |         |                                             |        |        | 
|      |       | Vulnerability                            | CSCwb74495 |                |         |                                             |        |        | 
|      |       |                                          | CSCwb74496 |                |         |                                             |        |        | 
|      |       |                                          | CSCwb74497 |                |         |                                             |        |        | 
|      |       |                                          | CSCwb74498 |                |         |                                             |        |        | 
|      |       |                                          | CSCwb74513 |                |         |                                             |        |        | 
+------+-------+------------------------------------------+------------+----------------+---------+---------------------------------------------+--------+--------+
| High | V     | Cisco ACI Multi-Site Orchestrator        | CSCwb95851 | CVE-2022-20921 | CWE-285 | Cisco ACI Multi-Site Orchestrator Software  | 1y105d | 1y105d | 
|      |       | Privilege Escalation Vulnerability       |            |                |         |                                             |        |        | 
+------+-------+------------------------------------------+------------+----------------+---------+---------------------------------------------+--------+--------+
| High | V     | Cisco Nexus 9000 Series Fabric Switches  | CSCvw87983 | CVE-2021-1586  | CWE-345 | Cisco NX-OS System Software in ACI Mode     | 2y104d | 1y287d | 
|      |       | ACI Mode Multi-Pod and Multi-Site TCP    | CSCvz75847 |                |         |                                             |        |        | 
|      |       | Denial of Service Vulnerability          |            |                |         |                                             |        |        | 
+------+-------+------------------------------------------+------------+----------------+---------+---------------------------------------------+--------+--------+

Filter: sev, bug, cve, cwe, prod, ver, added, updated
View:   list (def), url, sum, ver, all
```

[[Back]](./README.md)