# Policy - Slow Drain

## Get all policies

```
# iserver get aci policy drain --apic apic11

Apic: apic11 (mode:online, cache:off)

+-------------+----+-------------------------+------------------------------+-------------------+----------------------+------------+--------------+
| Policy Name | TF | Congestion Clear Action | Congestion Detect Multiplier | Flush Admin State | Flush Timeout [msec] | Interfaces | Ref Policies |
+-------------+----+-------------------------+------------------------------+-------------------+----------------------+------------+--------------+
| default     |    | off                     | 10                           | disabled          | 500                  | 400        | 83           | 
+-------------+----+-------------------------+------------------------------+-------------------+----------------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy drain --apic apic11

{
    "duration": 2619,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 1793,
        "total_time": 2215
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

True	422	-	connect apic11o.emea-sp.cisco.com
True	1075	1	apic11o.emea-sp.cisco.com class qosSdIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	387	400	apic11o.emea-sp.cisco.com class l1RsQosSdIfPolCons
True	331	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyDrain.md)