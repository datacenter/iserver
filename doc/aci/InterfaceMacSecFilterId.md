# Node Interface - MACsec

## Filter by port id

```
# iserver get aci intf macsec --apic apic21 --node bl2205-eu-spdc --id eth1/28

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface MacSec - State [#1]
-----------------------------

+----------------------+--------+---------+-----------+----------+------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
| Node                 | Health | Faults  | Interface | Admin    | Oper | Reason     | Session         | Peers | Cepher Suite | Confid Offset | Ker Server Prio | Replay Window |
+----------------------+--------+---------+-----------+----------+------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/28   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
+----------------------+--------+---------+-----------+----------+------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
```

Developer

```
# iserver get aci intf macsec --apic apic21 --node bl2205-eu-spdc --id eth1/28

{
    "duration": 3779,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 573,
        "disconnect_time": 0,
        "mo_time": 2731,
        "total_time": 3304
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

True	573	-	connect apic21o.emea-sp.cisco.com:443
True	480	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	652	28	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1175	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	424	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
```

[[Back]](./InterfaceMacSec.md)