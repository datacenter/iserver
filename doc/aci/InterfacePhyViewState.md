# Node Interface - Physical

## Default state focused output

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Phy - State [#36]
---------------------------

+----------------------+--------+---------+-----------+-------+-----------+------+--------------------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| Node                 | Health | Faults  | Interface | Admin | Switching | Oper | Reason             | Type | Layer    | PC  | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+----------------------+--------+---------+-----------+-------+-----------+------+--------------------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/1       | up    | disabled  | up   | connected          | leaf | switched | po2 | 3C:13:CC:B9:ED:B1 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/2       | up    | disabled  | up   | connected          | leaf | switched | po6 | 3C:13:CC:B9:ED:B2 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/3       | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:B3 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/4       | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:B4 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/5       | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:B5 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/6       | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:B6 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/7       | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:B7 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/8       | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:B8 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/9       | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:B9 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/10      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:BA | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/11      | up    | disabled  | up   | connected          | leaf | switched | po4 | 3C:13:CC:B9:ED:BB | trunk | 40G   | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/12      | up    | disabled  | up   | connected          | leaf | switched | po3 | 3C:13:CC:B9:ED:BC | trunk | 40G   | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/13      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:BD | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/14      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:BE | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/15      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:BF | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/16      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:C0 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/17      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:C1 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/18      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:C2 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/19      | up    | enabled   | up   | connected          | leaf | switched | po5 | 3C:13:CC:B9:ED:C3 | trunk | 40G   | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/20      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:C4 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/21      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:C5 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/22      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:C6 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/23      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:C7 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/24      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:C8 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/25      | up    | enabled   | up   | connected          | leaf | routed   |     | 3C:13:CC:B9:ED:C9 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/26      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:CA | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/27      | up    | disabled  | up   | connected          | leaf | switched | po1 | 3C:13:CC:B9:ED:CB | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/28      | up    | disabled  | down | sfp-missing        | leaf | switched |     | 3C:13:CC:B9:ED:CC | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/29      | up    | disabled  | down | sfp-missing        | fab  | routed   |     | 3C:13:CC:B9:ED:CD | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/30      | up    | disabled  | down | sfp-missing        | fab  | routed   |     | 3C:13:CC:B9:ED:CE | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/31      | up    | disabled  | down | link-not-connected | fab  | routed   |     | 3C:13:CC:B9:ED:CF | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/32      | up    | disabled  | down | sfp-missing        | fab  | routed   |     | 3C:13:CC:B9:ED:D0 | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/33      | up    | disabled  | down | sfp-missing        | fab  | routed   |     | 3C:13:CC:B9:ED:D1 | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/34      | up    | disabled  | down | sfp-missing        | fab  | routed   |     | 3C:13:CC:B9:ED:D2 | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/35      | up    | enabled   | up   | connected          | fab  | routed   |     | 3C:13:CC:B9:ED:D3 | trunk | 400G  | full   | 9366 | kp-fec      | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/36      | up    | enabled   | up   | connected          | fab  | routed   |     | 3C:13:CC:B9:ED:D4 | trunk | 400G  | full   | 9366 | kp-fec      | 
+----------------------+--------+---------+-----------+-------+-----------+------+--------------------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc

{
    "duration": 2796,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 533,
        "disconnect_time": 0,
        "mo_time": 1758,
        "total_time": 2291
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

True	533	-	connect apic21o.emea-sp.cisco.com:443
True	325	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1071	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	362	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)