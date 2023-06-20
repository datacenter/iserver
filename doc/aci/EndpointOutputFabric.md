# Endpoint

## Fabric specific output

```
# iserver get aci ep --apic apic11 --subnet 15.100.100.0/24 --view fabric

Apic: apic11 (mode:online, cache:off)
```

Developer

```
# iserver get aci ep --apic apic11 --subnet 15.100.100.0/24 --view fabric

{
    "duration": 1044,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 400,
        "disconnect_time": 0,
        "mo_time": 514,
        "total_time": 914
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

True	400	-	connect apic11o.emea-sp.cisco.com:443
True	514	208	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./Endpoint.md)