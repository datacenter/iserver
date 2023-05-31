# Policy - Priority Flow Control

## Get all policies

```
# iserver get aci policy pfc --apic apic11

Apic: apic11

+--------------+----+-------------+------------+--------------+
| Policy Name  | TF | Admin State | Interfaces | Ref Policies |
+--------------+----+-------------+------------+--------------+
| default      |    | auto        | 342        | 82           | 
| nidemo-dummy |    | auto        | 2          | 1            | 
| ProvaPAOLO   |    | off         | 0          | 0            | 
+--------------+----+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy pfc --apic apic11

{
    "duration": 1589,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 409,
        "disconnect_time": 0,
        "mo_time": 1039,
        "total_time": 1448
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

True	409	-	connect apic11o.emea-sp.cisco.com
True	329	3	apic11o.emea-sp.cisco.com class qosPfcIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	410	344	apic11o.emea-sp.cisco.com class l1RsQosPfcIfPolCons
True	300	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyPfc.md)