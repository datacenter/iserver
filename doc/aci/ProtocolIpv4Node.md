# Node Protocol - IPv4

## Show IPv4 route table entries for selected node

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+-------------------------------+--------------------+--------------------+-------------+-----------------+------------+-------------------------------+------------+--------+------------+
| Node                | VRF                           | Prefix             | Next Hop           | Type        | Source          | Interface  | NH VRF                        | MPLS Label | Active | Preference |
+---------------------+-------------------------------+--------------------+--------------------+-------------+-----------------+------------+-------------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 0.0.0.0/0          | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.200.156/30   | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.200.160/30   | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.234.0/24     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.239.0/24     | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.239.254/32   | 10.58.239.254/32   | local       | local           | vlan280    | common:Infra_BGP_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.0/22      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.128/27    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.158/32    | 10.58.24.158/32    | local       | local           | vlan295    | common:Infra_BGP_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.160/28    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.176/28    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.192/28    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.208/28    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.224/27    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.254/32    | 10.58.24.254/32    | local       | local           | vlan270    | common:Infra_BGP_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.64/28     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.24.80/28     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.244.0/24     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.25.128/27    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.25.160/28    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.250.0/24     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.26.64/27     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.27.0/28      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.27.110/32    | 10.58.27.110/32    | local       | local           | vlan310    | common:Infra_BGP_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.27.112/28    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.27.126/32    | 10.58.27.126/32    | local       | local           | vlan288    | common:Infra_BGP_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.27.128/28    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.27.142/32    | 10.58.27.142/32    | local       | local           | vlan312    | common:Infra_BGP_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.27.96/28     | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.28.0/23      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.28.102/32    | 10.58.28.102/32    | local       | local           | vlan278    | common:Infra_BGP_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.28.112/29    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.28.118/32    | 10.58.28.118/32    | local       | local           | vlan330    | common:Infra_BGP_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.28.80/28     | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.28.94/32     | 10.58.28.94/32     | local       | local           | vlan230    | common:Infra_BGP_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.28.96/29     | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.29.128/27    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.29.80/28     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.30.0/23      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.50.0/23      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.50.120/29    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.50.126/32    | 10.58.50.126/32    | local       | local           | vlan286    | common:Infra_BGP_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.50.160/27    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.50.80/28     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.51.128/27    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.51.158/32    | 10.58.51.158/32    | local       | local           | vlan334    | common:Infra_BGP_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 10.58.52.0/22      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.0/30   | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.112/32 | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.113/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.114/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.115/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.4/30   | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.40/30  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 192.168.254.44/30  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 205.205.205.205/32 | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 206.206.206.206/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 0.0.0.0/0          | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 115.115.115.115/32 | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 116.116.116.116/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.100.0/24    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.101.0/24    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.102.0/24    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.103.0/24    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.161.0/25    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.161.126/32  | 15.100.161.126/32  | local       | local           | vlan290    | common:Infra_privIP_VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.161.128/25  | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.161.254/32  | 15.100.161.254/32  | local       | local           | vlan440    | common:Infra_privIP_VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.4.0/24      | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.6.0/24      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.7.0/24      | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.103.0/24    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.104.0/24    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.133.0/24    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.134.0/24    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.254.254.240/28  | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.100/31 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.102/31 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.64/30  | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.68/30  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.88/31  | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.90/31  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.92/31  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.94/31  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.96/31  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.254.98/31  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 192.168.255.0/28   | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_VRF              | 0.0.0.0/0          | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:Infra_VRF              | 15.254.254.0/24    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_VRF              | 15.254.254.254/32  | 15.254.254.254/32  | local       | local           | vlan489    | common:Infra_VRF              | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:Infra_VRF              | 192.168.0.0/28     | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:Infra_VRF              | 192.168.0.14/32    | 192.168.0.14/32    | local       | local           | vlan489    | common:Infra_VRF              | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 0.0.0.0/0          | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 122.122.122.122/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.6.0/24      | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.6.254/32    | 15.100.6.254/32    | local       | local           | vlan344    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.0/24      | 15.100.7.252/32    | direct      | direct          | vlan472    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.7.254/32    | direct      | direct          | vlan472    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.7.0/32      | local       | broadcast       | null0      | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.0/32      | 15.100.7.252/32    | direct      | direct          | vlan472    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.7.254/32    | direct      | direct          | vlan472    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.7.0/32      | local       | broadcast       | null0      | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.252/32    | 15.100.7.252/32    | local       | local           | vlan472    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.254/32    | 15.100.7.254/32    | local       | local           | vlan472    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.100.7.255/32    | 15.100.7.255/32    | 0           | broadcast       | vlan472    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.101.4/32    | 15.254.101.4/32    | local       | local           | lo9        | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.101.4/32    | direct      | direct          | lo9        | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.101.5/32    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.0/24    | 15.254.103.252/32  | direct      | direct          | vlan496    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.103.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.0/32    | 15.254.103.252/32  | direct      | direct          | vlan496    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.103.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.252/32  | 15.254.103.252/32  | local       | local           | vlan496    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.255/32  | 15.254.103.255/32  | 0           | broadcast       | vlan496    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.0/24    | 15.254.104.254/32  | direct      | direct          | vlan497    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.104.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.0/32    | 15.254.104.254/32  | direct      | direct          | vlan497    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.104.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.254/32  | 15.254.104.254/32  | local       | local           | vlan497    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.104.255/32  | 15.254.104.255/32  | 0           | broadcast       | vlan497    | common:smi5Gc-cvim1-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 192.168.254.96/31  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 192.168.254.98/31  | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.100.8.0/24      | 15.100.8.252/32    | direct      | direct          | vlan470    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.8.254/32    | direct      | direct          | vlan470    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.8.0/32      | local       | broadcast       | null0      | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.100.8.0/32      | 15.100.8.252/32    | direct      | direct          | vlan470    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.8.254/32    | direct      | direct          | vlan470    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.8.0/32      | local       | broadcast       | null0      | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.100.8.252/32    | 15.100.8.252/32    | local       | local           | vlan470    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.100.8.254/32    | 15.100.8.254/32    | local       | local           | vlan470    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.100.8.255/32    | 15.100.8.255/32    | 0           | broadcast       | vlan470    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.101.6/32    | 15.254.101.6/32    | local       | local           | lo7        | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.101.6/32    | direct      | direct          | lo7        | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.101.7/32    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.0/24    | 15.254.106.252/32  | direct      | direct          | vlan492    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.106.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.0/32    | 15.254.106.252/32  | direct      | direct          | vlan492    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.106.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.252/32  | 15.254.106.252/32  | local       | local           | vlan492    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.255/32  | 15.254.106.255/32  | 0           | broadcast       | vlan492    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.0/24    | 15.254.107.254/32  | direct      | direct          | vlan493    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.107.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.0/32    | 15.254.107.254/32  | direct      | direct          | vlan493    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.107.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.254/32  | 15.254.107.254/32  | local       | local           | vlan493    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.107.255/32  | 15.254.107.255/32  | 0           | broadcast       | vlan493    | common:smi5Gc-cvim1-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 0.0.0.0/0          | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 124.124.124.124/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.0/24      | 15.100.4.252/32    | direct      | direct          | vlan469    | common:smi5Gc-cvim1_VRF       | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.4.254/32    | direct      | direct          | vlan469    | common:smi5Gc-cvim1_VRF       | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.4.0/32      | local       | broadcast       | null0      | common:smi5Gc-cvim1_VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.0/32      | 15.100.4.252/32    | direct      | direct          | vlan469    | common:smi5Gc-cvim1_VRF       | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.4.254/32    | direct      | direct          | vlan469    | common:smi5Gc-cvim1_VRF       | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.4.0/32      | local       | broadcast       | null0      | common:smi5Gc-cvim1_VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.252/32    | 15.100.4.252/32    | local       | local           | vlan469    | common:smi5Gc-cvim1_VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.254/32    | 15.100.4.254/32    | local       | local           | vlan469    | common:smi5Gc-cvim1_VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.4.255/32    | 15.100.4.255/32    | 0           | broadcast       | vlan469    | common:smi5Gc-cvim1_VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.5.0/24      | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.100.5.254/32    | 15.100.5.254/32    | local       | local           | vlan274    | common:smi5Gc-cvim1_VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.254.101.8/32    | 15.254.101.8/32    | local       | local           | lo6        | common:smi5Gc-cvim1_VRF       | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.101.8/32    | direct      | direct          | lo6        | common:smi5Gc-cvim1_VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 15.254.101.9/32    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 192.168.254.100/31 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 192.168.254.102/31 | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 0.0.0.0/0          | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 118.118.118.118/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.102.0/24    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.102.254/32  | 15.100.102.254/32  | local       | local           | vlan442    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.0/24    | 15.100.103.252/32  | direct      | direct          | vlan471    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.103.254/32  | direct      | direct          | vlan471    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.103.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.0/32    | 15.100.103.252/32  | direct      | direct          | vlan471    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.103.254/32  | direct      | direct          | vlan471    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.103.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.252/32  | 15.100.103.252/32  | local       | local           | vlan471    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.254/32  | 15.100.103.254/32  | local       | local           | vlan471    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.100.103.255/32  | 15.100.103.255/32  | 0           | broadcast       | vlan471    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.101.0/32    | 15.254.101.0/32    | local       | local           | lo8        | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.101.0/32    | direct      | direct          | lo8        | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.101.1/32    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.0/24    | 15.254.133.252/32  | direct      | direct          | vlan473    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.133.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.0/32    | 15.254.133.252/32  | direct      | direct          | vlan473    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.133.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252/32  | 15.254.133.252/32  | local       | local           | vlan473    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.255/32  | 15.254.133.255/32  | 0           | broadcast       | vlan473    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.0/24    | 15.254.134.254/32  | direct      | direct          | vlan474    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.134.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.0/32    | 15.254.134.254/32  | direct      | direct          | vlan474    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.134.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.254/32  | 15.254.134.254/32  | local       | local           | vlan474    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.134.255/32  | 15.254.134.255/32  | 0           | broadcast       | vlan474    | common:smi5Gc-cvim4-N3-N4_VRF | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 192.168.254.88/31  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 192.168.254.90/31  | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.100.104.0/24    | 15.100.104.252/32  | direct      | direct          | vlan498    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.104.254/32  | direct      | direct          | vlan498    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.104.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.100.104.0/32    | 15.100.104.252/32  | direct      | direct          | vlan498    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.104.254/32  | direct      | direct          | vlan498    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.104.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.100.104.252/32  | 15.100.104.252/32  | local       | local           | vlan498    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.100.104.254/32  | 15.100.104.254/32  | local       | local           | vlan498    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.100.104.255/32  | 15.100.104.255/32  | 0           | broadcast       | vlan498    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.100.199.0/24    | 15.100.199.252/32  | direct      | direct          | vlan479    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.199.250/32  | direct      | direct          | vlan479    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.199.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.100.199.0/32    | 15.100.199.252/32  | direct      | direct          | vlan479    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.199.250/32  | direct      | direct          | vlan479    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.100.199.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.100.199.250/32  | 15.100.199.250/32  | local       | local           | vlan479    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.100.199.252/32  | 15.100.199.252/32  | local       | local           | vlan479    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.100.199.255/32  | 15.100.199.255/32  | 0           | broadcast       | vlan479    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.101.100/32  | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.101.2/32    | 15.254.101.2/32    | local       | local           | lo12       | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.101.2/32    | direct      | direct          | lo12       | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.101.3/32    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.101.99/32   | 15.254.101.99/32   | local       | local           | lo10       | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.101.99/32   | direct      | direct          | lo10       | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.0/24    | 15.254.136.252/32  | direct      | direct          | vlan494    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.136.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.0/32    | 15.254.136.252/32  | direct      | direct          | vlan494    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 15.254.136.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.252/32  | 15.254.136.252/32  | local       | local           | vlan494    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.136.255/32  | 15.254.136.255/32  | 0           | broadcast       | vlan494    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.0/24    | 15.254.137.254/32  | direct      | direct          | vlan495    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.137.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.0/32    | 15.254.137.254/32  | direct      | direct          | vlan495    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | no     | 200        | 
|                     |                               |                    | 15.254.137.0/32    | local       | broadcast       | null0      | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.254/32  | 15.254.137.254/32  | local       | local           | vlan495    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 15.254.137.255/32  | 15.254.137.255/32  | 0           | broadcast       | vlan495    | common:smi5Gc-cvim4-N6_VRF    | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 0.0.0.0/0          | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 120.120.120.120/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 15.100.100.0/24    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 15.100.100.254/32  | 15.100.100.254/32  | local       | local           | vlan276    | common:smi5Gc-cvim4_VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 15.100.101.0/24    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 15.100.101.254/32  | 15.100.101.254/32  | local       | local           | vlan316    | common:smi5Gc-cvim4_VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 192.168.254.92/31  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 192.168.254.94/31  | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | cvim1a:cvim1a_VRF             | 192.168.111.0/24   | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | cvim1a:cvim1a_VRF             | 192.168.111.254/32 | 192.168.111.254/32 | local       | local           | vlan74     | cvim1a:cvim1a_VRF             | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | cvim1a:cvim1a_VRF             | 192.168.151.0/24   | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | cvim1a:cvim1a_VRF             | 192.168.151.254/32 | 192.168.151.254/32 | local       | local           | vlan32     | cvim1a:cvim1a_VRF             | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | cvim4a:cvim4a_VRF             | 192.168.152.0/24   | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | cvim4a:cvim4a_VRF             | 192.168.152.254/32 | 192.168.152.254/32 | local       | local           | vlan36     | cvim4a:cvim4a_VRF             | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | cvim4a:cvim4a_VRF             | 192.168.157.0/24   | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | cvim4a:cvim4a_VRF             | 192.168.157.254/32 | 192.168.157.254/32 | local       | local           | vlan268    | cvim4a:cvim4a_VRF             | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 121.121.121.121/32 | 121.121.121.121/32 | local       | local           | lo5        | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 0          | 
|                     |                               |                    | 121.121.121.121/32 | direct      | direct          | lo5        | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 122.122.122.122/32 | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 15.101.0.0/24      | 15.101.1.254/32    | static      | static          | vlan468    | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 15.101.1.0/24      | 15.101.1.3/32      | direct      | direct          | vlan468    | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 0          | 
|                     |                               |                    | 15.101.1.1/32      | direct      | direct          | vlan468    | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 0          | 
|                     |                               |                    | 15.101.1.0/32      | local       | broadcast       | null0      | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 15.101.1.0/32      | 15.101.1.3/32      | direct      | direct          | vlan468    | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 0          | 
|                     |                               |                    | 15.101.1.1/32      | direct      | direct          | vlan468    | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 0          | 
|                     |                               |                    | 15.101.1.0/32      | local       | broadcast       | null0      | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 15.101.1.1/32      | 15.101.1.1/32      | local       | local           | vlan468    | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 15.101.1.255/32    | 15.101.1.255/32    | 0           | broadcast       | vlan468    | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 15.101.1.3/32      | 15.101.1.3/32      | local       | local           | vlan468    | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 172.40.0.0/16      | 15.101.1.254/32    | static      | static          | vlan468    | ECMP-demo:ACC-ext_VRF         | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | ECMP-demo:MPC-CDC-2_VRF       | 15.2.203.0/24      | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | ECMP-demo:MPC-CDC-2_VRF       | 15.2.203.254/32    | 15.2.203.254/32    | local       | local           | vlan282    | ECMP-demo:MPC-CDC-2_VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF       | 99.99.99.0/24      | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF       | 99.99.99.254/32    | 99.99.99.254/32    | local       | local           | vlan58     | mgmt:EU-SPDC-ERSPAN-VRF       | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 0.0.0.0/0          | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.200.156/30   | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.200.160/30   | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.234.0/24     | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.0/22      | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.160/28    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.176/28    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.192/28    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.208/28    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.64/28     | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.24.80/28     | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.244.0/24     | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.25.128/27    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.25.160/28    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.250.0/24     | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.26.64/27     | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.27.0/28      | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.28.0/23      | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.28.160/27    | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.28.171/32    | 10.58.28.171/32    | local       | local           | vlan444    | mgmt:inb                      | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.28.190/32    | 10.58.28.190/32    | local       | local           | vlan444    | mgmt:inb                      | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.29.128/27    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.29.80/28     | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.30.0/23      | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.50.0/23      | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.50.160/27    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.50.80/28     | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 10.58.52.0/22      | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.112/32 | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.113/32 | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.114/32 | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.115/32 | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.16/30  | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.20/30  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.40/30  | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 192.168.254.44/30  | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 205.205.205.205/32 | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 206.206.206.206/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 0.0.0.0/0          | 15.3.9.254/32      | static      | static          | vlan499    | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 121.121.121.121/32 | 121.121.121.121/32 | local       | local           | lo13       | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 0          | 
|                     |                               |                    | 121.121.121.121/32 | direct      | direct          | lo13       | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 122.122.122.122/32 | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 15.3.7.0/24        | 172.16.30.161/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 172.16.30.121/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 15.3.9.0/24        | 15.3.9.3/32        | direct      | direct          | vlan499    | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 0          | 
|                     |                               |                    | 15.3.9.1/32        | direct      | direct          | vlan499    | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 0          | 
|                     |                               |                    | 15.3.9.0/32        | local       | broadcast       | null0      | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 15.3.9.0/32        | 15.3.9.3/32        | direct      | direct          | vlan499    | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 0          | 
|                     |                               |                    | 15.3.9.1/32        | direct      | direct          | vlan499    | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 0          | 
|                     |                               |                    | 15.3.9.0/32        | local       | broadcast       | null0      | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 15.3.9.1/32        | 15.3.9.1/32        | local       | local           | vlan499    | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 15.3.9.254/32      | 15.3.9.254/32      | 0           | am              | vlan499    | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 15.3.9.255/32      | 15.3.9.255/32      | 0           | broadcast       | vlan499    | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 15.3.9.3/32        | 15.3.9.3/32        | local       | local           | vlan499    | MPC-E:MPC-E-sPBR-OUT_VRF      | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.1/32      | 172.16.30.161/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.14/32     | 172.16.30.121/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.161/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.15/32     | 172.16.30.161/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.161/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.2/32      | 172.16.30.161/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 172.24.3.3/32      | 172.16.30.161/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 172.16.30.121/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 33.99.8.0/22       | 172.16.30.121/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 172.16.30.161/32   | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-IN_VRF             | 15.2.64.0/24       | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-IN_VRF             | 15.2.64.254/32     | 15.2.64.254/32     | local       | local           | vlan252    | MPC-F5T:F5-IN_VRF             | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 0.0.0.0/0          | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 15.2.10.0/24       | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 15.2.10.254/32     | 15.2.10.254/32     | local       | local           | vlan293    | MPC-F5T:F5-OUT_VRF            | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 15.2.7.0/24        | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.1/32      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.252/32    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 172.24.0.253/32    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 0.0.0.0/0          | 15.2.9.254/32      | ebgp        | bgp-50000       | vlan480    | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 20         | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 15.2.25.0/24       | 15.2.25.253/32     | direct      | direct          | vlan461    | MPC:MPC-sPBR-IN_VRF           | 0          | yes    | 0          | 
|                     |                               |                    | 15.2.25.254/32     | direct      | direct          | vlan461    | MPC:MPC-sPBR-IN_VRF           | 0          | yes    | 0          | 
|                     |                               |                    | 15.2.25.0/32       | local       | broadcast       | null0      | MPC:MPC-sPBR-IN_VRF           | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 15.2.25.0/32       | 15.2.25.253/32     | direct      | direct          | vlan461    | MPC:MPC-sPBR-IN_VRF           | 0          | yes    | 0          | 
|                     |                               |                    | 15.2.25.254/32     | direct      | direct          | vlan461    | MPC:MPC-sPBR-IN_VRF           | 0          | yes    | 0          | 
|                     |                               |                    | 15.2.25.0/32       | local       | broadcast       | null0      | MPC:MPC-sPBR-IN_VRF           | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 15.2.25.253/32     | 15.2.25.253/32     | local       | local           | vlan461    | MPC:MPC-sPBR-IN_VRF           | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 15.2.25.254/32     | 15.2.25.254/32     | local       | local           | vlan461    | MPC:MPC-sPBR-IN_VRF           | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 15.2.25.255/32     | 15.2.25.255/32     | 0           | broadcast       | vlan461    | MPC:MPC-sPBR-IN_VRF           | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 15.2.6.0/24        | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 15.2.62.0/24       | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 15.2.64.0/24       | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 15.3.21.0/24       | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 172.40.0.0/16      | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 172.60.0.0/16      | 15.2.25.1/32       | static      | static          | vlan461    | MPC:MPC-sPBR-IN_VRF           | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 201.201.201.201/32 | 201.201.201.201/32 | local       | local           | lo4        | MPC:MPC-sPBR-IN_VRF           | 0          | yes    | 0          | 
|                     |                               |                    | 201.201.201.201/32 | direct      | direct          | lo4        | MPC:MPC-sPBR-IN_VRF           | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 202.202.202.202/32 | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 0.0.0.0/0          | 15.2.9.254/32      | static      | static          | vlan480    | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 15.2.10.11/32      | 15.2.9.254/32      | static      | static          | vlan480    | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 15.2.7.0/24        | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 15.2.9.0/24        | 15.2.9.3/32        | direct      | direct          | vlan480    | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 0          | 
|                     |                               |                    | 15.2.9.1/32        | direct      | direct          | vlan480    | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 0          | 
|                     |                               |                    | 15.2.9.0/32        | local       | broadcast       | null0      | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 15.2.9.0/32        | 15.2.9.3/32        | direct      | direct          | vlan480    | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 0          | 
|                     |                               |                    | 15.2.9.1/32        | direct      | direct          | vlan480    | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 0          | 
|                     |                               |                    | 15.2.9.0/32        | local       | broadcast       | null0      | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 15.2.9.1/32        | 15.2.9.1/32        | local       | local           | vlan480    | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 15.2.9.255/32      | 15.2.9.255/32      | 0           | broadcast       | vlan480    | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 15.2.9.3/32        | 15.2.9.3/32        | local       | local           | vlan480    | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.1/32      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.14/32     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.15/32     | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.2/32      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.3/32      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.4/32      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.5/32      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 172.24.0.6/32      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 201.201.201.201/32 | 201.201.201.201/32 | local       | local           | lo11       | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 0          | 
|                     |                               |                    | 201.201.201.201/32 | direct      | direct          | lo11       | MPC:MPC-sPBR-OUT_VRF          | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 202.202.202.202/32 | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | NXOS-HandOff_Test:default     | 192.168.1.0/24     | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | NXOS-HandOff_Test:default     | 192.168.1.1/32     | 192.168.1.1/32     | local       | local           | vlan481    | NXOS-HandOff_Test:default     | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | NXOS-HandOff_Test:default     | 35.35.35.1/32      | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | NXOS-HandOff_Test:default     | 54.54.54.1/32      | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 0.0.0.0/32         | 10.3.0.1/32        | static      | static          | vlan9      | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.0.0/27        | 10.3.0.30/32       | direct      | direct          | vlan9      | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.0.0/32        | local       | broadcast       | null0      | overlay-1                     | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.0.0/32        | 10.3.0.30/32       | direct      | direct          | vlan9      | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.0.0/32        | local       | broadcast       | null0      | overlay-1                     | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.0.1/32        | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.0.1/32        | static      | static          | vlan9      | overlay-1                     | 0          | no     | 225        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.0.2/32        | 10.3.0.2/32        | 0           | am              | vlan9      | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.0.2/32        | static      | static          | vlan9      | overlay-1                     | 0          | no     | 1          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.0.3/32        | 10.3.0.3/32        | static      | static          | vlan9      | overlay-1                     | 0          | no     | 1          | 
|                     |                               |                    | 10.3.0.3/32        | 0           | am              | vlan9      | overlay-1                     | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.0.30/32       | 10.3.0.30/32       | local       | local           | vlan9      | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.0.3/32        | static      | static          | vlan9      | overlay-1                     | 0          | no     | 1          | 
|                     |                               |                    | 10.3.0.3/32        | 0           | am              | vlan9      | overlay-1                     | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.0.31/32       | 10.3.0.31/32       | 0           | broadcast       | vlan9      | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.0.3/32        | static      | static          | vlan9      | overlay-1                     | 0          | no     | 1          | 
|                     |                               |                    | 10.3.0.3/32        | 0           | am              | vlan9      | overlay-1                     | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.0.32/32       | 10.3.0.3/32        | static      | static          | vlan9      | overlay-1                     | 0          | no     | 1          | 
|                     |                               |                    | 10.3.0.3/32        | 0           | am              | vlan9      | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.0.32/32       | local       | local           | lo1023     | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.0.32/32       | direct      | direct          | lo1023     | overlay-1                     | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.0.33/32       | 10.3.0.3/32        | static      | static          | vlan9      | overlay-1                     | 0          | no     | 1          | 
|                     |                               |                    | 10.3.0.3/32        | 0           | am              | vlan9      | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.0.34/32       | 10.3.0.3/32        | static      | static          | vlan9      | overlay-1                     | 0          | no     | 1          | 
|                     |                               |                    | 10.3.0.3/32        | 0           | am              | vlan9      | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.0.35/32       | 10.3.0.3/32        | static      | static          | vlan9      | overlay-1                     | 0          | no     | 1          | 
|                     |                               |                    | 10.3.0.3/32        | 0           | am              | vlan9      | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.136.64/32     | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.136.65/32     | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.152.65/32     | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.152.66/32     | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.152.67/32     | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.192.101/32    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.192.102/32    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.192.103/32    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.192.64/32     | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.192.65/32     | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.192.67/32     | 10.3.192.67/32     | local       | local           | lo0        | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.192.67/32     | direct      | direct          | lo0        | overlay-1                     | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.192.68/32     | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.32.64/32      | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.32.65/32      | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.40.64/32      | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.40.65/32      | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.40.66/32      | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.40.67/32      | 10.3.40.67/32      | local       | local           | lo2        | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 10.3.40.67/32      | direct      | direct          | lo2        | overlay-1                     | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 10.3.48.64/32      | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 101.101.101.101/32 | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 102.102.102.102/32 | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 111.111.111.111/32 | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 112.112.112.112/32 | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 15.16.2.1/32       | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 15.16.2.5/32       | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.1.1/32      | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.10.1/32     | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.1/32     | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.225/32   | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.226/32   | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.227/32   | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.228/32   | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.230/32   | 10.3.0.1/32        | static      | static          | vlan9      | overlay-1                     | 0          | no     | 225        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.231/32   | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.232/32   | 172.16.11.232/32   | local       | local           | lo1        | overlay-1                     | 0          | yes    | 0          | 
|                     |                               |                    | 172.16.11.232/32   | direct      | direct          | lo1        | overlay-1                     | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.233/32   | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.234/32   | 10.3.0.2/32        | static      | static          | vlan9      | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.235/32   | 10.3.0.3/32        | static      | static          | vlan9      | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.236/32   | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.11.237/32   | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.12.1/32     | 10.3.32.65/32      | isis-l1-int | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-int | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.21.0/24     | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.21.1/32     | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.22.1/32     | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.30.120/32   | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.30.121/32   | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.30.160/32   | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.30.161/32   | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 172.16.30.88/32    | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 192.168.1.0/30     | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 192.168.1.4/30     | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 192.168.31.0/30    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | overlay-1                     | 192.168.32.0/30    | 10.3.192.65/32     | isis-l1-ext | isis-isis_infra | eth1/107.7 | overlay-1                     | 0          | yes    | 115        | 
|                     |                               |                    | 10.3.32.65/32      | isis-l1-ext | isis-isis_infra | eth1/108.8 | overlay-1                     | 0          | yes    | 115        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 0.0.0.0/0          | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.200.156/30   | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.200.160/30   | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.234.0/24     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.0/22      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.160/28    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.176/28    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.192/28    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.208/28    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.64/28     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.24.80/28     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.244.0/24     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.25.128/27    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.25.160/28    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.250.0/24     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.26.64/27     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
|                     |                               |                    | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.27.0/28      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.28.0/23      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.29.128/27    | 10.58.29.156/32    | direct      | direct          | vlan460    | SPIN_InnoLab:SPIN_VRF1        | 0          | yes    | 0          | 
|                     |                               |                    | 10.58.29.158/32    | direct      | direct          | vlan460    | SPIN_InnoLab:SPIN_VRF1        | 0          | yes    | 0          | 
|                     |                               |                    | 10.58.29.128/32    | local       | broadcast       | null0      | SPIN_InnoLab:SPIN_VRF1        | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.29.128/32    | 10.58.29.156/32    | direct      | direct          | vlan460    | SPIN_InnoLab:SPIN_VRF1        | 0          | yes    | 0          | 
|                     |                               |                    | 10.58.29.158/32    | direct      | direct          | vlan460    | SPIN_InnoLab:SPIN_VRF1        | 0          | yes    | 0          | 
|                     |                               |                    | 10.58.29.128/32    | local       | broadcast       | null0      | SPIN_InnoLab:SPIN_VRF1        | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.29.156/32    | 10.58.29.156/32    | local       | local           | vlan460    | SPIN_InnoLab:SPIN_VRF1        | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.29.158/32    | 10.58.29.158/32    | local       | local           | vlan460    | SPIN_InnoLab:SPIN_VRF1        | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.29.159/32    | 10.58.29.159/32    | 0           | broadcast       | vlan460    | SPIN_InnoLab:SPIN_VRF1        | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.29.80/28     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.30.0/23      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.50.0/23      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.50.160/27    | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.50.80/28     | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 10.58.52.0/22      | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 172.30.4.0/32      | 172.30.4.0/32      | local       | local           | lo3        | SPIN_InnoLab:SPIN_VRF1        | 0          | yes    | 0          | 
|                     |                               |                    | 172.30.4.0/32      | direct      | direct          | lo3        | SPIN_InnoLab:SPIN_VRF1        | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 172.30.4.1/32      | 10.3.192.68/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.112/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.113/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.114/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.115/32 | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.40/30  | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 192.168.254.44/30  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 200        | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 205.205.205.15/32  | 10.3.192.64/32     | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 206.206.206.15/32  | 10.3.32.64/32      | ibgp        | bgp-50000       |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | SPN_IntraLab:SPN_VRF1         | 192.168.0.0/24     | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | SPN_IntraLab:SPN_VRF1         | 192.168.0.254/32   | 192.168.0.254/32   | local       | local           | vlan244    | SPN_IntraLab:SPN_VRF1         | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | TESTING_BRUNO:default         | 192.168.1.0/24     | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
| pod-1/cl201-eu-spdc | TESTING_BRUNO:default         | 192.168.1.1/32     | 192.168.1.1/32     | local       | local           | vlan487    | TESTING_BRUNO:default         | 0          | yes    | 0          | 
| pod-1/cl201-eu-spdc | TESTING_BRUNO:default         | 192.168.2.0/24     | 10.3.40.64/32      | static      | static          |            | overlay-1                     | 0          | yes    | 1          | 
+---------------------+-------------------------------+--------------------+--------------------+-------------+-----------------+------------+-------------------------------+------------+--------+------------+

