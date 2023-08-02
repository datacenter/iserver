# Contract Filter

## Fault history view

```
# iserver get aci contract filter
    --apic apic21
    --name k8s/icmp
    --when any
    --view hfault

Apic: apic21 (mode:online, cache:off)

Contract Filter - Fault Records last 10y [#0]
---------------------------------------------
None
```

Developer

```
# iserver get aci contract filter
    --apic apic21
    --name k8s/icmp
    --when any
    --view hfault

{
    "duration": 5778,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 417,
        "disconnect_time": 0,
        "mo_time": 5238,
        "total_time": 5655
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

True	417	-	connect apic21o.emea-sp.cisco.com:443
True	506	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	4732	0	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ContractFilter.md)