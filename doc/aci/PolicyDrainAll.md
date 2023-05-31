# Policy - Slow Drain

## Get all policies

```
# iserver get aci policy drain --apic apic11

Apic: apic11

+-------------+----+-------------------------+------------------------------+-------------------+----------------------+------------+--------------+
| Policy Name | TF | Congestion Clear Action | Congestion Detect Multiplier | Flush Admin State | Flush Timeout [msec] | Interfaces | Ref Policies |
+-------------+----+-------------------------+------------------------------+-------------------+----------------------+------------+--------------+
| default     |    | off                     | 10                           | disabled          | 500                  | 344        | 83           | 
+-------------+----+-------------------------+------------------------------+-------------------+----------------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy drain --apic apic11

{
    "duration": 1604,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 419,
        "disconnect_time": 0,
        "mo_time": 1047,
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
    }
}

Log: apic
----------

True	419	-	connect apic11o.emea-sp.cisco.com
True	319	1	apic11o.emea-sp.cisco.com class qosSdIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	403	344	apic11o.emea-sp.cisco.com class l1RsQosSdIfPolCons
True	325	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyDrain.md)