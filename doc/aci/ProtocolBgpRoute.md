# Node Protocol - BGP

Show IP route table BGP-sourced entries learnt by selected nodes and neighbors.

```
# iserver get aci proto bgp --apic apic11 --node rl -o route

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------+----------------+---------------+------+-----------+--------------------------+------------+--------+------------+
| Node                | VRF                      | Prefix         | Next Hop      | Type | Source    | NH VRF                   | MPLS Label | Active | Preference |
+---------------------+--------------------------+----------------+---------------+------+-----------+--------------------------+------------+--------+------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.0.0/22   | 172.24.3.1/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.4.0/22   | 172.24.3.2/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.8.0/22   | 172.24.3.3/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.31.3.35/32 | 15.16.3.1/32  | ebgp | bgp-50000 | overlay-1                | 3          | yes    | 20         | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.0.0/22   | 172.24.3.1/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.4.0/22   | 172.24.3.2/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 33.99.8.0/22   | 172.24.3.3/32 | ebgp | bgp-50000 | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 20         | 
| pod-1/rl302-eu-spdc | overlay-1                | 172.31.3.35/32 | 15.16.3.5/32  | ebgp | bgp-50000 | overlay-1                | 3          | yes    | 20         | 
+---------------------+--------------------------+----------------+---------------+------+-----------+--------------------------+------------+--------+------------+
```

[[Back]](./ProtocolBgp.md)