# Node

## IP address specific output

```
# iserver get aci node --apic apic11 --address 10.3.192.68

Apic: apic11 (mode:online, cache:off)

Node - State [#1]
-----------------

+---------------------+---------+-------------+-------------+--------------+------+------------------+-------------+----------------+
| Node Name           | Node ID | VTEP IP     | Admin State | Fabric State | Role | Model            | Serial      | Version        |
+---------------------+---------+-------------+-------------+--------------+------+------------------+-------------+----------------+
| pod-1/cl202-eu-spdc | 202     | 10.3.192.68 | on          | active       | leaf | N9K-C93360YC-FX2 | FDO23350LJY | n9000-15.2(7g) | 
+---------------------+---------+-------------+-------------+--------------+------+------------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --address 10.3.192.68

{
    "duration": 2756,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 407,
        "disconnect_time": 0,
        "mo_time": 612,
        "total_time": 1019
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

True	407	-	connect apic11o.emea-sp.cisco.com:443
True	312	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	300	13	apic11o.emea-sp.cisco.com:443 class topSystem
```

[[Back]](./Node.md)