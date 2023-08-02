# Policy Group - Access Interface - Leaf Access PC/VPC

## All view

```
# iserver get aci pg access intf vpc --apic apic21 --when 30d --view all

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-group API call
[INFO] Requires per-interface API call

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

Policy Group - Access Interface PC/VPC - AAEP [#19]
---------------------------------------------------

+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| Name                   | AAEP               | Domain Type | Domain Name           | VLAN Pool              | VLAN Range            |
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| ESX20-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | Physical    | Infra_PhysDom         | ESX-CDC-22_VlanPool    | [1-1000] (static)     | 
|                        |                    | VMM         | vEPC-Dataplane        | Infra_VlanPool         | [2501-2502] (static)  | 
|                        |                    | Physical    | vEPC-ESX20_PhysDom    | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  | 
|                        |                    | Physical    | vEPC-ESX21-22_PhysDom |                        | [2503-2509] (static)  | 
|                        |                    | L3          | vEPC_ESX              |                        | [2700-2999] (dynamic) | 
|                        |                    |             |                       |                        | [2700-2999] (dynamic) | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| ESX21-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | Physical    | Infra_PhysDom         | ESX-CDC-22_VlanPool    | [1-1000] (static)     | 
|                        |                    | VMM         | vEPC-Dataplane        | Infra_VlanPool         | [2501-2502] (static)  | 
|                        |                    | Physical    | vEPC-ESX20_PhysDom    | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  | 
|                        |                    | Physical    | vEPC-ESX21-22_PhysDom |                        | [2503-2509] (static)  | 
|                        |                    | L3          | vEPC_ESX              |                        | [2700-2999] (dynamic) | 
|                        |                    |             |                       |                        | [2700-2999] (dynamic) | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| ESX22-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | Physical    | Infra_PhysDom         | ESX-CDC-22_VlanPool    | [1-1000] (static)     | 
|                        |                    | VMM         | vEPC-Dataplane        | Infra_VlanPool         | [2501-2502] (static)  | 
|                        |                    | Physical    | vEPC-ESX20_PhysDom    | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  | 
|                        |                    | Physical    | vEPC-ESX21-22_PhysDom |                        | [2503-2509] (static)  | 
|                        |                    | L3          | vEPC_ESX              |                        | [2700-2999] (dynamic) | 
|                        |                    |             |                       |                        | [2700-2999] (dynamic) | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| HX1-FI-A_PolGrp        | HX1_AAEP           | Physical    | HX1_PhysDom           | HX1_VlanPool           | [1000-4048] (static)  | 
|                        |                    |             |                       |                        | [70-79] (static)      | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| HX1-FI-B_PolGrp        | HX1_AAEP           | Physical    | HX1_PhysDom           | HX1_VlanPool           | [1000-4048] (static)  | 
|                        |                    |             |                       |                        | [70-79] (static)      | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| Infra_PolGrp           | Infra_AAEP         | L2          | Infra_L2dom           | Infra_VlanPool         | [1-1000] (static)     | 
|                        |                    | L3          | Infra_L3Dom           |                        |                       | 
|                        |                    | Physical    | Infra_PhysDom         |                        |                       | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| k8s_esx71_PolGrp       | k8s_esx_AAEP       | Physical    | k8s_esx_PhysDom       | k8s_esx_VlanPool       | [1300-1499] (dynamic) | 
|                        |                    |             |                       |                        | [800-809] (static)    | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| k8s_esx72_PolGrp       | k8s_esx_AAEP       | Physical    | k8s_esx_PhysDom       | k8s_esx_VlanPool       | [1300-1499] (dynamic) | 
|                        |                    |             |                       |                        | [800-809] (static)    | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| k8s_ocp_bm_1_PolGrp    | k8s_phys_AAEP      | L3          | k8s_phys_L3Dom        | k8s_phys_VlanPool      | [800-809] (static)    | 
|                        |                    | Physical    | k8s_phys_PhysDom      |                        | [810-813] (static)    | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| k8s_ocp_bm_2_PolGrp    | k8s_phys_AAEP      | L3          | k8s_phys_L3Dom        | k8s_phys_VlanPool      | [800-809] (static)    | 
|                        |                    | Physical    | k8s_phys_PhysDom      |                        | [810-813] (static)    | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| k8s_ocp_bm_3_PolGrp    | k8s_phys_AAEP      | L3          | k8s_phys_L3Dom        | k8s_phys_VlanPool      | [800-809] (static)    | 
|                        |                    | Physical    | k8s_phys_PhysDom      |                        | [810-813] (static)    | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| k8s_ocp_bm_4_PolGrp    | k8s_phys_AAEP      | L3          | k8s_phys_L3Dom        | k8s_phys_VlanPool      | [800-809] (static)    | 
|                        |                    | Physical    | k8s_phys_PhysDom      |                        | [810-813] (static)    | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| k8s_ocp_bm_5_PolGrp    | k8s_phys_AAEP      | L3          | k8s_phys_L3Dom        | k8s_phys_VlanPool      | [800-809] (static)    | 
|                        |                    | Physical    | k8s_phys_PhysDom      |                        | [810-813] (static)    | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| SPN_PolGrp             | SPN_AAEP           | Physical    | SPN_PhysDom           | SPN_VlanPool           | [2600-2699] (static)  | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| TEST-vPC               | TEST-AAP           | L3          | Infra_L3Dom           | Infra_VlanPool         | [1-1000] (static)     | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| UCSB1-FI-A_PolGrp      | UCSB1_AAEP         | L3          | UCSB1_L3Dom           | UCSB1_VlanPool         | [2-100] (static)      | 
|                        |                    | Physical    | UCSB1_PhysDom         |                        | [3701-4000] (dynamic) | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| UCSB1-FI-B_PolGrp      | UCSB1_AAEP         | L3          | UCSB1_L3Dom           | UCSB1_VlanPool         | [2-100] (static)      | 
|                        |                    | Physical    | UCSB1_PhysDom         |                        | [3701-4000] (dynamic) | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| UCSB1-R7DC-FI-A_PolGrp | UCSB1-R7DC_AAEP    | Physical    | UCSB1-R7DC_PhysDom    | UCSB1-R7DC_VlanPool    | [1701-1899] (dynamic) | 
|                        |                    |             |                       |                        | [2-100] (static)      | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+
| UCSB1-R7DC-FI-B_PolGrp | UCSB1-R7DC_AAEP    | Physical    | UCSB1-R7DC_PhysDom    | UCSB1-R7DC_VlanPool    | [1701-1899] (dynamic) | 
|                        |                    |             |                       |                        | [2-100] (static)      | 
+------------------------+--------------------+-------------+-----------------------+------------------------+-----------------------+

Policy Group - Access Interface PC/VPC - Deployed Nodes [#19]
-------------------------------------------------------------

+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| PG Name                | AAEP               | VLAN Pool              | VLAN Range            | Node           | Interfaces |
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| ESX20-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | ESX-CDC-22_VlanPool    | [1-1000] (static)     | cl2201-eu-spdc | 1          | 
|                        |                    | Infra_VlanPool         | [2501-2502] (static)  | cl2202-eu-spdc | 1          | 
|                        |                    | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  |                |            | 
|                        |                    |                        | [2503-2509] (static)  |                |            | 
|                        |                    |                        | [2700-2999] (dynamic) |                |            | 
|                        |                    |                        | [2700-2999] (dynamic) |                |            | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| ESX21-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | ESX-CDC-22_VlanPool    | [1-1000] (static)     | cl2207-eu-spdc | 1          | 
|                        |                    | Infra_VlanPool         | [2501-2502] (static)  | cl2208-eu-spdc | 1          | 
|                        |                    | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  |                |            | 
|                        |                    |                        | [2503-2509] (static)  |                |            | 
|                        |                    |                        | [2700-2999] (dynamic) |                |            | 
|                        |                    |                        | [2700-2999] (dynamic) |                |            | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| ESX22-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | ESX-CDC-22_VlanPool    | [1-1000] (static)     | bl2205-eu-spdc | 1          | 
|                        |                    | Infra_VlanPool         | [2501-2502] (static)  | bl2206-eu-spdc | 1          | 
|                        |                    | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  |                |            | 
|                        |                    |                        | [2503-2509] (static)  |                |            | 
|                        |                    |                        | [2700-2999] (dynamic) |                |            | 
|                        |                    |                        | [2700-2999] (dynamic) |                |            | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| HX1-FI-A_PolGrp        | HX1_AAEP           | HX1_VlanPool           | [1000-4048] (static)  | bl2205-eu-spdc | 1          | 
|                        |                    |                        | [70-79] (static)      | bl2206-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| HX1-FI-B_PolGrp        | HX1_AAEP           | HX1_VlanPool           | [1000-4048] (static)  | bl2205-eu-spdc | 1          | 
|                        |                    |                        | [70-79] (static)      | bl2206-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| Infra_PolGrp           | Infra_AAEP         | Infra_VlanPool         | [1-1000] (static)     | cl2201-eu-spdc | 1          | 
|                        |                    |                        |                       | cl2202-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| k8s_esx71_PolGrp       | k8s_esx_AAEP       | k8s_esx_VlanPool       | [1300-1499] (dynamic) | cl2207-eu-spdc | 1          | 
|                        |                    |                        | [800-809] (static)    | cl2208-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| k8s_esx72_PolGrp       | k8s_esx_AAEP       | k8s_esx_VlanPool       | [1300-1499] (dynamic) | cl2207-eu-spdc | 1          | 
|                        |                    |                        | [800-809] (static)    | cl2208-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| k8s_ocp_bm_1_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | 1          | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| k8s_ocp_bm_2_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | 1          | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| k8s_ocp_bm_3_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | 1          | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| k8s_ocp_bm_4_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | 1          | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| k8s_ocp_bm_5_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | 1          | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| SPN_PolGrp             | SPN_AAEP           | SPN_VlanPool           | [2600-2699] (static)  | bl2205-eu-spdc | 1          | 
|                        |                    |                        |                       | bl2206-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| TEST-vPC               | TEST-AAP           | Infra_VlanPool         | [1-1000] (static)     | cl2207-eu-spdc | 1          | 
|                        |                    |                        |                       | cl2208-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| UCSB1-FI-A_PolGrp      | UCSB1_AAEP         | UCSB1_VlanPool         | [2-100] (static)      | bl2205-eu-spdc | 1          | 
|                        |                    |                        | [3701-4000] (dynamic) | bl2206-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| UCSB1-FI-B_PolGrp      | UCSB1_AAEP         | UCSB1_VlanPool         | [2-100] (static)      | bl2205-eu-spdc | 1          | 
|                        |                    |                        | [3701-4000] (dynamic) | bl2206-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| UCSB1-R7DC-FI-A_PolGrp | UCSB1-R7DC_AAEP    | UCSB1-R7DC_VlanPool    | [1701-1899] (dynamic) | rl2701-eu-spdc | 1          | 
|                        |                    |                        | [2-100] (static)      | rl2702-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+
| UCSB1-R7DC-FI-B_PolGrp | UCSB1-R7DC_AAEP    | UCSB1-R7DC_VlanPool    | [1701-1899] (dynamic) | rl2701-eu-spdc | 1          | 
|                        |                    |                        | [2-100] (static)      | rl2702-eu-spdc | 1          | 
+------------------------+--------------------+------------------------+-----------------------+----------------+------------+

Policy Group - Access Interface PC/VPC - Deployed Interfaces [#19]
------------------------------------------------------------------

+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| PG Name                | AAEP               | VLAN Pool              | VLAN Range            | Node           | Intf Name |
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| ESX20-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | ESX-CDC-22_VlanPool    | [1-1000] (static)     | cl2201-eu-spdc | eth1/90   | 
|                        |                    | Infra_VlanPool         | [2501-2502] (static)  | cl2202-eu-spdc | eth1/90   | 
|                        |                    | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  |                |           | 
|                        |                    |                        | [2503-2509] (static)  |                |           | 
|                        |                    |                        | [2700-2999] (dynamic) |                |           | 
|                        |                    |                        | [2700-2999] (dynamic) |                |           | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| ESX21-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | ESX-CDC-22_VlanPool    | [1-1000] (static)     | cl2207-eu-spdc | eth1/19   | 
|                        |                    | Infra_VlanPool         | [2501-2502] (static)  | cl2208-eu-spdc | eth1/19   | 
|                        |                    | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  |                |           | 
|                        |                    |                        | [2503-2509] (static)  |                |           | 
|                        |                    |                        | [2700-2999] (dynamic) |                |           | 
|                        |                    |                        | [2700-2999] (dynamic) |                |           | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| ESX22-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | ESX-CDC-22_VlanPool    | [1-1000] (static)     | bl2205-eu-spdc | eth1/19   | 
|                        |                    | Infra_VlanPool         | [2501-2502] (static)  | bl2206-eu-spdc | eth1/19   | 
|                        |                    | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  |                |           | 
|                        |                    |                        | [2503-2509] (static)  |                |           | 
|                        |                    |                        | [2700-2999] (dynamic) |                |           | 
|                        |                    |                        | [2700-2999] (dynamic) |                |           | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| HX1-FI-A_PolGrp        | HX1_AAEP           | HX1_VlanPool           | [1000-4048] (static)  | bl2205-eu-spdc | eth1/11   | 
|                        |                    |                        | [70-79] (static)      | bl2206-eu-spdc | eth1/11   | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| HX1-FI-B_PolGrp        | HX1_AAEP           | HX1_VlanPool           | [1000-4048] (static)  | bl2205-eu-spdc | eth1/12   | 
|                        |                    |                        | [70-79] (static)      | bl2206-eu-spdc | eth1/12   | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| Infra_PolGrp           | Infra_AAEP         | Infra_VlanPool         | [1-1000] (static)     | cl2201-eu-spdc | eth1/96   | 
|                        |                    |                        |                       | cl2202-eu-spdc | eth1/96   | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| k8s_esx71_PolGrp       | k8s_esx_AAEP       | k8s_esx_VlanPool       | [1300-1499] (dynamic) | cl2207-eu-spdc | eth1/1/1  | 
|                        |                    |                        | [800-809] (static)    | cl2208-eu-spdc | eth1/1/1  | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| k8s_esx72_PolGrp       | k8s_esx_AAEP       | k8s_esx_VlanPool       | [1300-1499] (dynamic) | cl2207-eu-spdc | eth1/1/2  | 
|                        |                    |                        | [800-809] (static)    | cl2208-eu-spdc | eth1/1/2  | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| k8s_ocp_bm_1_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | eth1/1/3  | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | eth1/1/3  | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| k8s_ocp_bm_2_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | eth1/1/4  | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | eth1/1/4  | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| k8s_ocp_bm_3_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | eth1/2/1  | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | eth1/2/1  | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| k8s_ocp_bm_4_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | eth1/2/2  | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | eth1/2/2  | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| k8s_ocp_bm_5_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | eth1/2/3  | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | eth1/2/3  | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| SPN_PolGrp             | SPN_AAEP           | SPN_VlanPool           | [2600-2699] (static)  | bl2205-eu-spdc | eth1/27   | 
|                        |                    |                        |                       | bl2206-eu-spdc | eth1/27   | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| TEST-vPC               | TEST-AAP           | Infra_VlanPool         | [1-1000] (static)     | cl2207-eu-spdc | eth1/31   | 
|                        |                    |                        |                       | cl2208-eu-spdc | eth1/31   | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| UCSB1-FI-A_PolGrp      | UCSB1_AAEP         | UCSB1_VlanPool         | [2-100] (static)      | bl2205-eu-spdc | eth1/1    | 
|                        |                    |                        | [3701-4000] (dynamic) | bl2206-eu-spdc | eth1/1    | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| UCSB1-FI-B_PolGrp      | UCSB1_AAEP         | UCSB1_VlanPool         | [2-100] (static)      | bl2205-eu-spdc | eth1/2    | 
|                        |                    |                        | [3701-4000] (dynamic) | bl2206-eu-spdc | eth1/2    | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| UCSB1-R7DC-FI-A_PolGrp | UCSB1-R7DC_AAEP    | UCSB1-R7DC_VlanPool    | [1701-1899] (dynamic) | rl2701-eu-spdc | eth1/49   | 
|                        |                    |                        | [2-100] (static)      | rl2702-eu-spdc | eth1/49   | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+
| UCSB1-R7DC-FI-B_PolGrp | UCSB1-R7DC_AAEP    | UCSB1-R7DC_VlanPool    | [1701-1899] (dynamic) | rl2701-eu-spdc | eth1/50   | 
|                        |                    |                        | [2-100] (static)      | rl2702-eu-spdc | eth1/50   | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+

Policy Group - Access Interface PC/VPC - Deployed Interfaces with State [#19]
-----------------------------------------------------------------------------

+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| PG Name                | AAEP               | VLAN Pool              | VLAN Range            | Node           | Intf Name | State | Mode  | VLANs                                                       |
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| ESX20-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | ESX-CDC-22_VlanPool    | [1-1000] (static)     | cl2201-eu-spdc | eth1/90   | up    | trunk |                                                             | 
|                        |                    | Infra_VlanPool         | [2501-2502] (static)  | cl2202-eu-spdc | eth1/90   | up    | trunk |                                                             | 
|                        |                    | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  |                |           |       |       |                                                             | 
|                        |                    |                        | [2503-2509] (static)  |                |           |       |       |                                                             | 
|                        |                    |                        | [2700-2999] (dynamic) |                |           |       |       |                                                             | 
|                        |                    |                        | [2700-2999] (dynamic) |                |           |       |       |                                                             | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| ESX21-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | ESX-CDC-22_VlanPool    | [1-1000] (static)     | cl2207-eu-spdc | eth1/19   | up    | trunk |                                                             | 
|                        |                    | Infra_VlanPool         | [2501-2502] (static)  | cl2208-eu-spdc | eth1/19   | up    | trunk |                                                             | 
|                        |                    | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  |                |           |       |       |                                                             | 
|                        |                    |                        | [2503-2509] (static)  |                |           |       |       |                                                             | 
|                        |                    |                        | [2700-2999] (dynamic) |                |           |       |       |                                                             | 
|                        |                    |                        | [2700-2999] (dynamic) |                |           |       |       |                                                             | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| ESX22-CDC-22_PolGrp    | vEPC-ESX21-22_AAEP | ESX-CDC-22_VlanPool    | [1-1000] (static)     | bl2205-eu-spdc | eth1/19   | up    | trunk | 2700,2701,2800,2900                                         | 
|                        |                    | Infra_VlanPool         | [2501-2502] (static)  | bl2206-eu-spdc | eth1/19   | up    | trunk | 2700,2701,2800,2900                                         | 
|                        |                    | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  |                |           |       |       |                                                             | 
|                        |                    |                        | [2503-2509] (static)  |                |           |       |       |                                                             | 
|                        |                    |                        | [2700-2999] (dynamic) |                |           |       |       |                                                             | 
|                        |                    |                        | [2700-2999] (dynamic) |                |           |       |       |                                                             | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| HX1-FI-A_PolGrp        | HX1_AAEP           | HX1_VlanPool           | [1000-4048] (static)  | bl2205-eu-spdc | eth1/11   | up    | trunk |                                                             | 
|                        |                    |                        | [70-79] (static)      | bl2206-eu-spdc | eth1/11   | up    | trunk |                                                             | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| HX1-FI-B_PolGrp        | HX1_AAEP           | HX1_VlanPool           | [1000-4048] (static)  | bl2205-eu-spdc | eth1/12   | up    | trunk |                                                             | 
|                        |                    |                        | [70-79] (static)      | bl2206-eu-spdc | eth1/12   | up    | trunk |                                                             | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| Infra_PolGrp           | Infra_AAEP         | Infra_VlanPool         | [1-1000] (static)     | cl2201-eu-spdc | eth1/96   | up    | trunk |                                                             | 
|                        |                    |                        |                       | cl2202-eu-spdc | eth1/96   | up    | trunk |                                                             | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| k8s_esx71_PolGrp       | k8s_esx_AAEP       | k8s_esx_VlanPool       | [1300-1499] (dynamic) | cl2207-eu-spdc | eth1/1/1  | up    | trunk | 1300,1301,1302,1303,1304,1305,1306,1367,1368,1369,1435,1437 | 
|                        |                    |                        | [800-809] (static)    | cl2208-eu-spdc | eth1/1/1  | up    | trunk | 1300,1301,1302,1303,1304,1305,1306,1367,1368,1369,1435,1437 | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| k8s_esx72_PolGrp       | k8s_esx_AAEP       | k8s_esx_VlanPool       | [1300-1499] (dynamic) | cl2207-eu-spdc | eth1/1/2  | up    | trunk | 1300,1301,1302,1303,1304,1305,1306,1367,1368,1369,1435,1437 | 
|                        |                    |                        | [800-809] (static)    | cl2208-eu-spdc | eth1/1/2  | up    | trunk | 1300,1301,1302,1303,1304,1305,1306,1367,1368,1369,1435,1437 | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| k8s_ocp_bm_1_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | eth1/1/3  | up    | trunk | 801,809                                                     | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | eth1/1/3  | up    | trunk | 801,809                                                     | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| k8s_ocp_bm_2_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | eth1/1/4  | up    | trunk | 802,809                                                     | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | eth1/1/4  | up    | trunk | 802,809                                                     | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| k8s_ocp_bm_3_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | eth1/2/1  | down  | trunk | 809                                                         | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | eth1/2/1  | down  | trunk | 809                                                         | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| k8s_ocp_bm_4_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | eth1/2/2  | up    | trunk | 809                                                         | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | eth1/2/2  | up    | trunk | 809                                                         | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| k8s_ocp_bm_5_PolGrp    | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | eth1/2/3  | up    | trunk | 809                                                         | 
|                        |                    |                        | [810-813] (static)    | cl2208-eu-spdc | eth1/2/3  | up    | trunk | 809                                                         | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| SPN_PolGrp             | SPN_AAEP           | SPN_VlanPool           | [2600-2699] (static)  | bl2205-eu-spdc | eth1/27   | up    | trunk |                                                             | 
|                        |                    |                        |                       | bl2206-eu-spdc | eth1/27   | up    | trunk |                                                             | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| TEST-vPC               | TEST-AAP           | Infra_VlanPool         | [1-1000] (static)     | cl2207-eu-spdc | eth1/31   | down  | trunk |                                                             | 
|                        |                    |                        |                       | cl2208-eu-spdc | eth1/31   | down  | trunk |                                                             | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| UCSB1-FI-A_PolGrp      | UCSB1_AAEP         | UCSB1_VlanPool         | [2-100] (static)      | bl2205-eu-spdc | eth1/1    | up    | trunk |                                                             | 
|                        |                    |                        | [3701-4000] (dynamic) | bl2206-eu-spdc | eth1/1    | up    | trunk |                                                             | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| UCSB1-FI-B_PolGrp      | UCSB1_AAEP         | UCSB1_VlanPool         | [2-100] (static)      | bl2205-eu-spdc | eth1/2    | up    | trunk |                                                             | 
|                        |                    |                        | [3701-4000] (dynamic) | bl2206-eu-spdc | eth1/2    | up    | trunk |                                                             | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| UCSB1-R7DC-FI-A_PolGrp | UCSB1-R7DC_AAEP    | UCSB1-R7DC_VlanPool    | [1701-1899] (dynamic) | rl2701-eu-spdc | eth1/49   | up    | trunk |                                                             | 
|                        |                    |                        | [2-100] (static)      | rl2702-eu-spdc | eth1/49   | up    | trunk |                                                             | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+
| UCSB1-R7DC-FI-B_PolGrp | UCSB1-R7DC_AAEP    | UCSB1-R7DC_VlanPool    | [1701-1899] (dynamic) | rl2701-eu-spdc | eth1/50   | up    | trunk |                                                             | 
|                        |                    |                        | [2-100] (static)      | rl2702-eu-spdc | eth1/50   | up    | trunk |                                                             | 
+------------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-------------------------------------------------------------+

Policy Group - Access Interface PC/VPC - Faults [#6]
----------------------------------------------------

+---------------------+-----+-------+--------------------+-------------------------------+-----------+----------------------------------------------------------------------------+
| PG Name             | Sev | Code  | Cause              | Created Time                  | Lifecycle | Description                                                                |
+---------------------+-----+-------+--------------------+-------------------------------+-----------+----------------------------------------------------------------------------+
| ESX20-CDC-22_PolGrp | Maj | F1296 | interface-vpc-down | 2023-06-18T09:44:34.467+02:00 | raised    | Fault delegate: vPC ESX20-CDC-22_PolGrp is down in Pod 1 node 2201 fabric  | 
|                     |     |       |                    |                               |           | hostname cl2201-eu-spdc                                                    | 
| ESX20-CDC-22_PolGrp | Maj | F1296 | interface-vpc-down | 2023-06-18T09:18:19.916+02:00 | raised    | Fault delegate: vPC ESX20-CDC-22_PolGrp is down in Pod 1 node 2202 fabric  | 
|                     |     |       |                    |                               |           | hostname cl2202-eu-spdc                                                    | 
| ESX21-CDC-22_PolGrp | Maj | F1296 | interface-vpc-down | 2023-06-18T09:44:11.082+02:00 | raised    | Fault delegate: vPC ESX21-CDC-22_PolGrp is down in Pod 1 node 2207 fabric  | 
|                     |     |       |                    |                               |           | hostname cl2207-eu-spdc                                                    | 
| ESX21-CDC-22_PolGrp | Maj | F1296 | interface-vpc-down | 2023-06-18T09:16:15.179+02:00 | raised    | Fault delegate: vPC ESX21-CDC-22_PolGrp is down in Pod 1 node 2208 fabric  | 
|                     |     |       |                    |                               |           | hostname cl2208-eu-spdc                                                    | 
| k8s_ocp_bm_3_PolGrp | Maj | F1296 | interface-vpc-down | 2023-06-18T09:16:15.241+02:00 | raised    | Fault delegate: vPC k8s_ocp_bm_3_PolGrp is down in Pod 1 node 2208 fabric  | 
|                     |     |       |                    |                               |           | hostname cl2208-eu-spdc                                                    | 
| k8s_ocp_bm_3_PolGrp | Maj | F1296 | interface-vpc-down | 2023-06-18T09:44:11.056+02:00 | raised    | Fault delegate: vPC k8s_ocp_bm_3_PolGrp is down in Pod 1 node 2207 fabric  | 
|                     |     |       |                    |                               |           | hostname cl2207-eu-spdc                                                    | 
+---------------------+-----+-------+--------------------+-------------------------------+-----------+----------------------------------------------------------------------------+

Policy Group - Access Interface PC/VPC - Fault Records last 30d [#8]
--------------------------------------------------------------------

+---------------------+-----+-------+------------------------+-------------------------------+------------------+--------------------------------------------------------------------------------+
| PG Name             | Sev | Code  | Cause                  | Created Time                  | Lifecycle        | Description                                                                    |
+---------------------+-----+-------+------------------------+-------------------------------+------------------+--------------------------------------------------------------------------------+
| k8s_ocp_bm_1_PolGrp | --  | F2705 | interface-vpc-impaired | 2023-07-06T11:25:35.230+02:00 |                  | Fault delegate: vPC k8s_ocp_bm_1_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_1_PolGrp | --  | F2705 | interface-vpc-impaired | 2023-07-06T10:25:34.716+02:00 | retaining        | Fault delegate: vPC k8s_ocp_bm_1_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_1_PolGrp | Maj | F2705 | interface-vpc-impaired | 2023-07-06T10:23:25.497+02:00 | soaking-clearing | Fault delegate: vPC k8s_ocp_bm_1_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_1_PolGrp | Maj | F2705 | interface-vpc-impaired | 2023-07-06T10:23:22.145+02:00 | soaking          | Fault delegate: vPC k8s_ocp_bm_1_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_2_PolGrp | --  | F2705 | interface-vpc-impaired | 2023-07-06T11:25:35.232+02:00 |                  | Fault delegate: vPC k8s_ocp_bm_2_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_2_PolGrp | --  | F2705 | interface-vpc-impaired | 2023-07-06T10:25:34.718+02:00 | retaining        | Fault delegate: vPC k8s_ocp_bm_2_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_2_PolGrp | Maj | F2705 | interface-vpc-impaired | 2023-07-06T10:23:25.432+02:00 | soaking-clearing | Fault delegate: vPC k8s_ocp_bm_2_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
| k8s_ocp_bm_2_PolGrp | Maj | F2705 | interface-vpc-impaired | 2023-07-06T10:23:22.032+02:00 | soaking          | Fault delegate: vPC k8s_ocp_bm_2_PolGrp is impaired in Pod 1 node 2208 fabric  | 
|                     |     |       |                        |                               |                  | hostname cl2208-eu-spdc                                                        | 
+---------------------+-----+-------+------------------------+-------------------------------+------------------+--------------------------------------------------------------------------------+

Policy Group - Access Interface PC/VPC - Event Logs last 30d [#0]
-----------------------------------------------------------------
None

Policy Group - Access Interface PC/VPC - Audit Logs last 30d [#0]
-----------------------------------------------------------------
None
```

