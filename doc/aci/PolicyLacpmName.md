# Policy - Port Channel Member

## Filter by name

```
# iserver get aci policy lacp-m --apic apic11 --name default

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
# iserver get aci policy lacp-m --apic apic11 --name default

{
    "duration": 1844,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 577,
        "disconnect_time": 0,
        "mo_time": 1054,
        "total_time": 1631
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

True	577	-	connect apic11o.emea-sp.cisco.com
True	323	1	apic11o.emea-sp.cisco.com class lacpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	384	70	apic11o.emea-sp.cisco.com class l1RsLacpIfPolCons
True	347	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLacpm.md)