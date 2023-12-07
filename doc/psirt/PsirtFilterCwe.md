# Cisco PSIRT

## Filter by cwe

```
# iserver get psirt --cwe *-120

Advisory [#5]
-------------

+----------+-------+-----------------------------------------+------------+----------------+---------+----------------------------------------------------------------+--------+--------+
| Sev      | Final | Title                                   | Bug        | CVE            | CWE     | Product                                                        | Add    | Update |
+----------+-------+-----------------------------------------+------------+----------------+---------+----------------------------------------------------------------+--------+--------+
| High     | V     | Cisco NX-OS Software TACACS+ or RADIUS  | CSCwe72368 | CVE-2023-20168 | CWE-120 | Cisco NX-OS Software                                           | 106d   | 106d   | 
|          |       | Remote Authentication Directed Request  | CSCwe72648 |                |         |                                                                |        |        | 
|          |       | Denial of Service Vulnerability         | CSCwe72670 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwe72673 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwe72674 |                |         |                                                                |        |        | 
+----------+-------+-----------------------------------------+------------+----------------+---------+----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco Small Business Series Switches    | CSCwe27386 | CVE-2023-20024 | CWE-120 | Cisco Small Business Smart and Managed Switches                | 204d   | 204d   | 
|          |       | Buffer Overflow Vulnerabilities         | CSCwe27393 | CVE-2023-20156 | CWE-121 |                                                                |        |        | 
|          |       |                                         | CSCwe27394 | CVE-2023-20157 | CWE-122 |                                                                |        |        | 
|          |       |                                         | CSCwe27403 | CVE-2023-20158 | CWE-200 |                                                                |        |        | 
|          |       |                                         | CSCwe27424 | CVE-2023-20159 | CWE-787 |                                                                |        |        | 
|          |       |                                         | CSCwe27425 | CVE-2023-20160 |         |                                                                |        |        | 
|          |       |                                         | CSCwe27441 | CVE-2023-20161 |         |                                                                |        |        | 
|          |       |                                         | CSCwe27444 | CVE-2023-20162 |         |                                                                |        |        | 
|          |       |                                         | CSCwe27445 | CVE-2023-20189 |         |                                                                |        |        | 
|          |       |                                         | CSCwe32312 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwe32313 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwe32315 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwe32318 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwe32321 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwe32323 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwe32326 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwe32334 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwe32338 |                |         |                                                                |        |        | 
+----------+-------+-----------------------------------------+------------+----------------+---------+----------------------------------------------------------------+--------+--------+
| Critical | V     | ClamAV HFS+ Partition Scanning Buffer   | CSCwd74132 | CVE-2023-20032 | CWE-120 | Cisco Secure Web Appliance                                     | 295d   | 288d   | 
|          |       | Overflow Vulnerability Affecting Cisco  | CSCwd74133 |                |         | Cisco Secure Endpoint                                          |        |        | 
|          |       | Products: February 2023                 | CSCwd74134 |                |         | Cisco Secure Endpoint Private Cloud Administration Portal      |        |        | 
|          |       |                                         | CSCwd74135 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwe18204 |                |         |                                                                |        |        | 
+----------+-------+-----------------------------------------+------------+----------------+---------+----------------------------------------------------------------+--------+--------+
| Critical | V     | Vulnerability in Spring Framework       | CSCvv65984 | CVE-2022-22965 | CWE-120 | Cisco Emergency Responder                                      | 1y249d | 301d   | 
|          |       | Affecting Cisco Products: March 2022    | CSCwa79849 |                |         | Cisco Unity Connection                                         |        |        | 
|          |       |                                         | CSCwb43327 |                |         | Cisco Unified Communications Manager                           |        |        | 
|          |       |                                         | CSCwb43328 |                |         | Cisco Unified Communications Manager IM and Presence Service   |        |        | 
|          |       |                                         | CSCwb43331 |                |         | Cisco Prime License Manager                                    |        |        | 
|          |       |                                         | CSCwb43332 |                |         | Cisco Prime Collaboration Deployment                           |        |        | 
|          |       |                                         | CSCwb43335 |                |         | Cisco Firepower Management Center                              |        |        | 
|          |       |                                         | CSCwb43340 |                |         | Cisco Evolved Programmable Network Manager (EPNM)              |        |        | 
|          |       |                                         | CSCwb43342 |                |         | Cisco Firepower Threat Defense Software                        |        |        | 
|          |       |                                         | CSCwb43345 |                |         | Cisco IoT Field Network Director (IoT-FND)                     |        |        | 
|          |       |                                         | CSCwb43346 |                |         | Cisco HyperFlex HX Data Platform                               |        |        | 
|          |       |                                         | CSCwb43734 |                |         | Cisco Unified Communications Manager / Cisco Unity Connection  |        |        | 
|          |       |                                         | CSCwb43736 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwb43738 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwb43739 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwb44794 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwb69766 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwb70105 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwb84370 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwc96587 |                |         |                                                                |        |        | 
|          |       |                                         | CSCwd75689 |                |         |                                                                |        |        | 
+----------+-------+-----------------------------------------+------------+----------------+---------+----------------------------------------------------------------+--------+--------+
| Medium   | V     | Cisco RV340, RV340W, RV345, and RV345P  | CSCwc84443 | CVE-2023-20007 | CWE-120 | Cisco Small Business RV Series Router Firmware                 | 330d   | 329d   | 
|          |       | Dual WAN Gigabit VPN Routers Remote     |            |                |         |                                                                |        |        | 
|          |       | Code Execution and Denial of Service    |            |                |         |                                                                |        |        | 
|          |       | Vulnerability                           |            |                |         |                                                                |        |        | 
+----------+-------+-----------------------------------------+------------+----------------+---------+----------------------------------------------------------------+--------+--------+

Filter: sev, bug, cve, cwe, prod, ver, added, updated
View:   list (def), url, sum, ver, all
```

[[Back]](./README.md)