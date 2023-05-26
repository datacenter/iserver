# Node Interface - Physical

## Filter by fec

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --fec cl91*

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+-----------+------+-----------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason    | Type | Layer  | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-----------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl205-eu-spdc | 1/24      | up    | enabled   | up   | connected | leaf | routed |    | 4C:71:0D:7E:84:08 | trunk | 100G  | full   | 9216 | cl91-rs-fec | 
+---------------------+-----------+-------+-----------+------+-----------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
```

[[Back]](./InterfacePhy.md)