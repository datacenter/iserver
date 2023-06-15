# Node Interface - Physical

## Multiple nodes

```
# iserver get aci intf phy --apic apic11 --node cl --speed 100G --type leaf

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc

+---------------------+-----------+-------+-----------+------+--------------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason             | Type | Layer    | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+--------------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/cl201-eu-spdc | 1/97      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:23:FA:99 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 1/98      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:23:FA:9A | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 1/99      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:23:FA:9B | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 1/100     | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:23:FA:9C | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 1/101     | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:23:FA:9D | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 1/102     | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:23:FA:9E | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/97      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 10:B3:D5:B5:62:7D | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/98      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 10:B3:D5:B5:62:7E | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/99      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 10:B3:D5:B5:62:7F | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/100     | up    | disabled  | down | sfp-missing        | leaf | switched |    | 10:B3:D5:B5:62:80 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/101     | up    | disabled  | down | sfp-missing        | leaf | switched |    | 10:B3:D5:B5:62:81 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/102     | up    | disabled  | down | sfp-missing        | leaf | switched |    | 10:B3:D5:B5:62:82 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/1       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:E1 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/2       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:E2 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/3       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:E3 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/4       | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:E4 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/5       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:E5 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/6       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:E6 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/7       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:E7 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/8       | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:E8 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/9       | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:E9 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/10      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:EA | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/11      | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:EB | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/12      | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:EC | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/13      | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:ED | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/14      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:EE | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/17      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:F1 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/18      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:F2 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/19      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:F3 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/20      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:F4 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/21      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:F5 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/22      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:F6 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/23      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:F7 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/24      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:F8 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/25      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:F9 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/26      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:FA | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/27      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:FB | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl209-eu-spdc | 1/28      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:0F:FC | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/1       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:B1 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/2       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:B2 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/3       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:B3 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/4       | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:B4 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/5       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:B5 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/6       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:B6 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/7       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:B7 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/8       | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:B8 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/9       | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:B9 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/10      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:BA | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/11      | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:BB | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/12      | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:BC | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/13      | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:BD | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/14      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:BE | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/17      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:C1 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/18      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:C2 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/19      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:C3 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/20      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:C4 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/21      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:C5 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/22      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:C6 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/23      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:C7 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/24      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:C8 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/25      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:C9 | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/26      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:CA | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/27      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:CB | trunk | 100G  | full   | 9000 | disable-fec | 
| pod-1/cl210-eu-spdc | 1/28      | up    | disabled  | down | sfp-missing        | leaf | switched |    | C0:F8:7F:FE:10:CC | trunk | 100G  | full   | 9000 | disable-fec | 
+---------------------+-----------+-------+-----------+------+--------------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node cl --speed 100G --type leaf

{
    "duration": 3630,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 374,
        "disconnect_time": 0,
        "mo_time": 2846,
        "total_time": 3220
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

True	374	-	connect apic11o.emea-sp.cisco.com
True	285	13	apic11o.emea-sp.cisco.com class fabricNode
True	321	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l1PhysIf
True	362	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ethpmPhysIf
True	320	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l1PhysIf
True	348	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ethpmPhysIf
True	295	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l1PhysIf
True	311	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ethpmPhysIf
True	295	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l1PhysIf
True	309	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)