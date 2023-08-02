# Attachable Access Entity Profile (AAEP)

## State view

```
# iserver get aci aaep --apic apic11 --view state

Apic: apic11 (mode:online, cache:off)

Attachable Access Entity Profile (AAEP) [#30]
---------------------------------------------

+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| Faults  | Name                        | Infra VLAN | Domain Type | Domain Name                            | Domain State   | EPG  | PG Interface Type | PG Name                     |
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | cvim-brAPI_AAEP             | X          | Physical    | cvim-brAPI_PhysDom                     | formed         | --   | PC/VPC Interface  | pod-4a-br-API               | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod1a-API_PolGrp            | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | cvim1-SRIOV_AAEP            | X          | Physical    | smi5Gc-cvim1-SRIOV-FloatingSVI_PhysDom | formed         | --   | Leaf Access Port  | pod1a-SRIOV-0_PolGrp        | 
|         |                             |            | L3          | smi5Gc-cvim1-SRIOV_L3Dom               | formed         |      | Leaf Access Port  | pod1a-SRIOV-1_PolGrp        | 
|         |                             |            | Physical    | smi5Gc-cvim1-SRIOV_PhysDom             | formed         |      | Leaf Access Port  | pod1a-SRIoV-0_PolGrp        | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | cvim4-SRIOV_AAEP            | X          | Physical    | smi5Gc-cvim4-SRIOV-FloatingSVI_PhysDom | formed         | --   | Leaf Access Port  | cvim4-SRIoV-0_PolGrp        | 
|         |                             |            | L3          | smi5Gc-cvim4-SRIOV_L3Dom               | formed         |      | Leaf Access Port  | cvim4-SRIoV-1_PolGrp        | 
|         |                             |            | Physical    | smi5Gc-cvim4-SRIOV_PhysDom             | formed         |      | Leaf Access Port  | pod4a-AIO-1-SRIoV-0_PolGrp  | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod4a-AIO-1-SRIoV-1_PolGrp  | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod4a-AIO-2-SRIoV-0_PolGrp  | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod4a-AIO-2-SRIoV-1_PolGrp  | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod4a-AIO-3-SRIoV-0_PolGrp  | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod4a-AIO-3-SRIoV-1_PolGrp  | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod4a-COMP-1-SRIoV-0_PolGrp | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod4a-COMP-1-SRIoV-1_PolGrp | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod4a-COMP-2-SRIoV-0_PolGrp | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod4a-COMP-2-SRIoV-1_PolGrp | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod4a-COMP-3-SRIoV-0_PolGrp | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod4a-COMP-3-SRIoV-1_PolGrp | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | DC-CFP                      | X          | L3          | DC-CFP                                 | formed         | --   | Leaf Access Port  | BERLIN-35-RDC-3-vlan        | 
|         |                             |            | Physical    | DC-CFP                                 | formed         |      | Leaf Access Port  | SR-Demo-CDC-2-vlan          | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | SR-Demo-RDC-3-vlan          | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 1 | DC-CFP-AEP                  | X          | L3          | DC-CFP-EXT-DOMAIN                      | missing-target | --   |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | default                     | V          |             |                                        |                | None |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 1 | ESX-CDC_AAEP                | X          | Physical    | ESX-CDC_PhysDom                        | formed         | --   | Leaf Access Port  | ESX-CDC-DVS_PolGrp          | 
|         |                             |            | VMM         | EU-SPDC-CDC                            | formed         |      | Leaf Access Port  | ESX-CDC_PolGrp              | 
|         |                             |            | L3          | SPIN_InnoLab_Calico_L3Dom              | formed         |      |                   |                             | 
|         |                             |            | L3          | smi5Gc-ExtR_L3Dom                      | missing-target |      |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | ESX-R3DC_AAEP               | X          | Physical    | ESX-R3DC_PhysDom                       | formed         | --   | Leaf Access Port  | ESX-R3DC-DVS_PolGrp         | 
|         |                             |            | VMM         | EU-SPDC-R3DC                           | formed         |      |                   |                             | 
|         |                             |            | L3          | SPIN_InnoLab_Calico_RDC_L3Dom          | formed         |      |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 1 | ESX_AAEP                    | X          | Physical    | ESX_PhysDom                            | missing-target | --   |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | F5-ADC_AAEP                 | X          | Physical    | F5-ADC_PhysDom                         | formed         | --   |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | HX1_AAEP                    | X          | Physical    | HX1_PhysDom                            | formed         | --   | PC/VPC Interface  | HX1-FI-A_PolGrp             | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | HX1-FI-B_PolGrp             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | IKS1-mgmt_AAEP              | X          | Physical    | IKS1-mgmt_PhysDom                      | formed         | --   | Leaf Access Port  | IKS1-mgmt_PolGrp            | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | IKS2-mgmt_AAEP              | X          | Physical    | IKS2-mgmt_PhysDom                      | formed         | --   | Leaf Access Port  | IKS2-mgmt_PolGrp            | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | Infra-2_AAEP                | X          | Physical    | Infra-2_PhysDom                        | formed         | --   | PC/VPC Interface  | Infra-2_PolGrp              | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | Infra_AAEP                  | X          | L3          | Infra_L3Dom                            | formed         | --   | Leaf Access Port  | Infra-L3_PolGrp             | 
|         |                             |            | Physical    | Infra_PhysDom                          | formed         |      | Leaf Access Port  | Infra_PolGrp                | 
|         |                             |            | L2          | VNF-mgmt_L2Dom                         | formed         |      | PC/VPC Interface  | Infra_PolGrp                | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | NXOS_FABRIC_PolGrp          | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | Infra_L3_AAEP               | X          | L3          | Infra-BGP_L3Dom                        | formed         | --   | Leaf Access Port  | Infra-BGP_PolGrp            | 
|         |                             |            | L3          | Infra_L3Dom                            | formed         |      |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | multipodL3Out_AAEP          | X          | L3          | multipodL3Out_L3Dom                    | formed         | --   | Spine Access Port | multipodL3Out_PolGrp        | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | multipodL3Out_EntityProfile | X          | L3          | multipodL3Out_RoutedDomain             | formed         | --   | Spine Access Port | multipodL3Out_policyGroup   | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | nidemo-dummy                | X          | Physical    | nidemo-dummy                           | formed         | --   | Leaf Access Port  | nidemo-dummy                | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | pod1a_AAEP                  | X          | Physical    | pod1a_PhysDom                          | formed         | --   | PC/VPC Interface  | pod1a-AIO-1-PET_PolGrp      | 
|         |                             |            | Physical    | smi5Gc-cvim1-SRIOV-FloatingSVI_PhysDom | formed         |      | PC/VPC Interface  | pod1a-AIO-1-SAMX_PolGrp     | 
|         |                             |            | L3          | smi5Gc-cvim1-SRIOV_L3Dom               | formed         |      | Leaf Access Port  | pod1a-AIO-1-SRIoV-0_PolGrp  | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod1a-AIO-1-SRIoV-1_PolGrp  | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod1a-AIO-2-PET_PolGrp      | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod1a-AIO-2-SAMX_PolGrp     | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod1a-AIO-2-SRIoV-0_PolGrp  | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod1a-AIO-2-SRIoV-1_PolGrp  | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod1a-AIO-3-PET_PolGrp      | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod1a-AIO-3-SAMX_PolGrp     | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod1a-AIO-3-SRIoV-0_PolGrp  | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod1a-AIO-3-SRIoV-1_PolGrp  | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod1a-COMP-1-PET_PolGrp     | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod1a-COMP-1-SAMX_PolGrp    | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod1a-COMP-1-SRIoV-0_PolGrp | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod1a-COMP-1-SRIoV-1_PolGrp | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod1a-COMP-2-PET_PolGrp     | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod1a-COMP-2-SAMX_PolGrp    | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod1a-COMP-2-SRIoV-0_PolGrp | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | pod1a-COMP-2-SRIoV-1_PolGrp | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod1a-MX_PolGrp             | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod1a-NVBench_PolGrp        | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | pod4a_AAEP                  | X          | Physical    | pod4a_PhysDom                          | formed         | --   | PC/VPC Interface  | pod4a-AIO-1-PET_PolGrp      | 
|         |                             |            | Physical    | smi5Gc-cvim4-SRIOV-FloatingSVI_PhysDom | formed         |      | PC/VPC Interface  | pod4a-AIO-1-SAMX_PolGrp     | 
|         |                             |            | L3          | smi5Gc-cvim4-SRIOV_L3Dom               | formed         |      | PC/VPC Interface  | pod4a-AIO-2-PET_PolGrp      | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod4a-AIO-2-SAMX_PolGrp     | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod4a-AIO-3-PET_PolGrp      | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod4a-AIO-3-SAMX_PolGrp     | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod4a-COMP-1-PET_PolGrp     | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod4a-COMP-1-SAMX_PolGrp    | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod4a-COMP-2-PET_PolGrp     | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod4a-COMP-2-SAMX_PolGrp    | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod4a-COMP-3-PET_PolGrp     | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod4a-COMP-3-SAMX_PolGrp    | 
|         |                             |            |             |                                        |                |      | PC/VPC Interface  | pod4a-MX_PolGrp             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | Private5G_AAEP              | X          | Physical    | Private5G_PhysDom                      | formed         | --   | Leaf Access Port  | P5G-ACI1-Napoli_PolGrp      | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | P5G-CU-PCIe1-A_PolGrp       | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | P5G-CU-PCIe2-A_PolGrp       | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | P5G-Core-MLOM-1_PolGrp      | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | P5G-Core-PCIe1-A_PolGrp     | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | P5G-Core-PCIe2-A_PolGrp     | 
|         |                             |            |             |                                        |                |      | Leaf Access Port  | P5G-LOM_PolGrp              | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | RL-L3Out_EntityProfile      | X          | L3          | RL-L3Out_RoutedDomain                  | formed         | --   | Spine Access Port | RL-L3Out_policyGroup        | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | SPN_AAEP                    | X          | L3          | Infra_L3Dom                            | formed         | --   | PC/VPC Interface  | SPN_PolGrp                  | 
|         |                             |            | Physical    | SPN_PhysDom                            | formed         |      |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | SR-Infra-CDC-2_AAEP         | X          | L3          | SR-Infra-CDC-2_L3dom                   | formed         | --   |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | SR-Infra-RDC-3_AAEP         | X          | L3          | SR-Infra-RDC-3_L3Dom                   | formed         | --   |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | SR-Infra-RDC-4_AAEP         | X          | L3          | SR-Infra-RDC-4_L3dom                   | formed         | --   |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 1 | SR-Infra_AAEP               | X          | L3          | SR-Infra-CDC-3_L3Dom                   | missing-target | --   |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | UCSB1-R3DC_AAEP             | X          | VMM         | EU-SPDC-R3DC                           | formed         | --   | PC/VPC Interface  | UCSB1-R3DC-FI-A_PolGrp      | 
|         |                             |            | L3          | Infra_L3Dom                            | formed         |      | PC/VPC Interface  | UCSB1-R3DC-FI-B_PolGrp      | 
|         |                             |            | Physical    | UCSB1-R3DC_PhysDom                     | formed         |      |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
| 0 0 0 0 | UCSB1_AAEP                  | X          | VMM         | EU-SPDC-CDC                            | formed         | --   | PC/VPC Interface  | UCSB1-FI-A_PolGrp           | 
|         |                             |            | L3          | Infra_L3Dom                            | formed         |      | PC/VPC Interface  | UCSB1-FI-B_PolGrp           | 
|         |                             |            | L3          | UCSB1_L3Dom                            | formed         |      |                   |                             | 
|         |                             |            | Physical    | UCSB1_PhysDom                          | formed         |      |                   |                             | 
+---------+-----------------------------+------------+-------------+----------------------------------------+----------------+------+-------------------+-----------------------------+
```

Developer

```
# iserver get aci aaep --apic apic11 --view state

{
    "duration": 4126,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 391,
        "disconnect_time": 0,
        "mo_time": 3107,
        "total_time": 3498
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

True	391	-	connect apic11o.emea-sp.cisco.com:443
True	389	30	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	313	31	apic11o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	320	18	apic11o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	370	25	apic11o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	415	23	apic11o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	368	1	apic11o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	339	2	apic11o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	593	2	apic11o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
```

[[Back]](./Aaep.md)