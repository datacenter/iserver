# Node Interface - MACsec

## Filter by port id

```
# iserver get aci intf macsec --apic apic11 --node bl205-eu-spdc --id eth1/28

Apic: apic11o.emea-sp.cisco.com
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
    "duration": 2040,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 487,
        "disconnect_time": 0,
        "mo_time": 1358,
        "total_time": 1845
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
    }
}

Log: apic
----------

True	487	-	connect apic11o.emea-sp.cisco.com
True	300	11	apic11o.emea-sp.cisco.com class fabricNode
True	300	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/macsecIf
True	307	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	451	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
```

[[Back]](./InterfaceMacSec.md)