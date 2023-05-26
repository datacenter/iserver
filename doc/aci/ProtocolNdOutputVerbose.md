# Node Protocol - ND

## Verbose output

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc -o verbose

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

Neighbor Discovery Instance
---------------------------
- Node                   : pod-1/bl205-eu-spdc
- Admin State            : enabled
- Aging Interval         : 1380
- Neighbor Count         : 0
- Active Interface Count : 0


+-------------------------------+------------+-----------+
| VRF                           | Interfaces | Neighbors |
+-------------------------------+------------+-----------+
| common:Infra_BGP_VRF          | 6          | 0         | 
| common:Infra_privIP_VRF       | 2          | 0         | 
| common:Infra_VRF              | 1          | 0         | 
| common:smi5Gc-cvim1-N3-N4_VRF | 0          | 0         | 
| common:smi5Gc-cvim1_VRF       | 0          | 0         | 
| common:smi5Gc-cvim4-N3-N4_VRF | 0          | 0         | 
| common:smi5Gc-cvim4_VRF       | 0          | 0         | 
| ECMP-demo:ACC_VRF             | 0          | 0         | 
| ECMP-demo:INT-ext_VRF         | 1          | 0         | 
| ECMP-demo:MPC-CDC-2_VRF       | 1          | 0         | 
| iks-monitoring:iks-mon_VRF    | 1          | 0         | 
| management                    | 0          | 0         | 
| mgmt:EU-SPDC-ERSPAN-VRF       | 1          | 0         | 
| mgmt:inb                      | 1          | 0         | 
| MPC-E:CU-DU-Infra_VRF         | 1          | 0         | 
| MPC-E:MPC-E-sPBR-IN_VRF       | 5          | 0         | 
| MPC-F5T:F5-IN_VRF             | 1          | 0         | 
| MPC-F5T:F5-OUT_VRF            | 1          | 0         | 
| MPC:MPC-sPBR-IN_VRF           | 5          | 0         | 
| MPC:MPC-sPBR-OUT_VRF          | 0          | 0         | 
| NXOS-HandOff_Test:default     | 1          | 0         | 
| P5G:P5G_VRF                   | 1          | 0         | 
| SPIN_InnoLab:SPIN_VRF1        | 4          | 0         | 
| SPN_IntraLab:SPN_VRF1         | 1          | 0         | 
| TESTING_BRUNO:default         | 1          | 0         | 
| UC3-CL2023-Demo:default       | 0          | 0         | 
+-------------------------------+------------+-----------+
```

[[Back]](./ProtocolNd.md)