# ACI

## Cisco PSIRT

This feature gets the vulnerabilities in the context of specific APIC or group of APICs (aka domain).

Make sure the APIC is [defined](../aci/Controller.md) or provide full access details in the command options.

```
# iserver get aci psirt --apic dom:milan

Apic: apic11 (mode:online, cache:off)
Apic: apic21 (mode:online, cache:off)

Advisory - Apic: apic11 version 15.2(8e)
----------------------------------------

+------+-------+------------------------------------+------------+----------------+---------+--------------------------------------------------+------+--------+
| Sev  | Final | Title                              | Bug        | CVE            | CWE     | Product                                          | Add  | Update |
+------+-------+------------------------------------+------------+----------------+---------+--------------------------------------------------+------+--------+
| High | V     | Cisco ACI Multi-Site CloudSec      | CSCwf02544 | CVE-2023-20185 | CWE-330 | Cisco NX-OS System Software in ACI Mode 15.2(8e) | 155d | 152d   | 
|      |       | Encryption Information Disclosure  |            |                |         |                                                  |      |        | 
|      |       | Vulnerability                      |            |                |         |                                                  |      |        | 
+------+-------+------------------------------------+------------+----------------+---------+--------------------------------------------------+------+--------+

Advisory - Apic: apic21 version 16.0(2h)
----------------------------------------

+------+-------+------------------------------------+------------+----------------+---------+--------------------------------------------------+------+--------+
| Sev  | Final | Title                              | Bug        | CVE            | CWE     | Product                                          | Add  | Update |
+------+-------+------------------------------------+------------+----------------+---------+--------------------------------------------------+------+--------+
| High | V     | Cisco ACI Multi-Site CloudSec      | CSCwf02544 | CVE-2023-20185 | CWE-330 | Cisco NX-OS System Software in ACI Mode 16.0(2h) | 155d | 152d   | 
|      |       | Encryption Information Disclosure  |            |                |         |                                                  |      |        | 
|      |       | Vulnerability                      |            |                |         |                                                  |      |        | 
+------+-------+------------------------------------+------------+----------------+---------+--------------------------------------------------+------+--------+
```

[[Back]](./README.md)