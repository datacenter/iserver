# Policy - DPP

## Usage specific output

```
# iserver get aci policy dpp --apic apic11 --name default --view usage

Apic: apic11 (mode:online, cache:off)

+-------------+---------------------+-----------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Policy Name | Node                | Interface Count | Ref Policy Type               | Ref Policy Name                                                                                                     |
+-------------+---------------------+-----------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------+
| default     |                     |                 | l3extLIfP                     | uni/tn-ECMP-demo/out-ACC-ext_L3out/lnodep-ACC-ext_LNP/lifp-ACC-ext_LIfP                                             | 
|             |                     |                 | l3extLIfP                     | uni/tn-ECMP-demo/out-ACC-ext_L3out/lnodep-ACC-ext_LNP/lifp-ACC-ext_LIfP                                             | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-OUT/lnodep-MPC-E-OUT_LNP/lifp-MPC-E-OUT_lIfP                                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-OUT/lnodep-MPC-E-OUT_LNP/lifp-MPC-E-OUT_lIfP                                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-Residential-IN/lnodep-MPC-E-Residential-IN_LNP/lifp-MPC-E-Residential-IN-FI-A_lIfP           | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-Residential-IN/lnodep-MPC-E-Residential-IN_LNP/lifp-MPC-E-Residential-IN-FI-A_lIfP           | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-Residential-IN/lnodep-MPC-E-Residential-IN_LNP/lifp-MPC-E-Residential-IN-FI-B_lIfP           | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-Residential-IN/lnodep-MPC-E-Residential-IN_LNP/lifp-MPC-E-Residential-IN-FI-B_lIfP           | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-sPBR-IN/lnodep-MPC-E-sPBR-IN_LNP/lifp-MPC-E-CU-FI-A_lIfP                                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-sPBR-IN/lnodep-MPC-E-sPBR-IN_LNP/lifp-MPC-E-CU-FI-A_lIfP                                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-sPBR-IN/lnodep-MPC-E-sPBR-IN_LNP/lifp-MPC-E-CU-FI-B_lIfP                                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-sPBR-IN/lnodep-MPC-E-sPBR-IN_LNP/lifp-MPC-E-CU-FI-B_lIfP                                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-sPBR-OUT/lnodep-MPC-E-sPBR-OUT_LNP/lifp-MPC-E-sPBR-OUT-FI-A_lIfP                             | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-sPBR-OUT/lnodep-MPC-E-sPBR-OUT_LNP/lifp-MPC-E-sPBR-OUT-FI-A_lIfP                             | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-sPBR-OUT/lnodep-MPC-E-sPBR-OUT_LNP/lifp-MPC-E-sPBR-OUT-FI-B_lIfP                             | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-E/out-MPC-E-sPBR-OUT/lnodep-MPC-E-sPBR-OUT_LNP/lifp-MPC-E-sPBR-OUT-FI-B_lIfP                             | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-F5T/out-F5-OUT/lnodep-F5-OUT_nodeProfile/lifp-F5-OUT-A                                                   | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-F5T/out-F5-OUT/lnodep-F5-OUT_nodeProfile/lifp-F5-OUT-A                                                   | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-F5T/out-F5-OUT/lnodep-F5-OUT_nodeProfile/lifp-F5-OUT-B                                                   | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC-F5T/out-F5-OUT/lnodep-F5-OUT_nodeProfile/lifp-F5-OUT-B                                                   | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC/out-MPC-OUT/lnodep-MPC-OUT_LNP/lifp-MPC-OUT_lIfP                                                         | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC/out-MPC-OUT/lnodep-MPC-OUT_LNP/lifp-MPC-OUT_lIfP                                                         | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC/out-MPC-sPBR-IN/lnodep-MPC-sPBR-IN_LNP/lifp-MPC-sPBR-IN_lIfP                                             | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC/out-MPC-sPBR-IN/lnodep-MPC-sPBR-IN_LNP/lifp-MPC-sPBR-IN_lIfP                                             | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC/out-MPC-sPBR-OUT/lnodep-MPC-sPBR-OUT_LNP/lifp-MPC-sPBR-OUT-FI-A_lIfP                                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC/out-MPC-sPBR-OUT/lnodep-MPC-sPBR-OUT_LNP/lifp-MPC-sPBR-OUT-FI-A_lIfP                                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC/out-MPC-sPBR-OUT/lnodep-MPC-sPBR-OUT_LNP/lifp-MPC-sPBR-OUT-FI-B_lIfP                                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-MPC/out-MPC-sPBR-OUT/lnodep-MPC-sPBR-OUT_LNP/lifp-MPC-sPBR-OUT-FI-B_lIfP                                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-SPIN_InnoLab/out-Calico_L3Out/lnodep-Calico_L3Out_nodeProfile/lifp-Calico_L3Out_interfaceProfile             | 
|             |                     |                 | l3extLIfP                     | uni/tn-SPIN_InnoLab/out-Calico_L3Out/lnodep-Calico_L3Out_nodeProfile/lifp-Calico_L3Out_interfaceProfile             | 
|             |                     |                 | l3extLIfP                     | uni/tn-SPIN_InnoLab/out-Calico_RDC_L3Out/lnodep-Calico_RDC_L3Out_nodeProfile/lifp-Calico_RDC_L3Out_interfaceProfile | 
|             |                     |                 | l3extLIfP                     | uni/tn-SPIN_InnoLab/out-Calico_RDC_L3Out/lnodep-Calico_RDC_L3Out_nodeProfile/lifp-Calico_RDC_L3Out_interfaceProfile | 
|             |                     |                 | l3extLIfP                     | uni/tn-SPIN_InnoLab/out-IPN_L3Out/lnodep-IPN_L3Out_nodeProfile/lifp-IPN_L3Out_interfaceProfile                      | 
|             |                     |                 | l3extLIfP                     | uni/tn-SPIN_InnoLab/out-IPN_L3Out/lnodep-IPN_L3Out_nodeProfile/lifp-IPN_L3Out_interfaceProfile                      | 
|             |                     |                 | l3extLIfP                     | uni/tn-UC3-CL2023-Demo/out-K8S/lnodep-BL205_206/lifp-UCS_B1                                                         | 
|             |                     |                 | l3extLIfP                     | uni/tn-UC3-CL2023-Demo/out-K8S/lnodep-BL205_206/lifp-UCS_B1                                                         | 
|             |                     |                 | l3extLIfP                     | uni/tn-UC3-CL2023-Demo/out-LAB_Backbone/lnodep-BL205_206/lifp-IPN                                                   | 
|             |                     |                 | l3extLIfP                     | uni/tn-UC3-CL2023-Demo/out-LAB_Backbone/lnodep-BL205_206/lifp-IPN                                                   | 
|             |                     |                 | l3extLIfP                     | uni/tn-common/out-Infra_BGP_L3out/lnodep-Infra_BGP_L3out_LNP/lifp-Infra_BGP_L3out_LIfP                              | 
|             |                     |                 | l3extLIfP                     | uni/tn-common/out-Infra_BGP_L3out/lnodep-Infra_BGP_L3out_LNP/lifp-Infra_BGP_L3out_LIfP                              | 
|             |                     |                 | l3extLIfP                     | uni/tn-common/out-Infra_privIP_L3out/lnodep-Infra_privIP_LNP/lifp-Infra_privIP_LIfP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-common/out-Infra_privIP_L3out/lnodep-Infra_privIP_LNP/lifp-Infra_privIP_LIfP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-infra/out-CDC-2_SRL3out/lnodep-CDC-2_SRL3out_LNP/lifp-CDC-2_SRL3out_LIfP                                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-infra/out-CDC-2_SRL3out/lnodep-CDC-2_SRL3out_LNP/lifp-CDC-2_SRL3out_LIfP                                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-infra/out-RDC-3_SRL3out/lnodep-RDC-3_SRL3out_LNP/lifp-RDC-3_SRL3out_LIfP                                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-infra/out-RDC-3_SRL3out/lnodep-RDC-3_SRL3out_LNP/lifp-RDC-3_SRL3out_LIfP                                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-infra/out-RL-L3Out/lnodep-LNodeP_301/lifp-LIfP_301                                                           | 
|             |                     |                 | l3extLIfP                     | uni/tn-infra/out-RL-L3Out/lnodep-LNodeP_301/lifp-LIfP_301                                                           | 
|             |                     |                 | l3extLIfP                     | uni/tn-infra/out-RL-L3Out/lnodep-LNodeP_302/lifp-LIfP_302                                                           | 
|             |                     |                 | l3extLIfP                     | uni/tn-infra/out-RL-L3Out/lnodep-LNodeP_302/lifp-LIfP_302                                                           | 
|             |                     |                 | l3extLIfP                     | uni/tn-infra/out-multipodL3Out/lnodep-LNodeP_101/lifp-LIfP_101                                                      | 
|             |                     |                 | l3extLIfP                     | uni/tn-infra/out-multipodL3Out/lnodep-LNodeP_101/lifp-LIfP_101                                                      | 
|             |                     |                 | l3extLIfP                     | uni/tn-infra/out-multipodL3Out/lnodep-LNodeP_102/lifp-LIfP_102                                                      | 
|             |                     |                 | l3extLIfP                     | uni/tn-infra/out-multipodL3Out/lnodep-LNodeP_102/lifp-LIfP_102                                                      | 
|             |                     |                 | l3extLIfP                     | uni/tn-mgmt/out-INB_L3out/lnodep-INB_L3out_nodeProfile/lifp-INB_L3out_p2pIpv4                                       | 
|             |                     |                 | l3extLIfP                     | uni/tn-mgmt/out-INB_L3out/lnodep-INB_L3out_nodeProfile/lifp-INB_L3out_p2pIpv4                                       | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-4G_PDN_L3Out/lnodep-Anchor_Nodes_LNP/lifp-FLOATING-SVI_LIfP                                       | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-4G_PDN_L3Out/lnodep-Anchor_Nodes_LNP/lifp-FLOATING-SVI_LIfP                                       | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-4G_RAN_L3Out/lnodep-Anchor_Nodes_LNP/lifp-FLOATING-SVI_LIfP                                       | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-4G_RAN_L3Out/lnodep-Anchor_Nodes_LNP/lifp-FLOATING-SVI_LIfP                                       | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-TEST_FSVI_MODULE_L3Out/lnodep-Anchor_Nodes_LNP/lifp-FLOATING-SVI_LIfP                             | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-TEST_FSVI_MODULE_L3Out/lnodep-Anchor_Nodes_LNP/lifp-FLOATING-SVI_LIfP                             | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-4G-PDN_L3Out/lnodep-Anchor_Nodes_LNP/lifp-FLOATING-SVI_LIfP                          | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-4G-PDN_L3Out/lnodep-Anchor_Nodes_LNP/lifp-FLOATING-SVI_LIfP                          | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-4G_RAN_L3Out/lnodep-Anchor_Nodes_LNP/lifp-FLOATING-SVI_LIfP                          | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-4G_RAN_L3Out/lnodep-Anchor_Nodes_LNP/lifp-FLOATING-SVI_LIfP                          | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-BACKBONE_L3Out/lnodep-BL205_206_LNP/lifp-ETH1_24_LIP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-BACKBONE_L3Out/lnodep-BL205_206_LNP/lifp-ETH1_24_LIP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-Control_SBI_L3Out/lnodep-Anchor_Nodes_LNP/lifp-FLOATING-SVI_LIfP                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-Control_SBI_L3Out/lnodep-Anchor_Nodes_LNP/lifp-FLOATING-SVI_LIfP                     | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-N3-N4-BACKBONE_L3Out/lnodep-BL205_206_LNP/lifp-ETH1_24_LIP                           | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-N3-N4-BACKBONE_L3Out/lnodep-BL205_206_LNP/lifp-ETH1_24_LIP                           | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-N3-N4_L3Out/lnodep-Node201_LNP/lifp-FLOATING-SVI_LIP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-N3-N4_L3Out/lnodep-Node201_LNP/lifp-FLOATING-SVI_LIP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-N3-N4_L3Out/lnodep-Node202_LNP/lifp-FLOATING-SVI_LIP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-N3-N4_L3Out/lnodep-Node202_LNP/lifp-FLOATING-SVI_LIP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-N6_L3Out/lnodep-Node201_LNP/lifp-FLOATING-SVI_LIP                                    | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-N6_L3Out/lnodep-Node201_LNP/lifp-FLOATING-SVI_LIP                                    | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-N6_L3Out/lnodep-Node202_LNP/lifp-FLOATING-SVI_LIP                                    | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim1-N6_L3Out/lnodep-Node202_LNP/lifp-FLOATING-SVI_LIP                                    | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim4-BACKBONE_L3Out/lnodep-BL205_206_LNP/lifp-ETH1_24_LIP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim4-BACKBONE_L3Out/lnodep-BL205_206_LNP/lifp-ETH1_24_LIP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim4-N3-N4-BACKBONE_L3Out/lnodep-BL205_206_LNP/lifp-ETH1_24_LIP                           | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim4-N3-N4-BACKBONE_L3Out/lnodep-BL205_206_LNP/lifp-ETH1_24_LIP                           | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim4-N3-N4_L3Out/lnodep-Node201_LNP/lifp-FLOATING-SVI_LIP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim4-N3-N4_L3Out/lnodep-Node201_LNP/lifp-FLOATING-SVI_LIP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim4-N3-N4_L3Out/lnodep-Node202_LNP/lifp-FLOATING-SVI_LIP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim4-N3-N4_L3Out/lnodep-Node202_LNP/lifp-FLOATING-SVI_LIP                                 | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim4-N6_L3Out/lnodep-Node201_LNP/lifp-FLOATING-SVI_LIP                                    | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim4-N6_L3Out/lnodep-Node201_LNP/lifp-FLOATING-SVI_LIP                                    | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim4-N6_L3Out/lnodep-Node202_LNP/lifp-FLOATING-SVI_LIP                                    | 
|             |                     |                 | l3extLIfP                     | uni/tn-smi5Gc/out-smi5Gc-cvim4-N6_L3Out/lnodep-Node202_LNP/lifp-FLOATING-SVI_LIP                                    | 
| default     | pod-1/bl205-eu-spdc | 33              | Leaf Access Port Policy Group | BERLIN-35-RDC-3-vlan                                                                                                | 
|             | pod-1/bl206-eu-spdc | 33              | Leaf Access Port Policy Group | BERLIN-35-RDC-3-vlan                                                                                                | 
|             | pod-1/cl201-eu-spdc | 130             | Leaf Access Port Policy Group | BERLIN-35-RDC-3-vlan                                                                                                | 
|             | pod-1/cl202-eu-spdc | 130             | Leaf Access Port Policy Group | ESX-CDC-DVS_PolGrp                                                                                                  | 
|             | pod-1/cl209-eu-spdc | 28              | Leaf Access Port Policy Group | ESX-CDC-DVS_PolGrp                                                                                                  | 
|             | pod-1/cl210-eu-spdc | 28              | Leaf Access Port Policy Group | ESX-CDC-DVS_PolGrp                                                                                                  | 
|             | pod-1/rl301-eu-spdc | 44              | Leaf Access Port Policy Group | ESX-CDC_PolGrp                                                                                                      | 
|             | pod-1/rl302-eu-spdc | 44              | Leaf Access Port Policy Group | ESX-CDC_PolGrp                                                                                                      | 
|             |                     |                 | Leaf Access Port Policy Group | ESX-CDC_PolGrp                                                                                                      | 
|             |                     |                 | Leaf Access Port Policy Group | ESX-R3DC-DVS_PolGrp                                                                                                 | 
|             |                     |                 | Leaf Access Port Policy Group | ESX-R3DC-DVS_PolGrp                                                                                                 | 
|             |                     |                 | Leaf Access Port Policy Group | ESX-R3DC-DVS_PolGrp                                                                                                 | 
|             |                     |                 | Leaf Access Port Policy Group | IKS1-mgmt_PolGrp                                                                                                    | 
|             |                     |                 | Leaf Access Port Policy Group | IKS1-mgmt_PolGrp                                                                                                    | 
|             |                     |                 | Leaf Access Port Policy Group | IKS1-mgmt_PolGrp                                                                                                    | 
|             |                     |                 | Leaf Access Port Policy Group | IKS2-mgmt_PolGrp                                                                                                    | 
|             |                     |                 | Leaf Access Port Policy Group | IKS2-mgmt_PolGrp                                                                                                    | 
|             |                     |                 | Leaf Access Port Policy Group | IKS2-mgmt_PolGrp                                                                                                    | 
|             |                     |                 | Leaf Access Port Policy Group | Infra-BGP_PolGrp                                                                                                    | 
|             |                     |                 | Leaf Access Port Policy Group | Infra-BGP_PolGrp                                                                                                    | 
|             |                     |                 | Leaf Access Port Policy Group | Infra-BGP_PolGrp                                                                                                    | 
|             |                     |                 | Leaf Access Port Policy Group | Infra-L3_PolGrp                                                                                                     | 
|             |                     |                 | Leaf Access Port Policy Group | Infra-L3_PolGrp                                                                                                     | 
|             |                     |                 | Leaf Access Port Policy Group | Infra-L3_PolGrp                                                                                                     | 
|             |                     |                 | Leaf Access Port Policy Group | Infra_PolGrp                                                                                                        | 
|             |                     |                 | Leaf Access Port Policy Group | Infra_PolGrp                                                                                                        | 
|             |                     |                 | Leaf Access Port Policy Group | Infra_PolGrp                                                                                                        | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-ACI1-Napoli_PolGrp                                                                                              | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-ACI1-Napoli_PolGrp                                                                                              | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-ACI1-Napoli_PolGrp                                                                                              | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-CU-PCIe1-A_PolGrp                                                                                               | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-CU-PCIe1-A_PolGrp                                                                                               | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-CU-PCIe1-A_PolGrp                                                                                               | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-CU-PCIe2-A_PolGrp                                                                                               | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-CU-PCIe2-A_PolGrp                                                                                               | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-CU-PCIe2-A_PolGrp                                                                                               | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-Core-MLOM-1_PolGrp                                                                                              | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-Core-MLOM-1_PolGrp                                                                                              | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-Core-MLOM-1_PolGrp                                                                                              | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-Core-PCIe1-A_PolGrp                                                                                             | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-Core-PCIe1-A_PolGrp                                                                                             | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-Core-PCIe1-A_PolGrp                                                                                             | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-Core-PCIe2-A_PolGrp                                                                                             | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-Core-PCIe2-A_PolGrp                                                                                             | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-Core-PCIe2-A_PolGrp                                                                                             | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-LOM_PolGrp                                                                                                      | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-LOM_PolGrp                                                                                                      | 
|             |                     |                 | Leaf Access Port Policy Group | P5G-LOM_PolGrp                                                                                                      | 
|             |                     |                 | Leaf Access Port Policy Group | SR-Demo-CDC-2-vlan                                                                                                  | 
|             |                     |                 | Leaf Access Port Policy Group | SR-Demo-CDC-2-vlan                                                                                                  | 
|             |                     |                 | Leaf Access Port Policy Group | SR-Demo-CDC-2-vlan                                                                                                  | 
|             |                     |                 | Leaf Access Port Policy Group | SR-Demo-RDC-3-vlan                                                                                                  | 
|             |                     |                 | Leaf Access Port Policy Group | SR-Demo-RDC-3-vlan                                                                                                  | 
|             |                     |                 | Leaf Access Port Policy Group | SR-Demo-RDC-3-vlan                                                                                                  | 
|             |                     |                 | Leaf Access Port Policy Group | cvim4-SRIoV-0_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | cvim4-SRIoV-0_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | cvim4-SRIoV-0_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | cvim4-SRIoV-1_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | cvim4-SRIoV-1_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | cvim4-SRIoV-1_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | nidemo-dummy                                                                                                        | 
|             |                     |                 | Leaf Access Port Policy Group | nidemo-dummy                                                                                                        | 
|             |                     |                 | Leaf Access Port Policy Group | nidemo-dummy                                                                                                        | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-1-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-1-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-1-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-1-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-1-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-1-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-2-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-2-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-2-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-2-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-2-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-2-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-3-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-3-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-3-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-3-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-3-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-3-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-1-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-1-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-1-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-1-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-1-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-1-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-2-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-2-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-2-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-2-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-2-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-2-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-SRIOV-0_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-SRIOV-0_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-SRIOV-0_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-SRIOV-1_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-SRIOV-1_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-SRIOV-1_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-SRIoV-0_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-SRIoV-0_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-SRIoV-0_PolGrp                                                                                                | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-1-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-1-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-1-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-1-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-1-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-1-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-2-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-2-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-2-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-2-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-2-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-2-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-3-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-3-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-3-SRIoV-0_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-3-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-3-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-3-SRIoV-1_PolGrp                                                                                          | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-1-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-1-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-1-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-1-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-1-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-1-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-2-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-2-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-2-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-2-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-2-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-2-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-3-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-3-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-3-SRIoV-0_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-3-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-3-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-3-SRIoV-1_PolGrp                                                                                         | 
|             |                     |                 | PC/VPC Interface              | HX1-FI-A_PolGrp                                                                                                     | 
|             |                     |                 | PC/VPC Interface              | HX1-FI-A_PolGrp                                                                                                     | 
|             |                     |                 | PC/VPC Interface              | HX1-FI-A_PolGrp                                                                                                     | 
|             |                     |                 | PC/VPC Interface              | HX1-FI-B_PolGrp                                                                                                     | 
|             |                     |                 | PC/VPC Interface              | HX1-FI-B_PolGrp                                                                                                     | 
|             |                     |                 | PC/VPC Interface              | HX1-FI-B_PolGrp                                                                                                     | 
|             |                     |                 | PC/VPC Interface              | Infra-2_PolGrp                                                                                                      | 
|             |                     |                 | PC/VPC Interface              | Infra-2_PolGrp                                                                                                      | 
|             |                     |                 | PC/VPC Interface              | Infra-2_PolGrp                                                                                                      | 
|             |                     |                 | PC/VPC Interface              | Infra_PolGrp                                                                                                        | 
|             |                     |                 | PC/VPC Interface              | Infra_PolGrp                                                                                                        | 
|             |                     |                 | PC/VPC Interface              | Infra_PolGrp                                                                                                        | 
|             |                     |                 | PC/VPC Interface              | NXOS_FABRIC_PolGrp                                                                                                  | 
|             |                     |                 | PC/VPC Interface              | NXOS_FABRIC_PolGrp                                                                                                  | 
|             |                     |                 | PC/VPC Interface              | NXOS_FABRIC_PolGrp                                                                                                  | 
|             |                     |                 | PC/VPC Interface              | SPN_PolGrp                                                                                                          | 
|             |                     |                 | PC/VPC Interface              | SPN_PolGrp                                                                                                          | 
|             |                     |                 | PC/VPC Interface              | SPN_PolGrp                                                                                                          | 
|             |                     |                 | PC/VPC Interface              | UCSB1-FI-A_PolGrp                                                                                                   | 
|             |                     |                 | PC/VPC Interface              | UCSB1-FI-A_PolGrp                                                                                                   | 
|             |                     |                 | PC/VPC Interface              | UCSB1-FI-A_PolGrp                                                                                                   | 
|             |                     |                 | PC/VPC Interface              | UCSB1-FI-B_PolGrp                                                                                                   | 
|             |                     |                 | PC/VPC Interface              | UCSB1-FI-B_PolGrp                                                                                                   | 
|             |                     |                 | PC/VPC Interface              | UCSB1-FI-B_PolGrp                                                                                                   | 
|             |                     |                 | PC/VPC Interface              | UCSB1-R3DC-FI-A_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | UCSB1-R3DC-FI-A_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | UCSB1-R3DC-FI-A_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | UCSB1-R3DC-FI-B_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | UCSB1-R3DC-FI-B_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | UCSB1-R3DC-FI-B_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod-4a-br-API                                                                                                       | 
|             |                     |                 | PC/VPC Interface              | pod-4a-br-API                                                                                                       | 
|             |                     |                 | PC/VPC Interface              | pod-4a-br-API                                                                                                       | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-1-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-1-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-1-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-1-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-1-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-1-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-2-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-2-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-2-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-2-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-2-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-2-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-3-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-3-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-3-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-3-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-3-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-3-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-API_PolGrp                                                                                                    | 
|             |                     |                 | PC/VPC Interface              | pod1a-API_PolGrp                                                                                                    | 
|             |                     |                 | PC/VPC Interface              | pod1a-API_PolGrp                                                                                                    | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-1-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-1-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-1-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-1-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-1-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-1-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-2-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-2-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-2-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-2-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-2-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-2-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod1a-MX_PolGrp                                                                                                     | 
|             |                     |                 | PC/VPC Interface              | pod1a-MX_PolGrp                                                                                                     | 
|             |                     |                 | PC/VPC Interface              | pod1a-MX_PolGrp                                                                                                     | 
|             |                     |                 | PC/VPC Interface              | pod1a-NVBench_PolGrp                                                                                                | 
|             |                     |                 | PC/VPC Interface              | pod1a-NVBench_PolGrp                                                                                                | 
|             |                     |                 | PC/VPC Interface              | pod1a-NVBench_PolGrp                                                                                                | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-1-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-1-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-1-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-1-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-1-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-1-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-2-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-2-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-2-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-2-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-2-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-2-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-3-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-3-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-3-PET_PolGrp                                                                                              | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-3-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-3-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-3-SAMX_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-1-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-1-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-1-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-1-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-1-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-1-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-2-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-2-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-2-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-2-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-2-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-2-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-3-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-3-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-3-PET_PolGrp                                                                                             | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-3-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-3-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-3-SAMX_PolGrp                                                                                            | 
|             |                     |                 | PC/VPC Interface              | pod4a-MX_PolGrp                                                                                                     | 
|             |                     |                 | PC/VPC Interface              | pod4a-MX_PolGrp                                                                                                     | 
|             |                     |                 | PC/VPC Interface              | pod4a-MX_PolGrp                                                                                                     | 
+-------------+---------------------+-----------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------+
Context: phy
```

Developer

```
# iserver get aci policy dpp --apic apic11 --name default --view usage

{
    "duration": 4712,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 437,
        "disconnect_time": 0,
        "mo_time": 1098,
        "total_time": 1535
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

True	437	-	connect apic11o.emea-sp.cisco.com
True	368	2	apic11o.emea-sp.cisco.com class qosDppPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	413	470	apic11o.emea-sp.cisco.com class l1RsQosEgressDppIfPolCons
True	317	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyDpp.md)