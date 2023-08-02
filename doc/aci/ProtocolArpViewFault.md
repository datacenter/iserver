# Node Protocol - ARP

## Fault view

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --when any
    --view fault

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Protocol ARP - Faults [#0]
--------------------------
None
```

Developer

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --when any
    --view fault

{
    "duration": 1047,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 358,
        "disconnect_time": 0,
        "mo_time": 547,
        "total_time": 905
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

True	358	-	connect apic21o.emea-sp.cisco.com:443
True	283	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	264	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/arp query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ProtocolArp.md)