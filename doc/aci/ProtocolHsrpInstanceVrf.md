# Node Protocol - HSRP

## Show HSRP selected VRF domains for selected nodes

```
# iserver get aci proto hsrp --apic apic11 --node rl --vrf *mpc* -o vrf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------------+------------+
| Node                | VRF                            | Interfaces |
+---------------------+--------------------------------+------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 0          | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 0          | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 0          | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 0          | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 0          | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 0          | 
+---------------------+--------------------------------+------------+
```

[[Back]](./ProtocolHsrp.md)