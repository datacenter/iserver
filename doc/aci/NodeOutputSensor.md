# Node

## Sensor specific output

```
# iserver get aci node --apic apic11 --view sensor --name bl205*

Apic: apic11 (mode:online, cache:off)

Node - Sensor [#1]
------------------

+---------------------+---------------+--------+-------+-----+-----+------------+
| Node                | Sensor        | Type   | Value | Min | Max | Oper State |
+---------------------+---------------+--------+-------+-----+-----+------------+
| pod-1/bl205-eu-spdc | Inlet         | inlet  | 0     | 42  | 70  | normal     | 
| pod-1/bl205-eu-spdc | Outlet        | outlet | 0     | 70  | 80  | normal     | 
| pod-1/bl205-eu-spdc | Wolfridge     | asic   | 0     | 100 | 110 | normal     | 
| pod-1/bl205-eu-spdc | Wolfridge vrm | asic   | 0     | 90  | 120 | normal     | 
| pod-1/bl205-eu-spdc | x86 processor | cpu    | 0     | 80  | 105 | normal     | 
+---------------------+---------------+--------+-------+-----+-----+------------+
```

Developer

```
# iserver get aci node --apic apic11 --view sensor --name bl205*

{
    "duration": 1107,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 596,
        "total_time": 990
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

True	394	-	connect apic11o.emea-sp.cisco.com:443
True	292	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	304	131	apic11o.emea-sp.cisco.com:443 class eqptSensor
```

[[Back]](./Node.md)