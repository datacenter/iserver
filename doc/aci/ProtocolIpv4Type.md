# Node Protocol - IPv4

## Filter IPv4 route table entries by route type

Supported route types
- ibgp
- ebgp
- bgp
- static
- local
- direct

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc --type ibgp

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+-------------------------------+--------------------+-------------------+--------+-----------+-----------+-------------------------------+------------+--------+------------+
| Node                | VRF                           | Prefix             | Next Hop          | Type   | Source    | Interface | NH VRF                        | MPLS Label | Active | Preference |
+---------------------+-------------------------------+--------------------+-------------------+--------+-----------+-----------+-------------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 0.0.0.0/0          | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.200.156/30   | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.200.160/30   | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.234.0/24     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.0/22      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.160/28    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.176/28    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.192/28    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.208/28    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.64/28     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.80/28     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.244.0/24     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.25.128/27    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.25.160/28    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.250.0/24     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.26.64/27     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.27.0/28      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.28.0/23      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.29.128/27    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.29.80/28     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.30.0/23      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.50.0/23      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.50.160/27    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.50.80/28     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.52.0/22      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.0/30   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.112/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.113/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.114/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.115/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.4/30   | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.40/30  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.44/30  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 205.205.205.205/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 206.206.206.206/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 0.0.0.0/0          | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 115.115.115.115/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 116.116.116.116/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.100.0/24    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.101.0/24    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.102.0/24    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.103.0/24    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.4.0/24      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.6.0/24      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.7.0/24      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.103.0/24    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.104.0/24    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.133.0/24    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.134.0/24    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.254.240/28  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.100/31 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.102/31 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.64/30  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.68/30  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.88/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.90/31  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.92/31  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.94/31  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.96/31  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.98/31  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.255.0/28   | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_VRF              | 0.0.0.0/0          | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 0.0.0.0/0          | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 122.122.122.122/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.101.5/32    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.0/24    | 15.254.104.254/32 | direct | direct    | vlan497   | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.104.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.0/32    | 15.254.104.254/32 | direct | direct    | vlan497   | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.104.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 192.168.254.96/31  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 192.168.254.98/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.101.7/32    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.0/24    | 15.254.107.254/32 | direct | direct    | vlan493   | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.107.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.0/32    | 15.254.107.254/32 | direct | direct    | vlan493   | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.107.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 0.0.0.0/0          | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 124.124.124.124/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.254.101.9/32    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 192.168.254.100/31 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 192.168.254.102/31 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 0.0.0.0/0          | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 118.118.118.118/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.101.1/32    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.0/24    | 15.254.134.254/32 | direct | direct    | vlan474   | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.134.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.0/32    | 15.254.134.254/32 | direct | direct    | vlan474   | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.134.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 192.168.254.88/31  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 192.168.254.90/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.101.100/32  | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.101.3/32    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.0/24    | 15.254.137.254/32 | direct | direct    | vlan495   | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.137.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.0/32    | 15.254.137.254/32 | direct | direct    | vlan495   | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.137.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 0.0.0.0/0          | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 120.120.120.120/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 192.168.254.92/31  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 192.168.254.94/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 122.122.122.122/32 | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 0.0.0.0/0          | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.200.156/30   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.200.160/30   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.234.0/24     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.0/22      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.160/28    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.176/28    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.192/28    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.208/28    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.64/28     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.80/28     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.244.0/24     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.25.128/27    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.25.160/28    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.250.0/24     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.26.64/27     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.27.0/28      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.28.0/23      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.29.128/27    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.29.80/28     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.30.0/23      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.50.0/23      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.50.160/27    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.50.80/28     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.52.0/22      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.112/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.113/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.114/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.115/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.16/30  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.20/30  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.40/30  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.44/30  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 205.205.205.205/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 206.206.206.206/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 122.122.122.122/32 | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 15.3.7.0/24        | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.1/32      | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.14/32     | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.15/32     | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.2/32      | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.3/32      | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 33.99.8.0/22       | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 0.0.0.0/0          | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 15.2.7.0/24        | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.1/32      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.252/32    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.253/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 15.3.21.0/24       | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 172.40.0.0/16      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 202.202.202.202/32 | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 15.2.7.0/24        | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.1/32      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.14/32     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.15/32     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.2/32      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.3/32      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.4/32      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.5/32      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.6/32      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 202.202.202.202/32 | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | NXOS-HandOff_Test:default     | 35.35.35.1/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | NXOS-HandOff_Test:default     | 54.54.54.1/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 0.0.0.0/0          | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.200.156/30   | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.200.160/30   | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.234.0/24     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.0/22      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.160/28    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.176/28    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.192/28    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.208/28    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.64/28     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.80/28     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.244.0/24     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.25.128/27    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.25.160/28    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.250.0/24     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.26.64/27     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.27.0/28      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.28.0/23      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.29.80/28     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.30.0/23      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.50.0/23      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.50.160/27    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.50.80/28     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.52.0/22      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 172.30.4.1/32      | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.112/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.113/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.114/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.115/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.40/30  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.44/30  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 205.205.205.15/32  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 206.206.206.15/32  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
+---------------------+-------------------------------+--------------------+-------------------+--------+-----------+-----------+-------------------------------+------------+--------+------------+

IPv4 Routes Summary
-------------------
- Routes  : 189
- Default : True
- Direct  : 8
- Local   : 8
- BGP     : 189
- iBGP    : 189
- eBGP    : 0
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc --type ibgp

{
    "duration": 13736,
    "apic": {
        "read": true,
        "success": 34,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 33,
        "connect_time": 666,
        "disconnect_time": 0,
        "mo_time": 11319,
        "total_time": 11985
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

True	666	-	connect apic11o.emea-sp.cisco.com
True	326	13	apic11o.emea-sp.cisco.com class fabricNode
True	309	31	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
True	317	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-black-hole query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	357	145	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_BGP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	338	82	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_privIP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	342	11	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	339	46	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N3-N4_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	436	33	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N6_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	328	29	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	344	46	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4-N3-N4_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	354	49	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4-N6_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	377	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	328	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-cvim1a:cvim1a-tenant_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	349	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-cvim1a:cvim1a_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	380	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-cvim4a:cvim4a-tenant_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	331	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-cvim4a:cvim4a_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	329	20	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-ECMP-demo:ACC-ext_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	319	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-ECMP-demo:MPC-CDC-2_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	352	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-iks-monitoring:iks-mon_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	356	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-management query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	350	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	314	77	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-mgmt:inb query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	338	39	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	300	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	399	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	363	32	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	345	45	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC:MPC-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	324	10	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-NXOS-HandOff_Test:default query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	413	175	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-overlay-1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	286	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-P5G:P5G_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	334	82	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-SPIN_InnoLab:SPIN_VRF1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	324	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	318	6	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-TESTING_BRUNO:default query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
```

[[Back]](./ProtocolIpv4.md)