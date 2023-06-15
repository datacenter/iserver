# Node Interface - MACsec

## Filter by port id

```
# iserver get aci intf macsec --apic apic11 --node bl205-eu-spdc --id eth1/28

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
| Node                | Interface | Admin State | Oper State | Reason     | Session State   | Peers | Cepher Suite | Confid Offset | Ker Server Prio | Replay Window |
+---------------------+-----------+-------------+------------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
| pod-1/bl205-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
+---------------------+-----------+-------------+------------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
```

Developer

```
# iserver get aci intf macsec --apic apic11 --node bl205-eu-spdc --id eth1/28

{
    "duration": 1754,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 1194,
        "total_time": 1593
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

True	399	-	connect apic11o.emea-sp.cisco.com
True	323	13	apic11o.emea-sp.cisco.com class fabricNode
True	287	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/macsecIf
True	280	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	304	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
```

[[Back]](./InterfaceMacSec.md)