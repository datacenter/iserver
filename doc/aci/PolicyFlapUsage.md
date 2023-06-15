# Policy - Link Flap

## Usage specific output

```
# iserver get aci policy flap --apic apic11 --name default --view usage

Apic: apic11 (mode:online, cache:off)

+-------------+---------------------+-----------------+--------------------------------+-----------------------------+
| Policy Name | Node                | Interface Count | Ref Policy Type                | Ref Policy Name             |
+-------------+---------------------+-----------------+--------------------------------+-----------------------------+
| default     | pod-1/bl205-eu-spdc | 33              | Access Infra                   | infra                       | 
|             | pod-1/bl206-eu-spdc | 33              | Leaf Access Port Policy Group  | BERLIN-35-RDC-3-vlan        | 
|             | pod-1/cl201-eu-spdc | 127             | Leaf Access Port Policy Group  | ESX-CDC-DVS_PolGrp          | 
|             | pod-1/cl202-eu-spdc | 127             | Leaf Access Port Policy Group  | ESX-CDC_PolGrp              | 
|             | pod-1/cl209-eu-spdc | 28              | Leaf Access Port Policy Group  | ESX-R3DC-DVS_PolGrp         | 
|             | pod-1/cl210-eu-spdc | 28              | Leaf Access Port Policy Group  | IKS1-mgmt_PolGrp            | 
|             | pod-1/rl301-eu-spdc | 44              | Leaf Access Port Policy Group  | IKS2-mgmt_PolGrp            | 
|             | pod-1/rl302-eu-spdc | 44              | Leaf Access Port Policy Group  | Infra-BGP_PolGrp            | 
|             |                     |                 | Leaf Access Port Policy Group  | Infra-L3_PolGrp             | 
|             |                     |                 | Leaf Access Port Policy Group  | Infra_PolGrp                | 
|             |                     |                 | Leaf Access Port Policy Group  | P5G-ACI1-Napoli_PolGrp      | 
|             |                     |                 | Leaf Access Port Policy Group  | P5G-CU-PCIe1-A_PolGrp       | 
|             |                     |                 | Leaf Access Port Policy Group  | P5G-CU-PCIe2-A_PolGrp       | 
|             |                     |                 | Leaf Access Port Policy Group  | P5G-Core-MLOM-1_PolGrp      | 
|             |                     |                 | Leaf Access Port Policy Group  | P5G-Core-PCIe1-A_PolGrp     | 
|             |                     |                 | Leaf Access Port Policy Group  | P5G-Core-PCIe2-A_PolGrp     | 
|             |                     |                 | Leaf Access Port Policy Group  | P5G-LOM_PolGrp              | 
|             |                     |                 | Leaf Access Port Policy Group  | SR-Demo-CDC-2-vlan          | 
|             |                     |                 | Leaf Access Port Policy Group  | SR-Demo-RDC-3-vlan          | 
|             |                     |                 | Leaf Access Port Policy Group  | cvim4-SRIoV-0_PolGrp        | 
|             |                     |                 | Leaf Access Port Policy Group  | cvim4-SRIoV-1_PolGrp        | 
|             |                     |                 | Leaf Access Port Policy Group  | nidemo-dummy                | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-AIO-1-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-AIO-1-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-AIO-2-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-AIO-2-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-AIO-3-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-AIO-3-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-COMP-1-SRIoV-0_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-COMP-1-SRIoV-1_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-COMP-2-SRIoV-0_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-COMP-2-SRIoV-1_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-SRIOV-0_PolGrp        | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-SRIOV-1_PolGrp        | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-SRIoV-0_PolGrp        | 
|             |                     |                 | Leaf Access Port Policy Group  | pod4a-AIO-1-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod4a-AIO-1-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod4a-AIO-2-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod4a-AIO-2-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod4a-AIO-3-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod4a-AIO-3-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod4a-COMP-1-SRIoV-0_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group  | pod4a-COMP-1-SRIoV-1_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group  | pod4a-COMP-2-SRIoV-0_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group  | pod4a-COMP-2-SRIoV-1_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group  | pod4a-COMP-3-SRIoV-0_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group  | pod4a-COMP-3-SRIoV-1_PolGrp | 
|             |                     |                 | PC/VPC Interface               | HX1-FI-A_PolGrp             | 
|             |                     |                 | PC/VPC Interface               | HX1-FI-B_PolGrp             | 
|             |                     |                 | PC/VPC Interface               | Infra-2_PolGrp              | 
|             |                     |                 | PC/VPC Interface               | Infra_PolGrp                | 
|             |                     |                 | PC/VPC Interface               | NXOS_FABRIC_PolGrp          | 
|             |                     |                 | PC/VPC Interface               | SPN_PolGrp                  | 
|             |                     |                 | PC/VPC Interface               | UCSB1-FI-A_PolGrp           | 
|             |                     |                 | PC/VPC Interface               | UCSB1-FI-B_PolGrp           | 
|             |                     |                 | PC/VPC Interface               | UCSB1-R3DC-FI-A_PolGrp      | 
|             |                     |                 | PC/VPC Interface               | UCSB1-R3DC-FI-B_PolGrp      | 
|             |                     |                 | PC/VPC Interface               | pod-4a-br-API               | 
|             |                     |                 | PC/VPC Interface               | pod1a-AIO-1-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface               | pod1a-AIO-1-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod1a-AIO-2-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface               | pod1a-AIO-2-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod1a-AIO-3-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface               | pod1a-AIO-3-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod1a-API_PolGrp            | 
|             |                     |                 | PC/VPC Interface               | pod1a-COMP-1-PET_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod1a-COMP-1-SAMX_PolGrp    | 
|             |                     |                 | PC/VPC Interface               | pod1a-COMP-2-PET_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod1a-COMP-2-SAMX_PolGrp    | 
|             |                     |                 | PC/VPC Interface               | pod1a-MX_PolGrp             | 
|             |                     |                 | PC/VPC Interface               | pod1a-NVBench_PolGrp        | 
|             |                     |                 | PC/VPC Interface               | pod4a-AIO-1-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface               | pod4a-AIO-1-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod4a-AIO-2-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface               | pod4a-AIO-2-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod4a-AIO-3-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface               | pod4a-AIO-3-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod4a-COMP-1-PET_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod4a-COMP-1-SAMX_PolGrp    | 
|             |                     |                 | PC/VPC Interface               | pod4a-COMP-2-PET_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod4a-COMP-2-SAMX_PolGrp    | 
|             |                     |                 | PC/VPC Interface               | pod4a-COMP-3-PET_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod4a-COMP-3-SAMX_PolGrp    | 
|             |                     |                 | PC/VPC Interface               | pod4a-MX_PolGrp             | 
|             |                     |                 | Spine Access Port Policy Group | RL-L3Out_policyGroup        | 
|             |                     |                 | Spine Access Port Policy Group | multipodL3Out_PolGrp        | 
|             |                     |                 | Spine Access Port Policy Group | multipodL3Out_policyGroup   | 
+-------------+---------------------+-----------------+--------------------------------+-----------------------------+
Context: phy
```

Developer

```
# iserver get aci policy flap --apic apic11 --name default --view usage

{
    "duration": 2824,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 416,
        "disconnect_time": 0,
        "mo_time": 1024,
        "total_time": 1440
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

True	416	-	connect apic11o.emea-sp.cisco.com
True	330	1	apic11o.emea-sp.cisco.com class fabricLinkFlapPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	392	464	apic11o.emea-sp.cisco.com class l1RsLinkFlapPolCons
True	302	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyFlap.md)