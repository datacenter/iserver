# Node Interface - Physical

## Filter by mac address

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --mac edc3

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Phy - State [#1]
--------------------------

+----------------------+--------+---------+-----------+-------+-----------+------+-----------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| Node                 | Health | Faults  | Interface | Admin | Switching | Oper | Reason    | Type | Layer    | PC  | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+----------------------+--------+---------+-----------+-------+-----------+------+-----------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/19      | up    | enabled   | up   | connected | leaf | switched | po5 | 3C:13:CC:B9:ED:C3 | trunk | 40G   | full   | 9000 | disable-fec | 
+----------------------+--------+---------+-----------+-------+-----------+------+-----------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --mac edc3

{
    "duration": 2365,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 530,
        "disconnect_time": 0,
        "mo_time": 1549,
        "total_time": 2079
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

True	530	-	connect apic21o.emea-sp.cisco.com:443
True	320	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	937	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	292	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)