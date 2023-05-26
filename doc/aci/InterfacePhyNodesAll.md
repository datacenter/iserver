# Node Interface - Physical

## All nodes

```
# iserver get aci intf phy --apic apic11 --node any --fec cl91*

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason      | Type | Layer    | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl205-eu-spdc | 1/24      | up    | enabled   | up   | connected   | leaf | routed   |    | 4C:71:0D:7E:84:08 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
| pod-1/bl206-eu-spdc | 1/24      | up    | enabled   | up   | connected   | leaf | routed   |    | 3C:13:CC:C9:EC:C8 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
| pod-1/cl201-eu-spdc | 1/71      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:23:FA:7F | trunk | auto  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl201-eu-spdc | 1/72      | up    | disabled  | down | sfp-missing | leaf | switched |    | 4C:71:0D:23:FA:80 | trunk | auto  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl201-eu-spdc | 1/107     | up    | enabled   | up   | connected   | fab  | routed   |    | 4C:71:0D:23:FA:A3 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/cl201-eu-spdc | 1/108     | up    | enabled   | up   | connected   | fab  | routed   |    | 4C:71:0D:23:FA:A4 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/cl202-eu-spdc | 1/71      | up    | disabled  | down | sfp-missing | leaf | switched |    | 10:B3:D5:B5:62:63 | trunk | auto  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl202-eu-spdc | 1/72      | up    | disabled  | down | sfp-missing | leaf | switched |    | 10:B3:D5:B5:62:64 | trunk | auto  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl202-eu-spdc | 1/101     | up    | disabled  | down | sfp-missing | leaf | switched |    | 10:B3:D5:B5:62:81 | trunk | auto  | full   | 9000 | cl91-rs-fec | 
| pod-1/cl202-eu-spdc | 1/107     | up    | enabled   | up   | connected   | fab  | routed   |    | 10:B3:D5:B5:62:87 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/cl202-eu-spdc | 1/108     | up    | enabled   | up   | connected   | fab  | routed   |    | 10:B3:D5:B5:62:88 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/s101-eu-spdc  | 1/1       | up    | enabled   | up   | connected   | fab  | routed   |    | 4C:71:0D:55:D1:CD | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/s101-eu-spdc  | 1/2       | up    | enabled   | up   | connected   | fab  | routed   |    | 4C:71:0D:55:D1:CE | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/s101-eu-spdc  | 1/16      | up    | enabled   | up   | connected   | fab  | routed   |    | 4C:71:0D:55:D1:DC | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/s102-eu-spdc  | 1/1       | up    | enabled   | up   | connected   | fab  | routed   |    | 8C:94:1F:FA:54:21 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/s102-eu-spdc  | 1/2       | up    | enabled   | up   | connected   | fab  | routed   |    | 8C:94:1F:FA:54:22 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
| pod-1/s102-eu-spdc  | 1/16      | up    | enabled   | up   | connected   | fab  | routed   |    | 8C:94:1F:FA:54:30 | trunk | 100G  | full   | 9366 | cl91-rs-fec | 
+---------------------+-----------+-------+-----------+------+-------------+------+----------+----+-------------------+-------+-------+--------+------+-------------+
```

[[Back]](./InterfacePhy.md)