# Node

## Filter by model

```
# iserver get aci node --apic apic11 --model *c9336*

Apic: apic11 (mode:online, cache:off)

Node - State [#4]
-----------------

+---------------------+---------+---------------+-------------+--------------+-------------+------------------+-------------+----------------+
| Node Name           | Node ID | VTEP IP       | Admin State | Fabric State | Role        | Model            | Serial      | Version        |
+---------------------+---------+---------------+-------------+--------------+-------------+------------------+-------------+----------------+
| pod-1/cl201-eu-spdc | 201     | 10.3.192.67   | on          | active       | leaf        | N9K-C93360YC-FX2 | FDO23350LNB | n9000-15.2(7g) | 
| pod-1/cl202-eu-spdc | 202     | 10.3.192.68   | on          | active       | leaf        | N9K-C93360YC-FX2 | FDO23350LJY | n9000-15.2(7g) | 
| pod-1/rl301-eu-spdc | 301     | 172.16.30.160 | on          | active       | remote leaf | N9K-C9336C-FX2   | FDO2346137N | n9000-15.2(7g) | 
| pod-1/rl302-eu-spdc | 302     | 172.16.30.120 | on          | active       | remote leaf | N9K-C9336C-FX2   | FDO234613DB | n9000-15.2(7g) | 
+---------------------+---------+---------------+-------------+--------------+-------------+------------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --model *c9336*

{
    "duration": 793,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 408,
        "disconnect_time": 0,
        "mo_time": 293,
        "total_time": 701
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

True	408	-	connect apic11o.emea-sp.cisco.com:443
True	293	13	apic11o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./Node.md)