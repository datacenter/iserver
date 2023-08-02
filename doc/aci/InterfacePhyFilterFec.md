# Node Interface - Physical

## Filter by fec

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --fec cl91*

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Phy - State [#4]
--------------------------

+----------------------+--------+---------+-----------+-------+-----------+------+--------------------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| Node                 | Health | Faults  | Interface | Admin | Switching | Oper | Reason             | Type | Layer    | PC  | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+----------------------+--------+---------+-----------+-------+-----------+------+--------------------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/1       | up    | disabled  | up   | connected          | leaf | switched | po2 | 3C:13:CC:B9:ED:B1 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/2       | up    | disabled  | up   | connected          | leaf | switched | po6 | 3C:13:CC:B9:ED:B2 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/25      | up    | enabled   | up   | connected          | leaf | routed   |     | 3C:13:CC:B9:ED:C9 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/31      | up    | disabled  | down | link-not-connected | fab  | routed   |     | 3C:13:CC:B9:ED:CF | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
+----------------------+--------+---------+-----------+-------+-----------+------+--------------------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --fec cl91*

{
    "duration": 2618,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 560,
        "disconnect_time": 0,
        "mo_time": 1599,
        "total_time": 2159
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

True	560	-	connect apic21o.emea-sp.cisco.com:443
True	399	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	899	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	301	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)