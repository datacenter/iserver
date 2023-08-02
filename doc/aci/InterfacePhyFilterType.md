# Node Interface - Physical

## Filter by type

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --type fab

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Phy - State [#8]
--------------------------

+----------------------+--------+---------+-----------+-------+-----------+------+--------------------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| Node                 | Health | Faults  | Interface | Admin | Switching | Oper | Reason             | Type | Layer  | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+----------------------+--------+---------+-----------+-------+-----------+------+--------------------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/29      | up    | disabled  | down | sfp-missing        | fab  | routed |    | 3C:13:CC:B9:ED:CD | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/30      | up    | disabled  | down | sfp-missing        | fab  | routed |    | 3C:13:CC:B9:ED:CE | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/31      | up    | disabled  | down | link-not-connected | fab  | routed |    | 3C:13:CC:B9:ED:CF | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/32      | up    | disabled  | down | sfp-missing        | fab  | routed |    | 3C:13:CC:B9:ED:D0 | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/33      | up    | disabled  | down | sfp-missing        | fab  | routed |    | 3C:13:CC:B9:ED:D1 | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/34      | up    | disabled  | down | sfp-missing        | fab  | routed |    | 3C:13:CC:B9:ED:D2 | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/35      | up    | enabled   | up   | connected          | fab  | routed |    | 3C:13:CC:B9:ED:D3 | trunk | 400G  | full   | 9366 | kp-fec      | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/36      | up    | enabled   | up   | connected          | fab  | routed |    | 3C:13:CC:B9:ED:D4 | trunk | 400G  | full   | 9366 | kp-fec      | 
+----------------------+--------+---------+-----------+-------+-----------+------+--------------------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --type fab

{
    "duration": 2280,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 430,
        "disconnect_time": 0,
        "mo_time": 1533,
        "total_time": 1963
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

True	430	-	connect apic21o.emea-sp.cisco.com:443
True	338	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	909	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	286	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)