# Policy - Fibre Channel

## Filter by name

```
# iserver get aci policy fc --apic apic11 --name default

Apic: apic11 (mode:online, cache:off)

+-------------+-------+-----------+------------+-------+--------------+-----------------------+------------+--------------+
| Policy Name | TF    | Port Mode | Trunk Mode | Speed | Fill Pattern | Receive Buffer Credit | Interfaces | Ref Policies |
+-------------+-------+-----------+------------+-------+--------------+-----------------------+------------+--------------+
| default     | False | f         | trunk-off  | auto  | IDLE         | 64                    | 464        | 83           | 
+-------------+-------+-----------+------------+-------+--------------+-----------------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy fc --apic apic11 --name default

{
    "duration": 1890,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 436,
        "disconnect_time": 0,
        "mo_time": 1055,
        "total_time": 1491
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

True	436	-	connect apic11o.emea-sp.cisco.com
True	342	1	apic11o.emea-sp.cisco.com class fcIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	392	464	apic11o.emea-sp.cisco.com class l1RsFcIfPolCons
True	321	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyFc.md)