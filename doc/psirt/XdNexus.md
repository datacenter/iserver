# NX-OS

## Cisco PSIRT

This feature gets the vulnerabilities in the context of specific Nexus device or group of devices (aka domain).

Make sure the devices is [defined](../nexus/Device.md) or provide full access details in the command options.

```
# iserver get nx psirt --device ipn11

Device: ipn11

Advisory - Apic: ipn11 version 9.3(9)
-------------------------------------

+--------+-------+-----------------------------------------+------------+----------------+---------+-----------------------------------------+--------+--------+
| Sev    | Final | Title                                   | Bug        | CVE            | CWE     | Product                                 | Add    | Update |
+--------+-------+-----------------------------------------+------------+----------------+---------+-----------------------------------------+--------+--------+
| Medium | V     | Cisco Nexus 3000 and 9000 Series        | CSCwe47138 | CVE-2023-20115 | CWE-671 | Cisco NX-OS Software 9.3(9)             | 106d   | 106d   | 
|        |       | Switches SFTP Server File Access        |            |                |         |                                         |        |        | 
|        |       | Vulnerability                           |            |                |         |                                         |        |        | 
+--------+-------+-----------------------------------------+------------+----------------+---------+-----------------------------------------+--------+--------+
| High   | V     | Cisco NX-OS Software TACACS+ or RADIUS  | CSCwe72368 | CVE-2023-20168 | CWE-120 | Cisco NX-OS Software 9.3(9)             | 106d   | 106d   | 
|        |       | Remote Authentication Directed Request  | CSCwe72648 |                |         |                                         |        |        | 
|        |       | Denial of Service Vulnerability         | CSCwe72670 |                |         |                                         |        |        | 
|        |       |                                         | CSCwe72673 |                |         |                                         |        |        | 
|        |       |                                         | CSCwe72674 |                |         |                                         |        |        | 
+--------+-------+-----------------------------------------+------------+----------------+---------+-----------------------------------------+--------+--------+
| Medium | V     | Cisco NX-OS Software CLI Command        | CSCwd00653 | CVE-2023-20050 | CWE-78  | Cisco NX-OS Software 9.3(9)             | 288d   | 288d   | 
|        |       | Injection Vulnerability                 | CSCwd18009 |                |         |                                         |        |        | 
|        |       |                                         | CSCwd18011 |                |         |                                         |        |        | 
|        |       |                                         | CSCwd18012 |                |         |                                         |        |        | 
|        |       |                                         | CSCwd18013 |                |         |                                         |        |        | 
+--------+-------+-----------------------------------------+------------+----------------+---------+-----------------------------------------+--------+--------+
| High   | V     | Cisco FXOS and NX-OS Software Cisco     | CSCwb70210 | CVE-2022-20824 | CWE-121 | Cisco NX-OS Software 9.3(9)             | 1y105d | 1y105d | 
|        |       | Discovery Protocol Denial of Service    | CSCwb74493 |                |         | Cisco NX-OS System Software in ACI Mode |        |        | 
|        |       | and Arbitrary Code Execution            | CSCwb74494 |                |         |                                         |        |        | 
|        |       | Vulnerability                           | CSCwb74495 |                |         |                                         |        |        | 
|        |       |                                         | CSCwb74496 |                |         |                                         |        |        | 
|        |       |                                         | CSCwb74497 |                |         |                                         |        |        | 
|        |       |                                         | CSCwb74498 |                |         |                                         |        |        | 
|        |       |                                         | CSCwb74513 |                |         |                                         |        |        | 
+--------+-------+-----------------------------------------+------------+----------------+---------+-----------------------------------------+--------+--------+
```

[[Back]](./README.md)