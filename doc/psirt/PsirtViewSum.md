# Cisco PSIRT

## sum view

```
# iserver get psirt --prod *aci* --sev high -v sum

Advisory - Summary [#2]
-----------------------

+------+-------+------------------------------------------+------------------------------------------------------------------------------------------------------+
| Sev  | Final | Title                                    | Summary                                                                                              |
+------+-------+------------------------------------------+------------------------------------------------------------------------------------------------------+
| High | V     | Cisco ACI Multi-Site CloudSec            | A vulnerability in the Cisco ACI Multi-Site CloudSec encryption feature of Cisco Nexus 9000 Series   | 
|      |       | Encryption Information Disclosure        | Fabric Switches in ACI mode could allow an unauthenticated, remote attacker to read or modify        | 
|      |       | Vulnerability                            | intersite encrypted traffic.This vulnerability is due to an issue with the implementation of the     | 
|      |       |                                          | ciphers that are used by the CloudSec encryption feature on affected switches. An attacker with an   | 
|      |       |                                          | on-path position between the ACI sites could exploit this vulnerability by intercepting intersite    | 
|      |       |                                          | encrypted traffic and using cryptanalytic techniques to break the encryption. A successful exploit   | 
|      |       |                                          | could allow the attacker to read or modify the traffic that is transmitted between the sites.Cisco   | 
|      |       |                                          | has not released and will not release software updates that address this vulnerability. There are    | 
|      |       |                                          | no workarounds that address this vulnerability.This advisory is available at the following           | 
|      |       |                                          | link:<br><a                                                                                          | 
|      |       |                                          | href="https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-aci-    | 
|      |       |                                          | cloudsec-enc-                                                                                        | 
|      |       |                                          | Vs5Wn2sX">https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-    | 
|      |       |                                          | aci-cloudsec-enc-Vs5Wn2sX</a>                                                                        | 
+------+-------+------------------------------------------+------------------------------------------------------------------------------------------------------+
| High | V     | Cisco Nexus 9000 Series Fabric Switches  | A vulnerability in the Link Layer Discovery Protocol (LLDP) feature for Cisco Nexus 9000 Series      | 
|      |       | in ACI Mode Link Layer Discovery         | Fabric Switches in Application Centric Infrastructure (ACI) Mode could allow an unauthenticated,     | 
|      |       | Protocol Memory Leak Denial of Service   | adjacent attacker to cause a memory leak, which could result in an unexpected reload of the          | 
|      |       | Vulnerability                            | device.This vulnerability is due to incorrect error checking when parsing ingress LLDP packets. An   | 
|      |       |                                          | attacker could exploit this vulnerability by sending a steady stream of crafted LLDP packets to an   | 
|      |       |                                          | affected device. A successful exploit could allow the attacker to cause a memory leak, which could   | 
|      |       |                                          | result in a denial of service (DoS) condition when the device unexpectedly                           | 
|      |       |                                          | reloads.<strong>Note:</strong> This vulnerability cannot be exploited by transit traffic through     | 
|      |       |                                          | the device. The crafted LLDP packet must be targeted to a directly connected interface, and the      | 
|      |       |                                          | attacker must be in the same broadcast domain as the affected device (Layer 2 adjacent). In          | 
|      |       |                                          | addition, the attack surface for this vulnerability can be reduced by disabling LLDP on interfaces   | 
|      |       |                                          | where it is not required.Cisco has released software updates that address this vulnerability. There  | 
|      |       |                                          | are no workarounds that address this vulnerability.This advisory is available at the following       | 
|      |       |                                          | link:<br><a                                                                                          | 
|      |       |                                          | href="https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-aci-    | 
|      |       |                                          | lldp-dos-                                                                                            | 
|      |       |                                          | ySCNZOpX">https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-    | 
|      |       |                                          | aci-lldp-dos-ySCNZOpX</a>This advisory is part of the February 2023 Cisco FXOS and NX-OS Software    | 
|      |       |                                          | Security Advisory Bundled Publication. For a complete list of the advisories and links to them, see  | 
|      |       |                                          | <a href="https://sec.cloudapps.cisco.com/security/center/viewErp.x?alertId=ERP-75057"                | 
|      |       |                                          | rel="nofollow">Cisco Event Response: February 2023 Semiannual Cisco FXOS and NX-OS Software          | 
|      |       |                                          | Security Advisory Bundled Publication</a>.                                                           | 
+------+-------+------------------------------------------+------------------------------------------------------------------------------------------------------+

Filter: sev, bug, cve, cwe, prod, ver, added, updated
View:   list (def), url, sum, ver, all
```

[[Back]](./README.md)