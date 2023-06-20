# Node

## Filter by name

```
# iserver get aci node --apic apic11 --name bl*

Apic: apic11 (mode:online, cache:off)

+---------------------+---------+-------------+-------------+--------------+------+-----------------+-------------+----------------+
| Node Name           | Node ID | VTEP IP     | Admin State | Fabric State | Role | Model           | Serial      | Version        |
+---------------------+---------+-------------+-------------+--------------+------+-----------------+-------------+----------------+
| pod-1/bl205-eu-spdc | 205     | 10.3.192.64 | on          | active       | leaf | N9K-C93600CD-GX | FDO233804F9 | n9000-15.2(7g) | 
| pod-1/bl206-eu-spdc | 206     | 10.3.32.64  | on          | active       | leaf | N9K-C93600CD-GX | FDO24300ZJH | n9000-15.2(7g) | 
+---------------------+---------+-------------+-------------+--------------+------+-----------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --name bl*

{
    "duration": 1005,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 460,
        "disconnect_time": 0,
        "mo_time": 368,
        "total_time": 828
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

True	460	-	connect apic11o.emea-sp.cisco.com:443
True	368	13	apic11o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./Node.md)