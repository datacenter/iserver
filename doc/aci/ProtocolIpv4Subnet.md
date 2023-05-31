# Node Protocol - IPv4

## Filter IPv4 route table based on IP subnet

Example: Equal IP subnet

```
# iserver get aci proto ipv4 --apic apic11 --node rl --subnet 172.16.21.0/24

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc
```

Example: Contain IP subnet

```
# iserver get aci proto ipv4
    --apic apic11
    --node rl
    --subnet 172.16.21.16/28
    --longer

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node rl --subnet 172.16.21.0/24

{
    "duration": 1451,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 400,
        "disconnect_time": 0,
        "mo_time": 946,
        "total_time": 1346
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

True	400	-	connect apic11o.emea-sp.cisco.com
True	325	11	apic11o.emea-sp.cisco.com class fabricNode
True	317	19	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
True	304	19	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
```

[[Back]](./ProtocolIpv4.md)