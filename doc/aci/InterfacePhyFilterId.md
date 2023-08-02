# Node Interface - Physical

## Filter by id

Example: single id

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --id 1/24

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Phy - State [#1]
--------------------------

+----------------------+--------+---------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| Node                 | Health | Faults  | Interface | Admin | Switching | Oper | Reason      | Type | Layer    | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+----------------------+--------+---------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/24      | up    | disabled  | down | sfp-missing | leaf | switched |    | 3C:13:CC:B9:ED:C8 | trunk | 100G  | full   | 9000 | disable-fec | 
+----------------------+--------+---------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Example: id pattern

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --id 1/2*

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Phy - State [#11]
---------------------------

+----------------------+--------+---------+-----------+-------+-----------+------+-------------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| Node                 | Health | Faults  | Interface | Admin | Switching | Oper | Reason      | Type | Layer    | PC  | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+----------------------+--------+---------+-----------+-------+-----------+------+-------------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/2       | up    | disabled  | up   | connected   | leaf | switched | po6 | 3C:13:CC:B9:ED:B2 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/20      | up    | disabled  | down | sfp-missing | leaf | switched |     | 3C:13:CC:B9:ED:C4 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/21      | up    | disabled  | down | sfp-missing | leaf | switched |     | 3C:13:CC:B9:ED:C5 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/22      | up    | disabled  | down | sfp-missing | leaf | switched |     | 3C:13:CC:B9:ED:C6 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/23      | up    | disabled  | down | sfp-missing | leaf | switched |     | 3C:13:CC:B9:ED:C7 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/24      | up    | disabled  | down | sfp-missing | leaf | switched |     | 3C:13:CC:B9:ED:C8 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/25      | up    | enabled   | up   | connected   | leaf | routed   |     | 3C:13:CC:B9:ED:C9 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/26      | up    | disabled  | down | sfp-missing | leaf | switched |     | 3C:13:CC:B9:ED:CA | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/27      | up    | disabled  | up   | connected   | leaf | switched | po1 | 3C:13:CC:B9:ED:CB | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/28      | up    | disabled  | down | sfp-missing | leaf | switched |     | 3C:13:CC:B9:ED:CC | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 1/29      | up    | disabled  | down | sfp-missing | fab  | routed   |     | 3C:13:CC:B9:ED:CD | trunk | 400G  | full   | 9366 | disable-fec | 
+----------------------+--------+---------+-----------+-------+-----------+------+-------------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --id 1/24

{
    "duration": 2326,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 385,
        "disconnect_time": 0,
        "mo_time": 1609,
        "total_time": 1994
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

True	385	-	connect apic21o.emea-sp.cisco.com:443
True	328	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	978	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	303	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)