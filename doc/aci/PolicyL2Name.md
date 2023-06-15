# Policy - L2

## Filter by name

```
# iserver get aci policy l2 --apic apic11 --name default

Apic: apic11 (mode:online, cache:off)

+-------------+----+----------+----------+--------------+------------+--------------+
| Policy Name | TF | QinQ     | 802.1Qbg | VLAN Scope   | Interfaces | Ref Policies |
+-------------+----+----------+----------+--------------+------------+--------------+
| default     |    | disabled | disabled | Global scope | 233        | 2            | 
+-------------+----+----------+----------+--------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy l2 --apic apic11 --name default

{
    "duration": 1829,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 442,
        "disconnect_time": 0,
        "mo_time": 1019,
        "total_time": 1461
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

True	442	-	connect apic11o.emea-sp.cisco.com
True	325	6	apic11o.emea-sp.cisco.com class l2IfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	404	470	apic11o.emea-sp.cisco.com class l1RsL2IfPolCons
True	290	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyL2.md)