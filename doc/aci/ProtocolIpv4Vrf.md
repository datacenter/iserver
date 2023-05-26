# Node Protocol - IPv4

## Filter IPv4 route table entries by vrf name

```
# iserver get aci proto ipv4 --apic apic11 --node rl --vrf overlay-1

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----------+--------------------+--------------------+------------+-----------------+------------+-----------+------------+--------+------------+
| Node                | VRF       | Prefix             | Next Hop           | Type       | Source          | Interface  | NH VRF    | MPLS Label | Active | Preference |
+---------------------+-----------+--------------------+--------------------+------------+-----------------+------------+-----------+------------+--------+------------+
| pod-1/rl301-eu-spdc | overlay-1 | 10.3.0.0/16        | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.3.0.1/32        | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.3.0.2/32        | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.3.0.3/32        | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.3.0.33/32       | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.3.0.34/32       | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.3.0.35/32       | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.3.192.65/32     | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.3.32.65/32      | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.5.0.0/16        | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.5.0.1/32        | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.5.0.2/32        | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.5.0.3/32        | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.5.0.33/32       | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.5.0.34/32       | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.5.0.35/32       | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.5.80.97/32      | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 10.5.80.98/32      | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 101.101.101.101/32 | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 102.102.102.102/32 | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 111.111.111.111/32 | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 112.112.112.112/32 | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 131.131.131.131/32 | 131.131.131.131/32 | local      | local           | lo1        | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 131.131.131.131/32 | direct     | direct          | lo1        | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 132.132.132.132/32 | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | yes    | 10         | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | yes    | 10         | 
| pod-1/rl301-eu-spdc | overlay-1 | 15.16.3.0/30       | 15.16.3.2/32       | direct     | direct          | eth1/29    | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 15.16.3.0/32       | local      | broadcast       | null0      | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 15.16.3.0/32       | 15.16.3.2/32       | direct     | direct          | eth1/29    | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 15.16.3.0/32       | local      | broadcast       | null0      | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 15.16.3.1/32       | 15.16.3.1/32       | 0          | am              | eth1/29    | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
| pod-1/rl301-eu-spdc | overlay-1 | 15.16.3.2/32       | 15.16.3.2/32       | local      | local           | eth1/29    | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 15.16.3.3/32       | 15.16.3.3/32       | 0          | broadcast       | eth1/29    | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 15.16.3.5/32       | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | yes    | 10         | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | yes    | 10         | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
| pod-1/rl301-eu-spdc | overlay-1 | 171.171.171.171/32 | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.1.1/32      | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.10.1/32     | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.11.0/24     | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.11.1/32     | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.11.225/32   | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.11.226/32   | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.11.227/32   | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.11.228/32   | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.11.236/32   | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.12.1/32     | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.21.0/24     | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.21.1/32     | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.21.2/32     | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.21.230/32   | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.21.236/32   | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.21.238/32   | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.21.239/32   | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.21.240/32   | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.22.1/32     | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.30.120/32   | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | yes    | 10         | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | yes    | 10         | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.30.121/32   | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | yes    | 10         | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | yes    | 10         | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.30.160/32   | 172.16.30.160/32   | local      | local           | lo0        | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.16.30.160/32   | direct     | direct          | lo0        | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.30.161/32   | 172.16.30.161/32   | local      | local           | lo2        | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.16.30.161/32   | direct     | direct          | lo2        | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.30.32/32    | 172.16.30.32/32    | local      | local           | lo1023     | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.16.30.32/32    | direct     | direct          | lo1023     | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.30.88/32    | 172.16.30.88/32    | local      | local           | lo3        | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.16.30.88/32    | direct     | direct          | lo3        | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.70.208/32   | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.70.209/32   | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.70.232/32   | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.70.24/32    | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.16.70.25/32    | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.172.172.172/32 | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.31.2.0/29      | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.31.3.31/32     | 172.31.3.31/32     | local      | local           | lo4        | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.31.3.31/32     | direct     | direct          | lo4        | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 172.31.3.35/32     | 15.16.3.1/32       | ebgp       | bgp-50000       |            | overlay-1 | 3          | yes    | 20         | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.1.0/30     | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.1.20/30    | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.1.24/30    | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.1.4/30     | 192.168.31.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.31.0/30    | 192.168.31.1/32    | direct     | direct          | eth1/36.6  | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.0/32    | local      | broadcast       | null0      | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.31.0/32    | 192.168.31.1/32    | direct     | direct          | eth1/36.6  | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.31.0/32    | local      | broadcast       | null0      | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.31.1/32    | 192.168.31.1/32    | local      | local           | eth1/36.6  | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.31.2/32    | 192.168.31.2/32    | 0          | am              | eth1/36.6  | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.31.3/32    | 192.168.31.3/32    | 0          | broadcast       | eth1/36.6  | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.32.0/30    | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.32.2/32    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | yes    | 10         | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | yes    | 10         | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.71.0/30    | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.71.2/32    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.72.0/30    | 192.168.31.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | overlay-1 | 192.168.72.2/32    | 192.168.31.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.120/32   | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.3.0.0/16        | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.3.0.1/32        | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.3.0.2/32        | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.3.0.3/32        | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.3.0.33/32       | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.3.0.34/32       | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.3.0.35/32       | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.3.192.65/32     | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.3.32.65/32      | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.5.0.0/16        | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.5.0.1/32        | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.5.0.2/32        | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.5.0.3/32        | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.5.0.33/32       | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.5.0.34/32       | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.5.0.35/32       | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.5.80.97/32      | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 10.5.80.98/32      | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 101.101.101.101/32 | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 102.102.102.102/32 | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 111.111.111.111/32 | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 112.112.112.112/32 | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 131.131.131.131/32 | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | yes    | 10         | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | yes    | 10         | 
| pod-1/rl302-eu-spdc | overlay-1 | 132.132.132.132/32 | 132.132.132.132/32 | local      | local           | lo1        | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 132.132.132.132/32 | direct     | direct          | lo1        | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 15.16.3.1/32       | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | yes    | 10         | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | yes    | 10         | 
| pod-1/rl302-eu-spdc | overlay-1 | 15.16.3.4/30       | 15.16.3.6/32       | direct     | direct          | eth1/29    | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 15.16.3.4/32       | local      | broadcast       | null0      | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 15.16.3.4/32       | 15.16.3.6/32       | direct     | direct          | eth1/29    | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 15.16.3.4/32       | local      | broadcast       | null0      | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 15.16.3.5/32       | 15.16.3.5/32       | 0          | am              | eth1/29    | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
| pod-1/rl302-eu-spdc | overlay-1 | 15.16.3.6/32       | 15.16.3.6/32       | local      | local           | eth1/29    | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 15.16.3.7/32       | 15.16.3.7/32       | 0          | broadcast       | eth1/29    | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 171.171.171.171/32 | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.1.1/32      | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.10.1/32     | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.11.0/24     | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.11.1/32     | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.11.225/32   | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.11.226/32   | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.11.227/32   | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.11.228/32   | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.11.236/32   | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.12.1/32     | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.21.0/24     | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.21.1/32     | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.21.2/32     | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.21.230/32   | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.21.236/32   | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.21.238/32   | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.21.239/32   | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.21.240/32   | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.22.1/32     | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.30.120/32   | 172.16.30.120/32   | local      | local           | lo0        | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.16.30.120/32   | direct     | direct          | lo0        | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.30.121/32   | 172.16.30.121/32   | local      | local           | lo2        | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.16.30.121/32   | direct     | direct          | lo2        | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.30.160/32   | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | yes    | 10         | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | yes    | 10         | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.30.161/32   | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | yes    | 10         | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | yes    | 10         | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.30.32/32    | 172.16.30.32/32    | local      | local           | lo1023     | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.16.30.32/32    | direct     | direct          | lo1023     | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.30.88/32    | 172.16.30.88/32    | local      | local           | lo3        | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.16.30.88/32    | direct     | direct          | lo3        | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.70.208/32   | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.70.209/32   | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.70.232/32   | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.70.24/32    | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.16.70.25/32    | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.172.172.172/32 | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.31.2.0/29      | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.31.3.32/32     | 172.31.3.32/32     | local      | local           | lo4        | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.31.3.32/32     | direct     | direct          | lo4        | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 172.31.3.35/32     | 15.16.3.5/32       | ebgp       | bgp-50000       |            | overlay-1 | 3          | yes    | 20         | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.1.0/30     | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.1.20/30    | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.1.24/30    | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.1.4/30     | 192.168.32.2/32    | ospf-inter | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.31.0/30    | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.31.2/32    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | yes    | 10         | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | yes    | 10         | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.32.0/30    | 192.168.32.1/32    | direct     | direct          | eth1/36.6  | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.0/32    | local      | broadcast       | null0      | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.32.0/32    | 192.168.32.1/32    | direct     | direct          | eth1/36.6  | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 192.168.32.0/32    | local      | broadcast       | null0      | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.32.1/32    | 192.168.32.1/32    | local      | local           | eth1/36.6  | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.32.2/32    | 192.168.32.2/32    | 0          | am              | eth1/36.6  | overlay-1 | 0          | yes    | 0          | 
|                     |           |                    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | no     | 110        | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.32.3/32    | 192.168.32.3/32    | 0          | broadcast       | eth1/36.6  | overlay-1 | 0          | yes    | 0          | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.71.0/30    | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.71.2/32    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.72.0/30    | 192.168.32.2/32    | ospf-intra | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | overlay-1 | 192.168.72.2/32    | 192.168.32.2/32    | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |           |                    | 172.16.30.160/32   | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
+---------------------+-----------+--------------------+--------------------+------------+-----------------+------------+-----------+------------+--------+------------+
```

[[Back]](./ProtocolIpv4.md)