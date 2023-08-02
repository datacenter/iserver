# Contract Filter

## Event view

```
# iserver get aci contract filter
    --apic apic21
    --name k8s/icmp
    --when any
    --view event

Apic: apic21 (mode:online, cache:off)

Contract Filter - Event Logs last 10y [#0]
------------------------------------------
None
```

Developer

```
# iserver get aci contract filter
    --apic apic21
    --name k8s/icmp
    --when any
    --view event

{
    "duration": 5235,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 430,
        "disconnect_time": 0,
        "mo_time": 4701,
        "total_time": 5131
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

True	430	-	connect apic21o.emea-sp.cisco.com:443
True	349	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	4352	29	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ContractFilter.md)