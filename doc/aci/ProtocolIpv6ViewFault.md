# Node Protocol - IPv4

## Fault view

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc --view fault

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol IPv4 - Faults [#0]
---------------------------
None
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc --view fault

{
    "duration": 1473,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 934,
        "total_time": 1329
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

True	395	-	connect apic11o.emea-sp.cisco.com:443
True	305	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	303	30	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4 query query-target=children&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Dom
True	326	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/ipv4 query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ProtocolIpv4.md)