# Policy - Synchronous Ethernet

## Get all policies

```
# iserver get aci policy synce --apic apic11

Apic: apic11 (mode:online, cache:off)

+-------------+----+-------------+-----------------+-----------------+-----------------+-----------------+------------+--------------+
| Policy Name | TF | Admin State | Input Selection | Source Priority | Sync Status Msg | Wait-To-Restore | Interfaces | Ref Policies |
+-------------+----+-------------+-----------------+-----------------+-----------------+-----------------+------------+--------------+
| default     |    | disabled    | no              | 100             | yes             | 5               | 470        | 83           | 
+-------------+----+-------------+-----------------+-----------------+-----------------+-----------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy synce --apic apic11

{
    "duration": 1768,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 471,
        "disconnect_time": 0,
        "mo_time": 1013,
        "total_time": 1484
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

True	471	-	connect apic11o.emea-sp.cisco.com
True	336	1	apic11o.emea-sp.cisco.com class synceEthIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	365	470	apic11o.emea-sp.cisco.com class l1RsSynceEthIfPolCons
True	312	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicySynce.md)