Developer

```
# iserver get aci pg access intf vpc --apic apic21 --when 30d --view all

{
    "duration": 53597,
    "apic": {
        "read": true,
        "success": 93,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 92,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 48585,
        "total_time": 49007
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

True	422	-	connect apic21o.emea-sp.cisco.com:443
True	561	19	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	380	15	apic21o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	324	16	apic21o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	361	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	348	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	352	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	709	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	335	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	499	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-ESX20-CDC-22_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	409	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1921	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	409	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ethpmPhysIf
True	279	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/90] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	2005	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	389	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ethpmPhysIf
True	323	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/90] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	392	6	apic21o.emea-sp.cisco.com:443 class infraAccBndlGrp query rsp-subtree-include=faults,no-scoped,subtree
True	6186	1000	apic21o.emea-sp.cisco.com:443 class infraAccBndlGrp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	852	19	apic21o.emea-sp.cisco.com:443 class infraAccBndlGrp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	1298	1046	apic21o.emea-sp.cisco.com:443 class infraAccBndlGrp query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
True	468	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-ESX21-CDC-22_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	1146	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	349	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ethpmPhysIf
True	343	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1144	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	309	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ethpmPhysIf
True	312	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	661	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-ESX22-CDC-22_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	841	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	302	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	288	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	425	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	326	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	956	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	305	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ethpmPhysIf
True	354	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	274	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vlanCktEp
True	469	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-HX1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	321	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	290	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	466	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-HX1-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	335	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	291	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	367	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	467	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-Infra_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	288	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/96] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	333	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/96] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	469	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_esx71_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	313	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	291	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vlanCktEp
True	312	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	286	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vlanCktEp
True	460	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_esx72_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	297	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	299	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	464	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_ocp_bm_1_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	300	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	355	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	460	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_ocp_bm_2_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	284	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	290	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	455	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_ocp_bm_3_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	297	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/2/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	288	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/2/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	445	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_ocp_bm_4_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	288	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/2/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	284	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/2/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	458	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-k8s_ocp_bm_5_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	339	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/2/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	301	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/2/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	516	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-SPN_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	332	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	294	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	455	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-TEST-vPC query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	293	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	278	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	447	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-UCSB1-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	323	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	337	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	461	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-UCSB1-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	321	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	326	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	466	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-UCSB1-R7DC-FI-A_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	1407	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	303	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ethpmPhysIf
True	291	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/49] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1269	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	310	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ethpmPhysIf
True	292	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/49] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	456	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accbundle-UCSB1-R7DC-FI-B_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	287	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/50] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	324	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/50] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./PgAccessInterfaceVpc.md)