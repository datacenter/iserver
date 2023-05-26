# Node Protocol - IPv6

## Show IPv6 route table summary for selected node

```
# iserver get aci proto ipv6 --apic apic11 --node rl -o summary

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+--------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| VRF                            | State | Routes | Default | Direct | Local | BGP | iBGP | eBGP |
+--------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| black-hole                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_BGP_VRF           | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_privIP_VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| ECMP-demo:INT-ext_VRF          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| ECMP-demo:MPC-RDC-3_VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| management                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| mgmt:EU-SPDC-ERSPAN-VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| mgmt:inb                       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:CU-DU-Infra_VRF          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-E-sPBR-IN_VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-E-sPBR-OUT_VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-Residential-R3DC_VRF | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-F5T:F5-IN_VRF              | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-F5T:F5-OUT_VRF             | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC:MPC-sPBR-IN_VRF            | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| overlay-1                      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| SPIN_InnoLab:SPIN_RDC3_VRF     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| SPN_IntraLab:SPN_VRF1          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| UC3-CL2023-Demo:default        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| black-hole                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_BGP_VRF           | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_privIP_VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| ECMP-demo:INT-ext_VRF          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| ECMP-demo:MPC-RDC-3_VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| management                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| mgmt:EU-SPDC-ERSPAN-VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| mgmt:inb                       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:CU-DU-Infra_VRF          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-E-sPBR-IN_VRF        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-E-sPBR-OUT_VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-Residential-R3DC_VRF | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-F5T:F5-IN_VRF              | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-F5T:F5-OUT_VRF             | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC:MPC-sPBR-IN_VRF            | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| overlay-1                      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| SPIN_InnoLab:SPIN_RDC3_VRF     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| SPN_IntraLab:SPN_VRF1          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| UC3-CL2023-Demo:default        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
+--------------------------------+-------+--------+---------+--------+-------+-----+------+------+
```

[[Back]](./ProtocolIpv6.md)