# Endpoint

## Filter by ip

```
# iserver get aci ep --apic apic11 --address 15.2.61.6

Apic: apic11 (mode:online, cache:off)

+----+-------------------+------------+-------+---------------------+---------------------+
| SF | MAC Address       | IP Address | Encap | BD                  | VRF                 |
+----+-------------------+------------+-------+---------------------+---------------------+
| LV | 00:50:56:B2:04:77 | 15.2.61.6  | 2346  | MPC/sPBR-ASA-OUT_BD | MPC/MPC-sPBR-IN_VRF | 
+----+-------------------+------------+-------+---------------------+---------------------+
```

Developer

```
# iserver get aci ep --apic apic11 --address 15.2.61.6

{
    "duration": 1253,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 380,
        "disconnect_time": 0,
        "mo_time": 693,
        "total_time": 1073
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

True	380	-	connect apic11o.emea-sp.cisco.com:443
True	693	357	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./Endpoint.md)