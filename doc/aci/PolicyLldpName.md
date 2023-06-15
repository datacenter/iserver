# Policy - LLDP

## Filter by name

```
# iserver get aci policy lldp --apic apic11 --name default

Apic: apic11 (mode:online, cache:off)

+-------------+----+---------------+----------------+------------+--------------+
| Policy Name | TF | Receive State | Transmit State | Interfaces | Ref Policies |
+-------------+----+---------------+----------------+------------+--------------+
| default     |    | enabled       | enabled        | 0          | 0            | 
| default     |    | enabled       | enabled        | 293        | 56           | 
+-------------+----+---------------+----------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy lldp --apic apic11 --name default

{
    "duration": 1808,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 419,
        "disconnect_time": 0,
        "mo_time": 1060,
        "total_time": 1479
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

True	419	-	connect apic11o.emea-sp.cisco.com
True	349	10	apic11o.emea-sp.cisco.com class lldpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	393	394	apic11o.emea-sp.cisco.com class l1RsLldpIfPolCons
True	318	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLldp.md)