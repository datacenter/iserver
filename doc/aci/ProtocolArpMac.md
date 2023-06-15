# Node Protocol - ARP

## Filter adjacencies by MAC address

```
# iserver get aci proto arp --apic apic11 --mac 56b2

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc
```

Developer

```
# iserver get aci proto arp --apic apic11 --mac 56b2

{
    "duration": 1520,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 413,
        "disconnect_time": 0,
        "mo_time": 960,
        "total_time": 1373
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

True	413	-	connect apic11o.emea-sp.cisco.com
True	331	13	apic11o.emea-sp.cisco.com class fabricNode
True	325	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom
True	304	12	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)