# Policy - CDP

## Filter by reference policy name

```
# iserver get aci policy cdp --apic apic11 --ref *sriov* --view usage

Apic: apic11

+-------------+---------------------+-----------------+-------------------------------+-----------------------------+
| Policy Name | Node                | Interface Count | Ref Policy Type               | Ref Policy Name             |
+-------------+---------------------+-----------------+-------------------------------+-----------------------------+
| default     | pod-1/bl205-eu-spdc | 21              | Leaf Access Port Policy Group | cvim4-SRIoV-0_PolGrp        | 
|             | pod-1/bl206-eu-spdc | 21              | Leaf Access Port Policy Group | cvim4-SRIoV-1_PolGrp        | 
|             | pod-1/cl201-eu-spdc | 78              | Leaf Access Port Policy Group | pod1a-AIO-1-SRIoV-0_PolGrp  | 
|             | pod-1/cl202-eu-spdc | 78              | Leaf Access Port Policy Group | pod1a-AIO-1-SRIoV-1_PolGrp  | 
|             | pod-1/rl301-eu-spdc | 24              | Leaf Access Port Policy Group | pod1a-AIO-2-SRIoV-0_PolGrp  | 
|             | pod-1/rl302-eu-spdc | 24              | Leaf Access Port Policy Group | pod1a-AIO-2-SRIoV-1_PolGrp  | 
|             | pod-1/s101-eu-spdc  | 16              | Leaf Access Port Policy Group | pod1a-AIO-3-SRIoV-0_PolGrp  | 
|             | pod-1/s102-eu-spdc  | 16              | Leaf Access Port Policy Group | pod1a-AIO-3-SRIoV-1_PolGrp  | 
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
+-------------+---------------------+-----------------+-------------------------------+-----------------------------+
Context: phy
```

Developer

```
# iserver get aci policy cdp --apic apic11 --ref *sriov* --view usage

{
    "duration": 1660,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 406,
        "disconnect_time": 0,
        "mo_time": 1042,
        "total_time": 1448
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

True	406	-	connect apic11o.emea-sp.cisco.com
True	327	8	apic11o.emea-sp.cisco.com class cdpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	400	370	apic11o.emea-sp.cisco.com class l1RsCdpIfPolCons
True	315	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCdp.md)