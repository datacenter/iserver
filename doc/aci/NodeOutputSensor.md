# Node

## Sensor specific output

```
# iserver get aci node --apic apic11 --view sensor --name bl205*

Apic: apic11

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
    "duration": 1893,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 436,
        "disconnect_time": 0,
        "mo_time": 1323,
        "total_time": 1759
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

True	436	-	connect apic11o.emea-sp.cisco.com
True	1012	11	apic11o.emea-sp.cisco.com class fabricNode
True	311	121	apic11o.emea-sp.cisco.com class eqptSensor
```

[[Back]](./Node.md)