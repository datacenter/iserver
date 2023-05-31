# Policy - Synchronous Ethernet

## Get all policies

```
# iserver get aci policy synce --apic apic11

Apic: apic11

+-------------+----+-------------+-----------------+-----------------+-----------------+-----------------+------------+--------------+
| Policy Name | TF | Admin State | Input Selection | Source Priority | Sync Status Msg | Wait-To-Restore | Interfaces | Ref Policies |
+-------------+----+-------------+-----------------+-----------------+-----------------+-----------------+------------+--------------+
| default     |    | disabled    | no              | 100             | yes             | 5               | 414        | 83           | 
+-------------+----+-------------+-----------------+-----------------+-----------------+-----------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy synce --apic apic11

{
    "duration": 1554,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 387,
        "disconnect_time": 0,
        "mo_time": 1037,
        "total_time": 1424
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

True	387	-	connect apic11o.emea-sp.cisco.com
True	324	1	apic11o.emea-sp.cisco.com class synceEthIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	411	414	apic11o.emea-sp.cisco.com class l1RsSynceEthIfPolCons
True	302	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicySynce.md)