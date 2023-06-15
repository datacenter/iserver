# Node

## Filter by ip subnet

```
# iserver get aci node --apic apic11 --node-subnet 172.16.0.0/16

Apic: apic11 (mode:online, cache:off)

+---------------------+---------+--------+---------------+-------------+--------------+-------------+----------------+-------------+----------------+
| Node Name           | Node ID | Pod ID | IP Address    | Admin State | Fabric State | Role        | Model          | Serial      | Version        |
+---------------------+---------+--------+---------------+-------------+--------------+-------------+----------------+-------------+----------------+
| pod-1/rl301-eu-spdc | 301     | 1      | 172.16.30.160 | on          | active       | remote leaf | N9K-C9336C-FX2 | FDO2346137N | n9000-15.2(7g) | 
| pod-1/rl302-eu-spdc | 302     | 1      | 172.16.30.120 | on          | active       | remote leaf | N9K-C9336C-FX2 | FDO234613DB | n9000-15.2(7g) | 
+---------------------+---------+--------+---------------+-------------+--------------+-------------+----------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --node-subnet 172.16.0.0/16

{
    "duration": 975,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 445,
        "disconnect_time": 0,
        "mo_time": 336,
        "total_time": 781
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
True	336	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./Node.md)