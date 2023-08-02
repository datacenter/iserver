# Node

## Filter by node id

```
# iserver get aci node --apic apic11 --id 101

Apic: apic11 (mode:online, cache:off)

Node - State [#1]
-----------------

+--------------------+---------+-------------+-------------+--------------+-------+---------------+-------------+----------------+
| Node Name          | Node ID | VTEP IP     | Admin State | Fabric State | Role  | Model         | Serial      | Version        |
+--------------------+---------+-------------+-------------+--------------+-------+---------------+-------------+----------------+
| pod-1/s101-eu-spdc | 101     | 10.3.192.65 | on          | active       | spine | N9K-C9316D-GX | FDO233806C2 | n9000-15.2(7g) | 
+--------------------+---------+-------------+-------------+--------------+-------+---------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --id 101

{
    "duration": 1056,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 437,
        "disconnect_time": 0,
        "mo_time": 347,
        "total_time": 784
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

True	437	-	connect apic11o.emea-sp.cisco.com:443
True	347	13	apic11o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./Node.md)