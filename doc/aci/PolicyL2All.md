# Policy - L2

## Get all policies

```
# iserver get aci policy l2 --apic apic11

Apic: apic11

+----------------------+----+----------+----------+------------------+------------+--------------+
| Policy Name          | TF | QinQ     | 802.1Qbg | VLAN Scope       | Interfaces | Ref Policies |
+----------------------+----+----------+----------+------------------+------------+--------------+
| default              |    | disabled | disabled | Global scope     | 177        | 2            | 
| l2-disabled-disabled |    | disabled | disabled | Global scope     | 4          | 3            | 
| L2-global_Pol        |    | disabled | disabled | Global scope     | 0          | 0            | 
| L2-local_Pol         |    | disabled | disabled | Port Local scope | 231        | 77           | 
| nidemo-dummy         |    | disabled | disabled | Global scope     | 2          | 1            | 
| vepa                 |    | disabled | disabled | Global scope     | 0          | 0            | 
+----------------------+----+----------+----------+------------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy l2 --apic apic11

{
    "duration": 1575,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 379,
        "disconnect_time": 0,
        "mo_time": 1044,
        "total_time": 1423
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

True	379	-	connect apic11o.emea-sp.cisco.com
True	318	6	apic11o.emea-sp.cisco.com class l2IfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	418	414	apic11o.emea-sp.cisco.com class l1RsL2IfPolCons
True	308	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyL2.md)