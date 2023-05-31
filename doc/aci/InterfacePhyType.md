# Node Interface - Physical

## Filter by type

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --type fab

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+-----------+------+-------------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason      | Type | Layer  | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-------------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl205-eu-spdc | 1/29      | up    | disabled  | down | sfp-missing | fab  | routed |    | 4C:71:0D:7E:84:0D | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/30      | up    | disabled  | down | sfp-missing | fab  | routed |    | 4C:71:0D:7E:84:0E | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/31      | up    | disabled  | down | sfp-missing | fab  | routed |    | 4C:71:0D:7E:84:0F | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/32      | up    | disabled  | down | sfp-missing | fab  | routed |    | 4C:71:0D:7E:84:10 | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/33      | up    | disabled  | down | sfp-missing | fab  | routed |    | 4C:71:0D:7E:84:11 | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/34      | up    | disabled  | down | sfp-missing | fab  | routed |    | 4C:71:0D:7E:84:12 | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/35      | up    | enabled   | up   | connected   | fab  | routed |    | 4C:71:0D:7E:84:13 | trunk | 400G  | full   | 9366 | kp-fec      | 
| pod-1/bl205-eu-spdc | 1/36      | up    | enabled   | up   | connected   | fab  | routed |    | 4C:71:0D:7E:84:14 | trunk | 400G  | full   | 9366 | kp-fec      | 
+---------------------+-----------+-------+-----------+------+-------------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --type fab

{
    "duration": 1462,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 398,
        "disconnect_time": 0,
        "mo_time": 921,
        "total_time": 1319
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

True	398	-	connect apic11o.emea-sp.cisco.com
True	298	11	apic11o.emea-sp.cisco.com class fabricNode
True	312	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	311	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)