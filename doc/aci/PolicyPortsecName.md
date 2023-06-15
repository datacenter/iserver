# Policy - Port Security

## Filter by name

```
# iserver get aci policy portsec --apic apic11 --name default

Apic: apic11 (mode:online, cache:off)

+-------------+----+---------+-------------------+------------------+------------+--------------+
| Policy Name | TF | Timeout | Maximum Endpoints | Violation Action | Interfaces | Ref Policies |
+-------------+----+---------+-------------------+------------------+------------+--------------+
| default     |    | 60      | 0                 | protect          | 470        | 83           | 
+-------------+----+---------+-------------------+------------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy portsec --apic apic11 --name default

{
    "duration": 1655,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 393,
        "disconnect_time": 0,
        "mo_time": 974,
        "total_time": 1367
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

True	393	-	connect apic11o.emea-sp.cisco.com
True	317	1	apic11o.emea-sp.cisco.com class l2PortSecurityPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	369	470	apic11o.emea-sp.cisco.com class l1RsL2PortSecurityCons
True	288	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyPortsec.md)