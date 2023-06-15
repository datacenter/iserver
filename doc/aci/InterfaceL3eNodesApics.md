# Node Interface - Encapsulated Routed

## Multi-APIC

```
# iserver get aci intf l3e --apic dom:milan --node any

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc
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

+--------+----------------------+------------+-------------+------------+-------------+---------+---------+------+--------------------+
| Apic   | Node                 | Interface  | Admin State | Oper State | Reason      | Encap   | SR-MPLS | MTU  | IP Unnumbered Intf |
+--------+----------------------+------------+-------------+------------+-------------+---------+---------+------+--------------------+
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.46 | up          | up         |             | vlan-24 | no      | 9000 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.47 | up          | up         |             | vlan-20 | no      | 1500 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.48 | up          | up         |             | vlan-14 | no      | 9000 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.50 | up          | up         |             | vlan-15 | no      | 9216 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.51 | up          | up         |             | vlan-23 | no      | 9000 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.52 | up          | up         |             | vlan-21 | no      | 9000 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.53 | up          | up         |             | vlan-25 | no      | 9000 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.54 | up          | up         |             | vlan-11 | no      | 9216 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.55 | up          | up         |             | vlan-22 | no      | 9000 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/35.9  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/36.10 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.54 | up          | up         |             | vlan-20 | no      | 1500 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.55 | up          | up         |             | vlan-14 | no      | 9000 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.56 | up          | up         |             | vlan-24 | no      | 9000 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.59 | up          | up         |             | vlan-11 | no      | 9216 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.60 | up          | up         |             | vlan-15 | no      | 9216 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.61 | up          | up         |             | vlan-21 | no      | 9000 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.62 | up          | up         |             | vlan-23 | no      | 9000 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.63 | up          | up         |             | vlan-25 | no      | 9000 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.64 | up          | up         |             | vlan-22 | no      | 9000 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/35.9  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/36.10 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/107.7 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/108.8 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/107.7 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/108.8 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/35.9  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/36.9  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/31.1  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/32.2  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/33.7  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/34.8  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/35.5  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/36.6  | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/31.1  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/32.2  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/33.7  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/34.8  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/35.5  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/36.6  | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/1.18  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s101-eu-spdc   | eth1/10.10 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/11.11 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/12.12 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/13.22 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s101-eu-spdc   | eth1/14.14 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/15.15 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/16.16 | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/2.17  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s101-eu-spdc   | eth1/3.3   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/4.4   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/5.19  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s101-eu-spdc   | eth1/6.20  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s101-eu-spdc   | eth1/7.7   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/8.8   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/9.9   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/1.18  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s102-eu-spdc   | eth1/10.10 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/11.11 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/12.12 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/13.22 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s102-eu-spdc   | eth1/14.14 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/15.15 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/16.16 | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/2.17  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s102-eu-spdc   | eth1/3.3   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/4.4   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/5.19  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s102-eu-spdc   | eth1/6.20  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s102-eu-spdc   | eth1/7.7   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/8.8   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/9.9   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/25.1  | up          | up         |             | vlan-20 | no      | 1500 |                    | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/25.2  | up          | up         |             | vlan-14 | no      | 9000 |                    | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/25.5  | up          | up         |             | vlan-11 | no      | 9000 |                    | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/35.9  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/36.10 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/25.2  | up          | up         |             | vlan-11 | no      | 9000 |                    | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/25.3  | up          | up         |             | vlan-20 | no      | 1500 |                    | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/25.4  | up          | up         |             | vlan-14 | no      | 9000 |                    | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/35.10 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/36.9  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/107.7 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/108.8 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/107.7 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/108.8 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/35.8  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/36.7  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/35.7  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/36.8  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/35.9  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/36.9  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/51.1  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/52.2  | up          | up         |             | vlan-4  | no      | 9216 |                    | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/53.5  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/54.6  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/51.1  | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/52.2  | up          | up         |             | vlan-4  | no      | 9216 |                    | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/53.5  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/54.6  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/1.40  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/10.10 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/11.11 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/12.12 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/13.13 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/14.14 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/15.15 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/16.16 | up          | up         |             | vlan-4  | no      | 9216 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/17.17 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/18.18 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/19.2  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/2.39  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/20.20 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/21.21 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/22.22 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/23.23 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/24.24 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/25.25 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/26.26 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/27.27 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/28.28 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/29.29 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/3.3   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/30.30 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/31.31 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/32.32 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/33.33 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/34.34 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/4.4   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/5.38  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/6.37  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/7.35  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/8.36  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/9.9   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/1.40  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/10.10 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/11.11 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/12.12 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/13.13 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/14.14 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/15.15 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/16.16 | up          | up         |             | vlan-4  | no      | 9216 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/17.17 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/18.18 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/19.19 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/2.39  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/20.2  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/21.21 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/22.22 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/23.23 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/24.24 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/25.25 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/26.26 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/27.27 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/28.28 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/29.29 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/3.3   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/30.30 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/31.31 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/32.32 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/33.33 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/34.34 | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/4.4   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/5.38  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/6.37  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/7.35  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/8.36  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/9.9   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
+--------+----------------------+------------+-------------+------------+-------------+---------+---------+------+--------------------+
```

Developer

```
# iserver get aci intf l3e --apic dom:milan --node any

{
    "duration": 16233,
    "apic": {
        "read": true,
        "success": 48,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 46,
        "connect_time": 783,
        "disconnect_time": 0,
        "mo_time": 14231,
        "total_time": 15014
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

True	394	-	connect apic11o.emea-sp.cisco.com
True	304	13	apic11o.emea-sp.cisco.com class fabricNode
True	389	-	connect apic21o.emea-sp.cisco.com
True	302	15	apic21o.emea-sp.cisco.com class fabricNode
True	300	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	323	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4If
True	339	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	317	68	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4If
True	292	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	303	75	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4If
True	302	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	311	74	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4If
True	308	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	285	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4If
True	316	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	321	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4If
True	287	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	305	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4If
True	290	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	305	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4If
True	303	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	290	44	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4If
True	307	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	311	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4If
True	345	5	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	297	33	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/ipv4If
True	288	5	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	304	33	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/ipv4If
True	307	2	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	296	35	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/ipv4If
True	299	2	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	337	35	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/ipv4If
True	294	2	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	292	34	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/ipv4If
True	311	2	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	315	33	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/ipv4If
True	328	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	307	12	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/ipv4If
True	320	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	315	12	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/ipv4If
True	363	4	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	333	18	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/ipv4If
True	300	4	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	348	19	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/ipv4If
True	320	34	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	308	62	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/ipv4If
True	290	34	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	293	62	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/ipv4If
```

[[Back]](./InterfaceL3e.md)