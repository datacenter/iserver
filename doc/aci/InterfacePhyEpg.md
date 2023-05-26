# Node Interface - Physical

## Filter by deployed EPG name

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --epg *SPIN-CSR*

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+-----------+------+-----------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason    | Type | Layer    | PC  | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-----------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl205-eu-spdc | 1/1       | up    | enabled   | up   | connected | leaf | switched | po5 | 4C:71:0D:7E:83:F1 | trunk | 40G   | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/2       | up    | enabled   | up   | connected | leaf | switched | po3 | 4C:71:0D:7E:83:F2 | trunk | 40G   | full   | 9000 | disable-fec | 
+---------------------+-----------+-------+-----------+------+-----------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
```

[[Back]](./InterfacePhy.md)