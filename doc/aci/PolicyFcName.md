# Policy - Fibre Channel

## Filter by name

```
# iserver get aci policy fc --apic apic11 --name default

Apic: apic11

+-------------+-------+-----------+------------+-------+--------------+-----------------------+------------+--------------+
| Policy Name | TF    | Port Mode | Trunk Mode | Speed | Fill Pattern | Receive Buffer Credit | Interfaces | Ref Policies |
+-------------+-------+-----------+------------+-------+--------------+-----------------------+------------+--------------+
| default     | False | f         | trunk-off  | auto  | IDLE         | 64                    | 408        | 83           | 
+-------------+-------+-----------+------------+-------+--------------+-----------------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy fc --apic apic11 --name default

{
    "duration": 1570,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 403,
        "disconnect_time": 0,
        "mo_time": 1013,
        "total_time": 1416
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

True	403	-	connect apic11o.emea-sp.cisco.com
True	318	1	apic11o.emea-sp.cisco.com class fcIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	401	408	apic11o.emea-sp.cisco.com class l1RsFcIfPolCons
True	294	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyFc.md)