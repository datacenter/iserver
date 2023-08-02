# Contract Filter

## Fault view

```
# iserver get aci contract filter --apic apic21 --name k8s/icmp --view fault

Apic: apic21 (mode:online, cache:off)

Contract Filter - Faults [#0]
-----------------------------
None
```

Developer

```
# iserver get aci contract filter --apic apic21 --name k8s/icmp --view fault

{
    "duration": 1255,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 433,
        "disconnect_time": 0,
        "mo_time": 722,
        "total_time": 1155
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

True	433	-	connect apic21o.emea-sp.cisco.com:443
True	370	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	352	0	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ContractFilter.md)