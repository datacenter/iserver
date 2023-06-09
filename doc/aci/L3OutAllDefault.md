# L3 Out

## Get main properties of L3 outs

- L3 out name and tenant
- enabled protocols
- VRF name
- L3 Domain

```
# iserver get aci l3out --apic apic11

Apic: apic11 (mode:online, cache:off)

+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| L3Out                                    | MPLS | PIM | BGP | OSPF | EIGRP | VRF                            | L3 Domain                     |
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| common/default                           | X    | X   | X   | X    | X     | common/default                 | Infra-BGP_L3Dom               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| common/Infra_BGP_L3out                   | X    | X   | V   | X    | X     | common/Infra_BGP_VRF           | Infra-BGP_L3Dom               | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| common/Infra_privIP_L3out                | X    | X   | V   | X    | X     | common/Infra_privIP_VRF        | Infra-BGP_L3Dom               | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| ECMP-demo/ACC-ext_L3out                  | X    | X   | X   | X    | X     | ECMP-demo/ACC-ext_VRF          | Infra_L3Dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| ECMP-demo/L3OUT-ACC_L3out                | X    | X   | V   | X    | X     | ECMP-demo/ACC_VRF              | cvim2_L3dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| ECMP-demo/L3OUT-INT_L3out                | X    | X   | V   | X    | X     | ECMP-demo/INT_VRF              | cvim2_L3dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| ECMP-demo/MPC-demo_CDDC-2_L3out          | V    | X   | X   | X    | X     | ECMP-demo/ACC_VRF              |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| infra/CDC-2_SRL3out                      | V    | X   | V   | X    | X     | infra/overlay-1                | SR-Infra-CDC-2_L3dom          | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| infra/multipodL3Out                      | X    | X   | V   | V    | X     | infra/overlay-1                | multipodL3Out_RoutedDomain    | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| infra/RDC-3_SRL3out                      | V    | X   | V   | X    | X     | infra/overlay-1                | SR-Infra-RDC-3_L3dom          | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| infra/RL-L3Out                           | X    | X   | V   | V    | X     | infra/overlay-1                | RL-L3Out_RoutedDomain         | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| mgmt/INB_L3out                           | X    | X   | V   | X    | X     | mgmt/inb                       | Infra_L3Dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| MPC-E/CU-DU-Infra-SR-Backbone            | V    | X   | X   | X    | X     | MPC-E/CU-DU-Infra_VRF          |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| MPC-E/MPC-E-OUT                          | X    | X   | X   | X    | X     | MPC-E/MPC-E-sPBR-OUT_VRF       | Infra_L3Dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| MPC-E/MPC-E-Residential-IN               | X    | X   | X   | X    | X     | MPC-E/MPC-Residential-R3DC_VRF | Infra_L3Dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| MPC-E/MPC-E-sPBR-IN                      | X    | X   | X   | X    | X     | MPC-E/MPC-E-sPBR-IN_VRF        | Infra_L3Dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| MPC-E/MPC-E-sPBR-OUT                     | X    | X   | V   | X    | X     | MPC-E/MPC-E-sPBR-OUT_VRF       | Infra_L3Dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| MPC-E/MPC-Residential-R3DC_SRL3out       | V    | X   | X   | X    | X     | MPC-E/MPC-Residential-R3DC_VRF |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| MPC-F5T/F5-OUT                           | X    | X   | V   | X    | X     | MPC-F5T/F5-OUT_VRF             | UCSB1_L3Dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| MPC/MPC-OUT                              | X    | X   | X   | X    | X     | MPC/MPC-sPBR-OUT_VRF           | Infra_L3Dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| MPC/MPC-sPBR-IN                          | X    | X   | X   | X    | X     | MPC/MPC-sPBR-IN_VRF            | Infra_L3Dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| MPC/MPC-sPBR-IN_SRL3out                  | V    | X   | X   | X    | X     | MPC/MPC-sPBR-IN_VRF            |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| MPC/MPC-sPBR-OUT                         | X    | X   | V   | X    | X     | MPC/MPC-sPBR-OUT_VRF           | UCSB1_L3Dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| NXOS-HandOff_Test/SR_CORE                | V    | X   | X   | X    | X     | NXOS-HandOff_Test/default      |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/4G_PDN_L3Out                      | X    | X   | V   | X    | X     | common/smi5Gc-cvim4-N6_VRF     | smi5Gc-cvim4-SRIOV_L3Dom      | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/4G_RAN_L3Out                      | X    | X   | V   | X    | X     | common/smi5Gc-cvim4-N3-N4_VRF  | smi5Gc-cvim4-SRIOV_L3Dom      | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/smi5Gc-cvim1-4G-PDN_L3Out         | X    | X   | V   | X    | X     | common/smi5Gc-cvim1-N6_VRF     | smi5Gc-cvim1-SRIOV_L3Dom      | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/smi5Gc-cvim1-4G_RAN_L3Out         | X    | X   | V   | X    | X     | common/smi5Gc-cvim1-N3-N4_VRF  | smi5Gc-cvim1-SRIOV_L3Dom      | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/smi5Gc-cvim1-BACKBONE_L3Out       | X    | X   | V   | X    | X     | common/smi5Gc-cvim1_VRF        | Infra-BGP_L3Dom               | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/smi5Gc-cvim1-Control_SBI_L3Out    | X    | X   | V   | X    | X     | common/smi5Gc-cvim1_VRF        | smi5Gc-cvim1-SRIOV_L3Dom      | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/smi5Gc-cvim1-N3-N4-BACKBONE_L3Out | X    | X   | V   | X    | X     | common/smi5Gc-cvim1-N3-N4_VRF  | Infra-BGP_L3Dom               | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/smi5Gc-cvim1-N3-N4_L3Out          | X    | X   | V   | X    | X     | common/smi5Gc-cvim1-N3-N4_VRF  | smi5Gc-cvim1-SRIOV_L3Dom      | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/smi5Gc-cvim1-N6_L3Out             | X    | X   | V   | X    | X     | common/smi5Gc-cvim1-N6_VRF     | smi5Gc-cvim1-SRIOV_L3Dom      | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/smi5Gc-cvim4-BACKBONE_L3Out       | X    | X   | V   | X    | X     | common/smi5Gc-cvim4_VRF        | Infra-BGP_L3Dom               | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/smi5Gc-cvim4-N3-N4-BACKBONE_L3Out | X    | X   | V   | X    | X     | common/smi5Gc-cvim4-N3-N4_VRF  | Infra-BGP_L3Dom               | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/smi5Gc-cvim4-N3-N4_L3Out          | X    | X   | V   | X    | X     | common/smi5Gc-cvim4-N3-N4_VRF  | smi5Gc-cvim4-SRIOV_L3Dom      | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/smi5Gc-cvim4-N6_L3Out             | X    | X   | V   | X    | X     | common/smi5Gc-cvim4-N6_VRF     | smi5Gc-cvim4-SRIOV_L3Dom      | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| smi5Gc/TEST_FSVI_MODULE_L3Out            | X    | X   | V   | X    | X     | common/smi5Gc-cvim4-N6_VRF     | smi5Gc-cvim4-SRIOV_L3Dom      | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| SPIN_InnoLab/Calico_L3Out                | X    | X   | V   | X    | X     | SPIN_InnoLab/SPIN_VRF1         | SPIN_InnoLab_Calico_L3Dom     | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| SPIN_InnoLab/Calico_RDC3                 | V    | X   | X   | X    | X     | SPIN_InnoLab/SPIN_RDC3_VRF     |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| SPIN_InnoLab/Calico_RDC_L3Out            | X    | X   | V   | X    | X     | SPIN_InnoLab/SPIN_RDC3_VRF     | SPIN_InnoLab_Calico_RDC_L3Dom | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| SPIN_InnoLab/Calico_SRL3Out              | V    | X   | X   | X    | X     | SPIN_InnoLab/SPIN_VRF1         |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| SPIN_InnoLab/IPN_L3Out                   | X    | X   | V   | X    | X     | SPIN_InnoLab/SPIN_VRF1         | Infra-BGP_L3Dom               | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| UC3-CL2023-Demo/K8S                      | X    | X   | V   | X    | X     | UC3-CL2023-Demo/default        | UCSB1_L3Dom                   | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| UC3-CL2023-Demo/LAB_Backbone             | X    | X   | V   | X    | X     | UC3-CL2023-Demo/default        | Infra-BGP_L3Dom               | 
|                                          |      |     |     |      |       |                                |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| UC3-CL2023-Demo/SR_Backbone              | V    | X   | X   | X    | X     | UC3-CL2023-Demo/default        |                               | 
+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
```

Developer

```
# iserver get aci l3out --apic apic11

{
    "duration": 1958,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 430,
        "disconnect_time": 0,
        "mo_time": 743,
        "total_time": 1173
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

True	430	-	connect apic11o.emea-sp.cisco.com
True	388	46	apic11o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	355	43	apic11o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)