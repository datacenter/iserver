# Node Protocol - BGP

## Fault view

```
# iserver get aci proto bgp --apic apic11 --node rl301 --view fault

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

Protocol BGP - Faults [#0]
--------------------------
None
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl301 --view fault

{
    "duration": 1246,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 613,
        "total_time": 1024
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

True	411	-	connect apic11o.emea-sp.cisco.com:443
True	309	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	304	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ProtocolBgp.md)