# Node Interface - Encapsulated Routed

## Multiple nodes

```
# iserver get aci intf l3e --apic apic11 --node cl

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: cl201-eu-spdc
- node: cl202-eu-spdc

+---------------------+--------------+-------------+------------+--------+---------+------+--------------------+
| Node                | Interface    | Admin State | Oper State | Encap  | SR-MPLS | MTU  | IP Unnumbered Intf |
+---------------------+--------------+-------------+------------+--------+---------+------+--------------------+
| pod-1/cl201-eu-spdc | eth1/107.7   | up          | up         | vlan-2 | no      | 9366 | lo0                | 
| pod-1/cl201-eu-spdc | eth1/108.504 | up          | up         | vlan-2 | no      | 9366 | lo0                | 
| pod-1/cl202-eu-spdc | eth1/107.8   | up          | up         | vlan-2 | no      | 9366 | lo0                | 
| pod-1/cl202-eu-spdc | eth1/108.500 | up          | up         | vlan-2 | no      | 9366 | lo0                | 
+---------------------+--------------+-------------+------------+--------+---------+------+--------------------+
```

[[Back]](./InterfaceL3e.md)