# Endpoint

## Filter by hypervisor

```
# iserver get aci ep --apic apic11 --hv esx3* --view vm

Apic: apic11 (mode:online, cache:off)

+----+-------------------+------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| SF | MAC Address       | IP Address | VMM         | Hypervisor             | VM Name                                | VM State   | vNIC Name         | vNIC State |
+----+-------------------+------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| V  | 00:50:56:B2:0D:E2 |            | EU-SPDC-CDC | esx3-eu-spdc.cisco.com | Linux-test02                           | poweredOff | Network adapter 1 | down       | 
+----+-------------------+------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| V  | 00:50:56:B2:33:BB |            | EU-SPDC-CDC | esx3-eu-spdc.cisco.com | cw-na-platform-5.0.0-81-release-230502 | poweredOff | Network adapter 1 | down       | 
+----+-------------------+------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| V  | 00:50:56:B2:78:68 |            | EU-SPDC-CDC | esx3-eu-spdc.cisco.com | cw-na-platform-5.0.0-81-release-230502 | poweredOff | Network adapter 2 | down       | 
+----+-------------------+------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| V  | 00:50:56:B2:AB:88 |            | EU-SPDC-CDC | esx3-eu-spdc.cisco.com | paris2024-collector                    | poweredOff | Network adapter 1 | down       | 
+----+-------------------+------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
```

Developer

```
# iserver get aci ep --apic apic11 --hv esx3* --view vm

{
    "duration": 5343,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 430,
        "disconnect_time": 0,
        "mo_time": 2683,
        "total_time": 3113
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
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	430	-	connect apic11o.emea-sp.cisco.com
True	614	191	apic11o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	799	658	apic11o.emea-sp.cisco.com class compVm
True	933	1874	apic11o.emea-sp.cisco.com class compVNic
True	337	68	apic11o.emea-sp.cisco.com class compHv
```

[[Back]](./Endpoint.md)