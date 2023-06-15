# Policy - Port Channel Member

## Get all policies

```
# iserver get aci policy lacp-m --apic apic11

Apic: apic11 (mode:online, cache:off)

+-------------+----+----------+---------------+------------+--------------+
| Policy Name | TF | Priority | Transmit Rate | Interfaces | Ref Policies |
+-------------+----+----------+---------------+------------+--------------+
| default     |    | 32768    | normal        | 70         | 1            | 
+-------------+----+----------+---------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy lacp-m --apic apic11

{
    "duration": 1694,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 401,
        "disconnect_time": 0,
        "mo_time": 1039,
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
    },
    "cache_hits": 0
}

Log: apic
----------

True	401	-	connect apic11o.emea-sp.cisco.com
True	337	1	apic11o.emea-sp.cisco.com class lacpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	375	70	apic11o.emea-sp.cisco.com class l1RsLacpIfPolCons
True	327	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLacpm.md)