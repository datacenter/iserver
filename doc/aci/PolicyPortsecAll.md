# Policy - Port Security

## Get all policies

```
# iserver get aci policy portsec --apic apic11

Apic: apic11

+-------------+----+---------+-------------------+------------------+------------+--------------+
| Policy Name | TF | Timeout | Maximum Endpoints | Violation Action | Interfaces | Ref Policies |
+-------------+----+---------+-------------------+------------------+------------+--------------+
| default     |    | 60      | 0                 | protect          | 414        | 83           | 
+-------------+----+---------+-------------------+------------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy portsec --apic apic11

{
    "duration": 1552,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 1033,
        "total_time": 1432
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

True	399	-	connect apic11o.emea-sp.cisco.com
True	311	1	apic11o.emea-sp.cisco.com class l2PortSecurityPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	425	414	apic11o.emea-sp.cisco.com class l1RsL2PortSecurityCons
True	297	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyPortsec.md)