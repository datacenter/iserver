# Node Protocol - IPv6

## Show IPv6 route table summary for selected node

```
# iserver get aci proto ipv6 --apic apic11 --node cl201-eu-spdc -o summary

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+-------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| VRF                           | State | Routes | Default | Direct | Local | BGP | iBGP | eBGP |
+-------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| black-hole                    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_BGP_VRF          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_privIP_VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_VRF              | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:smi5Gc-cvim1-N3-N4_VRF | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:smi5Gc-cvim1-N6_VRF    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:smi5Gc-cvim1_VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:smi5Gc-cvim4-N3-N4_VRF | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:smi5Gc-cvim4-N6_VRF    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:smi5Gc-cvim4_VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| cvim1a:cvim1a-tenant_VRF      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| cvim1a:cvim1a_VRF             | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| cvim4a:cvim4a-tenant_VRF      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| cvim4a:cvim4a_VRF             | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| ECMP-demo:ACC-ext_VRF         | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| ECMP-demo:MPC-CDC-2_VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| iks-monitoring:iks-mon_VRF    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| management                    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| mgmt:EU-SPDC-ERSPAN-VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| mgmt:inb                      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-E-sPBR-OUT_VRF      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-F5T:F5-IN_VRF             | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-F5T:F5-OUT_VRF            | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC:MPC-sPBR-IN_VRF           | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC:MPC-sPBR-OUT_VRF          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| NXOS-HandOff_Test:default     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| overlay-1                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| P5G:P5G_VRF                   | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| SPIN_InnoLab:SPIN_VRF1        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| SPN_IntraLab:SPN_VRF1         | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| TESTING_BRUNO:default         | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
+-------------------------------+-------+--------+---------+--------+-------+-----+------+------+
```

[[Back]](./ProtocolIpv6.md)