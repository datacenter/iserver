# Policy - CoPP

## Filter by name

```
# iserver get aci policy copp --apic apic11 --name default

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
# iserver get aci policy copp --apic apic11 --name default

{
    "duration": 3314,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 2535,
        "total_time": 2957
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

True	422	-	connect apic11o.emea-sp.cisco.com
True	333	1	apic11o.emea-sp.cisco.com class coppIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	344	0	apic11o.emea-sp.cisco.com class coppProtoClassP
True	1523	464	apic11o.emea-sp.cisco.com class l1RsCoppIfPolCons
True	335	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCopp.md)