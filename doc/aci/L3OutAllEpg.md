# L3 Out

## Get EPG properties of L3 outs

- L3 out name and tenant
- VRF name
- L3 Domain
- External EPG

```
# iserver get aci l3out --apic apic11 --view epg

Apic: apic11 (mode:online, cache:off)

+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| L3Out Name                               | VRF                            | L3 Domain                     | External EPG                |
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| common/default                           | common/default                 | Infra-BGP_L3Dom               |                             | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| common/Infra_BGP_L3out                   | common/Infra_BGP_VRF           | Infra-BGP_L3Dom               | Infra_BGP_L3out_ExtEPG      | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| common/Infra_privIP_L3out                | common/Infra_privIP_VRF        | Infra-BGP_L3Dom               | Infra_privIP_ExtEPG         | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| ECMP-demo/ACC-ext_L3out                  | ECMP-demo/ACC-ext_VRF          | Infra_L3Dom                   | ACC-ext_ExtEPG              | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| ECMP-demo/L3OUT-ACC_L3out                | ECMP-demo/ACC_VRF              | cvim2_L3dom                   | ACC_ExtEPG                  | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| ECMP-demo/L3OUT-INT_L3out                | ECMP-demo/INT_VRF              | cvim2_L3dom                   | INT_ExtEPG                  | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| ECMP-demo/MPC-demo_CDDC-2_L3out          | ECMP-demo/ACC_VRF              |                               | MPC-demo_CDDC-2_ExtEPG      | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| infra/CDC-2_SRL3out                      | infra/overlay-1                | SR-Infra-CDC-2_L3dom          | CDC-2_SRL3out_ExtEPG        | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| infra/multipodL3Out                      | infra/overlay-1                | multipodL3Out_RoutedDomain    | ipnInstP                    | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| infra/RDC-3_SRL3out                      | infra/overlay-1                | SR-Infra-RDC-3_L3dom          | RDC-3_SRL3out_ExtEPG        | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| infra/RL-L3Out                           | infra/overlay-1                | RL-L3Out_RoutedDomain         | ipnInstP                    | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| mgmt/INB_L3out                           | mgmt/inb                       | Infra_L3Dom                   | INB_ExtEPG                  | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| MPC-E/CU-DU-Infra-SR-Backbone            | MPC-E/CU-DU-Infra_VRF          |                               | default                     | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| MPC-E/MPC-E-OUT                          | MPC-E/MPC-E-sPBR-OUT_VRF       | Infra_L3Dom                   | MPC-E-OUT                   | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| MPC-E/MPC-E-Residential-IN               | MPC-E/MPC-Residential-R3DC_VRF | Infra_L3Dom                   | MPC-E-Residential-IN        | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| MPC-E/MPC-E-sPBR-IN                      | MPC-E/MPC-E-sPBR-IN_VRF        | Infra_L3Dom                   | MPC-E-sPBR-IN               | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| MPC-E/MPC-E-sPBR-OUT                     | MPC-E/MPC-E-sPBR-OUT_VRF       | Infra_L3Dom                   | MPC-E-sPBR-OUT              | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| MPC-E/MPC-Residential-R3DC_SRL3out       | MPC-E/MPC-Residential-R3DC_VRF |                               | MPC-Residential-R3DC_ExtEPG | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| MPC-F5T/F5-OUT                           | MPC-F5T/F5-OUT_VRF             | UCSB1_L3Dom                   | F5_ExtEPG                   | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| MPC/MPC-OUT                              | MPC/MPC-sPBR-OUT_VRF           | Infra_L3Dom                   | MPC-OUT                     | 
|                                          |                                |                               | Residential-Gaming          | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| MPC/MPC-sPBR-IN                          | MPC/MPC-sPBR-IN_VRF            | Infra_L3Dom                   | MPC-sPBR-IN                 | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| MPC/MPC-sPBR-IN_SRL3out                  | MPC/MPC-sPBR-IN_VRF            |                               | MPC-sPBR-IN_ExtEPG          | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| MPC/MPC-sPBR-OUT                         | MPC/MPC-sPBR-OUT_VRF           | UCSB1_L3Dom                   | MPC-sPBR-OUT                | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| NXOS-HandOff_Test/SR_CORE                | NXOS-HandOff_Test/default      |                               | SR_CORE                     | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/4G_PDN_L3Out                      | common/smi5Gc-cvim4-N6_VRF     | smi5Gc-cvim4-SRIOV_L3Dom      | default                     | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/4G_RAN_L3Out                      | common/smi5Gc-cvim4-N3-N4_VRF  | smi5Gc-cvim4-SRIOV_L3Dom      | default                     | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/smi5Gc-cvim1-4G-PDN_L3Out         | common/smi5Gc-cvim1-N6_VRF     | smi5Gc-cvim1-SRIOV_L3Dom      | default                     | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/smi5Gc-cvim1-4G_RAN_L3Out         | common/smi5Gc-cvim1-N3-N4_VRF  | smi5Gc-cvim1-SRIOV_L3Dom      | default                     | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/smi5Gc-cvim1-BACKBONE_L3Out       | common/smi5Gc-cvim1_VRF        | Infra-BGP_L3Dom               | LAB_BACKBONE                | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/smi5Gc-cvim1-Control_SBI_L3Out    | common/smi5Gc-cvim1_VRF        | smi5Gc-cvim1-SRIOV_L3Dom      | default                     | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/smi5Gc-cvim1-N3-N4-BACKBONE_L3Out | common/smi5Gc-cvim1-N3-N4_VRF  | Infra-BGP_L3Dom               | LAB_BACKBONE                | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/smi5Gc-cvim1-N3-N4_L3Out          | common/smi5Gc-cvim1-N3-N4_VRF  | smi5Gc-cvim1-SRIOV_L3Dom      | smi5Gc-cvim1-N3-N4_ExtEPG   | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/smi5Gc-cvim1-N6_L3Out             | common/smi5Gc-cvim1-N6_VRF     | smi5Gc-cvim1-SRIOV_L3Dom      | smi5Gc-cvim1-N6_ExtEPG      | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/smi5Gc-cvim4-BACKBONE_L3Out       | common/smi5Gc-cvim4_VRF        | Infra-BGP_L3Dom               | LAB_BACKBONE                | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/smi5Gc-cvim4-N3-N4-BACKBONE_L3Out | common/smi5Gc-cvim4-N3-N4_VRF  | Infra-BGP_L3Dom               | LAB_BACKBONE                | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/smi5Gc-cvim4-N3-N4_L3Out          | common/smi5Gc-cvim4-N3-N4_VRF  | smi5Gc-cvim4-SRIOV_L3Dom      | smi5Gc-cvim4-N3-N4_ExtEPG   | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/smi5Gc-cvim4-N6_L3Out             | common/smi5Gc-cvim4-N6_VRF     | smi5Gc-cvim4-SRIOV_L3Dom      | smi5Gc-cvim4-N6_ExtEPG      | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| smi5Gc/TEST_FSVI_MODULE_L3Out            | common/smi5Gc-cvim4-N6_VRF     | smi5Gc-cvim4-SRIOV_L3Dom      | default                     | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| SPIN_InnoLab/Calico_L3Out                | SPIN_InnoLab/SPIN_VRF1         | SPIN_InnoLab_Calico_L3Dom     | Calico_Default              | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| SPIN_InnoLab/Calico_RDC3                 | SPIN_InnoLab/SPIN_RDC3_VRF     |                               | WORLD                       | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| SPIN_InnoLab/Calico_RDC_L3Out            | SPIN_InnoLab/SPIN_RDC3_VRF     | SPIN_InnoLab_Calico_RDC_L3Dom | Calico_RDC                  | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| SPIN_InnoLab/Calico_SRL3Out              | SPIN_InnoLab/SPIN_VRF1         |                               | REMOTE_DCs                  | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| SPIN_InnoLab/IPN_L3Out                   | SPIN_InnoLab/SPIN_VRF1         | Infra-BGP_L3Dom               | Default                     | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| UC3-CL2023-Demo/K8S                      | UC3-CL2023-Demo/default        | UCSB1_L3Dom                   | SECURE                      | 
|                                          |                                |                               | K8S                         | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| UC3-CL2023-Demo/LAB_Backbone             | UC3-CL2023-Demo/default        | Infra-BGP_L3Dom               | LAB                         | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
| UC3-CL2023-Demo/SR_Backbone              | UC3-CL2023-Demo/default        |                               | K8S_Far_Edge                | 
+------------------------------------------+--------------------------------+-------------------------------+-----------------------------+
```

Developer

```
# iserver get aci l3out --apic apic11 --view epg

{
    "duration": 1496,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 418,
        "disconnect_time": 0,
        "mo_time": 739,
        "total_time": 1157
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

True	418	-	connect apic11o.emea-sp.cisco.com
True	397	46	apic11o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	342	43	apic11o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)