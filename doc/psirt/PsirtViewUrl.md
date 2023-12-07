# Cisco PSIRT

## url view

```
# iserver get psirt --prod *aci* --sev high -v url

Advisory - URL [#2]
-------------------

+------+-------+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sev  | Final | Title                                    | URL                                                                                                                                                                        |
+------+-------+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| High | V     | Cisco ACI Multi-Site CloudSec            | cvrf: https://sec.cloudapps.cisco.com/security/center/contentxml/CiscoSecurityAdvisory/cisco-sa-aci-cloudsec-enc-Vs5Wn2sX/cvrf/cisco-sa-aci-cloudsec-enc-Vs5Wn2sX_cvrf.xml | 
|      |       | Encryption Information Disclosure        | csaf: https://sec.cloudapps.cisco.com/security/center/contentjson/CiscoSecurityAdvisory/cisco-sa-aci-cloudsec-enc-Vs5Wn2sX/csaf/cisco-sa-aci-cloudsec-enc-Vs5Wn2sX.json    | 
|      |       | Vulnerability                            | pub:  https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-aci-cloudsec-enc-Vs5Wn2sX                                                     | 
+------+-------+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| High | V     | Cisco Nexus 9000 Series Fabric Switches  | cvrf: https://sec.cloudapps.cisco.com/security/center/contentxml/CiscoSecurityAdvisory/cisco-sa-aci-lldp-dos-ySCNZOpX/cvrf/cisco-sa-aci-lldp-dos-ySCNZOpX_cvrf.xml         | 
|      |       | in ACI Mode Link Layer Discovery         | csaf: https://sec.cloudapps.cisco.com/security/center/contentjson/CiscoSecurityAdvisory/cisco-sa-aci-lldp-dos-ySCNZOpX/csaf/cisco-sa-aci-lldp-dos-ySCNZOpX.json            | 
|      |       | Protocol Memory Leak Denial of Service   | pub:  https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-aci-lldp-dos-ySCNZOpX                                                         | 
|      |       | Vulnerability                            |                                                                                                                                                                            | 
+------+-------+------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Filter: sev, bug, cve, cwe, prod, ver, added, updated
View:   list (def), url, sum, ver, all
```

[[Back]](./README.md)