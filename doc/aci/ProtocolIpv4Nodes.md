# Node Protocol - IPv4

## Show IPv4 route table entries for selected nodes

```
# iserver get aci proto ipv4 --apic apic11 --node rl

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node rl

{
    "duration": 1492,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 982,
        "total_time": 1404
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

True	422	-	connect apic11o.emea-sp.cisco.com
True	402	11	apic11o.emea-sp.cisco.com class fabricNode
True	282	19	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
True	298	19	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
```

[[Back]](./ProtocolIpv4.md)