# Node

## Temperature specific output

```
# iserver get aci node --apic apic11 --view temp --name bl205*

Apic: apic11 (mode:online, cache:off)

+---------------------+--------------------+-----+------+-----+
| Node                | Sensor             | Avg | Last | Max |
+---------------------+--------------------+-----+------+-----+
| pod-1/bl205-eu-spdc | supslot-1.sensor-1 | 21  | 21   | 21  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-2 | 27  | 27   | 27  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-3 | 32  | 32   | 32  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-4 | 48  | 48   | 48  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-5 | 37  | 37   | 37  | 
+---------------------+--------------------+-----+------+-----+
```

Developer

```
# iserver get aci node --apic apic11 --view temp --name bl205*

{
    "duration": 2026,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 527,
        "disconnect_time": 0,
        "mo_time": 1288,
        "total_time": 1815
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

True	527	-	connect apic11o.emea-sp.cisco.com:443
True	403	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	885	1996	apic11o.emea-sp.cisco.com:443 class eqptTemp
```

[[Back]](./Node.md)