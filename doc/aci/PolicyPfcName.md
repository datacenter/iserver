# Policy - Priority Flow Control

## Filter by name

```
# iserver get aci policy pfc --apic apic11 --name default

Apic: apic11 (mode:online, cache:off)

+-------------+----+-------------+------------+--------------+
| Policy Name | TF | Admin State | Interfaces | Ref Policies |
+-------------+----+-------------+------------+--------------+
| default     |    | auto        | 398        | 82           | 
+-------------+----+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy pfc --apic apic11 --name default

{
    "duration": 1785,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 1059,
        "total_time": 1486
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

True	427	-	connect apic11o.emea-sp.cisco.com
True	340	3	apic11o.emea-sp.cisco.com class qosPfcIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	401	400	apic11o.emea-sp.cisco.com class l1RsQosPfcIfPolCons
True	318	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyPfc.md)