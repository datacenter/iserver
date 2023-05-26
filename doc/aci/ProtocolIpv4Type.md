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

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+-------------------------------+--------------------+-------------------+--------+-----------+-----------+-------------------------------+------------+--------+------------+
| Node                | VRF                           | Prefix             | Next Hop          | Type   | Source    | Interface | NH VRF                        | MPLS Label | Active | Preference |
+---------------------+-------------------------------+--------------------+-------------------+--------+-----------+-----------+-------------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 0.0.0.0/0          | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.200.156/30   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.200.160/30   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.234.0/24     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.0/22      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.160/28    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.176/28    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.192/28    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.208/28    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.64/28     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.80/28     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.244.0/24     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.25.128/27    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.25.160/28    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.250.0/24     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.26.64/27     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.27.0/28      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.28.0/23      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.29.128/27    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.29.80/28     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.30.0/23      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.50.0/23      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.50.160/27    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.50.80/28     | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.52.0/22      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.0/30   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.112/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.113/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.114/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.115/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.4/30   | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.40/30  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.44/30  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 205.205.205.205/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 206.206.206.206/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 0.0.0.0/0          | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 115.115.115.115/32 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 116.116.116.116/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.1/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.10/32     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.12/32     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.13/32     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.15/32     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.192/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.193/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.194/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.195/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.2/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.224/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.225/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.228/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.229/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.230/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.231/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.232/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.233/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.234/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.235/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.236/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.237/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.238/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.240/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.241/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.242/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.4/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.5/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.7/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.0.9/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.100.0/24    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.101.0/24    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.102.0/24    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.103.0/24    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.4.0/24      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.6.0/24      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.7.0/24      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.224/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.225/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.228/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.229/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.230/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.231/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.232/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.233/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.234/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.235/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.236/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.237/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.238/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.240/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.241/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.96.242/32   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.103.0/24    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.104.0/24    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.133.0/24    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.134.0/24    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.254.240/28  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.100/31 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.102/31 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.64/30  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.68/30  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.88/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.90/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.92/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.94/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.96/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.98/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.255.0/28   | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_VRF              | 0.0.0.0/0          | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 0.0.0.0/0          | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 122.122.122.122/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.101.5/32    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.0/24    | 15.254.104.254/32 | direct | direct    | vlan470   | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.104.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.0/32    | 15.254.104.254/32 | direct | direct    | vlan470   | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.104.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 192.168.254.96/31  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 192.168.254.98/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.101.7/32    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.0/24    | 15.254.107.254/32 | direct | direct    | vlan474   | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.107.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.0/32    | 15.254.107.254/32 | direct | direct    | vlan474   | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.107.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 0.0.0.0/0          | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 124.124.124.124/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.254.101.9/32    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 192.168.254.100/31 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 192.168.254.102/31 | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 0.0.0.0/0          | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 118.118.118.118/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.101.1/32    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.0/24    | 15.254.134.254/32 | direct | direct    | vlan463   | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.134.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.0/32    | 15.254.134.254/32 | direct | direct    | vlan463   | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.134.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 192.168.254.88/31  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 192.168.254.90/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.101.100/32  | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.101.3/32    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.0/24    | 15.254.137.254/32 | direct | direct    | vlan461   | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.137.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.0/32    | 15.254.137.254/32 | direct | direct    | vlan461   | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.137.0/32   | local  | broadcast | null0     | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 0.0.0.0/0          | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 120.120.120.120/32 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 192.168.254.92/31  | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 192.168.254.94/31  | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 122.122.122.122/32 | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 0.0.0.0/0          | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
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
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.14/32     | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.15/32     | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.2/32      | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.3/32      | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 33.99.0.0/22       | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 33.99.4.0/22       | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 33.99.8.0/22       | 172.16.30.121/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 172.16.30.161/32  | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 0.0.0.0/0          | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 15.2.7.0/24        | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.1/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.252/32    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.253/32    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 15.3.21.0/24       | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 172.40.0.0/16      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 202.202.202.202/32 | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 15.2.7.0/24        | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.1/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.14/32     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.15/32     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.2/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.3/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.4/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.5/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.6/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 202.202.202.202/32 | 10.3.192.68/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 88.99.0.0/22       | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 88.99.12.0/22      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 88.99.16.0/22      | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 88.99.20.0/22      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 88.99.4.0/22       | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 88.99.8.0/22       | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | NXOS-HandOff_Test:default     | 35.35.35.1/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | NXOS-HandOff_Test:default     | 54.54.54.1/32      | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 0.0.0.0/0          | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
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
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.26.64/27     | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                     | 0          | yes    | 200        | 
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
```

[[Back]](./ProtocolIpv4.md)