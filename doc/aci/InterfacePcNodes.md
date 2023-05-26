# Node Interface - Port Channel (PC)

## Multiple nodes

```
# iserver get aci intf pc --apic apic11 --node rl

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----+------------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| Node                | Id  | Name                   | Admin | Switching | State | Reason | Oper Mode | VPC Domain | Active Links |
+---------------------+-----+------------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| pod-1/rl301-eu-spdc | po1 | UCSB1-R3DC-FI-A_PolGrp | up    | enabled   | up    |        | active    | 300        | 1            | 
| pod-1/rl301-eu-spdc | po2 | UCSB1-R3DC-FI-B_PolGrp | up    | enabled   | up    |        | active    | 300        | 1            | 
| pod-1/rl302-eu-spdc | po1 | UCSB1-R3DC-FI-B_PolGrp | up    | enabled   | up    |        | active    | 300        | 1            | 
| pod-1/rl302-eu-spdc | po2 | UCSB1-R3DC-FI-A_PolGrp | up    | enabled   | up    |        | active    | 300        | 1            | 
+---------------------+-----+------------------------+-------+-----------+-------+--------+-----------+------------+--------------+
```

[[Back]](./InterfacePc.md)