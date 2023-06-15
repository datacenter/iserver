# Node Interface - Physical

## Filter by operational state

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --oper down

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+-----------+------+--------------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason             | Type | Layer    | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+--------------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl205-eu-spdc | 1/3       | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:83:F3 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/4       | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:83:F4 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/5       | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:83:F5 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/6       | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:83:F6 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/7       | up    | disabled  | down | link-not-connected | leaf | switched |    | 4C:71:0D:7E:83:F7 | trunk | 40G   | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/8       | up    | disabled  | down | link-not-connected | leaf | switched |    | 4C:71:0D:7E:83:F8 | trunk | 40G   | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/9       | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:83:F9 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/10      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:83:FA | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/13      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:83:FD | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/14      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:83:FE | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/17      | up    | enabled   | down | link-not-connected | leaf | switched |    | 4C:71:0D:7E:84:01 | trunk | 40G   | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/18      | up    | enabled   | down | link-not-connected | leaf | switched |    | 4C:71:0D:7E:84:02 | trunk | 40G   | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/20      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:84:04 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/21      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:84:05 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/22      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:84:06 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/23      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:84:07 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/25      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:84:09 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/26      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:7E:84:0A | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/29      | up    | disabled  | down | sfp-missing        | fab  | routed   |    | 4C:71:0D:7E:84:0D | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/30      | up    | disabled  | down | sfp-missing        | fab  | routed   |    | 4C:71:0D:7E:84:0E | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/31      | up    | disabled  | down | sfp-missing        | fab  | routed   |    | 4C:71:0D:7E:84:0F | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/32      | up    | disabled  | down | sfp-missing        | fab  | routed   |    | 4C:71:0D:7E:84:10 | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/33      | up    | disabled  | down | sfp-missing        | fab  | routed   |    | 4C:71:0D:7E:84:11 | trunk | 400G  | full   | 9366 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/34      | up    | disabled  | down | sfp-missing        | fab  | routed   |    | 4C:71:0D:7E:84:12 | trunk | 400G  | full   | 9366 | disable-fec | 
+---------------------+-----------+-------+-----------+------+--------------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --oper down

{
    "duration": 2360,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 425,
        "disconnect_time": 0,
        "mo_time": 956,
        "total_time": 1381
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

True	425	-	connect apic11o.emea-sp.cisco.com
True	299	13	apic11o.emea-sp.cisco.com class fabricNode
True	330	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	327	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)