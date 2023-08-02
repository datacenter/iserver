# Node Protocol - ARP

## Inst view

```
# iserver get aci proto arp --apic apic21 --node bl2205-eu-spdc --view inst

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Protocol ARP - Instance [#1]
----------------------------

+----------------------+-------------+--------+---------+
| Node                 | Admin State | Health | Faults  |
+----------------------+-------------+--------+---------+
| pod-1/bl2205-eu-spdc | enabled     | 100    | 0 0 0 0 | 
+----------------------+-------------+--------+---------+
```

Developer

```
# iserver get aci proto arp --apic apic21 --node bl2205-eu-spdc --view inst

{
    "duration": 1087,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 377,
        "disconnect_time": 0,
        "mo_time": 534,
        "total_time": 911
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

True	377	-	connect apic21o.emea-sp.cisco.com:443
True	275	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	259	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/arp query query-target=children&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolArp.md)