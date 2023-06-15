# Policy - CoPP

## Get all policies

```
# iserver get aci policy copp --apic apic11

Apic: apic11 (mode:online, cache:off)

+-------------+----+-----------+------------+--------------+
| Policy Name | TF | Protocols | Interfaces | Ref Policies |
+-------------+----+-----------+------------+--------------+
| default     |    | 0         | 464        | 86           | 
+-------------+----+-----------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy copp --apic apic11

{
    "duration": 2205,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 414,
        "disconnect_time": 0,
        "mo_time": 1387,
        "total_time": 1801
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

True	414	-	connect apic11o.emea-sp.cisco.com
True	320	1	apic11o.emea-sp.cisco.com class coppIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	323	0	apic11o.emea-sp.cisco.com class coppProtoClassP
True	410	464	apic11o.emea-sp.cisco.com class l1RsCoppIfPolCons
True	334	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCopp.md)