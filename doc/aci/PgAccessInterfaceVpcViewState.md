# Policy Group - Access Interface - Leaf Access PC/VPC

## State view

```
# iserver get aci pg access intf vpc --apic apic21

Apic: apic21 (mode:online, cache:off)

Policy Group - Access Interface PC/VPC [#19]
--------------------------------------------

+---------+------------------------+--------------------+----------------+-------------+-----------------+-----------------------+-----------+---------+---------+--------------+------------+----------+
| Faults  | Name                   | AAEP               | CDP            | Link Level  | LLDP            | LACP                  | Link Flap | MCP     | STP     | L2           | Storm Ctrl | Port Sec |
+---------+------------------------+--------------------+----------------+-------------+-----------------+-----------------------+-----------+---------+---------+--------------+------------+----------+
| 0 2 0 0 | ESX20-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | CDP-enable     | 10G-auto    | LLDP-enable     | vEPC-dataplane_vPCPol | default   | default | default | L2-local_Pol | default    | default  | 
| 0 2 0 0 | ESX21-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | CDP-enable     | 40G-fix     | LLDP-enable     | vEPC-dataplane_vPCPol | default   | default | default | L2-local_Pol | default    | default  | 
| 0 0 0 0 | ESX22-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | CDP-enable     | 40G-fix     | LLDP-enable     | vEPC-dataplane_vPCPol | default   | default | default | L2-local_Pol | default    | default  | 
| 0 0 0 0 | HX1-FI-A_PolGrp        | HX1_AAEP           | CDP-enable     | Inherit     | LLDP-enable     | LACP-active           | default   | default | default | L2-local_Pol | default    | default  | 
| 0 0 0 0 | HX1-FI-B_PolGrp        | HX1_AAEP           | CDP-enable     | Inherit     | LLDP-enable     | LACP-active           | default   | default | default | L2-local_Pol | default    | default  | 
| 0 0 0 0 | Infra_PolGrp           | Infra_AAEP         | CDP-enable     | 10G-fix     | LLDP-enable     | LACP-active           | default   | default | default | L2-local     | default    | default  | 
| 0 0 0 0 | k8s_esx71_PolGrp       | k8s_esx_AAEP       | k8s_cdp_enable | k8s_default | k8s_lldp_enable | k8s_lacp_active       | default   | default | default | k8s_l2_local | default    | default  | 
| 0 0 0 0 | k8s_esx72_PolGrp       | k8s_esx_AAEP       | k8s_cdp_enable | k8s_default | k8s_lldp_enable | k8s_lacp_active       | default   | default | default | k8s_l2_local | default    | default  | 
| 0 0 0 0 | k8s_ocp_bm_1_PolGrp    | k8s_phys_AAEP      | k8s_cdp_enable | k8s_default | k8s_lldp_enable | k8s_lacp_active       | default   | default | default | k8s_l2_local | default    | default  | 
| 0 0 0 0 | k8s_ocp_bm_2_PolGrp    | k8s_phys_AAEP      | k8s_cdp_enable | k8s_default | k8s_lldp_enable | k8s_lacp_active       | default   | default | default | k8s_l2_local | default    | default  | 
| 0 2 0 0 | k8s_ocp_bm_3_PolGrp    | k8s_phys_AAEP      | k8s_cdp_enable | k8s_default | k8s_lldp_enable | k8s_lacp_active       | default   | default | default | k8s_l2_local | default    | default  | 
| 0 0 0 0 | k8s_ocp_bm_4_PolGrp    | k8s_phys_AAEP      | k8s_cdp_enable | k8s_default | k8s_lldp_enable | k8s_lacp_active       | default   | default | default | k8s_l2_local | default    | default  | 
| 0 0 0 0 | k8s_ocp_bm_5_PolGrp    | k8s_phys_AAEP      | k8s_cdp_enable | k8s_default | k8s_lldp_enable | k8s_lacp_active       | default   | default | default | k8s_l2_local | default    | default  | 
| 0 0 0 0 | SPN_PolGrp             | SPN_AAEP           | CDP-enable     | 10G-fix     | LLDP-enable     | LACP-active           | default   | default | default | L2-local_Pol | default    | default  | 
| 0 0 0 0 | TEST-vPC               | TEST-AAP           | CDP-enable     | 100G-auto   | LLDP-enable     | LACP-active           | default   | default | default | default      | default    | default  | 
| 0 0 0 0 | UCSB1-FI-A_PolGrp      | UCSB1_AAEP         | CDP-enable     | Inherit     | LLDP-enable     | LACP-active           | default   | default | default | L2-local_Pol | default    | default  | 
| 0 0 0 0 | UCSB1-FI-B_PolGrp      | UCSB1_AAEP         | CDP-enable     | Inherit     | LLDP-enable     | LACP-active           | default   | default | default | L2-local_Pol | default    | default  | 
| 0 0 0 0 | UCSB1-R7DC-FI-A_PolGrp | UCSB1-R7DC_AAEP    | CDP-enable     | 10G-auto    | LLDP-enable     | LACP-active           | default   | default | default | L2-local_Pol | default    | default  | 
| 0 0 0 0 | UCSB1-R7DC-FI-B_PolGrp | UCSB1-R7DC_AAEP    | CDP-enable     | Inherit     | LLDP-enable     | LACP-active           | default   | default | default | L2-local_Pol | default    | default  | 
+---------+------------------------+--------------------+----------------+-------------+-----------------+-----------------------+-----------+---------+---------+--------------+------------+----------+
```

Developer

```
# iserver get aci pg access intf vpc --apic apic21

{
    "duration": 1261,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 417,
        "disconnect_time": 0,
        "mo_time": 497,
        "total_time": 914
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

True	417	-	connect apic21o.emea-sp.cisco.com:443
True	497	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
```

[[Back]](./PgAccessInterfaceVpc.md)