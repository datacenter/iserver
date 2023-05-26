# Node Protocol - IPv4

## Show IPv4 route table summary for selected node

```
# iserver get aci proto ipv4 --apic apic11 --node rl -o summary

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| Node                | VRF                            | State | Routes | Default | Direct | Local | BGP | iBGP | eBGP |
+---------------------+--------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| pod-1/rl301-eu-spdc | black-hole                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | common:Infra_BGP_VRF           | up    | 51     | True    | 0      | 5     | 35  | 35   | 0    | 
| pod-1/rl301-eu-spdc | common:Infra_privIP_VRF        | up    | 74     | True    | 0      | 1     | 72  | 72   | 0    | 
| pod-1/rl301-eu-spdc | ECMP-demo:INT-ext_VRF          | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | ECMP-demo:MPC-RDC-3_VRF        | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | management                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF        | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | mgmt:inb                       | up    | 38     | True    | 0      | 2     | 35  | 35   | 0    | 
| pod-1/rl301-eu-spdc | MPC-E:CU-DU-Infra_VRF          | up    | 8      | False   | 0      | 1     | 6   | 0    | 6    | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | up    | 20     | True    | 3      | 10    | 2   | 2    | 0    | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | up    | 20     | True    | 3      | 5     | 8   | 5    | 3    | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | up    | 10     | True    | 3      | 5     | 2   | 1    | 1    | 
| pod-1/rl301-eu-spdc | MPC-F5T:F5-IN_VRF              | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | MPC-F5T:F5-OUT_VRF             | up    | 7      | True    | 0      | 1     | 5   | 5    | 0    | 
| pod-1/rl301-eu-spdc | MPC:MPC-sPBR-IN_VRF            | up    | 17     | True    | 0      | 5     | 7   | 7    | 0    | 
| pod-1/rl301-eu-spdc | overlay-1                      | up    | 80     | False   | 10     | 12    | 1   | 0    | 1    | 
| pod-1/rl301-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | up    | 10     | True    | 3      | 5     | 3   | 1    | 2    | 
| pod-1/rl301-eu-spdc | SPN_IntraLab:SPN_VRF1          | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl301-eu-spdc | UC3-CL2023-Demo:default        | up    | 17     | True    | 0      | 0     | 17  | 17   | 0    | 
| pod-1/rl302-eu-spdc | black-hole                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | common:Infra_BGP_VRF           | up    | 51     | True    | 0      | 5     | 35  | 35   | 0    | 
| pod-1/rl302-eu-spdc | common:Infra_privIP_VRF        | up    | 74     | True    | 0      | 1     | 72  | 72   | 0    | 
| pod-1/rl302-eu-spdc | ECMP-demo:INT-ext_VRF          | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | ECMP-demo:MPC-RDC-3_VRF        | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | management                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF        | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | mgmt:inb                       | up    | 38     | True    | 0      | 2     | 35  | 35   | 0    | 
| pod-1/rl302-eu-spdc | MPC-E:CU-DU-Infra_VRF          | up    | 8      | False   | 0      | 1     | 6   | 0    | 6    | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | up    | 20     | True    | 3      | 10    | 2   | 2    | 0    | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | up    | 20     | True    | 3      | 5     | 8   | 5    | 3    | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | up    | 10     | True    | 3      | 5     | 2   | 1    | 1    | 
| pod-1/rl302-eu-spdc | MPC-F5T:F5-IN_VRF              | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | MPC-F5T:F5-OUT_VRF             | up    | 7      | True    | 0      | 1     | 5   | 5    | 0    | 
| pod-1/rl302-eu-spdc | MPC:MPC-sPBR-IN_VRF            | up    | 17     | True    | 0      | 5     | 7   | 7    | 0    | 
| pod-1/rl302-eu-spdc | overlay-1                      | up    | 80     | False   | 10     | 12    | 1   | 0    | 1    | 
| pod-1/rl302-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | up    | 10     | True    | 3      | 5     | 3   | 1    | 2    | 
| pod-1/rl302-eu-spdc | SPN_IntraLab:SPN_VRF1          | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/rl302-eu-spdc | UC3-CL2023-Demo:default        | up    | 17     | True    | 0      | 0     | 17  | 17   | 0    | 
+---------------------+--------------------------------+-------+--------+---------+--------+-------+-----+------+------+
```

[[Back]](./ProtocolIpv4.md)