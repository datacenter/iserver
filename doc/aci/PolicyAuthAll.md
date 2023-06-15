# Policy - 802.1X

## Get all policies

```
# iserver get aci policy auth --apic apic11

Apic: apic11 (mode:online, cache:off)

+-------------+----+-------------+-------------+------------+--------------+
| Policy Name | TF | Admin State | Host Mode   | Interfaces | Ref Policies |
+-------------+----+-------------+-------------+------------+--------------+
| default     |    | disabled    | single-host | 0          | 83           | 
+-------------+----+-------------+-------------+------------+--------------+
```

Developer

```
# iserver get aci policy auth --apic apic11

{
    "duration": 1292,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 442,
        "disconnect_time": 0,
        "mo_time": 708,
        "total_time": 1150
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

True	442	-	connect apic11o.emea-sp.cisco.com
True	341	1	apic11o.emea-sp.cisco.com class l2PortAuthPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	367	0	apic11o.emea-sp.cisco.com class l1RsL2PortAuthCons
```

[[Back]](./PolicyAuth.md)