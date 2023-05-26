# Node Interface - Encapsulated Routed

## Default state output

```
# iserver get aci intf l3e --apic apic11 --node bl205-eu-spdc

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+------------+-------------+------------+---------+---------+------+--------------------+
| Node                | Interface  | Admin State | Oper State | Encap   | SR-MPLS | MTU  | IP Unnumbered Intf |
+---------------------+------------+-------------+------------+---------+---------+------+--------------------+
| pod-1/bl205-eu-spdc | eth1/24.36 | up          | up         | vlan-20 | no      | 1500 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.60 | up          | up         | vlan-24 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.62 | up          | up         | vlan-14 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.64 | up          | up         | vlan-21 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.65 | up          | up         | vlan-23 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.66 | up          | up         | vlan-22 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.67 | up          | up         | vlan-11 | no      | 9216 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.68 | up          | up         | vlan-25 | no      | 9000 |                    | 
| pod-1/bl205-eu-spdc | eth1/24.71 | up          | up         | vlan-15 | no      | 9216 |                    | 
| pod-1/bl205-eu-spdc | eth1/35.9  | up          | up         | vlan-2  | no      | 9366 | lo0                | 
| pod-1/bl205-eu-spdc | eth1/36.83 | up          | up         | vlan-2  | no      | 9366 | lo0                | 
+---------------------+------------+-------------+------------+---------+---------+------+--------------------+
```

[[Back]](./InterfaceL3e.md)