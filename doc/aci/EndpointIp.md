# Endpoint

## Filter by ip

```
# iserver get aci ep --apic apic11 --address 15.2.61.6

Apic: apic11 (mode:online, cache:off)
```

Developer

```
# iserver get aci ep --apic apic11 --address 15.2.61.6

{
    "duration": 2472,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 438,
        "disconnect_time": 0,
        "mo_time": 1562,
        "total_time": 2000
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

True	438	-	connect apic11o.emea-sp.cisco.com
True	1562	190	apic11o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./Endpoint.md)