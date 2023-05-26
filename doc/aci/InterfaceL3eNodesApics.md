# Node Interface - Encapsulated Routed

## Multi-APIC

```
# iserver get aci intf l3e --apic dom:milan --node any

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

+--------+----------------------+--------------+-------------+------------+-------------+---------+---------+------+--------------------+
| Apic   | Node                 | Interface    | Admin State | Oper State | Reason      | Encap   | SR-MPLS | MTU  | IP Unnumbered Intf |
+--------+----------------------+--------------+-------------+------------+-------------+---------+---------+------+--------------------+
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.36   | up          | up         |             | vlan-20 | no      | 1500 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.60   | up          | up         |             | vlan-24 | no      | 9000 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.62   | up          | up         |             | vlan-14 | no      | 9000 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.64   | up          | up         |             | vlan-21 | no      | 9000 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.65   | up          | up         |             | vlan-23 | no      | 9000 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.66   | up          | up         |             | vlan-22 | no      | 9000 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.67   | up          | up         |             | vlan-11 | no      | 9216 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.68   | up          | up         |             | vlan-25 | no      | 9000 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24.71   | up          | up         |             | vlan-15 | no      | 9216 |                    | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/35.9    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/36.83   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.38   | up          | up         |             | vlan-20 | no      | 1500 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.40   | up          | up         |             | vlan-24 | no      | 9000 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.43   | up          | up         |             | vlan-23 | no      | 9000 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.44   | up          | up         |             | vlan-21 | no      | 9000 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.45   | up          | up         |             | vlan-22 | no      | 9000 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.46   | up          | up         |             | vlan-25 | no      | 9000 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.47   | up          | up         |             | vlan-14 | no      | 9000 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.48   | up          | up         |             | vlan-11 | no      | 9216 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24.49   | up          | up         |             | vlan-15 | no      | 9216 |                    | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/35.10   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/36.74   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/107.7   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/108.504 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/107.8   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/108.500 | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/31.1    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/32.2    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/33.47   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/34.48   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/35.5    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/36.6    | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/31.1    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/32.2    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/33.7    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/34.8    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/35.5    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/36.6    | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/1.21    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s101-eu-spdc   | eth1/10.10   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/11.11   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/12.12   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/13.13   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/14.14   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/15.15   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/16.16   | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/2.23    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s101-eu-spdc   | eth1/3.3     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/4.4     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/5.20    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s101-eu-spdc   | eth1/6.22    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s101-eu-spdc   | eth1/7.7     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/8.8     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s101-eu-spdc   | eth1/9.9     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/1.28    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s102-eu-spdc   | eth1/10.10   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/11.11   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/12.12   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/13.13   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/14.14   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/15.15   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/16.16   | up          | up         |             | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/2.27    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s102-eu-spdc   | eth1/3.3     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/4.4     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/5.29    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s102-eu-spdc   | eth1/6.26    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic11 | pod-1/s102-eu-spdc   | eth1/7.7     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/8.8     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic11 | pod-1/s102-eu-spdc   | eth1/9.9     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/25.1    | up          | up         |             | vlan-11 | no      | 9000 |                    | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/25.19   | up          | up         |             | vlan-14 | no      | 9000 |                    | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/25.20   | up          | up         |             | vlan-20 | no      | 1500 |                    | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/35.10   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/36.8    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/25.17   | up          | up         |             | vlan-14 | no      | 9000 |                    | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/25.18   | up          | up         |             | vlan-20 | no      | 1500 |                    | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/25.19   | up          | up         |             | vlan-11 | no      | 9000 |                    | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/35.10   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/36.9    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/107.7   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/108.36  | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/107.9   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/108.7   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/35.7    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/36.32   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/35.37   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/36.8    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/51.1    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/52.2    | up          | up         |             | vlan-4  | no      | 9216 |                    | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/53.13   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/54.12   | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/51.1    | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/52.2    | up          | up         |             | vlan-4  | no      | 9216 |                    | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/53.6    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/54.5    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/1.40    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/10.10   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/11.11   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/12.12   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/13.13   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/14.14   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/15.15   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/16.16   | up          | up         |             | vlan-4  | no      | 9216 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/17.17   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/18.18   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/19.19   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/2.5     | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/20.20   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/21.21   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/22.22   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/23.23   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/24.24   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/25.25   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/26.26   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/27.27   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/28.28   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/29.29   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/3.3     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/30.30   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/31.31   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/32.32   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/33.33   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/34.34   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/4.4     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/5.1     | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/6.6     | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/7.39    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/8.7     | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/9.9     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/1.36    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/10.10   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/11.11   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/12.12   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/13.13   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/14.14   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/15.15   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/16.16   | up          | up         |             | vlan-4  | no      | 9216 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/17.17   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/18.18   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/19.19   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/2.39    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/20.20   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/21.21   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/22.22   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/23.23   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/24.24   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/25.25   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/26.26   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/27.27   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/28.28   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/29.29   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/3.3     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/30.30   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/31.31   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/32.32   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/33.33   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/34.34   | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/4.4     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/5.35    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/6.1     | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/7.37    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/8.40    | up          | up         |             | vlan-2  | no      | 9366 | lo0                | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/9.9     | up          | down       | parent-down | vlan-4  | no      | 9150 |                    | 
+--------+----------------------+--------------+-------------+------------+-------------+---------+---------+------+--------------------+
```

[[Back]](./InterfaceL3e.md)