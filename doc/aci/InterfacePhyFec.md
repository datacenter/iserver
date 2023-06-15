# Node Interface - Physical

## Filter by fec

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --fec cl91*

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+-----------+------+-----------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason    | Type | Layer  | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-----------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl205-eu-spdc | 1/24      | up    | enabled   | up   | connected | leaf | routed |    | 4C:71:0D:7E:84:08 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
+---------------------+-----------+-------+-----------+------+-----------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --fec cl91*

{
    "duration": 1435,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 391,
        "disconnect_time": 0,
        "mo_time": 931,
        "total_time": 1322
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

True	391	-	connect apic11o.emea-sp.cisco.com
True	305	13	apic11o.emea-sp.cisco.com class fabricNode
True	301	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	325	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)