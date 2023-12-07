# Cisco PSIRT

## Default output

```
# iserver get psirt --prod *aci* --sev high

Advisory [#2]
-------------

+------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------+------+--------+
| Sev  | Final | Title                                    | Bug        | CVE            | CWE     | Product                                 | Add  | Update |
+------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------+------+--------+
| High | V     | Cisco ACI Multi-Site CloudSec            | CSCwf02544 | CVE-2023-20185 | CWE-330 | Cisco NX-OS System Software in ACI Mode | 155d | 152d   | 
|      |       | Encryption Information Disclosure        |            |                |         |                                         |      |        | 
|      |       | Vulnerability                            |            |                |         |                                         |      |        | 
+------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------+------+--------+
| High | V     | Cisco Nexus 9000 Series Fabric Switches  | CSCwc23246 | CVE-2023-20089 | CWE-789 | Cisco NX-OS System Software in ACI Mode | 288d | 288d   | 
|      |       | in ACI Mode Link Layer Discovery         |            |                |         |                                         |      |        | 
|      |       | Protocol Memory Leak Denial of Service   |            |                |         |                                         |      |        | 
|      |       | Vulnerability                            |            |                |         |                                         |      |        | 
+------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------+------+--------+

Filter: sev, bug, cve, cwe, prod, ver, added, updated
View:   list (def), url, sum, ver, all
```

[[Back]](./README.md)