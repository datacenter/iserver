# Node Interface - Physical

## Filter by layer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --layer l3

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Phy - State [#9]
--------------------------

+----------------------+--------+---------+-----------+-------+-----------+------+--------------------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| Node                 | Health | Faults  | Interface | Admin | Switching | Oper | Reason             | Type | Layer  | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+----------------------+--------+---------+-----------+-------+-----------+------+--------------------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/25      | up    | enabled   | up   | connected          | leaf | routed |    | 3C:13:CC:B9:ED:C9 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
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
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --layer l3

{
    "duration": 2486,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 421,
        "disconnect_time": 0,
        "mo_time": 1612,
        "total_time": 2033
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

True	421	-	connect apic21o.emea-sp.cisco.com:443
True	315	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	976	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	321	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)