# Endpoint

## Filter by subnet

```
# iserver get aci ep --apic apic11 --subnet 15.100.100.0/24

Apic: apic11 (mode:online, cache:off)
```

Developer

```
# iserver get aci ep --apic apic11 --subnet 15.100.100.0/24

{
    "duration": 1405,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 463,
        "disconnect_time": 0,
        "mo_time": 615,
        "total_time": 1078
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

True	463	-	connect apic11o.emea-sp.cisco.com
True	615	191	apic11o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./Endpoint.md)