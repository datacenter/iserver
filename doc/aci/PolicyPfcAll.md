# Policy - Priority Flow Control

## Get all policies

```
# iserver get aci policy pfc --apic apic11

Apic: apic11 (mode:online, cache:off)

+--------------+----+-------------+------------+--------------+
| Policy Name  | TF | Admin State | Interfaces | Ref Policies |
+--------------+----+-------------+------------+--------------+
| default      |    | auto        | 398        | 82           | 
| nidemo-dummy |    | auto        | 2          | 1            | 
| ProvaPAOLO   |    | off         | 0          | 0            | 
+--------------+----+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy pfc --apic apic11

{
    "duration": 1879,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 426,
        "disconnect_time": 0,
        "mo_time": 1076,
        "total_time": 1502
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

True	426	-	connect apic11o.emea-sp.cisco.com
True	338	3	apic11o.emea-sp.cisco.com class qosPfcIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	398	400	apic11o.emea-sp.cisco.com class l1RsQosPfcIfPolCons
True	340	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyPfc.md)