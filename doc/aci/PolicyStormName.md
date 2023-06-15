# Policy - Storm Control

## Filter by name

```
# iserver get aci policy storm --apic apic11 --name default

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
# iserver get aci policy storm --apic apic11 --name default

{
    "duration": 2039,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 442,
        "disconnect_time": 0,
        "mo_time": 1140,
        "total_time": 1582
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
True	351	1	apic11o.emea-sp.cisco.com class stormctrlIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	440	470	apic11o.emea-sp.cisco.com class l1RsStormctrlIfPolCons
True	349	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyStorm.md)