# Node Interface - Encapsulated Routed

## Filter by interface id

```
# iserver get aci intf l3e --apic apic11 --node bl205-eu-spdc --id eth1/36.83

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+------------+-------------+------------+--------+---------+------+--------------------+
| Node                | Interface  | Admin State | Oper State | Encap  | SR-MPLS | MTU  | IP Unnumbered Intf |
+---------------------+------------+-------------+------------+--------+---------+------+--------------------+
| pod-1/bl205-eu-spdc | eth1/36.83 | up          | up         | vlan-2 | no      | 9366 | lo0                | 
+---------------------+------------+-------------+------------+--------+---------+------+--------------------+
```

[[Back]](./InterfaceL3e.md)