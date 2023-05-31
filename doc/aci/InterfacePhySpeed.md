# Node Interface - Physical

## Filter by interface speed

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --speed 100G

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason      | Type | Layer    | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl205-eu-spdc | 1/3       | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:83:F3 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/4       | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:83:F4 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/5       | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:83:F5 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/6       | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:83:F6 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/9       | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:83:F9 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/10      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:83:FA | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/13      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:83:FD | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/14      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:83:FE | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/20      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:84:04 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/21      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:84:05 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/22      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:84:06 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/23      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:84:07 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/24      | up    | enabled   | up   | connected   | leaf | routed   |    | 4C:71:0D:7E:84:08 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
| pod-1/bl205-eu-spdc | 1/25      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:84:09 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/26      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:7E:84:0A | trunk | 100G  | full   | 9000 | disable-fec | 
+---------------------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --speed 100G

{
    "duration": 1654,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 435,
        "disconnect_time": 0,
        "mo_time": 975,
        "total_time": 1410
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

True	435	-	connect apic11o.emea-sp.cisco.com
True	324	11	apic11o.emea-sp.cisco.com class fabricNode
True	334	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	317	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)