# Attachable Access Entity Profile (AAEP)

## Get AAEPs

```
# iserver get aci aaep --apic apic11

Apic: apic11 (mode:online, cache:off)

+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| Attachable Access Entity Profile | Infra VLAN | Domain Name                            | Domain Type | Domain State   | Policy Group Name           | Policy Group Interface Type    |
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| cvim-brAPI_AAEP                  | X          | cvim-brAPI_PhysDom                     | Physical    | formed         | pod-4a-br-API               | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod1a-API_PolGrp            | PC/VPC Interface               | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| cvim1-SRIOV_AAEP                 | X          | smi5Gc-cvim1-SRIOV-FloatingSVI_PhysDom | Physical    | formed         | pod1a-SRIOV-0_PolGrp        | Leaf Access Port Policy Group  | 
|                                  |            | smi5Gc-cvim1-SRIOV_L3Dom               | L3          | formed         | pod1a-SRIOV-1_PolGrp        | Leaf Access Port Policy Group  | 
|                                  |            | smi5Gc-cvim1-SRIOV_PhysDom             | Physical    | formed         | pod1a-SRIoV-0_PolGrp        | Leaf Access Port Policy Group  | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| cvim4-SRIOV_AAEP                 | X          | smi5Gc-cvim4-SRIOV-FloatingSVI_PhysDom | Physical    | formed         | cvim4-SRIoV-0_PolGrp        | Leaf Access Port Policy Group  | 
|                                  |            | smi5Gc-cvim4-SRIOV_L3Dom               | L3          | formed         | cvim4-SRIoV-1_PolGrp        | Leaf Access Port Policy Group  | 
|                                  |            | smi5Gc-cvim4-SRIOV_PhysDom             | Physical    | formed         | pod4a-AIO-1-SRIoV-0_PolGrp  | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod4a-AIO-1-SRIoV-1_PolGrp  | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod4a-AIO-2-SRIoV-0_PolGrp  | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod4a-AIO-2-SRIoV-1_PolGrp  | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod4a-AIO-3-SRIoV-0_PolGrp  | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod4a-AIO-3-SRIoV-1_PolGrp  | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod4a-COMP-1-SRIoV-0_PolGrp | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod4a-COMP-1-SRIoV-1_PolGrp | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod4a-COMP-2-SRIoV-0_PolGrp | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod4a-COMP-2-SRIoV-1_PolGrp | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod4a-COMP-3-SRIoV-0_PolGrp | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod4a-COMP-3-SRIoV-1_PolGrp | Leaf Access Port Policy Group  | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| DC-CFP                           | X          | DC-CFP                                 | L3          | formed         | BERLIN-35-RDC-3-vlan        | Leaf Access Port Policy Group  | 
|                                  |            | DC-CFP                                 | Physical    | formed         | SR-Demo-CDC-2-vlan          | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | SR-Demo-RDC-3-vlan          | Leaf Access Port Policy Group  | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| DC-CFP-AEP                       | X          | DC-CFP-EXT-DOMAIN                      | L3          | missing-target |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| default                          | V          |                                        |             |                |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| ESX-CDC_AAEP                     | X          | ESX-CDC_PhysDom                        | Physical    | formed         | ESX-CDC-DVS_PolGrp          | Leaf Access Port Policy Group  | 
|                                  |            | EU-SPDC-CDC                            | VMM         | formed         | ESX-CDC_PolGrp              | Leaf Access Port Policy Group  | 
|                                  |            | SPIN_InnoLab_Calico_L3Dom              | L3          | formed         |                             |                                | 
|                                  |            | smi5Gc-ExtR_L3Dom                      | L3          | missing-target |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| ESX-R3DC_AAEP                    | X          | ESX-R3DC_PhysDom                       | Physical    | formed         | ESX-R3DC-DVS_PolGrp         | Leaf Access Port Policy Group  | 
|                                  |            | EU-SPDC-R3DC                           | VMM         | formed         |                             |                                | 
|                                  |            | SPIN_InnoLab_Calico_RDC_L3Dom          | L3          | formed         |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| ESX_AAEP                         | X          | ESX_PhysDom                            | Physical    | missing-target |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| F5-ADC_AAEP                      | X          | F5-ADC_PhysDom                         | Physical    | formed         |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| HX1_AAEP                         | X          | HX1_PhysDom                            | Physical    | formed         | HX1-FI-A_PolGrp             | PC/VPC Interface               | 
|                                  |            |                                        |             |                | HX1-FI-B_PolGrp             | PC/VPC Interface               | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| IKS1-mgmt_AAEP                   | X          | IKS1-mgmt_PhysDom                      | Physical    | formed         | IKS1-mgmt_PolGrp            | Leaf Access Port Policy Group  | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| IKS2-mgmt_AAEP                   | X          | IKS2-mgmt_PhysDom                      | Physical    | formed         | IKS2-mgmt_PolGrp            | Leaf Access Port Policy Group  | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| Infra-2_AAEP                     | X          | Infra-2_PhysDom                        | Physical    | formed         | Infra-2_PolGrp              | PC/VPC Interface               | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| Infra_AAEP                       | X          | Infra_L3Dom                            | L3          | formed         | Infra-L3_PolGrp             | Leaf Access Port Policy Group  | 
|                                  |            | Infra_PhysDom                          | Physical    | formed         | Infra_PolGrp                | Leaf Access Port Policy Group  | 
|                                  |            | VNF-mgmt_L2Dom                         | L2          | formed         | Infra_PolGrp                | PC/VPC Interface               | 
|                                  |            |                                        |             |                | NXOS_FABRIC_PolGrp          | PC/VPC Interface               | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| Infra_L3_AAEP                    | X          | Infra-BGP_L3Dom                        | L3          | formed         | Infra-BGP_PolGrp            | Leaf Access Port Policy Group  | 
|                                  |            | Infra_L3Dom                            | L3          | formed         |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| multipodL3Out_AAEP               | X          | multipodL3Out_L3Dom                    | L3          | formed         | multipodL3Out_PolGrp        | Spine Access Port Policy Group | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| multipodL3Out_EntityProfile      | X          | multipodL3Out_RoutedDomain             | L3          | formed         | multipodL3Out_policyGroup   | Spine Access Port Policy Group | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| nidemo-dummy                     | X          | nidemo-dummy                           | Physical    | formed         | nidemo-dummy                | Leaf Access Port Policy Group  | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| pod1a_AAEP                       | X          | pod1a_PhysDom                          | Physical    | formed         | pod1a-AIO-1-PET_PolGrp      | PC/VPC Interface               | 
|                                  |            | smi5Gc-cvim1-SRIOV-FloatingSVI_PhysDom | Physical    | formed         | pod1a-AIO-1-SAMX_PolGrp     | PC/VPC Interface               | 
|                                  |            | smi5Gc-cvim1-SRIOV_L3Dom               | L3          | formed         | pod1a-AIO-1-SRIoV-0_PolGrp  | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod1a-AIO-1-SRIoV-1_PolGrp  | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod1a-AIO-2-PET_PolGrp      | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod1a-AIO-2-SAMX_PolGrp     | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod1a-AIO-2-SRIoV-0_PolGrp  | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod1a-AIO-2-SRIoV-1_PolGrp  | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod1a-AIO-3-PET_PolGrp      | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod1a-AIO-3-SAMX_PolGrp     | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod1a-AIO-3-SRIoV-0_PolGrp  | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod1a-AIO-3-SRIoV-1_PolGrp  | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod1a-COMP-1-PET_PolGrp     | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod1a-COMP-1-SAMX_PolGrp    | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod1a-COMP-1-SRIoV-0_PolGrp | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod1a-COMP-1-SRIoV-1_PolGrp | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod1a-COMP-2-PET_PolGrp     | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod1a-COMP-2-SAMX_PolGrp    | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod1a-COMP-2-SRIoV-0_PolGrp | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod1a-COMP-2-SRIoV-1_PolGrp | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | pod1a-MX_PolGrp             | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod1a-NVBench_PolGrp        | PC/VPC Interface               | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| pod4a_AAEP                       | X          | pod4a_PhysDom                          | Physical    | formed         | pod4a-AIO-1-PET_PolGrp      | PC/VPC Interface               | 
|                                  |            | smi5Gc-cvim4-SRIOV-FloatingSVI_PhysDom | Physical    | formed         | pod4a-AIO-1-SAMX_PolGrp     | PC/VPC Interface               | 
|                                  |            | smi5Gc-cvim4-SRIOV_L3Dom               | L3          | formed         | pod4a-AIO-2-PET_PolGrp      | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod4a-AIO-2-SAMX_PolGrp     | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod4a-AIO-3-PET_PolGrp      | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod4a-AIO-3-SAMX_PolGrp     | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod4a-COMP-1-PET_PolGrp     | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod4a-COMP-1-SAMX_PolGrp    | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod4a-COMP-2-PET_PolGrp     | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod4a-COMP-2-SAMX_PolGrp    | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod4a-COMP-3-PET_PolGrp     | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod4a-COMP-3-SAMX_PolGrp    | PC/VPC Interface               | 
|                                  |            |                                        |             |                | pod4a-MX_PolGrp             | PC/VPC Interface               | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| Private5G_AAEP                   | X          | Private5G_PhysDom                      | Physical    | formed         | P5G-ACI1-Napoli_PolGrp      | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | P5G-CU-PCIe1-A_PolGrp       | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | P5G-CU-PCIe2-A_PolGrp       | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | P5G-Core-MLOM-1_PolGrp      | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | P5G-Core-PCIe1-A_PolGrp     | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | P5G-Core-PCIe2-A_PolGrp     | Leaf Access Port Policy Group  | 
|                                  |            |                                        |             |                | P5G-LOM_PolGrp              | Leaf Access Port Policy Group  | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| RL-L3Out_EntityProfile           | X          | RL-L3Out_RoutedDomain                  | L3          | formed         | RL-L3Out_policyGroup        | Spine Access Port Policy Group | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| SPN_AAEP                         | X          | Infra_L3Dom                            | L3          | formed         | SPN_PolGrp                  | PC/VPC Interface               | 
|                                  |            | SPN_PhysDom                            | Physical    | formed         |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| SR-Infra-CDC-2_AAEP              | X          | SR-Infra-CDC-2_L3dom                   | L3          | formed         |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| SR-Infra-RDC-3_AAEP              | X          | SR-Infra-RDC-3_L3Dom                   | L3          | formed         |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| SR-Infra-RDC-4_AAEP              | X          | SR-Infra-RDC-4_L3dom                   | L3          | formed         |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| SR-Infra_AAEP                    | X          | SR-Infra-CDC-3_L3Dom                   | L3          | missing-target |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| UCSB1-R3DC_AAEP                  | X          | EU-SPDC-R3DC                           | VMM         | formed         | UCSB1-R3DC-FI-A_PolGrp      | PC/VPC Interface               | 
|                                  |            | Infra_L3Dom                            | L3          | formed         | UCSB1-R3DC-FI-B_PolGrp      | PC/VPC Interface               | 
|                                  |            | UCSB1-R3DC_PhysDom                     | Physical    | formed         |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
| UCSB1_AAEP                       | X          | EU-SPDC-CDC                            | VMM         | formed         | UCSB1-FI-A_PolGrp           | PC/VPC Interface               | 
|                                  |            | Infra_L3Dom                            | L3          | formed         | UCSB1-FI-B_PolGrp           | PC/VPC Interface               | 
|                                  |            | UCSB1_L3Dom                            | L3          | formed         |                             |                                | 
|                                  |            | UCSB1_PhysDom                          | Physical    | formed         |                             |                                | 
+----------------------------------+------------+----------------------------------------+-------------+----------------+-----------------------------+--------------------------------+
```

Developer

```
# iserver get aci aaep --apic apic11

{
    "duration": 1375,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 444,
        "disconnect_time": 0,
        "mo_time": 392,
        "total_time": 836
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

True	444	-	connect apic11o.emea-sp.cisco.com
True	392	30	apic11o.emea-sp.cisco.com class infraAttEntityP query rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
```

[[Back]](./Aaep.md)