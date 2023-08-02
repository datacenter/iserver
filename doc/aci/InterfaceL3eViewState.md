# Node Interface - Encapsulated Routed

## State view

```
# iserver get aci intf l3e --apic apic21 --node any

Apic: apic21 (mode:online, cache:off)
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: cl2209-eu-spdc
- node: cl2210-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+----------------------+--------+---------+-------------+-------+------+-------------+---------+---------+------+--------------------+-------+-------------------+
| Node                 | Health | Faults  | Interface   | Admin | Oper | Reason      | Encap   | SR-MPLS | MTU  | IP Unnumbered Intf | Delay | Router MAC        |
+----------------------+--------+---------+-------------+-------+------+-------------+---------+---------+------+--------------------+-------+-------------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/25.17  | up    | up   |             | vlan-20 | no      | 1500 |                    | 1     | 00:22:BD:F8:19:FF | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/25.18  | up    | up   |             | vlan-14 | no      | 9000 |                    | 1     | 00:22:BD:F8:22:06 | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/25.19  | up    | up   |             | vlan-11 | no      | 9000 |                    | 1     | 00:22:BD:F8:22:05 | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/35.9   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/36.10  | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | eth1/25.3   | up    | up   |             | vlan-11 | no      | 9000 |                    | 1     | 00:22:BD:F8:22:06 | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | eth1/25.4   | up    | up   |             | vlan-14 | no      | 9000 |                    | 1     | 00:22:BD:F8:22:06 | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | eth1/25.5   | up    | up   |             | vlan-20 | no      | 1500 |                    | 1     | 00:22:BD:F8:19:FF | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | eth1/35.10  | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | eth1/36.9   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | eth1/107.7  | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | eth1/108.8  | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | eth1/107.34 | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | eth1/108.8  | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | eth1/35.8   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | eth1/36.7   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | eth1/35.32  | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | eth1/36.7   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/cl2209-eu-spdc | 100    | 0 0 0 0 | eth1/35.9   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/cl2210-eu-spdc | 100    | 0 0 0 0 | eth1/36.9   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | eth1/51.1   | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | eth1/52.2   | up    | up   |             | vlan-4  | no      | 9216 |                    | 1     | 00:22:BD:F8:19:FF | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | eth1/53.6   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | eth1/54.5   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | eth1/51.1   | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | eth1/52.2   | up    | up   |             | vlan-4  | no      | 9216 |                    | 1     | 00:22:BD:F8:19:FF | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | eth1/53.17  | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | eth1/54.16  | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/1.39   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/10.10  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/11.11  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/12.12  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/13.13  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/14.14  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/15.15  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/16.16  | up    | up   |             | vlan-4  | no      | 9216 |                    | 1     | 00:22:BD:F8:19:FF | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/17.17  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/18.18  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/19.7   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/2.36   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/20.20  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/21.21  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/22.22  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/23.23  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/24.24  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/25.25  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/26.26  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/27.27  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/28.28  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/29.29  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/3.3    | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/30.30  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/31.31  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/32.32  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/33.33  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/34.34  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/4.4    | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/5.1    | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/6.35   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/7.40   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/8.37   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | eth1/9.9    | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/1.6    | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/10.10  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/11.11  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/12.12  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/13.13  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/14.14  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/15.15  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/16.16  | up    | up   |             | vlan-4  | no      | 9216 |                    | 1     | 00:22:BD:F8:19:FF | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/17.17  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/18.18  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/19.19  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/2.40   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/20.8   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/21.21  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/22.22  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/23.23  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/24.24  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/25.25  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/26.26  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/27.27  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/28.28  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/29.29  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/3.3    | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/30.30  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/31.31  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/32.32  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/33.33  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/34.34  | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/4.4    | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/5.7    | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/6.2    | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/7.5    | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/8.39   | up    | up   |             | vlan-2  | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | eth1/9.9    | up    | down | parent-down | vlan-4  | no      | 9150 |                    | 1     | 00:00:00:00:00:00 | 
+----------------------+--------+---------+-------------+-------+------+-------------+---------+---------+------+--------------------+-------+-------------------+
```

Developer

```
# iserver get aci intf l3e --apic apic21 --node any

{
    "duration": 14127,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 667,
        "disconnect_time": 0,
        "mo_time": 12443,
        "total_time": 13110
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	667	-	connect apic21o.emea-sp.cisco.com:443
True	637	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	460	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	384	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4If
True	408	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	415	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ipv4If
True	416	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	381	35	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ipv4If
True	443	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	386	35	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ipv4If
True	630	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	397	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ipv4If
True	419	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	425	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4If
True	457	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	405	14	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/ipv4If
True	489	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	427	14	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/ipv4If
True	452	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	474	18	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ipv4If
True	494	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	375	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ipv4If
True	428	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	1541	62	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/ipv4If
True	719	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	381	62	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/ipv4If
```

[[Back]](./InterfaceL3e.md)