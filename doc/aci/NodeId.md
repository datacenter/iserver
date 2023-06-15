# Node

## Filter by node id

```
# iserver get aci node --apic apic11 --id 101

Apic: apic11 (mode:online, cache:off)

+--------------------+---------+--------+-------------+-------------+--------------+-------+---------------+-------------+----------------+
| Node Name          | Node ID | Pod ID | IP Address  | Admin State | Fabric State | Role  | Model         | Serial      | Version        |
+--------------------+---------+--------+-------------+-------------+--------------+-------+---------------+-------------+----------------+
| pod-1/s101-eu-spdc | 101     | 1      | 10.3.192.65 | on          | active       | spine | N9K-C9316D-GX | FDO233806C2 | n9000-15.2(7g) | 
+--------------------+---------+--------+-------------+-------------+--------------+-------+---------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --id 101

{
    "duration": 897,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 339,
        "total_time": 766
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

True	427	-	connect apic11o.emea-sp.cisco.com
True	339	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./Node.md)