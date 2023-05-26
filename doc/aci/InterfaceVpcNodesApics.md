# Node Interface - Virtual Port Channel (VPC)

## Multi-APIC

```
# iserver get aci intf vpc --apic dom:milan --node any

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
Apic: apic21o.emea-sp.cisco.com
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+--------+----------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
| Apic   | Node                 | VPC Domain Id | Oper Role | Oper State                      | Peer State | Constistency | Local Members | Remote Members |
+--------+----------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
| apic11 | pod-1/bl205-eu-spdc  | 105           | master    | configured-master,vpcs-reinited | up         | pass         | 5/5           | 5/5            | 
| apic11 | pod-1/bl206-eu-spdc  | 105           | slave     | vpcs-reinited                   | up         | pass         | 5/5           | 5/5            | 
| apic11 | pod-1/cl201-eu-spdc  | 100           | master    | configured-master,vpcs-reinited | up         | pass         | 27/28         | 25/28          | 
| apic11 | pod-1/cl202-eu-spdc  | 100           | slave     | vpcs-reinited                   | up         | pass         | 25/28         | 27/28          | 
| apic11 | pod-1/rl301-eu-spdc  | 300           | master    | configured-master,vpcs-reinited | up         | pass         | 2/2           | 2/2            | 
| apic11 | pod-1/rl302-eu-spdc  | 300           | slave     | vpcs-reinited                   | up         | pass         | 2/2           | 2/2            | 
| apic21 | pod-1/bl2205-eu-spdc | 256           | master    | configured-master,vpcs-reinited | up         | pass         | 5/6           | 5/6            | 
| apic21 | pod-1/bl2206-eu-spdc | 256           | slave     | vpcs-reinited                   | up         | pass         | 5/6           | 5/6            | 
| apic21 | pod-1/cl2201-eu-spdc | 212           | master    | configured-master,vpcs-reinited | up         | pass         | 1/2           | 1/2            | 
| apic21 | pod-1/cl2202-eu-spdc | 212           | slave     | vpcs-reinited                   | up         | pass         | 1/2           | 1/2            | 
| apic21 | pod-1/cl2207-eu-spdc | 278           | master    | configured-master,vpcs-reinited | up         | pass         | 6/8           | 6/8            | 
| apic21 | pod-1/cl2208-eu-spdc | 278           | slave     | vpcs-reinited                   | up         | pass         | 6/8           | 6/8            | 
| apic21 | pod-1/rl2701-eu-spdc | 227           | master    | configured-master,vpcs-reinited | up         | pass         | 2/2           | 2/2            | 
| apic21 | pod-1/rl2702-eu-spdc | 227           | slave     | vpcs-reinited                   | up         | pass         | 2/2           | 2/2            | 
+--------+----------------------+---------------+-----------+---------------------------------+------------+--------------+---------------+----------------+
```

[[Back]](./InterfaceVpc.md)