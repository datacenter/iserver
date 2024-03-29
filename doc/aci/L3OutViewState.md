# L3 Out

## State view

- L3 out name and tenant
- enabled protocols
- VRF name
- L3 Domain

```
# iserver get aci l3out --apic apic11

Apic: apic11 (mode:online, cache:off)

L3Out [#46]
-----------

+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| Faults  | L3Out                                    | MPLS | PIM | BGP | OSPF | EIGRP | VRF                            | L3 Domain                     |
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | common/default                           | X    | X   | X   | X    | X     | common/default                 | Infra-BGP_L3Dom               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | common/Infra_BGP_L3out                   | X    | X   | V   | X    | X     | common/Infra_BGP_VRF           | Infra-BGP_L3Dom               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | common/Infra_privIP_L3out                | X    | X   | V   | X    | X     | common/Infra_privIP_VRF        | Infra-BGP_L3Dom               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | ECMP-demo/ACC-ext_L3out                  | X    | X   | X   | X    | X     | ECMP-demo/ACC-ext_VRF          | Infra_L3Dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | ECMP-demo/L3OUT-ACC_L3out                | X    | X   | V   | X    | X     | ECMP-demo/ACC_VRF              | cvim2_L3dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | ECMP-demo/L3OUT-INT_L3out                | X    | X   | V   | X    | X     | ECMP-demo/INT_VRF              | cvim2_L3dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | ECMP-demo/MPC-demo_CDDC-2_L3out          | V    | X   | X   | X    | X     | ECMP-demo/ACC_VRF              |                               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | infra/CDC-2_SRL3out                      | V    | X   | V   | X    | X     | infra/overlay-1                | SR-Infra-CDC-2_L3dom          | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | infra/multipodL3Out                      | X    | X   | V   | V    | X     | infra/overlay-1                | multipodL3Out_RoutedDomain    | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 1 | infra/RDC-3_SRL3out                      | V    | X   | V   | X    | X     | infra/overlay-1                | SR-Infra-RDC-3_L3dom          | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | infra/RL-L3Out                           | X    | X   | V   | V    | X     | infra/overlay-1                | RL-L3Out_RoutedDomain         | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | mgmt/INB_L3out                           | X    | X   | V   | X    | X     | mgmt/inb                       | Infra_L3Dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | MPC-E/CU-DU-Infra-SR-Backbone            | V    | X   | X   | X    | X     | MPC-E/CU-DU-Infra_VRF          |                               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | MPC-E/MPC-E-OUT                          | X    | X   | X   | X    | X     | MPC-E/MPC-E-sPBR-OUT_VRF       | Infra_L3Dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | MPC-E/MPC-E-Residential-IN               | X    | X   | X   | X    | X     | MPC-E/MPC-Residential-R3DC_VRF | Infra_L3Dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | MPC-E/MPC-E-sPBR-IN                      | X    | X   | X   | X    | X     | MPC-E/MPC-E-sPBR-IN_VRF        | Infra_L3Dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | MPC-E/MPC-E-sPBR-OUT                     | X    | X   | V   | X    | X     | MPC-E/MPC-E-sPBR-OUT_VRF       | Infra_L3Dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | MPC-E/MPC-Residential-R3DC_SRL3out       | V    | X   | X   | X    | X     | MPC-E/MPC-Residential-R3DC_VRF |                               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | MPC-F5T/F5-OUT                           | X    | X   | V   | X    | X     | MPC-F5T/F5-OUT_VRF             | UCSB1_L3Dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | MPC/MPC-OUT                              | X    | X   | X   | X    | X     | MPC/MPC-sPBR-OUT_VRF           | Infra_L3Dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | MPC/MPC-sPBR-IN                          | X    | X   | X   | X    | X     | MPC/MPC-sPBR-IN_VRF            | Infra_L3Dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | MPC/MPC-sPBR-IN_SRL3out                  | V    | X   | X   | X    | X     | MPC/MPC-sPBR-IN_VRF            |                               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | MPC/MPC-sPBR-OUT                         | X    | X   | V   | X    | X     | MPC/MPC-sPBR-OUT_VRF           | UCSB1_L3Dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | NXOS-HandOff_Test/SR_CORE                | V    | X   | X   | X    | X     | NXOS-HandOff_Test/default      |                               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/4G_PDN_L3Out                      | X    | X   | V   | X    | X     | common/smi5Gc-cvim4-N6_VRF     | smi5Gc-cvim4-SRIOV_L3Dom      | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/4G_RAN_L3Out                      | X    | X   | V   | X    | X     | common/smi5Gc-cvim4-N3-N4_VRF  | smi5Gc-cvim4-SRIOV_L3Dom      | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/smi5Gc-cvim1-4G-PDN_L3Out         | X    | X   | V   | X    | X     | common/smi5Gc-cvim1-N6_VRF     | smi5Gc-cvim1-SRIOV_L3Dom      | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/smi5Gc-cvim1-4G_RAN_L3Out         | X    | X   | V   | X    | X     | common/smi5Gc-cvim1-N3-N4_VRF  | smi5Gc-cvim1-SRIOV_L3Dom      | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/smi5Gc-cvim1-BACKBONE_L3Out       | X    | X   | V   | X    | X     | common/smi5Gc-cvim1_VRF        | Infra-BGP_L3Dom               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/smi5Gc-cvim1-Control_SBI_L3Out    | X    | X   | V   | X    | X     | common/smi5Gc-cvim1_VRF        | smi5Gc-cvim1-SRIOV_L3Dom      | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/smi5Gc-cvim1-N3-N4-BACKBONE_L3Out | X    | X   | V   | X    | X     | common/smi5Gc-cvim1-N3-N4_VRF  | Infra-BGP_L3Dom               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/smi5Gc-cvim1-N3-N4_L3Out          | X    | X   | V   | X    | X     | common/smi5Gc-cvim1-N3-N4_VRF  | smi5Gc-cvim1-SRIOV_L3Dom      | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/smi5Gc-cvim1-N6_L3Out             | X    | X   | V   | X    | X     | common/smi5Gc-cvim1-N6_VRF     | smi5Gc-cvim1-SRIOV_L3Dom      | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/smi5Gc-cvim4-BACKBONE_L3Out       | X    | X   | V   | X    | X     | common/smi5Gc-cvim4_VRF        | Infra-BGP_L3Dom               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/smi5Gc-cvim4-N3-N4-BACKBONE_L3Out | X    | X   | V   | X    | X     | common/smi5Gc-cvim4-N3-N4_VRF  | Infra-BGP_L3Dom               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/smi5Gc-cvim4-N3-N4_L3Out          | X    | X   | V   | X    | X     | common/smi5Gc-cvim4-N3-N4_VRF  | smi5Gc-cvim4-SRIOV_L3Dom      | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/smi5Gc-cvim4-N6_L3Out             | X    | X   | V   | X    | X     | common/smi5Gc-cvim4-N6_VRF     | smi5Gc-cvim4-SRIOV_L3Dom      | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | smi5Gc/TEST_FSVI_MODULE_L3Out            | X    | X   | V   | X    | X     | common/smi5Gc-cvim4-N6_VRF     | smi5Gc-cvim4-SRIOV_L3Dom      | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_L3Out                | X    | X   | V   | X    | X     | SPIN_InnoLab/SPIN_VRF1         | SPIN_InnoLab_Calico_L3Dom     | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_RDC3                 | V    | X   | X   | X    | X     | SPIN_InnoLab/SPIN_RDC3_VRF     |                               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_RDC_L3Out            | X    | X   | V   | X    | X     | SPIN_InnoLab/SPIN_RDC3_VRF     | SPIN_InnoLab_Calico_RDC_L3Dom | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/Calico_SRL3Out              | V    | X   | X   | X    | X     | SPIN_InnoLab/SPIN_VRF1         |                               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | SPIN_InnoLab/IPN_L3Out                   | X    | X   | V   | X    | X     | SPIN_InnoLab/SPIN_VRF1         | Infra-BGP_L3Dom               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | UC3-CL2023-Demo/K8S                      | X    | X   | V   | X    | X     | UC3-CL2023-Demo/default        | UCSB1_L3Dom                   | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | UC3-CL2023-Demo/LAB_Backbone             | X    | X   | V   | X    | X     | UC3-CL2023-Demo/default        | Infra-BGP_L3Dom               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
| 0 0 0 0 | UC3-CL2023-Demo/SR_Backbone              | V    | X   | X   | X    | X     | UC3-CL2023-Demo/default        |                               | 
+---------+------------------------------------------+------+-----+-----+------+-------+--------------------------------+-------------------------------+
```

Developer

```
# iserver get aci l3out --apic apic11

{
    "duration": 1632,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 473,
        "disconnect_time": 0,
        "mo_time": 855,
        "total_time": 1328
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

True	473	-	connect apic11o.emea-sp.cisco.com:443
True	470	46	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	385	43	apic11o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)