# Node Interface - Port Channel (PC)

## Filter by port channel's vpc domain

```
# iserver get aci intf pc --apic apic11 --node any --domain 105

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

+---------------------+-----+-------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| Node                | Id  | Name              | Admin | Switching | State | Reason | Oper Mode | VPC Domain | Active Links |
+---------------------+-----+-------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| pod-1/bl205-eu-spdc | po1 | HX1-FI-B_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po2 | SPN_PolGrp        | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po3 | UCSB1-FI-B_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po4 | HX1-FI-A_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po5 | UCSB1-FI-A_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po1 | HX1-FI-A_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po2 | HX1-FI-B_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po3 | UCSB1-FI-B_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po4 | UCSB1-FI-A_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po5 | SPN_PolGrp        | up    | enabled   | up    |        | active    | 105        | 1            | 
+---------------------+-----+-------------------+-------+-----------+-------+--------+-----------+------------+--------------+
```

[[Back]](./InterfacePc.md)