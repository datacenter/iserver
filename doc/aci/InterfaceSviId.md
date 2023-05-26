# Node Interface - SVI

## Filter by interface id

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --id vlan35

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| Node                | Interface | Admin State | Oper State | Type        | Medium | Multicast | MTU  | Fabric Encap   |
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| pod-1/bl205-eu-spdc | vlan35    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040482 | 
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
```

[[Back]](./InterfaceSvi.md)