# Node

## Filter by ip subnet

```
# iserver get aci node --apic apic11 --subnet 172.16.0.0/16

Apic: apic11 (mode:online, cache:off)

Node - State [#2]
-----------------

+---------------------+---------+---------------+-------------+--------------+-------------+----------------+-------------+----------------+
| Node Name           | Node ID | VTEP IP       | Admin State | Fabric State | Role        | Model          | Serial      | Version        |
+---------------------+---------+---------------+-------------+--------------+-------------+----------------+-------------+----------------+
| pod-1/rl301-eu-spdc | 301     | 172.16.30.160 | on          | active       | remote leaf | N9K-C9336C-FX2 | FDO2346137N | n9000-15.2(7g) | 
| pod-1/rl302-eu-spdc | 302     | 172.16.30.120 | on          | active       | remote leaf | N9K-C9336C-FX2 | FDO234613DB | n9000-15.2(7g) | 
+---------------------+---------+---------------+-------------+--------------+-------------+----------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --subnet 172.16.0.0/16

{
    "duration": 1214,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 417,
        "disconnect_time": 0,
        "mo_time": 597,
        "total_time": 1014
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

True	417	-	connect apic11o.emea-sp.cisco.com:443
True	302	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	295	13	apic11o.emea-sp.cisco.com:443 class topSystem
```

[[Back]](./Node.md)