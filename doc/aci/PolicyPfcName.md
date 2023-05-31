# Policy - Priority Flow Control

## Filter by name

```
# iserver get aci policy pfc --apic apic11 --name default

Apic: apic11

+-------------+----+-------------+------------+--------------+
| Policy Name | TF | Admin State | Interfaces | Ref Policies |
+-------------+----+-------------+------------+--------------+
| default     |    | auto        | 342        | 82           | 
+-------------+----+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy pfc --apic apic11 --name default

{
    "duration": 1569,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 441,
        "disconnect_time": 0,
        "mo_time": 1012,
        "total_time": 1453
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

True	441	-	connect apic11o.emea-sp.cisco.com
True	317	3	apic11o.emea-sp.cisco.com class qosPfcIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	391	344	apic11o.emea-sp.cisco.com class l1RsQosPfcIfPolCons
True	304	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyPfc.md)