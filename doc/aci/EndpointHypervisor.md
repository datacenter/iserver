# Endpoint

## Filter by hypervisor

```
# iserver get aci ep --apic apic11 --hv esx3* --view vm

Apic: apic11 (mode:online, cache:off)

+----+-------------------+--------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| SF | MAC Address       | IP Address   | VMM         | Hypervisor             | VM Name                                | VM State   | vNIC Name         | vNIC State |
+----+-------------------+--------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| V  | 00:50:56:B2:0D:E2 |              | EU-SPDC-CDC | esx3-eu-spdc.cisco.com | Linux-test02                           | poweredOff | Network adapter 1 | down       | 
+----+-------------------+--------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| V  | 00:50:56:B2:33:BB |              | EU-SPDC-CDC | esx3-eu-spdc.cisco.com | cw-na-platform-5.0.0-81-release-230502 | poweredOff | Network adapter 1 | down       | 
+----+-------------------+--------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| V  | 00:50:56:B2:78:68 |              | EU-SPDC-CDC | esx3-eu-spdc.cisco.com | cw-na-platform-5.0.0-81-release-230502 | poweredOff | Network adapter 2 | down       | 
+----+-------------------+--------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| LV | 00:50:56:B2:92:87 | 10.58.239.45 | EU-SPDC-CDC | esx3-eu-spdc.cisco.com | cnc41-worker-2                         | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+--------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
```

Developer

```
# iserver get aci ep --apic apic11 --hv esx3* --view vm

{
    "duration": 4801,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 381,
        "disconnect_time": 0,
        "mo_time": 3585,
        "total_time": 3966
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

True	381	-	connect apic11o.emea-sp.cisco.com:443
True	600	209	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	1855	654	apic11o.emea-sp.cisco.com:443 class compVm
True	818	1870	apic11o.emea-sp.cisco.com:443 class compVNic
True	312	68	apic11o.emea-sp.cisco.com:443 class compHv
```

[[Back]](./Endpoint.md)