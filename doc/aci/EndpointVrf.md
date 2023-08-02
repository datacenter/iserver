# Endpoint

## Filter by vrf

```
# iserver get aci ep --apic apic11 --vrf *MPC*

Apic: apic11 (mode:online, cache:off)
```

Developer

```
# iserver get aci ep --apic apic11 --vrf *MPC*

{
    "duration": 1428,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 448,
        "disconnect_time": 0,
        "mo_time": 732,
        "total_time": 1180
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

True	448	-	connect apic11o.emea-sp.cisco.com:443
True	732	361	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./Endpoint.md)