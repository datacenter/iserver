# Policy - Fibre Channel

## Get all policies

```
# iserver get aci policy fc --apic apic11

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
# iserver get aci policy fc --apic apic11

{
    "duration": 1825,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 430,
        "disconnect_time": 0,
        "mo_time": 1041,
        "total_time": 1471
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

True	430	-	connect apic11o.emea-sp.cisco.com
True	327	1	apic11o.emea-sp.cisco.com class fcIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	387	464	apic11o.emea-sp.cisco.com class l1RsFcIfPolCons
True	327	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyFc.md)