# Cisco PSIRT

## Filter by sev

```
# iserver get psirt --sev crit

Advisory [#21]
--------------

+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Sev      | Final | Title                                    | Bug        | CVE            | CWE     | Product                                                         | Add    | Update |
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco Firepower Management Center        | CSCwd02925 | CVE-2023-20048 | CWE-269 | Cisco Firepower Management Center                               | 36d    | 36d    | 
|          |       | Software Command Injection               |            |                |         |                                                                 |        |        | 
|          |       | Vulnerability                            |            |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Multiple Vulnerabilities in Cisco IOS    | CSCwh87343 | CVE-2023-20198 | CWE-420 | Cisco IOS XE Software                                           | 52d    | 36d    | 
|          |       | XE Software Web UI Feature               |            | CVE-2023-20273 | CWE-78  |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco Catalyst SD-WAN Manager            | CSCvw59643 | CVE-2023-20034 | CWE-286 | Cisco SD-WAN Solution                                           | 71d    | 43d    | 
|          |       | Vulnerabilities                          | CSCvz62234 | CVE-2023-20252 | CWE-399 | Cisco SD-WAN vManage                                            |        |        | 
|          |       |                                          | CSCwd46383 | CVE-2023-20253 | CWE-798 | Cisco SD-WAN vSmart                                             |        |        | 
|          |       |                                          | CSCwf55823 | CVE-2023-20254 | CWE-862 |                                                                 |        |        | 
|          |       |                                          | CSCwf68936 | CVE-2023-20262 |         |                                                                 |        |        | 
|          |       |                                          | CSCwh03202 |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco Emergency Responder Static         | CSCwh34565 | CVE-2023-20101 | CWE-798 | Cisco Emergency Responder                                       | 64d    | 64d    | 
|          |       | Credentials Vulnerability                |            |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco BroadWorks Application Delivery    | CSCwh02758 | CVE-2023-20238 | CWE-287 | Cisco BroadWorks                                                | 92d    | 92d    | 
|          |       | Platform and Xtended Services Platform   |            |                |         |                                                                 |        |        | 
|          |       | Authentication Bypass Vulnerability      |            |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco  SD-WAN vManage Unauthenticated    | CSCwf76218 | CVE-2023-20214 | CWE-287 | Cisco SD-WAN vManage                                            | 148d   | 148d   | 
|          |       | REST API Access Vulnerability            | CSCwf82344 |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco Expressway Series and Cisco        | CSCvz54058 | CVE-2023-20105 | CWE-20  | Cisco TelePresence Video Communication Server (VCS) Expressway  | 183d   | 183d   | 
|          |       | TelePresence Video Communication Server  | CSCwf28030 | CVE-2023-20192 | CWE-269 |                                                                 |        |        | 
|          |       | Privilege Escalation Vulnerabilities     |            |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco Small Business Series Switches     | CSCwe27386 | CVE-2023-20024 | CWE-120 | Cisco Small Business Smart and Managed Switches                 | 204d   | 204d   | 
|          |       | Buffer Overflow Vulnerabilities          | CSCwe27393 | CVE-2023-20156 | CWE-121 |                                                                 |        |        | 
|          |       |                                          | CSCwe27394 | CVE-2023-20157 | CWE-122 |                                                                 |        |        | 
|          |       |                                          | CSCwe27403 | CVE-2023-20158 | CWE-200 |                                                                 |        |        | 
|          |       |                                          | CSCwe27424 | CVE-2023-20159 | CWE-787 |                                                                 |        |        | 
|          |       |                                          | CSCwe27425 | CVE-2023-20160 |         |                                                                 |        |        | 
|          |       |                                          | CSCwe27441 | CVE-2023-20161 |         |                                                                 |        |        | 
|          |       |                                          | CSCwe27444 | CVE-2023-20162 |         |                                                                 |        |        | 
|          |       |                                          | CSCwe27445 | CVE-2023-20189 |         |                                                                 |        |        | 
|          |       |                                          | CSCwe32312 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwe32313 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwe32315 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwe32318 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwe32321 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwe32323 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwe32326 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwe32334 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwe32338 |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco SPA112 2-Port Phone Adapters       | CSCwe50762 | CVE-2023-20126 | CWE-306 | Cisco Small Business IP Phones                                  | 218d   | 218d   | 
|          |       | Remote Command Execution Vulnerability   |            |                |         | Cisco Analog Telephone Adaptor (ATA) Software                   |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco Industrial Network Director        | CSCwc29352 | CVE-2023-20036 | CWE-552 | Cisco Industrial Network Director                               | 232d   | 232d   | 
|          |       | Vulnerabilities                          | CSCwc29354 | CVE-2023-20039 | CWE-78  |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco Modeling Labs External             | CSCwe60374 | CVE-2023-20154 | CWE-305 | Cisco Modeling Labs                                             | 232d   | 232d   | 
|          |       | Authentication Bypass Vulnerability      |            |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco Expressway Series and Cisco        | CSCwa01080 | CVE-2022-20812 | CWE-158 | Cisco TelePresence Video Communication Server (VCS) Expressway  | 1y154d | 247d   | 
|          |       | TelePresence Video Communication Server  | CSCwa01085 | CVE-2022-20813 | CWE-36  |                                                                 |        |        | 
|          |       | Vulnerabilities                          |            |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco IP Phone 6800, 7800, and 8800      | CSCwc78400 | CVE-2023-20078 | CWE-121 | Cisco IP Phones with Multiplatform Firmware                     | 281d   | 262d   | 
|          |       | Series Web UI Vulnerabilities            | CSCwd39132 | CVE-2023-20079 | CWE-78  | Cisco Session Initiation Protocol (SIP) Software                |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco Small Business RV016, RV042,       | CSCwd47551 | CVE-2023-20025 | CWE-293 | Cisco Small Business RV Series Router Firmware                  | 330d   | 268d   | 
|          |       | RV042G, RV082, RV320, and RV325 Routers  | CSCwd60199 | CVE-2023-20026 | CWE-77  |                                                                 |        |        | 
|          |       | Vulnerabilities                          | CSCwe41652 | CVE-2023-20118 |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | ClamAV HFS+ Partition Scanning Buffer    | CSCwd74132 | CVE-2023-20032 | CWE-120 | Cisco Secure Web Appliance                                      | 295d   | 288d   | 
|          |       | Overflow Vulnerability Affecting Cisco   | CSCwd74133 |                |         | Cisco Secure Endpoint                                           |        |        | 
|          |       | Products: February 2023                  | CSCwd74134 |                |         | Cisco Secure Endpoint Private Cloud Administration Portal       |        |        | 
|          |       |                                          | CSCwd74135 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwe18204 |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Vulnerability in Spring Framework        | CSCvv65984 | CVE-2022-22965 | CWE-120 | Cisco Emergency Responder                                       | 1y249d | 301d   | 
|          |       | Affecting Cisco Products: March 2022     | CSCwa79849 |                |         | Cisco Unity Connection                                          |        |        | 
|          |       |                                          | CSCwb43327 |                |         | Cisco Unified Communications Manager                            |        |        | 
|          |       |                                          | CSCwb43328 |                |         | Cisco Unified Communications Manager IM and Presence Service    |        |        | 
|          |       |                                          | CSCwb43331 |                |         | Cisco Prime License Manager                                     |        |        | 
|          |       |                                          | CSCwb43332 |                |         | Cisco Prime Collaboration Deployment                            |        |        | 
|          |       |                                          | CSCwb43335 |                |         | Cisco Firepower Management Center                               |        |        | 
|          |       |                                          | CSCwb43340 |                |         | Cisco Evolved Programmable Network Manager (EPNM)               |        |        | 
|          |       |                                          | CSCwb43342 |                |         | Cisco Firepower Threat Defense Software                         |        |        | 
|          |       |                                          | CSCwb43345 |                |         | Cisco IoT Field Network Director (IoT-FND)                      |        |        | 
|          |       |                                          | CSCwb43346 |                |         | Cisco HyperFlex HX Data Platform                                |        |        | 
|          |       |                                          | CSCwb43734 |                |         | Cisco Unified Communications Manager / Cisco Unity Connection   |        |        | 
|          |       |                                          | CSCwb43736 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwb43738 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwb43739 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwb44794 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwb69766 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwb70105 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwb84370 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwc96587 |                |         |                                                                 |        |        | 
|          |       |                                          | CSCwd75689 |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco IOS and IOS XE Software DHCP       | CSCsm45390 | CVE-2017-12240 | CWE-20  | Cisco IOS                                                       | 6y72d  | 355d   | 
|          |       | Remote Code Execution Vulnerability      | CSCuw77959 |                |         | Cisco IOS XE Software                                           |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco IOS and IOS XE Software Smart      | CSCvg76186 | CVE-2018-0171  | CWE-787 | Cisco IOS                                                       | 5y255d | 357d   | 
|          |       | Install Remote Code Execution            |            |                |         | Cisco IOS XE Software                                           |        |        | 
|          |       | Vulnerability                            |            |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco RV132W and RV134W Remote Code      | CSCvg92737 | CVE-2018-0125  | CWE-20  | Cisco Small Business RV Series Router Firmware                  | 5y304d | 357d   | 
|          |       | Execution and Denial of Service          | CSCvh60170 |                |         |                                                                 |        |        | 
|          |       | Vulnerability                            |            |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco HyperFlex HX Command Injection     | CSCvx36014 | CVE-2021-1497  | CWE-78  | Cisco HyperFlex HX Data Platform                                | 2y216d | 357d   | 
|          |       | Vulnerabilities                          | CSCvx36019 | CVE-2021-1498  |         |                                                                 |        |        | 
|          |       |                                          | CSCvx37435 |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+
| Critical | V     | Cisco Secure Access Control System Java  | CSCvh25988 | CVE-2018-0147  | CWE-20  | Cisco Secure Access Control System (ACS)                        | 5y276d | 357d   | 
|          |       | Deserialization Vulnerability            |            |                |         |                                                                 |        |        | 
+----------+-------+------------------------------------------+------------+----------------+---------+-----------------------------------------------------------------+--------+--------+

Filter: sev, bug, cve, cwe, prod, ver, added, updated
View:   list (def), url, sum, ver, all
```

[[Back]](./README.md)