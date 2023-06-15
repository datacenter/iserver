# Policy - Storm Control

## Get all policies

```
# iserver get aci policy storm --apic apic11

Apic: apic11 (mode:online, cache:off)

+-------------+-------+-------------+------------+----------------+-------------+------------------+----------------------+------------+-----------+--------------+
| Policy Name | TF    | Packet Type | Rate [%]   | Burst Rate [%] | Rate [pps]  | Burst Rate [pps] | Storm Control Action | Storm Soak | Instances | Ref Policies |
+-------------+-------+-------------+------------+----------------+-------------+------------------+----------------------+------------+-----------+--------------+
| default     | False | all         | 100.000000 | 100.000000     | unspecified | unspecified      | drop                 | 3          | 470       | 83           | 
+-------------+-------+-------------+------------+----------------+-------------+------------------+----------------------+------------+-----------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy storm --apic apic11

{
    "duration": 1786,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 408,
        "disconnect_time": 0,
        "mo_time": 1035,
        "total_time": 1443
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

True	408	-	connect apic11o.emea-sp.cisco.com
True	340	1	apic11o.emea-sp.cisco.com class stormctrlIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	387	470	apic11o.emea-sp.cisco.com class l1RsStormctrlIfPolCons
True	308	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyStorm.md)