# Node Protocol - IPv4

## Filter IPv4 route table entries by route type

Supported route types
- ibgp
- ebgp
- bgp
- static
- local
- direct

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc --type ibgp

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc --type ibgp

{
    "duration": 1107,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 620,
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
    }
}

Log: apic
----------

True	404	-	connect apic11o.emea-sp.cisco.com
True	316	11	apic11o.emea-sp.cisco.com class fabricNode
True	304	31	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
```

[[Back]](./ProtocolIpv4.md)