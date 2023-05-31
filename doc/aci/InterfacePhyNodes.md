# Node Interface - Physical

## Multiple nodes

```
# iserver get aci intf phy --apic apic11 --node cl --speed 100G --type leaf

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: cl201-eu-spdc
- node: cl202-eu-spdc

+---------------------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason      | Type | Layer    | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/cl201-eu-spdc | 1/97      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:23:FA:99 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 1/98      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:23:FA:9A | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 1/99      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:23:FA:9B | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 1/100     | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:23:FA:9C | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 1/101     | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:23:FA:9D | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 1/102     | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:23:FA:9E | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/97      | up    | disabled  | down | sfp-missing | leaf | switched |    | 10:B3:D5:B5:62:7D | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/98      | up    | disabled  | down | sfp-missing | leaf | switched |    | 10:B3:D5:B5:62:7E | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/99      | up    | disabled  | down | sfp-missing | leaf | switched |    | 10:B3:D5:B5:62:7F | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/100     | up    | disabled  | down | sfp-missing | leaf | switched |    | 10:B3:D5:B5:62:80 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/102     | up    | disabled  | down | sfp-missing | leaf | switched |    | 10:B3:D5:B5:62:82 | trunk | 100G  | full   | 9000 | disable-fec | 
+---------------------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node cl --speed 100G --type leaf

{
    "duration": 2798,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 412,
        "disconnect_time": 0,
        "mo_time": 1834,
        "total_time": 2246
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

True	412	-	connect apic11o.emea-sp.cisco.com
True	351	11	apic11o.emea-sp.cisco.com class fabricNode
True	354	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l1PhysIf
True	371	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ethpmPhysIf
True	377	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l1PhysIf
True	381	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)