IPv4 Routes Summary
-------------------
- Routes  : 421
- Default : True
- Direct  : 55
- Local   : 119
- BGP     : 190
- iBGP    : 189
- eBGP    : 1
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc

{
    "duration": 14119,
    "apic": {
        "read": true,
        "success": 34,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 33,
        "connect_time": 444,
        "disconnect_time": 0,
        "mo_time": 11132,
        "total_time": 11576
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

True	444	-	connect apic11o.emea-sp.cisco.com
True	321	13	apic11o.emea-sp.cisco.com class fabricNode
True	306	31	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
True	313	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-black-hole query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	366	145	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_BGP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	326	82	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_privIP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	334	11	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	324	46	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N3-N4_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	337	33	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N6_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	332	29	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	355	46	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4-N3-N4_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	350	49	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4-N6_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	366	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	319	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-cvim1a:cvim1a-tenant_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	344	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-cvim1a:cvim1a_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	335	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-cvim4a:cvim4a-tenant_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	299	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-cvim4a:cvim4a_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	304	20	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-ECMP-demo:ACC-ext_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	301	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-ECMP-demo:MPC-CDC-2_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	336	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-iks-monitoring:iks-mon_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	333	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-management query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	318	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	343	77	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-mgmt:inb query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	350	39	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	327	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	322	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	349	32	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	483	45	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC:MPC-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	337	10	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-NXOS-HandOff_Test:default query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	372	175	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-overlay-1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	316	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-P5G:P5G_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	353	82	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-SPIN_InnoLab:SPIN_VRF1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	356	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	305	6	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-TESTING_BRUNO:default query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
```

[[Back]](./ProtocolIpv4.md)