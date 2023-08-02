# Node Interface - Tunnel

## Fault view

```
# iserver get aci intf tun --apic apic21 --view fault

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Loopback - Faults [#0]
--------------------------------
None
```

Developer

```
# iserver get aci intf tun --apic apic21 --view fault

{
    "duration": 1567,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 382,
        "disconnect_time": 0,
        "mo_time": 1068,
        "total_time": 1450
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

True	382	-	connect apic21o.emea-sp.cisco.com:443
True	291	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	397	22	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/tunnelIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	380	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/tunnelIf query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./InterfaceTunnel.md)