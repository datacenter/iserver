# Policy - Port Security

## Filter by name

```
# iserver get aci policy portsec --apic apic11 --name default

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
# iserver get aci policy portsec --apic apic11 --name default

{
    "duration": 1596,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 402,
        "disconnect_time": 0,
        "mo_time": 1038,
        "total_time": 1440
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

True	402	-	connect apic11o.emea-sp.cisco.com
True	314	1	apic11o.emea-sp.cisco.com class l2PortSecurityPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	416	414	apic11o.emea-sp.cisco.com class l1RsL2PortSecurityCons
True	308	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyPortsec.md)