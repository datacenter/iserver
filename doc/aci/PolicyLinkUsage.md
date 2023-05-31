# Policy - Link Level

## Usage specific output

```
# iserver get aci policy link --apic apic11 --name default --view usage

Apic: apic11

+-------------+---------------------+-----------------+--------------------------------+-----------------------------+
| Policy Name | Node                | Interface Count | Ref Policy Type                | Ref Policy Name             |
+-------------+---------------------+-----------------+--------------------------------+-----------------------------+
| default     | pod-1/bl205-eu-spdc | 17              | Access Infra                   | infra                       | 
|             | pod-1/bl206-eu-spdc | 22              | Leaf Access Port Policy Group  | ESX-CDC-DVS_PolGrp          | 
|             | pod-1/cl201-eu-spdc | 110             | Leaf Access Port Policy Group  | ESX-R3DC-DVS_PolGrp         | 
|             | pod-1/cl202-eu-spdc | 114             | Leaf Access Port Policy Group  | Infra-BGP_PolGrp            | 
|             | pod-1/rl301-eu-spdc | 38              | Leaf Access Port Policy Group  | pod1a-AIO-1-SRIoV-0_PolGrp  | 
|             | pod-1/rl302-eu-spdc | 38              | Leaf Access Port Policy Group  | pod1a-AIO-1-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-AIO-2-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-AIO-2-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-AIO-3-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-AIO-3-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-COMP-1-SRIoV-0_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-COMP-1-SRIoV-1_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-COMP-2-SRIoV-0_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group  | pod1a-COMP-2-SRIoV-1_PolGrp | 
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
|             |                     |                 | PC/VPC Interface               | pod1a-AIO-1-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface               | pod1a-AIO-1-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod1a-AIO-2-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface               | pod1a-AIO-2-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface               | pod1a-AIO-3-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface               | pod1a-AIO-3-SAMX_PolGrp     | 
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
# iserver get aci policy link --apic apic11 --name default --view usage

{
    "duration": 1736,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 1005,
        "total_time": 1416
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
    }
}

Log: apic
----------

True	411	-	connect apic11o.emea-sp.cisco.com
True	314	29	apic11o.emea-sp.cisco.com class fabricHIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	398	408	apic11o.emea-sp.cisco.com class l1RsHIfPolCons
True	293	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLink.md)