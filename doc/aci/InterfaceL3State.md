# Node Interface - Encapsulated Routed

## Filter by operational state

```
# iserver get aci intf l3e --apic apic11 --node any --oper down

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

+---------------------+------------+-------------+------------+-------------+--------+---------+------+
| Node                | Interface  | Admin State | Oper State | Reason      | Encap  | SR-MPLS | MTU  |
+---------------------+------------+-------------+------------+-------------+--------+---------+------+
| pod-1/rl301-eu-spdc | eth1/31.1  | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/rl301-eu-spdc | eth1/32.2  | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/rl301-eu-spdc | eth1/35.5  | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/rl302-eu-spdc | eth1/31.1  | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/rl302-eu-spdc | eth1/32.2  | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/rl302-eu-spdc | eth1/35.5  | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/10.10 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/11.11 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/12.12 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/13.13 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/14.14 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/15.15 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/3.3   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/4.4   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/7.7   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/8.8   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s101-eu-spdc  | eth1/9.9   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/10.10 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/11.11 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/12.12 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/13.13 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/14.14 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/15.15 | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/3.3   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/4.4   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/7.7   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/8.8   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
| pod-1/s102-eu-spdc  | eth1/9.9   | up          | down       | parent-down | vlan-4 | no      | 9150 | 
+---------------------+------------+-------------+------------+-------------+--------+---------+------+
```

[[Back]](./InterfaceL3e.md)