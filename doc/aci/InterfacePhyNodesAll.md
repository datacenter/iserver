# Node Interface - Physical

## All nodes

```
# iserver get aci intf phy --apic apic11 --node any --fec cl91*

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-----------+-------+-----------+------+--------------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason             | Type | Layer    | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+--------------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl205-eu-spdc | 1/24      | up    | enabled   | up   | connected          | leaf | routed   |    | 4C:71:0D:7E:84:08 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
| pod-1/bl206-eu-spdc | 1/24      | up    | enabled   | up   | connected          | leaf | routed   |    | 3C:13:CC:C9:EC:C8 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
| pod-1/cl201-eu-spdc | 1/71      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:23:FA:7F | trunk | 25G   | full   | 9000 | cl91-rs-fec | 
| pod-1/cl201-eu-spdc | 1/72      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 4C:71:0D:23:FA:80 | trunk | 25G   | full   | 9000 | cl91-rs-fec | 
| pod-1/cl201-eu-spdc | 1/107     | up    | enabled   | up   | connected          | fab  | routed   |    | 4C:71:0D:23:FA:A3 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/cl201-eu-spdc | 1/108     | up    | enabled   | up   | connected          | fab  | routed   |    | 4C:71:0D:23:FA:A4 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/cl202-eu-spdc | 1/71      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 10:B3:D5:B5:62:63 | trunk | 25G   | full   | 9000 | cl91-rs-fec | 
| pod-1/cl202-eu-spdc | 1/72      | up    | disabled  | down | sfp-missing        | leaf | switched |    | 10:B3:D5:B5:62:64 | trunk | 25G   | full   | 9000 | cl91-rs-fec | 
| pod-1/cl202-eu-spdc | 1/107     | up    | enabled   | up   | connected          | fab  | routed   |    | 10:B3:D5:B5:62:87 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/cl202-eu-spdc | 1/108     | up    | enabled   | up   | connected          | fab  | routed   |    | 10:B3:D5:B5:62:88 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/1       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:E1 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/2       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:E2 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/3       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:E3 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/5       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:E5 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/6       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:E6 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/7       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:E7 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/11      | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:EB | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/12      | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:EC | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl209-eu-spdc | 1/13      | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:0F:ED | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/1       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:B1 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/2       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:B2 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/3       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:B3 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/5       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:B5 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/6       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:B6 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/7       | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:B7 | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/11      | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:BB | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/12      | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:BC | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl210-eu-spdc | 1/13      | up    | disabled  | down | link-not-connected | leaf | switched |    | C0:F8:7F:FE:10:BD | trunk | 100G  | full   | 9000 | cl91-rs-fec | 
| pod-1/s101-eu-spdc  | 1/1       | up    | enabled   | up   | connected          | fab  | routed   |    | 4C:71:0D:55:D1:CD | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/s101-eu-spdc  | 1/2       | up    | enabled   | up   | connected          | fab  | routed   |    | 4C:71:0D:55:D1:CE | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/s101-eu-spdc  | 1/16      | up    | enabled   | up   | connected          | fab  | routed   |    | 4C:71:0D:55:D1:DC | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/s102-eu-spdc  | 1/1       | up    | enabled   | up   | connected          | fab  | routed   |    | 8C:94:1F:FA:54:21 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/s102-eu-spdc  | 1/2       | up    | enabled   | up   | connected          | fab  | routed   |    | 8C:94:1F:FA:54:22 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/s102-eu-spdc  | 1/16      | up    | enabled   | up   | connected          | fab  | routed   |    | 8C:94:1F:FA:54:30 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
+---------------------+-----------+-------+-----------+------+--------------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node any --fec cl91*

{
    "duration": 7863,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 398,
        "disconnect_time": 0,
        "mo_time": 6699,
        "total_time": 7097
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

True	398	-	connect apic11o.emea-sp.cisco.com
True	303	13	apic11o.emea-sp.cisco.com class fabricNode
True	315	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	323	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	303	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l1PhysIf
True	319	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ethpmPhysIf
True	344	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l1PhysIf
True	346	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ethpmPhysIf
True	362	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l1PhysIf
True	360	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ethpmPhysIf
True	302	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l1PhysIf
True	326	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ethpmPhysIf
True	293	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l1PhysIf
True	310	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ethpmPhysIf
True	364	52	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l1PhysIf
True	319	48	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ethpmPhysIf
True	301	52	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l1PhysIf
True	301	48	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ethpmPhysIf
True	299	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l1PhysIf
True	288	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ethpmPhysIf
True	288	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l1PhysIf
True	333	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)