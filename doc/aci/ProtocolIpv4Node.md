# Node Protocol - IPv4

## Show IPv4 route table entries for selected node

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc

{
    "duration": 1126,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 644,
        "total_time": 1038
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

True	394	-	connect apic11o.emea-sp.cisco.com
True	328	11	apic11o.emea-sp.cisco.com class fabricNode
True	316	31	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
```

[[Back]](./ProtocolIpv4.md)