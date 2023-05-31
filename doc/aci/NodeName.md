# Node

## Filter by name

```
# iserver get aci node --apic apic11 --name bl*

Apic: apic11

+---------------------+---------+--------+-------------+-------------+--------------+------+-----------------+-------------+----------------+
| Node Name           | Node ID | Pod ID | IP Address  | Admin State | Fabric State | Role | Model           | Serial      | Version        |
+---------------------+---------+--------+-------------+-------------+--------------+------+-----------------+-------------+----------------+
| pod-1/bl205-eu-spdc | 205     | 1      | 10.3.192.64 | on          | active       | leaf | N9K-C93600CD-GX | FDO233804F9 | n9000-15.2(7f) | 
| pod-1/bl206-eu-spdc | 206     | 1      | 10.3.32.64  | on          | active       | leaf | N9K-C93600CD-GX | FDO24300ZJH | n9000-15.2(7f) | 
+---------------------+---------+--------+-------------+-------------+--------------+------+-----------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --name bl*

{
    "duration": 825,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 396,
        "disconnect_time": 0,
        "mo_time": 311,
        "total_time": 707
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

True	396	-	connect apic11o.emea-sp.cisco.com
True	311	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./Node.md)