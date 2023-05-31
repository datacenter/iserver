# Endpoint

## Filter by ip

```
# iserver get aci ep --apic apic11 --address 15.2.61.6

Apic: apic11

+----+-------------------+------------+--------+---------------------+---------------------+
| SF | MAC Address       | IP Address | Tenant | BD                  | VRF                 |
+----+-------------------+------------+--------+---------------------+---------------------+
| LV | 00:50:56:B2:04:77 | 15.2.61.6  | MPC    | MPC/sPBR-ASA-OUT_BD | MPC/MPC-sPBR-IN_VRF | 
+----+-------------------+------------+--------+---------------------+---------------------+
```

Developer

```
# iserver get aci ep --apic apic11 --address 15.2.61.6

{
    "duration": 1058,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 561,
        "total_time": 956
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

True	395	-	connect apic11o.emea-sp.cisco.com
True	561	322	apic11o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
```

[[Back]](./Endpoint.md)