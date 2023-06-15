# Node

## IP address specific output

```
# iserver get aci node --apic apic11 --node-ip 10.3.192.68

Apic: apic11 (mode:online, cache:off)

+---------------------+---------+--------+-------------+-------------+--------------+------+------------------+-------------+----------------+
| Node Name           | Node ID | Pod ID | IP Address  | Admin State | Fabric State | Role | Model            | Serial      | Version        |
+---------------------+---------+--------+-------------+-------------+--------------+------+------------------+-------------+----------------+
| pod-1/cl202-eu-spdc | 202     | 1      | 10.3.192.68 | on          | active       | leaf | N9K-C93360YC-FX2 | FDO23350LJY | n9000-15.2(7g) | 
+---------------------+---------+--------+-------------+-------------+--------------+------+------------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --node-ip 10.3.192.68

{
    "duration": 935,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 445,
        "disconnect_time": 0,
        "mo_time": 331,
        "total_time": 776
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

True	445	-	connect apic11o.emea-sp.cisco.com
True	331	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./Node.md)