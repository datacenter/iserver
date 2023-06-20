# Endpoint

## Filter by ip

```
# iserver get aci ep --apic apic11 --address 15.2.61.6

Apic: apic11 (mode:online, cache:off)

+----+-------------------+------------+--------+-------+---------------------+---------------------+
| SF | MAC Address       | IP Address | Tenant | Encap | BD                  | VRF                 |
+----+-------------------+------------+--------+-------+---------------------+---------------------+
| LV | 00:50:56:B2:04:77 | 15.2.61.6  | MPC    | 2020  | MPC/sPBR-ASA-OUT_BD | MPC/MPC-sPBR-IN_VRF | 
+----+-------------------+------------+--------+-------+---------------------+---------------------+
```

Developer

```
# iserver get aci ep --apic apic11 --address 15.2.61.6

{
    "duration": 1236,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 595,
        "disconnect_time": 0,
        "mo_time": 534,
        "total_time": 1129
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

True	595	-	connect apic11o.emea-sp.cisco.com:443
True	534	208	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./Endpoint.md)