# Node

## Filter by name

```
# iserver get aci node --apic apic11 --name bl*

Apic: apic11 (mode:online, cache:off)

+---------------------+---------+--------+-------------+-------------+--------------+------+-----------------+-------------+----------------+
| Node Name           | Node ID | Pod ID | IP Address  | Admin State | Fabric State | Role | Model           | Serial      | Version        |
+---------------------+---------+--------+-------------+-------------+--------------+------+-----------------+-------------+----------------+
| pod-1/bl205-eu-spdc | 205     | 1      | 10.3.192.64 | on          | active       | leaf | N9K-C93600CD-GX | FDO233804F9 | n9000-15.2(7g) | 
| pod-1/bl206-eu-spdc | 206     | 1      | 10.3.32.64  | on          | active       | leaf | N9K-C93600CD-GX | FDO24300ZJH | n9000-15.2(7g) | 
+---------------------+---------+--------+-------------+-------------+--------------+------+-----------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --name bl*

{
    "duration": 915,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 437,
        "disconnect_time": 0,
        "mo_time": 349,
        "total_time": 786
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

True	437	-	connect apic11o.emea-sp.cisco.com
True	349	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./Node.md)