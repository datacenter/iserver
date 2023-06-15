# Policy - Slow Drain

## Filter by name

```
# iserver get aci policy drain --apic apic11 --name default

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
# iserver get aci policy drain --apic apic11 --name default

{
    "duration": 1816,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 421,
        "disconnect_time": 0,
        "mo_time": 1045,
        "total_time": 1466
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

True	421	-	connect apic11o.emea-sp.cisco.com
True	340	1	apic11o.emea-sp.cisco.com class qosSdIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	376	400	apic11o.emea-sp.cisco.com class l1RsQosSdIfPolCons
True	329	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyDrain.md)