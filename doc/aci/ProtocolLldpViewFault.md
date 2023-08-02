# Node Protocol - LLDP

## Fault view

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view fault

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol LLDP - Faults [#0]
---------------------------
None
Interface context: lldp
```

Developer

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view fault

{
    "duration": 1491,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 447,
        "disconnect_time": 0,
        "mo_time": 881,
        "total_time": 1328
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

True	447	-	connect apic11o.emea-sp.cisco.com:443
True	297	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	296	13	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	288	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ProtocolLldp.md)