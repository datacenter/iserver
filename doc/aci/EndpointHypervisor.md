# Endpoint

## Filter by hypervisor

```
# iserver get aci ep --apic apic11 --hv esx3* --view vm

Apic: apic11

+----+-------------------+---------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| SF | MAC Address       | IP Address    | VMM         | Hypervisor             | VM Name                                | VM State   | vNIC Name         | vNIC State |
+----+-------------------+---------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| LV | 00:50:56:B2:0D:E2 | 10.58.239.39  | EU-SPDC-CDC | esx3-eu-spdc.cisco.com | Linux-test02                           | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+---------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| V  | 00:50:56:B2:33:BB |               | EU-SPDC-CDC | esx3-eu-spdc.cisco.com | cw-na-platform-5.0.0-81-release-230502 | poweredOff | Network adapter 1 | down       | 
+----+-------------------+---------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| V  | 00:50:56:B2:78:68 |               | EU-SPDC-CDC | esx3-eu-spdc.cisco.com | cw-na-platform-5.0.0-81-release-230502 | poweredOff | Network adapter 2 | down       | 
+----+-------------------+---------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
| LV | 00:50:56:B2:AB:88 | 10.58.239.172 | EU-SPDC-CDC | esx3-eu-spdc.cisco.com | paris2024-collector                    | poweredOn  | Network adapter 1 | up         | 
+----+-------------------+---------------+-------------+------------------------+----------------------------------------+------------+-------------------+------------+
```

Developer

```
# iserver get aci ep --apic apic11 --hv esx3* --view vm

{
    "duration": 3244,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 389,
        "disconnect_time": 0,
        "mo_time": 2071,
        "total_time": 2460
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
    }
}

Log: apic
----------

True	389	-	connect apic11o.emea-sp.cisco.com
True	539	323	apic11o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
True	513	656	apic11o.emea-sp.cisco.com class compVm
True	684	1872	apic11o.emea-sp.cisco.com class compVNic
True	335	68	apic11o.emea-sp.cisco.com class compHv
```

[[Back]](./Endpoint.md)