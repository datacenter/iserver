# Policy - Slow Drain

## Filter by name

```
# iserver get aci policy drain --apic apic11 --name default

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
# iserver get aci policy drain --apic apic11 --name default

{
    "duration": 1590,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 400,
        "disconnect_time": 0,
        "mo_time": 1056,
        "total_time": 1456
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

True	400	-	connect apic11o.emea-sp.cisco.com
True	330	1	apic11o.emea-sp.cisco.com class qosSdIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	419	344	apic11o.emea-sp.cisco.com class l1RsQosSdIfPolCons
True	307	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyDrain.md)