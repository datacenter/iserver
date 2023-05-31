# Node Protocol - IPv4

## Filter IPv4 route table entries by vrf name

```
# iserver get aci proto ipv4 --apic apic11 --node rl --vrf overlay-1

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node rl --vrf overlay-1

{
    "duration": 1430,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 910,
        "total_time": 1321
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
    }
}

Log: apic
----------

True	411	-	connect apic11o.emea-sp.cisco.com
True	317	11	apic11o.emea-sp.cisco.com class fabricNode
True	299	19	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
True	294	19	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
```

[[Back]](./ProtocolIpv4.md)