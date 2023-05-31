# Node

## Temperature specific output

```
# iserver get aci node --apic apic11 --view temp --name bl205*

Apic: apic11

+---------------------+--------------------+-----+------+-----+
| Node                | Sensor             | Avg | Last | Max |
+---------------------+--------------------+-----+------+-----+
| pod-1/bl205-eu-spdc | supslot-1.sensor-1 | 20  | 20   | 20  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-1 | 20  | 20   | 20  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-2 | 26  | 26   | 26  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-2 | 26  | 26   | 26  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-3 | 31  | 31   | 31  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-3 | 31  | 31   | 31  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-4 | 47  | 47   | 47  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-4 | 47  | 47   | 47  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-5 | 36  | 36   | 36  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-5 | 36  | 36   | 36  | 
+---------------------+--------------------+-----+------+-----+
```

Developer

```
# iserver get aci node --apic apic11 --view temp --name bl205*

{
    "duration": 1755,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 423,
        "disconnect_time": 0,
        "mo_time": 1135,
        "total_time": 1558
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

True	423	-	connect apic11o.emea-sp.cisco.com
True	349	11	apic11o.emea-sp.cisco.com class fabricNode
True	786	1856	apic11o.emea-sp.cisco.com class eqptTemp
```

[[Back]](./Node.md)