# Policy - L2

## Filter by name

```
# iserver get aci policy l2 --apic apic11 --name default

Apic: apic11

+-------------+----+----------+----------+--------------+------------+--------------+
| Policy Name | TF | QinQ     | 802.1Qbg | VLAN Scope   | Interfaces | Ref Policies |
+-------------+----+----------+----------+--------------+------------+--------------+
| default     |    | disabled | disabled | Global scope | 177        | 2            | 
+-------------+----+----------+----------+--------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy l2 --apic apic11 --name default

{
    "duration": 1567,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 1071,
        "total_time": 1468
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

True	397	-	connect apic11o.emea-sp.cisco.com
True	311	6	apic11o.emea-sp.cisco.com class l2IfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	435	414	apic11o.emea-sp.cisco.com class l1RsL2IfPolCons
True	325	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyL2.md)