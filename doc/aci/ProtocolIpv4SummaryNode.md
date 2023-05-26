# Node Protocol - IPv4

## Show IPv4 route table summary for selected node

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc -o summary

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+-------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| Node                | VRF                           | State | Routes | Default | Direct | Local | BGP | iBGP | eBGP |
+---------------------+-------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| pod-1/cl201-eu-spdc | black-hole                    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | up    | 57     | True    | 0      | 11    | 35  | 35   | 0    | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | up    | 76     | True    | 0      | 2     | 72  | 72   | 0    | 
| pod-1/cl201-eu-spdc | common:Infra_VRF              | up    | 5      | True    | 0      | 2     | 1   | 1    | 0    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | up    | 56     | True    | 7      | 12    | 37  | 7    | 30   | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | up    | 24     | False   | 7      | 11    | 8   | 3    | 5    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | up    | 15     | True    | 3      | 6     | 5   | 5    | 0    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | up    | 39     | True    | 7      | 12    | 23  | 7    | 16   | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | up    | 24     | False   | 10     | 16    | 4   | 4    | 0    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | up    | 8      | True    | 0      | 2     | 4   | 4    | 0    | 
| pod-1/cl201-eu-spdc | cvim1a:cvim1a-tenant_VRF      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | cvim1a:cvim1a_VRF             | up    | 4      | False   | 0      | 2     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | cvim4a:cvim4a-tenant_VRF      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | cvim4a:cvim4a_VRF             | up    | 4      | False   | 0      | 2     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | up    | 9      | False   | 3      | 5     | 1   | 1    | 0    | 
| pod-1/cl201-eu-spdc | ECMP-demo:MPC-CDC-2_VRF       | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | iks-monitoring:iks-mon_VRF    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | management                    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF       | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | up    | 38     | True    | 0      | 2     | 35  | 35   | 0    | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | up    | 18     | True    | 3      | 5     | 10  | 10   | 0    | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-IN_VRF             | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | up    | 7      | True    | 0      | 1     | 5   | 5    | 0    | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | up    | 15     | True    | 3      | 5     | 4   | 3    | 1    | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | up    | 25     | True    | 3      | 5     | 16  | 16   | 0    | 
| pod-1/cl201-eu-spdc | NXOS-HandOff_Test:default     | up    | 4      | False   | 0      | 1     | 2   | 2    | 0    | 
| pod-1/cl201-eu-spdc | overlay-1                     | up    | 62     | False   | 6      | 7     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | P5G:P5G_VRF                   | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | up    | 40     | True    | 3      | 5     | 33  | 33   | 0    | 
| pod-1/cl201-eu-spdc | SPN_IntraLab:SPN_VRF1         | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | TESTING_BRUNO:default         | up    | 3      | False   | 0      | 1     | 0   | 0    | 0    | 
+---------------------+-------------------------------+-------+--------+---------+--------+-------+-----+------+------+
```

[[Back]](./ProtocolIpv4.md)