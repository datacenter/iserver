# Policy - 802.1X

## Verbose output

```
# iserver get aci policy auth --apic apic11 --name default --view verbose

Apic: apic11

802.1x Policy Properties
------------------------
- Policy Name : default
- TF          : False
- Admin State : disabled
- Host Mode   : single-host


+-----------------------------+-------------------------------+-----------------+
| Policy Name                 | Policy Type                   | Policy Class    |
+-----------------------------+-------------------------------+-----------------+
| BERLIN-35-RDC-3-vlan        | Leaf Access Port Policy Group | infraAccPortGrp | 
| ESX-CDC-DVS_PolGrp          | Leaf Access Port Policy Group | infraAccPortGrp | 
| ESX-CDC_PolGrp              | Leaf Access Port Policy Group | infraAccPortGrp | 
| ESX-R3DC-DVS_PolGrp         | Leaf Access Port Policy Group | infraAccPortGrp | 
| IKS1-mgmt_PolGrp            | Leaf Access Port Policy Group | infraAccPortGrp | 
| IKS2-mgmt_PolGrp            | Leaf Access Port Policy Group | infraAccPortGrp | 
| Infra-BGP_PolGrp            | Leaf Access Port Policy Group | infraAccPortGrp | 
| Infra-L3_PolGrp             | Leaf Access Port Policy Group | infraAccPortGrp | 
| Infra_PolGrp                | Leaf Access Port Policy Group | infraAccPortGrp | 
| P5G-ACI1-Napoli_PolGrp      | Leaf Access Port Policy Group | infraAccPortGrp | 
| P5G-CU-PCIe1-A_PolGrp       | Leaf Access Port Policy Group | infraAccPortGrp | 
| P5G-CU-PCIe2-A_PolGrp       | Leaf Access Port Policy Group | infraAccPortGrp | 
| P5G-Core-MLOM-1_PolGrp      | Leaf Access Port Policy Group | infraAccPortGrp | 
| P5G-Core-PCIe1-A_PolGrp     | Leaf Access Port Policy Group | infraAccPortGrp | 
| P5G-Core-PCIe2-A_PolGrp     | Leaf Access Port Policy Group | infraAccPortGrp | 
| P5G-LOM_PolGrp              | Leaf Access Port Policy Group | infraAccPortGrp | 
| SR-Demo-CDC-2-vlan          | Leaf Access Port Policy Group | infraAccPortGrp | 
| SR-Demo-RDC-3-vlan          | Leaf Access Port Policy Group | infraAccPortGrp | 
| cvim4-SRIoV-0_PolGrp        | Leaf Access Port Policy Group | infraAccPortGrp | 
| cvim4-SRIoV-1_PolGrp        | Leaf Access Port Policy Group | infraAccPortGrp | 
| nidemo-dummy                | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-AIO-1-SRIoV-0_PolGrp  | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-AIO-1-SRIoV-1_PolGrp  | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-AIO-2-SRIoV-0_PolGrp  | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-AIO-2-SRIoV-1_PolGrp  | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-AIO-3-SRIoV-0_PolGrp  | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-AIO-3-SRIoV-1_PolGrp  | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-COMP-1-SRIoV-0_PolGrp | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-COMP-1-SRIoV-1_PolGrp | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-COMP-2-SRIoV-0_PolGrp | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-COMP-2-SRIoV-1_PolGrp | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-SRIOV-0_PolGrp        | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-SRIOV-1_PolGrp        | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod1a-SRIoV-0_PolGrp        | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod4a-AIO-1-SRIoV-0_PolGrp  | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod4a-AIO-1-SRIoV-1_PolGrp  | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod4a-AIO-2-SRIoV-0_PolGrp  | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod4a-AIO-2-SRIoV-1_PolGrp  | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod4a-AIO-3-SRIoV-0_PolGrp  | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod4a-AIO-3-SRIoV-1_PolGrp  | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod4a-COMP-1-SRIoV-0_PolGrp | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod4a-COMP-1-SRIoV-1_PolGrp | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod4a-COMP-2-SRIoV-0_PolGrp | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod4a-COMP-2-SRIoV-1_PolGrp | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod4a-COMP-3-SRIoV-0_PolGrp | Leaf Access Port Policy Group | infraAccPortGrp | 
| pod4a-COMP-3-SRIoV-1_PolGrp | Leaf Access Port Policy Group | infraAccPortGrp | 
| HX1-FI-A_PolGrp             | PC/VPC Interface              | infraAccBndlGrp | 
| HX1-FI-B_PolGrp             | PC/VPC Interface              | infraAccBndlGrp | 
| Infra-2_PolGrp              | PC/VPC Interface              | infraAccBndlGrp | 
| Infra_PolGrp                | PC/VPC Interface              | infraAccBndlGrp | 
| NXOS_FABRIC_PolGrp          | PC/VPC Interface              | infraAccBndlGrp | 
| SPN_PolGrp                  | PC/VPC Interface              | infraAccBndlGrp | 
| UCSB1-FI-A_PolGrp           | PC/VPC Interface              | infraAccBndlGrp | 
| UCSB1-FI-B_PolGrp           | PC/VPC Interface              | infraAccBndlGrp | 
| UCSB1-R3DC-FI-A_PolGrp      | PC/VPC Interface              | infraAccBndlGrp | 
| UCSB1-R3DC-FI-B_PolGrp      | PC/VPC Interface              | infraAccBndlGrp | 
| pod-4a-br-API               | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-AIO-1-PET_PolGrp      | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-AIO-1-SAMX_PolGrp     | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-AIO-2-PET_PolGrp      | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-AIO-2-SAMX_PolGrp     | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-AIO-3-PET_PolGrp      | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-AIO-3-SAMX_PolGrp     | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-API_PolGrp            | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-COMP-1-PET_PolGrp     | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-COMP-1-SAMX_PolGrp    | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-COMP-2-PET_PolGrp     | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-COMP-2-SAMX_PolGrp    | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-MX_PolGrp             | PC/VPC Interface              | infraAccBndlGrp | 
| pod1a-NVBench_PolGrp        | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-AIO-1-PET_PolGrp      | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-AIO-1-SAMX_PolGrp     | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-AIO-2-PET_PolGrp      | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-AIO-2-SAMX_PolGrp     | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-AIO-3-PET_PolGrp      | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-AIO-3-SAMX_PolGrp     | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-COMP-1-PET_PolGrp     | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-COMP-1-SAMX_PolGrp    | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-COMP-2-PET_PolGrp     | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-COMP-2-SAMX_PolGrp    | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-COMP-3-PET_PolGrp     | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-COMP-3-SAMX_PolGrp    | PC/VPC Interface              | infraAccBndlGrp | 
| pod4a-MX_PolGrp             | PC/VPC Interface              | infraAccBndlGrp | 
+-----------------------------+-------------------------------+-----------------+
```

Developer

```
# iserver get aci policy auth --apic apic11 --name default --view verbose

{
    "duration": 1243,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 417,
        "disconnect_time": 0,
        "mo_time": 695,
        "total_time": 1112
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

True	417	-	connect apic11o.emea-sp.cisco.com
True	345	1	apic11o.emea-sp.cisco.com class l2PortAuthPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	350	0	apic11o.emea-sp.cisco.com class l1RsL2PortAuthCons
```

[[Back]](./PolicyAuth.md)