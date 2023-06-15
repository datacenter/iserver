# Policy - LLDP

## Usage specific output

```
# iserver get aci policy lldp --apic apic11 --name default --view usage

Apic: apic11 (mode:online, cache:off)

+-------------+---------------------+-----------------+-------------------------------+-----------------------------+
| Policy Name | Node                | Interface Count | Ref Policy Type               | Ref Policy Name             |
+-------------+---------------------+-----------------+-------------------------------+-----------------------------+
| default     |                     |                 |                               |                             | 
| default     | pod-1/bl205-eu-spdc | 16              | Access Infra                  | infra                       | 
|             | pod-1/bl206-eu-spdc | 21              | Access Switch Policy Group    | HighLPMRo                   | 
|             | pod-1/cl201-eu-spdc | 74              | Access Switch Policy Group    | HighLPN_prof                | 
|             | pod-1/cl202-eu-spdc | 78              | Leaf Access Port Policy Group | cvim4-SRIoV-0_PolGrp        | 
|             | pod-1/cl209-eu-spdc | 28              | Leaf Access Port Policy Group | cvim4-SRIoV-1_PolGrp        | 
|             | pod-1/cl210-eu-spdc | 28              | Leaf Access Port Policy Group | pod1a-AIO-1-SRIoV-0_PolGrp  | 
|             | pod-1/rl301-eu-spdc | 24              | Leaf Access Port Policy Group | pod1a-AIO-1-SRIoV-1_PolGrp  | 
|             | pod-1/rl302-eu-spdc | 24              | Leaf Access Port Policy Group | pod1a-AIO-2-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-2-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-3-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-AIO-3-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-1-SRIoV-0_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-1-SRIoV-1_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-2-SRIoV-0_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-COMP-2-SRIoV-1_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-SRIOV-0_PolGrp        | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-SRIOV-1_PolGrp        | 
|             |                     |                 | Leaf Access Port Policy Group | pod1a-SRIoV-0_PolGrp        | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-1-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-1-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-2-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-2-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-3-SRIoV-0_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-AIO-3-SRIoV-1_PolGrp  | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-1-SRIoV-0_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-1-SRIoV-1_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-2-SRIoV-0_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-2-SRIoV-1_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-3-SRIoV-0_PolGrp | 
|             |                     |                 | Leaf Access Port Policy Group | pod4a-COMP-3-SRIoV-1_PolGrp | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-1-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-1-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-2-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-2-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-3-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface              | pod1a-AIO-3-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-1-PET_PolGrp     | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-1-SAMX_PolGrp    | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-2-PET_PolGrp     | 
|             |                     |                 | PC/VPC Interface              | pod1a-COMP-2-SAMX_PolGrp    | 
|             |                     |                 | PC/VPC Interface              | pod1a-MX_PolGrp             | 
|             |                     |                 | PC/VPC Interface              | pod1a-NVBench_PolGrp        | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-1-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-1-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-2-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-2-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-3-PET_PolGrp      | 
|             |                     |                 | PC/VPC Interface              | pod4a-AIO-3-SAMX_PolGrp     | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-1-PET_PolGrp     | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-1-SAMX_PolGrp    | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-2-PET_PolGrp     | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-2-SAMX_PolGrp    | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-3-PET_PolGrp     | 
|             |                     |                 | PC/VPC Interface              | pod4a-COMP-3-SAMX_PolGrp    | 
|             |                     |                 | VMM Domain                    | EU-SPDC-CDC                 | 
|             |                     |                 | VMM Domain                    | EU-SPDC-R3DC                | 
+-------------+---------------------+-----------------+-------------------------------+-----------------------------+
Context: phy
```

Developer

```
# iserver get aci policy lldp --apic apic11 --name default --view usage

{
    "duration": 2435,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 429,
        "disconnect_time": 0,
        "mo_time": 1116,
        "total_time": 1545
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

True	429	-	connect apic11o.emea-sp.cisco.com
True	361	10	apic11o.emea-sp.cisco.com class lldpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	380	394	apic11o.emea-sp.cisco.com class l1RsLldpIfPolCons
True	375	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLldp.md)