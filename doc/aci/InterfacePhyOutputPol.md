# Node Interface - Physical

## Policy focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view pol

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+------+-------------------+-------------------------+----------------+-----------+-------------+-------------+--------------+---------+
| Node                | Interface | Oper | Type | Policy Group Type | Policy Group Name       | Link Level     | Link Flap | CDP         | MCP         | LLDP         | STP     |
+---------------------+-----------+------+------+-------------------+-------------------------+----------------+-----------+-------------+-------------+--------------+---------+
| pod-1/bl205-eu-spdc | 1/1       | up   | leaf | infraAccBndlGrp   | UCSB1-FI-A_PolGrp       | Inherit        | default   | CDP_enable  | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/2       | up   | leaf | infraAccBndlGrp   | UCSB1-FI-B_PolGrp       | Inherit        | default   | CDP_enable  | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/3       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/4       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/5       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/6       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/7       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/8       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/9       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/10      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/11      | up   | leaf | infraAccBndlGrp   | HX1-FI-A_PolGrp         | Inherit        | default   | CDP_enable  | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/12      | up   | leaf | infraAccBndlGrp   | HX1-FI-B_PolGrp         | Inherit        | default   | CDP_enable  | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/13      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/14      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/15      | up   | leaf | infraAccPortGrp   | P5G-CU-PCIe1-A_PolGrp   | Inherit        | default   | default     | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/16      | up   | leaf | infraAccPortGrp   | P5G-CU-PCIe2-A_PolGrp   | Inherit        | default   | default     | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/17      | down | leaf | infraAccPortGrp   | P5G-Core-PCIe1-A_PolGrp | Inherit        | default   | default     | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/18      | down | leaf | infraAccPortGrp   | P5G-Core-PCIe2-A_PolGrp | Inherit        | default   | default     | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/19      | up   | leaf | infraAccPortGrp   | P5G-Core-MLOM-1_PolGrp  | Inherit        | default   | default     | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/20      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/21      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/22      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/23      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/24      | up   | leaf | infraAccPortGrp   | Infra-BGP_PolGrp        | default        | default   | CDP_enable  | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/25      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/26      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/27      | up   | leaf | infraAccBndlGrp   | SPN_PolGrp              | 10G-fix        | default   | CDP_enable  | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/28      | up   | leaf | infraAccPortGrp   | SR-Demo-CDC-2-vlan      | fabric-inherit | default   | cdp-enabled | mcp-enabled | lldp-enabled | default | 
| pod-1/bl205-eu-spdc | 1/29      | down | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/30      | down | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/31      | down | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/32      | down | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/33      | down | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/34      | down | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/35      | up   | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/36      | up   | fab  |                   |                         |                |           |             |             |              |         | 
+---------------------+-----------+------+------+-------------------+-------------------------+----------------+-----------+-------------+-------------+--------------+---------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view pol

{
    "duration": 6917,
    "apic": {
        "read": true,
        "success": 20,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 19,
        "connect_time": 403,
        "disconnect_time": 0,
        "mo_time": 6107,
        "total_time": 6510
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

True	403	-	connect apic11o.emea-sp.cisco.com
True	297	13	apic11o.emea-sp.cisco.com class fabricNode
True	297	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	307	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	284	12	apic11o.emea-sp.cisco.com mo uni/infra/nodecfgcont/node-205 query query-target=subtree&target-subtree-class=infraRsInterfacePolProfile
True	287	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-UCSB1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	291	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-Core-PCIe1-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	287	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-HX1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	293	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-SR-Demo-CDC-2 query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	307	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-SPN_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	292	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-HX1-FI-B_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	303	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-Core-MLOM-1_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	283	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-Infra-BGP_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	283	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-CU-PCIe1-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	299	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-Core-PCIe2-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	339	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-P5G-CU-PCIe2-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	294	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-UCSB1-FI-B_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	518	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	340	30	apic11o.emea-sp.cisco.com class infraAttEntityP query rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	506	46	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
```

[[Back]](./InterfacePhy.md)