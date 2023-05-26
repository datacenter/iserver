# Node Protocol - IPv4

## Filter IPv4 route table that include IP address

```
# iserver get aci proto ipv4 --apic apic11 --node rl --ip 172.16.21.28

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------------+----------------+------------------+------------+-----------------+------------+-----------+------------+--------+------------+
| Node                | VRF                            | Prefix         | Next Hop         | Type       | Source          | Interface  | NH VRF    | MPLS Label | Active | Preference |
+---------------------+--------------------------------+----------------+------------------+------------+-----------------+------------+-----------+------------+--------+------------+
| pod-1/rl301-eu-spdc | common:Infra_BGP_VRF           | 0.0.0.0/0      | 172.16.11.233/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
|                     |                                |                | 172.16.11.237/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
| pod-1/rl301-eu-spdc | common:Infra_privIP_VRF        | 0.0.0.0/0      | 172.16.11.233/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
|                     |                                |                | 172.16.11.237/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
| pod-1/rl301-eu-spdc | mgmt:inb                       | 0.0.0.0/0      | 172.16.11.233/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
|                     |                                |                | 172.16.11.237/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 0.0.0.0/0      | 172.16.11.232/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
|                     |                                |                | 172.16.11.231/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 0.0.0.0/0      | 172.16.11.232/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
|                     |                                |                | 172.16.11.231/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 0.0.0.0/0      | 172.31.3.35/32   | ebgp       | bgp-50000       |            | overlay-1 | 24097      | yes    | 20         | 
| pod-1/rl301-eu-spdc | MPC-F5T:F5-OUT_VRF             | 0.0.0.0/0      | 172.16.11.233/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
|                     |                                |                | 172.16.11.237/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
| pod-1/rl301-eu-spdc | MPC:MPC-sPBR-IN_VRF            | 0.0.0.0/0      | 172.16.11.232/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
|                     |                                |                | 172.16.11.231/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
| pod-1/rl301-eu-spdc | overlay-1                      | 172.16.21.0/24 | 192.168.31.2/32  | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |                                |                | 172.16.30.120/32 | isis-l1    | isis-isis_infra | eth1/33.47 | overlay-1 | 0          | no     | 250        | 
|                     |                                |                | 172.16.30.120/32 | isis-l1    | isis-isis_infra | eth1/34.48 | overlay-1 | 0          | no     | 250        | 
| pod-1/rl301-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | 0.0.0.0/0      | 172.31.3.35/32   | ebgp       | bgp-50000       |            | overlay-1 | 24006      | yes    | 20         | 
| pod-1/rl301-eu-spdc | UC3-CL2023-Demo:default        | 0.0.0.0/0      | 172.16.11.233/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
|                     |                                |                | 172.16.11.237/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
| pod-1/rl302-eu-spdc | common:Infra_BGP_VRF           | 0.0.0.0/0      | 172.16.11.233/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
|                     |                                |                | 172.16.11.237/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
| pod-1/rl302-eu-spdc | common:Infra_privIP_VRF        | 0.0.0.0/0      | 172.16.11.233/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
|                     |                                |                | 172.16.11.237/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
| pod-1/rl302-eu-spdc | mgmt:inb                       | 0.0.0.0/0      | 172.16.11.233/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
|                     |                                |                | 172.16.11.237/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 0.0.0.0/0      | 172.16.11.232/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
|                     |                                |                | 172.16.11.231/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 0.0.0.0/0      | 172.16.11.232/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
|                     |                                |                | 172.16.11.231/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 0.0.0.0/0      | 172.31.3.35/32   | ebgp       | bgp-50000       |            | overlay-1 | 24097      | yes    | 20         | 
| pod-1/rl302-eu-spdc | MPC-F5T:F5-OUT_VRF             | 0.0.0.0/0      | 172.16.11.233/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
|                     |                                |                | 172.16.11.237/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
| pod-1/rl302-eu-spdc | MPC:MPC-sPBR-IN_VRF            | 0.0.0.0/0      | 172.16.11.232/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
|                     |                                |                | 172.16.11.231/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 1          | 
| pod-1/rl302-eu-spdc | overlay-1                      | 172.16.21.0/24 | 192.168.32.2/32  | ospf-type2 | ospf-default    | eth1/36.6  | overlay-1 | 0          | yes    | 110        | 
|                     |                                |                | 172.16.30.160/32 | isis-l1    | isis-isis_infra | eth1/33.7  | overlay-1 | 0          | no     | 250        | 
|                     |                                |                | 172.16.30.160/32 | isis-l1    | isis-isis_infra | eth1/34.8  | overlay-1 | 0          | no     | 250        | 
| pod-1/rl302-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | 0.0.0.0/0      | 172.31.3.35/32   | ebgp       | bgp-50000       |            | overlay-1 | 24006      | yes    | 20         | 
| pod-1/rl302-eu-spdc | UC3-CL2023-Demo:default        | 0.0.0.0/0      | 172.16.11.233/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
|                     |                                |                | 172.16.11.237/32 | ibgp       | bgp-50000       |            | overlay-1 | 0          | yes    | 200        | 
+---------------------+--------------------------------+----------------+------------------+------------+-----------------+------------+-----------+------------+--------+------------+
```

[[Back]](./ProtocolIpv4.md)