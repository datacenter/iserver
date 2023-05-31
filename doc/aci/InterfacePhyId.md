# Node Interface - Physical

## Filter by id

Example: single id

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --id 1/24

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+-----------+------+-----------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason    | Type | Layer  | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-----------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl205-eu-spdc | 1/24      | up    | enabled   | up   | connected | leaf | routed |    | 4C:71:0D:7E:84:08 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
+---------------------+-----------+-------+-----------+------+-----------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Example: id pattern

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --id 1/2*

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+-----------+------+-------------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason      | Type | Layer    | PC  | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-------------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl205-eu-spdc | 1/2       | up    | enabled   | up   | connected   | leaf | switched | po3 | 4C:71:0D:7E:83:F2 | trunk | 40G   | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/20      | up    | disabled  | down | sfp-missing | leaf | switched |     | 4C:71:0D:7E:84:04 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/21      | up    | disabled  | down | sfp-missing | leaf | switched |     | 4C:71:0D:7E:84:05 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/22      | up    | disabled  | down | sfp-missing | leaf | switched |     | 4C:71:0D:7E:84:06 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/23      | up    | disabled  | down | sfp-missing | leaf | switched |     | 4C:71:0D:7E:84:07 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/24      | up    | enabled   | up   | connected   | leaf | routed   |     | 4C:71:0D:7E:84:08 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
| pod-1/bl205-eu-spdc | 1/25      | up    | disabled  | down | sfp-missing | leaf | switched |     | 4C:71:0D:7E:84:09 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/26      | up    | disabled  | down | sfp-missing | leaf | switched |     | 4C:71:0D:7E:84:0A | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/27      | up    | enabled   | up   | connected   | leaf | switched | po2 | 4C:71:0D:7E:84:0B | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/28      | up    | enabled   | up   | connected   | leaf | routed   |     | 4C:71:0D:7E:84:0C | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/29      | up    | disabled  | down | sfp-missing | fab  | routed   |     | 4C:71:0D:7E:84:0D | trunk | 400G  | full   | 9366 | disable-fec | 
+---------------------+-----------+-------+-----------+------+-------------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --id 1/24

{
    "duration": 1732,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 553,
        "disconnect_time": 0,
        "mo_time": 1015,
        "total_time": 1568
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

True	553	-	connect apic11o.emea-sp.cisco.com
True	303	11	apic11o.emea-sp.cisco.com class fabricNode
True	343	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	369	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)