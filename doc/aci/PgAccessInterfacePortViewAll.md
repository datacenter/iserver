# Policy Group - Access Interface - Leaf Access Port

## All view

```
# iserver get aci pg access intf port --apic apic21 --when any --view all

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-group API call
[INFO] Requires per-interface API call

Policy Group - Access Interface Port [#8]
-----------------------------------------

+---------+---------------------------+-----------------+-------------+-----------+----------------+---------+-----------------+---------+---------------+
| Faults  | Name                      | AAEP            | Link Level  | Link Flap | CDP            | MCP     | LLDP            | STP     | Storm Control |
+---------+---------------------------+-----------------+-------------+-----------+----------------+---------+-----------------+---------+---------------+
| 0 0 0 0 | ESX-CDC-22_PolGrp         | ESX-CDC-22_AAEP | Inherit     | default   | CDP-enable     | default | LLDP-enable     | default | default       | 
| 0 0 0 0 | ESX-R7DC_PolGrp           | ESX-R7DC_AAEP   | Inherit     | default   | default        | default | LLDP-enable     | default | default       | 
| 0 0 0 0 | Infra-L3_PolGrp           | Infra_AAEP      | Inherit     | default   | CDP-enable     | default | LLDP-enable     | default | default       | 
| 0 0 0 0 | k8s_sriov_2207_bm_PolGrp  | k8s_phys_AAEP   | k8s_default | default   | k8s_cdp_enable | default | k8s_lldp_enable | default | default       | 
| 0 0 0 0 | k8s_sriov_2207_esx_PolGrp | k8s_phys_AAEP   | k8s_default | default   | k8s_cdp_enable | default | k8s_lldp_enable | default | default       | 
| 0 0 0 0 | k8s_sriov_2208_bm_PolGrp  | k8s_phys_AAEP   | k8s_default | default   | k8s_cdp_enable | default | k8s_lldp_enable | default | default       | 
| 0 0 0 0 | k8s_sriov_2208_esx_PolGrp | k8s_phys_AAEP   | k8s_default | default   | k8s_cdp_enable | default | k8s_lldp_enable | default | default       | 
| 0 0 0 0 | nidemo-bare-metal         | nidemo          | 10G-auto    | default   | default        | default | LLDP-enable     | default | default       | 
+---------+---------------------------+-----------------+-------------+-----------+----------------+---------+-----------------+---------+---------------+

Policy Group - Access Interface Port - AAEP [#8]
------------------------------------------------

+---------------------------+-----------------+-------------+--------------------+---------------------+-----------------------+
| Name                      | AAEP            | Domain Type | Domain Name        | VLAN Pool           | VLAN Range            |
+---------------------------+-----------------+-------------+--------------------+---------------------+-----------------------+
| ESX-CDC-22_PolGrp         | ESX-CDC-22_AAEP | Physical    | ESX-CDC-22_PhysDom | ESX-CDC-22_VlanPool | [2501-2502] (static)  | 
|                           |                 | VMM         | EU-SPDC-CDC-22     |                     | [2503-2509] (static)  | 
|                           |                 | L3          | vEPC_ESX           |                     | [2700-2999] (dynamic) | 
+---------------------------+-----------------+-------------+--------------------+---------------------+-----------------------+
| ESX-R7DC_PolGrp           | ESX-R7DC_AAEP   | Physical    | ESX-R7DC_PhysDom   | ESX-R7DC_VlanPool   | [3701-3800] (dynamic) | 
|                           |                 | VMM         | EU-SPDC-R7DC       |                     |                       | 
+---------------------------+-----------------+-------------+--------------------+---------------------+-----------------------+
| Infra-L3_PolGrp           | Infra_AAEP      | L2          | Infra_L2dom        | Infra_VlanPool      | [1-1000] (static)     | 
|                           |                 | L3          | Infra_L3Dom        |                     |                       | 
|                           |                 | Physical    | Infra_PhysDom      |                     |                       | 
+---------------------------+-----------------+-------------+--------------------+---------------------+-----------------------+
| k8s_sriov_2207_bm_PolGrp  | k8s_phys_AAEP   | L3          | k8s_phys_L3Dom     | k8s_phys_VlanPool   | [800-809] (static)    | 
|                           |                 | Physical    | k8s_phys_PhysDom   |                     | [810-813] (static)    | 
+---------------------------+-----------------+-------------+--------------------+---------------------+-----------------------+
| k8s_sriov_2207_esx_PolGrp | k8s_phys_AAEP   | L3          | k8s_phys_L3Dom     | k8s_phys_VlanPool   | [800-809] (static)    | 
|                           |                 | Physical    | k8s_phys_PhysDom   |                     | [810-813] (static)    | 
+---------------------------+-----------------+-------------+--------------------+---------------------+-----------------------+
| k8s_sriov_2208_bm_PolGrp  | k8s_phys_AAEP   | L3          | k8s_phys_L3Dom     | k8s_phys_VlanPool   | [800-809] (static)    | 
|                           |                 | Physical    | k8s_phys_PhysDom   |                     | [810-813] (static)    | 
+---------------------------+-----------------+-------------+--------------------+---------------------+-----------------------+
| k8s_sriov_2208_esx_PolGrp | k8s_phys_AAEP   | L3          | k8s_phys_L3Dom     | k8s_phys_VlanPool   | [800-809] (static)    | 
|                           |                 | Physical    | k8s_phys_PhysDom   |                     | [810-813] (static)    | 
+---------------------------+-----------------+-------------+--------------------+---------------------+-----------------------+
| nidemo-bare-metal         | nidemo          | Physical    | nidemo             | nidemo-3000-3001    | [3000-3001] (static)  | 
|                           |                 | L2          | test               |                     |                       | 
+---------------------------+-----------------+-------------+--------------------+---------------------+-----------------------+

Policy Group - Access Interface Port - Deployed Nodes [#8]
----------------------------------------------------------

+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| PG Name                   | AAEP            | VLAN Pool           | VLAN Range            | Node           | Interfaces |
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| ESX-CDC-22_PolGrp         | ESX-CDC-22_AAEP | ESX-CDC-22_VlanPool | [2501-2502] (static)  | cl2201-eu-spdc | 17         | 
|                           |                 |                     | [2503-2509] (static)  | cl2202-eu-spdc | 17         | 
|                           |                 |                     | [2700-2999] (dynamic) |                |            | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| ESX-R7DC_PolGrp           | ESX-R7DC_AAEP   | ESX-R7DC_VlanPool   | [3701-3800] (dynamic) | rl2701-eu-spdc | 13         | 
|                           |                 |                     |                       | rl2702-eu-spdc | 13         | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| Infra-L3_PolGrp           | Infra_AAEP      | Infra_VlanPool      | [1-1000] (static)     | bl2205-eu-spdc | 1          | 
|                           |                 |                     |                       | bl2206-eu-spdc | 1          | 
|                           |                 |                     |                       | cl2201-eu-spdc | 1          | 
|                           |                 |                     |                       | cl2202-eu-spdc | 1          | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| k8s_sriov_2207_bm_PolGrp  | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2207-eu-spdc | 10         | 
|                           |                 |                     | [810-813] (static)    |                |            | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| k8s_sriov_2207_esx_PolGrp | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2207-eu-spdc | 4          | 
|                           |                 |                     | [810-813] (static)    |                |            | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| k8s_sriov_2208_bm_PolGrp  | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2208-eu-spdc | 10         | 
|                           |                 |                     | [810-813] (static)    |                |            | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| k8s_sriov_2208_esx_PolGrp | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2208-eu-spdc | 4          | 
|                           |                 |                     | [810-813] (static)    |                |            | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+
| nidemo-bare-metal         | nidemo          | nidemo-3000-3001    | [3000-3001] (static)  | rl2701-eu-spdc | 2          | 
|                           |                 |                     |                       | rl2702-eu-spdc | 2          | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+------------+

Policy Group - Access Interface Port - Deployed Interfaces [#8]
---------------------------------------------------------------

+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| PG Name                   | AAEP            | VLAN Pool           | VLAN Range            | Node           | Intf Name |
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| ESX-CDC-22_PolGrp         | ESX-CDC-22_AAEP | ESX-CDC-22_VlanPool | [2501-2502] (static)  | cl2201-eu-spdc | eth1/31   | 
|                           |                 |                     | [2503-2509] (static)  | cl2201-eu-spdc | eth1/32   | 
|                           |                 |                     | [2700-2999] (dynamic) | cl2201-eu-spdc | eth1/33   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/34   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/35   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/36   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/37   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/38   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/39   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/40   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/41   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/42   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/43   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/44   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/45   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/46   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/47   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/31   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/32   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/33   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/34   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/35   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/36   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/37   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/38   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/39   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/40   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/41   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/42   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/43   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/44   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/45   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/46   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/47   | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| ESX-R7DC_PolGrp           | ESX-R7DC_AAEP   | ESX-R7DC_VlanPool   | [3701-3800] (dynamic) | rl2701-eu-spdc | eth1/1    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/10   | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/11   | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/12   | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/13   | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/2    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/3    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/4    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/5    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/6    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/7    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/8    | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/9    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/1    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/10   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/11   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/12   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/13   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/2    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/3    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/4    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/5    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/6    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/7    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/8    | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/9    | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| Infra-L3_PolGrp           | Infra_AAEP      | Infra_VlanPool      | [1-1000] (static)     | bl2205-eu-spdc | eth1/25   | 
|                           |                 |                     |                       | bl2206-eu-spdc | eth1/25   | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/25   | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/25   | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| k8s_sriov_2207_bm_PolGrp  | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2207-eu-spdc | eth1/3/3  | 
|                           |                 |                     | [810-813] (static)    | cl2207-eu-spdc | eth1/3/4  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/4/1  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/4/2  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/4/3  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/5/3  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/5/4  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/6/1  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/6/2  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/6/3  | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| k8s_sriov_2207_esx_PolGrp | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2207-eu-spdc | eth1/3/1  | 
|                           |                 |                     | [810-813] (static)    | cl2207-eu-spdc | eth1/3/2  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/5/1  | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/5/2  | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| k8s_sriov_2208_bm_PolGrp  | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2208-eu-spdc | eth1/3/3  | 
|                           |                 |                     | [810-813] (static)    | cl2208-eu-spdc | eth1/3/4  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/4/1  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/4/2  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/4/3  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/5/3  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/5/4  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/6/1  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/6/2  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/6/3  | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| k8s_sriov_2208_esx_PolGrp | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2208-eu-spdc | eth1/3/1  | 
|                           |                 |                     | [810-813] (static)    | cl2208-eu-spdc | eth1/3/2  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/5/1  | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/5/2  | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+
| nidemo-bare-metal         | nidemo          | nidemo-3000-3001    | [3000-3001] (static)  | rl2701-eu-spdc | eth1/19   | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/20   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/19   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/20   | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+

Policy Group - Access Interface Port - Deployed Interfaces with State [#8]
--------------------------------------------------------------------------

+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+--------------------------------------------------------+
| PG Name                   | AAEP            | VLAN Pool           | VLAN Range            | Node           | Intf Name | State | Mode  | VLANs                                                  |
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+--------------------------------------------------------+
| ESX-CDC-22_PolGrp         | ESX-CDC-22_AAEP | ESX-CDC-22_VlanPool | [2501-2502] (static)  | cl2201-eu-spdc | eth1/31   | up    | trunk | 2701,2702,2703,2704,2708,2902                          | 
|                           |                 |                     | [2503-2509] (static)  | cl2201-eu-spdc | eth1/32   | up    | trunk | 2701,2702,2703,2704,2708,2902                          | 
|                           |                 |                     | [2700-2999] (dynamic) | cl2201-eu-spdc | eth1/33   | down  | trunk | 2701,2702,2703,2704,2708,2902                          | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/34   | up    | trunk | 2701,2702,2703,2704,2708,2800,2801,2804,2900,2901,2902 | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/35   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/36   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/37   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/38   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/39   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/40   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/41   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/42   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/43   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/44   | up    | trunk | 2701,2702,2703,2704,2708,2902                          | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/45   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/46   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/47   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/31   | up    | trunk | 2701,2702,2703,2704,2708,2902                          | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/32   | up    | trunk | 2701,2702,2703,2704,2708,2902                          | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/33   | down  | trunk | 2701,2702,2703,2704,2708,2902                          | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/34   | up    | trunk | 2701,2702,2703,2704,2708,2800,2801,2804,2900,2901,2902 | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/35   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/36   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/37   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/38   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/39   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/40   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/41   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/42   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/43   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/44   | up    | trunk | 2701,2702,2703,2704,2708,2902                          | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/45   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/46   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/47   | up    | trunk | 2701,2702,2703,2704,2708,2804,2902                     | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+--------------------------------------------------------+
| ESX-R7DC_PolGrp           | ESX-R7DC_AAEP   | ESX-R7DC_VlanPool   | [3701-3800] (dynamic) | rl2701-eu-spdc | eth1/1    | down  | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/10   | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/11   | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/12   | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/13   | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/2    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/3    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/4    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/5    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/6    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/7    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/8    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/9    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/1    | down  | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/10   | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/11   | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/12   | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/13   | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/2    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/3    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/4    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/5    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/6    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/7    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/8    | up    | trunk | 3735,3736                                              | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/9    | up    | trunk | 3735,3736                                              | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+--------------------------------------------------------+
| Infra-L3_PolGrp           | Infra_AAEP      | Infra_VlanPool      | [1-1000] (static)     | bl2205-eu-spdc | eth1/25   | up    | trunk |                                                        | 
|                           |                 |                     |                       | bl2206-eu-spdc | eth1/25   | up    | trunk |                                                        | 
|                           |                 |                     |                       | cl2201-eu-spdc | eth1/25   | down  | trunk |                                                        | 
|                           |                 |                     |                       | cl2202-eu-spdc | eth1/25   | down  | trunk |                                                        | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+--------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2207-eu-spdc | eth1/3/3  | up    | trunk | 808                                                    | 
|                           |                 |                     | [810-813] (static)    | cl2207-eu-spdc | eth1/3/4  | up    | trunk | 808                                                    | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/4/1  | up    | trunk | 808                                                    | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/4/2  | up    | trunk | 808                                                    | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/4/3  | up    | trunk | 808                                                    | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/5/3  | up    | trunk | 807                                                    | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/5/4  | up    | trunk | 807                                                    | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/6/1  | up    | trunk | 807                                                    | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/6/2  | up    | trunk | 807                                                    | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/6/3  | up    | trunk | 807                                                    | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+--------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2207-eu-spdc | eth1/3/1  | up    | trunk | 808                                                    | 
|                           |                 |                     | [810-813] (static)    | cl2207-eu-spdc | eth1/3/2  | up    | trunk | 808                                                    | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/5/1  | up    | trunk | 807                                                    | 
|                           |                 |                     |                       | cl2207-eu-spdc | eth1/5/2  | up    | trunk | 807                                                    | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+--------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2208-eu-spdc | eth1/3/3  | up    | trunk | 808                                                    | 
|                           |                 |                     | [810-813] (static)    | cl2208-eu-spdc | eth1/3/4  | up    | trunk | 808                                                    | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/4/1  | up    | trunk | 808                                                    | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/4/2  | up    | trunk | 808                                                    | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/4/3  | up    | trunk | 808                                                    | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/5/3  | up    | trunk | 807                                                    | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/5/4  | up    | trunk | 807                                                    | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/6/1  | up    | trunk | 807                                                    | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/6/2  | up    | trunk | 807                                                    | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/6/3  | down  | trunk | 807                                                    | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+--------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | k8s_phys_AAEP   | k8s_phys_VlanPool   | [800-809] (static)    | cl2208-eu-spdc | eth1/3/1  | up    | trunk | 808                                                    | 
|                           |                 |                     | [810-813] (static)    | cl2208-eu-spdc | eth1/3/2  | up    | trunk | 808                                                    | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/5/1  | up    | trunk | 807                                                    | 
|                           |                 |                     |                       | cl2208-eu-spdc | eth1/5/2  | up    | trunk | 807                                                    | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+--------------------------------------------------------+
| nidemo-bare-metal         | nidemo          | nidemo-3000-3001    | [3000-3001] (static)  | rl2701-eu-spdc | eth1/19   | down  | trunk |                                                        | 
|                           |                 |                     |                       | rl2701-eu-spdc | eth1/20   | down  | trunk |                                                        | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/19   | down  | trunk | 3000                                                   | 
|                           |                 |                     |                       | rl2702-eu-spdc | eth1/20   | down  | trunk |                                                        | 
+---------------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+--------------------------------------------------------+

Policy Group - Access Interface Port - Faults [#0]
--------------------------------------------------
None

Policy Group - Access Interface Port - Fault Records last 10y [#0]
------------------------------------------------------------------
None

Policy Group - Access Interface Port - Event Logs last 10y [#1]
---------------------------------------------------------------

+--------------------------+------+----------+------------+-------------------------------+-----------------------+-------------------------------------------------------------------------+
| PG Name                  | Sev  | Code     | Cause      | Created Time                  | Description           | Change Set                                                              |
+--------------------------+------+----------+------------+-------------------------------+-----------------------+-------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp | Info | E4214324 | transition | 2023-06-18T01:02:31.456+02:00 | RsQosDppIfPol created | forceResolve:yes, rType:mo, state:formed, stateQual:default-target,     | 
|                          |      |          |            |                               |                       | tCl:qosDppPol, tDn:uni/infra/qosdpppol-default, tRn:qosdpppol-default,  | 
|                          |      |          |            |                               |                       | tType:name, userdom:all                                                 | 
+--------------------------+------+----------+------------+-------------------------------+-----------------------+-------------------------------------------------------------------------+

Policy Group - Access Interface Port - Audit Logs last 10y [#309]
-----------------------------------------------------------------

+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| PG Name                   | Sev  | Code     | Cause      | Created Time                  | Description                                  | Change Set                                                                       |
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214301 | transition | 2022-07-06T15:23:16.780+02:00 | RsL2IfPol modified                           | tnL2IfPolName (Old: L2-local, New: L2-local_Pol)                                 | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214295 | transition | 2022-07-06T15:23:16.779+02:00 | RsHIfPol modified                            | tnFabricHIfPolName (Old: , New: Inherit)                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4212195 | transition | 2022-07-06T15:23:16.779+02:00 | AccPortGrp ESX-CDC-22_PolGrp modified        | descr (Old: , New: ACI2 CL2201-2202 to ESX2-13 Policy Group (Created by          | 
|                           |      |          |            |                               |                                              | Ansible))                                                                        | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214295 | transition | 2021-12-17T12:25:49.628+02:00 | RsHIfPol modified                            | tnFabricHIfPolName (Old: 10G-fix, New: )                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214276 | transition | 2021-10-18T19:08:45.420+02:00 | RsAttEntP created                            | tDn:uni/infra/attentp-ESX-CDC-22_AAEP, userdom::all:common:                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214330 | transition | 2021-10-18T19:08:45.420+02:00 | RsQosIngressDppIfPol created                 | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4218184 | transition | 2021-10-18T19:08:45.420+02:00 | RsSynceEthIfPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4218086 | transition | 2021-10-18T19:08:45.420+02:00 | RsQosLlfcIfPol created                       | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214348 | transition | 2021-10-18T19:08:45.420+02:00 | RsStpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214333 | transition | 2021-10-18T19:08:45.420+02:00 | RsQosPfcIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214336 | transition | 2021-10-18T19:08:45.420+02:00 | RsQosSdIfPol created                         | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214345 | transition | 2021-10-18T19:08:45.420+02:00 | RsStormctrlIfPol created                     | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214327 | transition | 2021-10-18T19:08:45.419+02:00 | RsQosEgressDppIfPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214324 | transition | 2021-10-18T19:08:45.419+02:00 | RsQosDppIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214315 | transition | 2021-10-18T19:08:45.419+02:00 | RsMcpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214967 | transition | 2021-10-18T19:08:45.419+02:00 | RsMacsecIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214318 | transition | 2021-10-18T19:08:45.419+02:00 | RsMonIfInfraPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4217527 | transition | 2021-10-18T19:08:45.418+02:00 | RsLinkFlapPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214294 | transition | 2021-10-18T19:08:45.418+02:00 | RsHIfPol created                             | tnFabricHIfPolName:10G-fix, userdom:all                                          | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214964 | transition | 2021-10-18T19:08:45.418+02:00 | RsL2PortAuthPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214306 | transition | 2021-10-18T19:08:45.418+02:00 | RsL2PortSecurityPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214300 | transition | 2021-10-18T19:08:45.418+02:00 | RsL2IfPol created                            | tnL2IfPolName:L2-local, userdom:all                                              | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214312 | transition | 2021-10-18T19:08:45.418+02:00 | RsLldpIfPol created                          | tnLldpIfPolName:LLDP-enable, userdom:all                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214279 | transition | 2021-10-18T19:08:45.417+02:00 | RsCdpIfPol created                           | tnCdpIfPolName:CDP-enable, userdom:all                                           | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4215159 | transition | 2021-10-18T19:08:45.417+02:00 | RsDwdmIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214288 | transition | 2021-10-18T19:08:45.417+02:00 | RsFcIfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4214961 | transition | 2021-10-18T19:08:45.417+02:00 | RsCoppIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-CDC-22_PolGrp         | Info | E4212194 | transition | 2021-10-18T19:08:45.416+02:00 | AccPortGrp ESX-CDC-22_PolGrp created         | name:ESX-CDC-22_PolGrp, userdom::all:common:                                     | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4218184 | transition | 2022-07-06T15:23:18.304+02:00 | RsSynceEthIfPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214348 | transition | 2022-07-06T15:23:18.304+02:00 | RsStpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214276 | transition | 2022-07-06T15:23:18.304+02:00 | RsAttEntP created                            | tDn:uni/infra/attentp-ESX-R7DC_AAEP, userdom::all:common:                        | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214330 | transition | 2022-07-06T15:23:18.303+02:00 | RsQosIngressDppIfPol created                 | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4218086 | transition | 2022-07-06T15:23:18.303+02:00 | RsQosLlfcIfPol created                       | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214336 | transition | 2022-07-06T15:23:18.303+02:00 | RsQosSdIfPol created                         | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214327 | transition | 2022-07-06T15:23:18.303+02:00 | RsQosEgressDppIfPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214333 | transition | 2022-07-06T15:23:18.303+02:00 | RsQosPfcIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214345 | transition | 2022-07-06T15:23:18.303+02:00 | RsStormctrlIfPol created                     | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4217527 | transition | 2022-07-06T15:23:18.302+02:00 | RsLinkFlapPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214324 | transition | 2022-07-06T15:23:18.302+02:00 | RsQosDppIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214318 | transition | 2022-07-06T15:23:18.302+02:00 | RsMonIfInfraPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214967 | transition | 2022-07-06T15:23:18.302+02:00 | RsMacsecIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214312 | transition | 2022-07-06T15:23:18.302+02:00 | RsLldpIfPol created                          | tnLldpIfPolName:LLDP-enable, userdom:all                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214315 | transition | 2022-07-06T15:23:18.302+02:00 | RsMcpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214294 | transition | 2022-07-06T15:23:18.301+02:00 | RsHIfPol created                             | tnFabricHIfPolName:Inherit, userdom:all                                          | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214288 | transition | 2022-07-06T15:23:18.301+02:00 | RsFcIfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4215159 | transition | 2022-07-06T15:23:18.301+02:00 | RsDwdmIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214306 | transition | 2022-07-06T15:23:18.301+02:00 | RsL2PortSecurityPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214964 | transition | 2022-07-06T15:23:18.301+02:00 | RsL2PortAuthPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214300 | transition | 2022-07-06T15:23:18.301+02:00 | RsL2IfPol created                            | tnL2IfPolName:L2-local_Pol, userdom:all                                          | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214961 | transition | 2022-07-06T15:23:18.300+02:00 | RsCoppIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4212194 | transition | 2022-07-06T15:23:18.300+02:00 | AccPortGrp ESX-R7DC_PolGrp created           | descr:ACI2 RL2701-2702 to ESX2-13 Policy Group (Created by Ansible),             | 
|                           |      |          |            |                               |                                              | name:ESX-R7DC_PolGrp, userdom::all:common:                                       | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| ESX-R7DC_PolGrp           | Info | E4214279 | transition | 2022-07-06T15:23:18.300+02:00 | RsCdpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| Infra-L3_PolGrp           | Info | E4214301 | transition | 2022-07-08T16:21:22.109+02:00 | RsL2IfPol modified                           | tnL2IfPolName (Old: L2-local, New: L2-local_Pol)                                 | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| Infra-L3_PolGrp           | Info | E4212195 | transition | 2022-07-08T16:21:22.108+02:00 | AccPortGrp Infra-L3_PolGrp modified          | descr (Old: , New: ACI2 to IPN Infra Policy Group for Routed subnets (Created    | 
|                           |      |          |            |                               |                                              | by Ansible))                                                                     | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| Infra-L3_PolGrp           | Info | E4214295 | transition | 2022-07-08T16:21:22.108+02:00 | RsHIfPol modified                            | tnFabricHIfPolName (Old: , New: Inherit)                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214965 | transition | 2023-05-29T09:08:53.142+02:00 | RsL2PortAuthPol modified                     | tnL2PortAuthPolName (Old: , New: default)                                        | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214276 | transition | 2023-04-05T23:37:55.913+02:00 | RsAttEntP created                            | annotation:orchestrator:terraform, tDn:uni/infra/attentp-k8s_phys_AAEP,          | 
|                           |      |          |            |                               |                                              | userdom::all:common:                                                             | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214301 | transition | 2023-04-05T23:37:55.779+02:00 | RsL2IfPol modified                           | annotation (Old: , New: orchestrator:terraform), tnL2IfPolName (Old: , New:      | 
|                           |      |          |            |                               |                                              | k8s_l2_local)                                                                    | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214280 | transition | 2023-04-05T23:37:55.651+02:00 | RsCdpIfPol modified                          | annotation (Old: , New: orchestrator:terraform), tnCdpIfPolName (Old: , New:     | 
|                           |      |          |            |                               |                                              | k8s_cdp_enable)                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214295 | transition | 2023-04-05T23:37:55.498+02:00 | RsHIfPol modified                            | annotation (Old: , New: orchestrator:terraform), tnFabricHIfPolName (Old: ,      | 
|                           |      |          |            |                               |                                              | New: k8s_default)                                                                | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214313 | transition | 2023-04-05T23:37:55.343+02:00 | RsLldpIfPol modified                         | annotation (Old: , New: orchestrator:terraform), tnLldpIfPolName (Old: , New:    | 
|                           |      |          |            |                               |                                              | k8s_lldp_enable)                                                                 | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4218184 | transition | 2023-04-05T23:37:53.562+02:00 | RsSynceEthIfPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214345 | transition | 2023-04-05T23:37:53.562+02:00 | RsStormctrlIfPol created                     | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214348 | transition | 2023-04-05T23:37:53.562+02:00 | RsStpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214336 | transition | 2023-04-05T23:37:53.561+02:00 | RsQosSdIfPol created                         | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214324 | transition | 2023-04-05T23:37:53.561+02:00 | RsQosDppIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214333 | transition | 2023-04-05T23:37:53.561+02:00 | RsQosPfcIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4218086 | transition | 2023-04-05T23:37:53.561+02:00 | RsQosLlfcIfPol created                       | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214315 | transition | 2023-04-05T23:37:53.561+02:00 | RsMcpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214318 | transition | 2023-04-05T23:37:53.561+02:00 | RsMonIfInfraPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214330 | transition | 2023-04-05T23:37:53.561+02:00 | RsQosIngressDppIfPol created                 | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214327 | transition | 2023-04-05T23:37:53.561+02:00 | RsQosEgressDppIfPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214964 | transition | 2023-04-05T23:37:53.560+02:00 | RsL2PortAuthPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214300 | transition | 2023-04-05T23:37:53.560+02:00 | RsL2IfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214288 | transition | 2023-04-05T23:37:53.560+02:00 | RsFcIfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4217527 | transition | 2023-04-05T23:37:53.560+02:00 | RsLinkFlapPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214967 | transition | 2023-04-05T23:37:53.560+02:00 | RsMacsecIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214306 | transition | 2023-04-05T23:37:53.560+02:00 | RsL2PortSecurityPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214312 | transition | 2023-04-05T23:37:53.560+02:00 | RsLldpIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214294 | transition | 2023-04-05T23:37:53.560+02:00 | RsHIfPol created                             | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4212194 | transition | 2023-04-05T23:37:53.559+02:00 | AccPortGrp k8s_sriov_2207_bm_PolGrp created  | annotation:orchestrator:terraform, descr:k8s_sriov_bm Access Policy,             | 
|                           |      |          |            |                               |                                              | name:k8s_sriov_2207_bm_PolGrp, nameAlias:kali, userdom::all:common:              | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214961 | transition | 2023-04-05T23:37:53.559+02:00 | RsCoppIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4214279 | transition | 2023-04-05T23:37:53.559+02:00 | RsCdpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_bm_PolGrp  | Info | E4215159 | transition | 2023-04-05T23:37:53.559+02:00 | RsDwdmIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214276 | transition | 2023-04-05T23:37:56.061+02:00 | RsAttEntP created                            | annotation:orchestrator:terraform, tDn:uni/infra/attentp-k8s_phys_AAEP,          | 
|                           |      |          |            |                               |                                              | userdom::all:common:                                                             | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214301 | transition | 2023-04-05T23:37:55.885+02:00 | RsL2IfPol modified                           | annotation (Old: , New: orchestrator:terraform), tnL2IfPolName (Old: , New:      | 
|                           |      |          |            |                               |                                              | k8s_l2_local)                                                                    | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214280 | transition | 2023-04-05T23:37:55.753+02:00 | RsCdpIfPol modified                          | annotation (Old: , New: orchestrator:terraform), tnCdpIfPolName (Old: , New:     | 
|                           |      |          |            |                               |                                              | k8s_cdp_enable)                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214295 | transition | 2023-04-05T23:37:55.600+02:00 | RsHIfPol modified                            | annotation (Old: , New: orchestrator:terraform), tnFabricHIfPolName (Old: ,      | 
|                           |      |          |            |                               |                                              | New: k8s_default)                                                                | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214313 | transition | 2023-04-05T23:37:55.459+02:00 | RsLldpIfPol modified                         | annotation (Old: , New: orchestrator:terraform), tnLldpIfPolName (Old: , New:    | 
|                           |      |          |            |                               |                                              | k8s_lldp_enable)                                                                 | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4218086 | transition | 2023-04-05T23:37:53.585+02:00 | RsQosLlfcIfPol created                       | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214336 | transition | 2023-04-05T23:37:53.585+02:00 | RsQosSdIfPol created                         | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4218184 | transition | 2023-04-05T23:37:53.585+02:00 | RsSynceEthIfPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214333 | transition | 2023-04-05T23:37:53.585+02:00 | RsQosPfcIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214348 | transition | 2023-04-05T23:37:53.585+02:00 | RsStpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214345 | transition | 2023-04-05T23:37:53.585+02:00 | RsStormctrlIfPol created                     | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214330 | transition | 2023-04-05T23:37:53.584+02:00 | RsQosIngressDppIfPol created                 | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214315 | transition | 2023-04-05T23:37:53.584+02:00 | RsMcpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214967 | transition | 2023-04-05T23:37:53.584+02:00 | RsMacsecIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4217527 | transition | 2023-04-05T23:37:53.584+02:00 | RsLinkFlapPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214327 | transition | 2023-04-05T23:37:53.584+02:00 | RsQosEgressDppIfPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214318 | transition | 2023-04-05T23:37:53.584+02:00 | RsMonIfInfraPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214312 | transition | 2023-04-05T23:37:53.584+02:00 | RsLldpIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214324 | transition | 2023-04-05T23:37:53.584+02:00 | RsQosDppIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214294 | transition | 2023-04-05T23:37:53.583+02:00 | RsHIfPol created                             | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214300 | transition | 2023-04-05T23:37:53.583+02:00 | RsL2IfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214288 | transition | 2023-04-05T23:37:53.583+02:00 | RsFcIfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214279 | transition | 2023-04-05T23:37:53.583+02:00 | RsCdpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214961 | transition | 2023-04-05T23:37:53.583+02:00 | RsCoppIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214964 | transition | 2023-04-05T23:37:53.583+02:00 | RsL2PortAuthPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4215159 | transition | 2023-04-05T23:37:53.583+02:00 | RsDwdmIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4214306 | transition | 2023-04-05T23:37:53.583+02:00 | RsL2PortSecurityPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2207_esx_PolGrp | Info | E4212194 | transition | 2023-04-05T23:37:53.582+02:00 | AccPortGrp k8s_sriov_2207_esx_PolGrp created | annotation:orchestrator:terraform, descr:k8s_sriov_esx Access Policy,            | 
|                           |      |          |            |                               |                                              | name:k8s_sriov_2207_esx_PolGrp, nameAlias:kali, userdom::all:common:             | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214276 | transition | 2023-04-05T23:37:55.844+02:00 | RsAttEntP created                            | annotation:orchestrator:terraform, tDn:uni/infra/attentp-k8s_phys_AAEP,          | 
|                           |      |          |            |                               |                                              | userdom::all:common:                                                             | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214301 | transition | 2023-04-05T23:37:55.710+02:00 | RsL2IfPol modified                           | annotation (Old: , New: orchestrator:terraform), tnL2IfPolName (Old: , New:      | 
|                           |      |          |            |                               |                                              | k8s_l2_local)                                                                    | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214280 | transition | 2023-04-05T23:37:55.526+02:00 | RsCdpIfPol modified                          | annotation (Old: , New: orchestrator:terraform), tnCdpIfPolName (Old: , New:     | 
|                           |      |          |            |                               |                                              | k8s_cdp_enable)                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214295 | transition | 2023-04-05T23:37:55.382+02:00 | RsHIfPol modified                            | annotation (Old: , New: orchestrator:terraform), tnFabricHIfPolName (Old: ,      | 
|                           |      |          |            |                               |                                              | New: k8s_default)                                                                | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214313 | transition | 2023-04-05T23:37:55.172+02:00 | RsLldpIfPol modified                         | annotation (Old: , New: orchestrator:terraform), tnLldpIfPolName (Old: , New:    | 
|                           |      |          |            |                               |                                              | k8s_lldp_enable)                                                                 | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214348 | transition | 2023-04-05T23:37:53.548+02:00 | RsStpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4218184 | transition | 2023-04-05T23:37:53.548+02:00 | RsSynceEthIfPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214333 | transition | 2023-04-05T23:37:53.547+02:00 | RsQosPfcIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214327 | transition | 2023-04-05T23:37:53.547+02:00 | RsQosEgressDppIfPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214330 | transition | 2023-04-05T23:37:53.547+02:00 | RsQosIngressDppIfPol created                 | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214336 | transition | 2023-04-05T23:37:53.547+02:00 | RsQosSdIfPol created                         | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4218086 | transition | 2023-04-05T23:37:53.547+02:00 | RsQosLlfcIfPol created                       | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214345 | transition | 2023-04-05T23:37:53.547+02:00 | RsStormctrlIfPol created                     | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214967 | transition | 2023-04-05T23:37:53.546+02:00 | RsMacsecIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4217527 | transition | 2023-04-05T23:37:53.546+02:00 | RsLinkFlapPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214315 | transition | 2023-04-05T23:37:53.546+02:00 | RsMcpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214324 | transition | 2023-04-05T23:37:53.546+02:00 | RsQosDppIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214318 | transition | 2023-04-05T23:37:53.546+02:00 | RsMonIfInfraPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214312 | transition | 2023-04-05T23:37:53.546+02:00 | RsLldpIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214294 | transition | 2023-04-05T23:37:53.545+02:00 | RsHIfPol created                             | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214300 | transition | 2023-04-05T23:37:53.545+02:00 | RsL2IfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214964 | transition | 2023-04-05T23:37:53.545+02:00 | RsL2PortAuthPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214288 | transition | 2023-04-05T23:37:53.545+02:00 | RsFcIfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214306 | transition | 2023-04-05T23:37:53.545+02:00 | RsL2PortSecurityPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4215159 | transition | 2023-04-05T23:37:53.545+02:00 | RsDwdmIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214279 | transition | 2023-04-05T23:37:53.544+02:00 | RsCdpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4214961 | transition | 2023-04-05T23:37:53.544+02:00 | RsCoppIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_bm_PolGrp  | Info | E4212194 | transition | 2023-04-05T23:37:53.544+02:00 | AccPortGrp k8s_sriov_2208_bm_PolGrp created  | annotation:orchestrator:terraform, descr:k8s_sriov_bm Access Policy,             | 
|                           |      |          |            |                               |                                              | name:k8s_sriov_2208_bm_PolGrp, nameAlias:kali, userdom::all:common:              | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214276 | transition | 2023-04-05T23:37:56.900+02:00 | RsAttEntP created                            | annotation:orchestrator:terraform, tDn:uni/infra/attentp-k8s_phys_AAEP,          | 
|                           |      |          |            |                               |                                              | userdom::all:common:                                                             | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214301 | transition | 2023-04-05T23:37:56.792+02:00 | RsL2IfPol modified                           | annotation (Old: , New: orchestrator:terraform), tnL2IfPolName (Old: , New:      | 
|                           |      |          |            |                               |                                              | k8s_l2_local)                                                                    | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214280 | transition | 2023-04-05T23:37:56.668+02:00 | RsCdpIfPol modified                          | annotation (Old: , New: orchestrator:terraform), tnCdpIfPolName (Old: , New:     | 
|                           |      |          |            |                               |                                              | k8s_cdp_enable)                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214295 | transition | 2023-04-05T23:37:56.509+02:00 | RsHIfPol modified                            | annotation (Old: , New: orchestrator:terraform), tnFabricHIfPolName (Old: ,      | 
|                           |      |          |            |                               |                                              | New: k8s_default)                                                                | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214313 | transition | 2023-04-05T23:37:56.411+02:00 | RsLldpIfPol modified                         | annotation (Old: , New: orchestrator:terraform), tnLldpIfPolName (Old: , New:    | 
|                           |      |          |            |                               |                                              | k8s_lldp_enable)                                                                 | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214348 | transition | 2023-04-05T23:37:53.574+02:00 | RsStpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4218184 | transition | 2023-04-05T23:37:53.574+02:00 | RsSynceEthIfPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214327 | transition | 2023-04-05T23:37:53.573+02:00 | RsQosEgressDppIfPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214333 | transition | 2023-04-05T23:37:53.573+02:00 | RsQosPfcIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214330 | transition | 2023-04-05T23:37:53.573+02:00 | RsQosIngressDppIfPol created                 | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4218086 | transition | 2023-04-05T23:37:53.573+02:00 | RsQosLlfcIfPol created                       | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214318 | transition | 2023-04-05T23:37:53.573+02:00 | RsMonIfInfraPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214336 | transition | 2023-04-05T23:37:53.573+02:00 | RsQosSdIfPol created                         | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214345 | transition | 2023-04-05T23:37:53.573+02:00 | RsStormctrlIfPol created                     | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214324 | transition | 2023-04-05T23:37:53.573+02:00 | RsQosDppIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214312 | transition | 2023-04-05T23:37:53.572+02:00 | RsLldpIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214288 | transition | 2023-04-05T23:37:53.572+02:00 | RsFcIfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214967 | transition | 2023-04-05T23:37:53.572+02:00 | RsMacsecIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4217527 | transition | 2023-04-05T23:37:53.572+02:00 | RsLinkFlapPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214306 | transition | 2023-04-05T23:37:53.572+02:00 | RsL2PortSecurityPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214300 | transition | 2023-04-05T23:37:53.572+02:00 | RsL2IfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214294 | transition | 2023-04-05T23:37:53.572+02:00 | RsHIfPol created                             | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214315 | transition | 2023-04-05T23:37:53.572+02:00 | RsMcpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214964 | transition | 2023-04-05T23:37:53.572+02:00 | RsL2PortAuthPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214961 | transition | 2023-04-05T23:37:53.571+02:00 | RsCoppIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4214279 | transition | 2023-04-05T23:37:53.571+02:00 | RsCdpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4215159 | transition | 2023-04-05T23:37:53.571+02:00 | RsDwdmIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| k8s_sriov_2208_esx_PolGrp | Info | E4212194 | transition | 2023-04-05T23:37:53.571+02:00 | AccPortGrp k8s_sriov_2208_esx_PolGrp created | annotation:orchestrator:terraform, descr:k8s_sriov_esx Access Policy,            | 
|                           |      |          |            |                               |                                              | name:k8s_sriov_2208_esx_PolGrp, nameAlias:kali, userdom::all:common:             | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214276 | transition | 2023-03-06T19:40:31.770+02:00 | RsAttEntP created                            | annotation:orchestrator:terraform, tDn:uni/infra/attentp-nidemo,                 | 
|                           |      |          |            |                               |                                              | userdom::all:common:                                                             | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214295 | transition | 2023-03-06T19:40:31.639+02:00 | RsHIfPol modified                            | annotation (Old: , New: orchestrator:terraform), tnFabricHIfPolName (Old: ,      | 
|                           |      |          |            |                               |                                              | New: 10G-auto)                                                                   | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214313 | transition | 2023-03-06T19:40:31.533+02:00 | RsLldpIfPol modified                         | annotation (Old: , New: orchestrator:terraform), tnLldpIfPolName (Old: , New:    | 
|                           |      |          |            |                               |                                              | LLDP-enable)                                                                     | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214348 | transition | 2023-03-06T19:40:30.235+02:00 | RsStpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4218184 | transition | 2023-03-06T19:40:30.235+02:00 | RsSynceEthIfPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214345 | transition | 2023-03-06T19:40:30.235+02:00 | RsStormctrlIfPol created                     | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214330 | transition | 2023-03-06T19:40:30.234+02:00 | RsQosIngressDppIfPol created                 | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214336 | transition | 2023-03-06T19:40:30.234+02:00 | RsQosSdIfPol created                         | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214327 | transition | 2023-03-06T19:40:30.234+02:00 | RsQosEgressDppIfPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214333 | transition | 2023-03-06T19:40:30.234+02:00 | RsQosPfcIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4218086 | transition | 2023-03-06T19:40:30.234+02:00 | RsQosLlfcIfPol created                       | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214324 | transition | 2023-03-06T19:40:30.234+02:00 | RsQosDppIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4217527 | transition | 2023-03-06T19:40:30.233+02:00 | RsLinkFlapPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214318 | transition | 2023-03-06T19:40:30.233+02:00 | RsMonIfInfraPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214315 | transition | 2023-03-06T19:40:30.233+02:00 | RsMcpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214306 | transition | 2023-03-06T19:40:30.233+02:00 | RsL2PortSecurityPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214967 | transition | 2023-03-06T19:40:30.233+02:00 | RsMacsecIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214312 | transition | 2023-03-06T19:40:30.233+02:00 | RsLldpIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214961 | transition | 2023-03-06T19:40:30.232+02:00 | RsCoppIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214964 | transition | 2023-03-06T19:40:30.232+02:00 | RsL2PortAuthPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214288 | transition | 2023-03-06T19:40:30.232+02:00 | RsFcIfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4215159 | transition | 2023-03-06T19:40:30.232+02:00 | RsDwdmIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214294 | transition | 2023-03-06T19:40:30.232+02:00 | RsHIfPol created                             | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214300 | transition | 2023-03-06T19:40:30.232+02:00 | RsL2IfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4212194 | transition | 2023-03-06T19:40:30.231+02:00 | AccPortGrp nidemo-bare-metal created         | annotation:orchestrator:terraform, descr:VANNIEW temporary demo feel free to     | 
|                           |      |          |            |                               |                                              | destroy, name:nidemo-bare-metal, userdom::all:common:                            | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214279 | transition | 2023-03-06T19:40:30.231+02:00 | RsCdpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214350 | transition | 2023-03-06T19:39:54.431+02:00 | RsStpIfPol deleted                           |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214347 | transition | 2023-03-06T19:39:54.431+02:00 | RsStormctrlIfPol deleted                     |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4218186 | transition | 2023-03-06T19:39:54.431+02:00 | RsSynceEthIfPol deleted                      |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214338 | transition | 2023-03-06T19:39:54.431+02:00 | RsQosSdIfPol deleted                         |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4218088 | transition | 2023-03-06T19:39:54.430+02:00 | RsQosLlfcIfPol deleted                       |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214332 | transition | 2023-03-06T19:39:54.430+02:00 | RsQosIngressDppIfPol deleted                 |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214335 | transition | 2023-03-06T19:39:54.430+02:00 | RsQosPfcIfPol deleted                        |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214320 | transition | 2023-03-06T19:39:54.429+02:00 | RsMonIfInfraPol deleted                      |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214326 | transition | 2023-03-06T19:39:54.429+02:00 | RsQosDppIfPol deleted                        |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214329 | transition | 2023-03-06T19:39:54.429+02:00 | RsQosEgressDppIfPol deleted                  |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214314 | transition | 2023-03-06T19:39:54.428+02:00 | RsLldpIfPol deleted                          |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214969 | transition | 2023-03-06T19:39:54.428+02:00 | RsMacsecIfPol deleted                        |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214317 | transition | 2023-03-06T19:39:54.428+02:00 | RsMcpIfPol deleted                           |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4217529 | transition | 2023-03-06T19:39:54.427+02:00 | RsLinkFlapPol deleted                        |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214308 | transition | 2023-03-06T19:39:54.427+02:00 | RsL2PortSecurityPol deleted                  |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214966 | transition | 2023-03-06T19:39:54.427+02:00 | RsL2PortAuthPol deleted                      |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214302 | transition | 2023-03-06T19:39:54.426+02:00 | RsL2IfPol deleted                            |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214296 | transition | 2023-03-06T19:39:54.426+02:00 | RsHIfPol deleted                             |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214290 | transition | 2023-03-06T19:39:54.426+02:00 | RsFcIfPol deleted                            |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214963 | transition | 2023-03-06T19:39:54.425+02:00 | RsCoppIfPol deleted                          |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4215161 | transition | 2023-03-06T19:39:54.425+02:00 | RsDwdmIfPol deleted                          |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214278 | transition | 2023-03-06T19:39:54.424+02:00 | RsAttEntP deleted                            |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214281 | transition | 2023-03-06T19:39:54.424+02:00 | RsCdpIfPol deleted                           |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4212196 | transition | 2023-03-06T19:39:54.423+02:00 | AccPortGrp nidemo-bare-metal deleted         |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214276 | transition | 2023-03-06T19:33:34.739+02:00 | RsAttEntP created                            | tDn:uni/infra/attentp-nidemo, userdom::all:common:                               | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214295 | transition | 2023-03-06T19:27:38.949+02:00 | RsHIfPol modified                            | annotation (Old: , New: orchestrator:terraform), tnFabricHIfPolName (Old: ,      | 
|                           |      |          |            |                               |                                              | New: 10G-auto)                                                                   | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214313 | transition | 2023-03-06T19:27:38.867+02:00 | RsLldpIfPol modified                         | annotation (Old: , New: orchestrator:terraform), tnLldpIfPolName (Old: , New:    | 
|                           |      |          |            |                               |                                              | LLDP-enable)                                                                     | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214345 | transition | 2023-03-06T19:27:37.602+02:00 | RsStormctrlIfPol created                     | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214348 | transition | 2023-03-06T19:27:37.602+02:00 | RsStpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4218184 | transition | 2023-03-06T19:27:37.602+02:00 | RsSynceEthIfPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214336 | transition | 2023-03-06T19:27:37.602+02:00 | RsQosSdIfPol created                         | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214318 | transition | 2023-03-06T19:27:37.601+02:00 | RsMonIfInfraPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4218086 | transition | 2023-03-06T19:27:37.601+02:00 | RsQosLlfcIfPol created                       | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214327 | transition | 2023-03-06T19:27:37.601+02:00 | RsQosEgressDppIfPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214324 | transition | 2023-03-06T19:27:37.601+02:00 | RsQosDppIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214330 | transition | 2023-03-06T19:27:37.601+02:00 | RsQosIngressDppIfPol created                 | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214333 | transition | 2023-03-06T19:27:37.601+02:00 | RsQosPfcIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214964 | transition | 2023-03-06T19:27:37.600+02:00 | RsL2PortAuthPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214312 | transition | 2023-03-06T19:27:37.600+02:00 | RsLldpIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4217527 | transition | 2023-03-06T19:27:37.600+02:00 | RsLinkFlapPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214315 | transition | 2023-03-06T19:27:37.600+02:00 | RsMcpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214306 | transition | 2023-03-06T19:27:37.600+02:00 | RsL2PortSecurityPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214967 | transition | 2023-03-06T19:27:37.600+02:00 | RsMacsecIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214279 | transition | 2023-03-06T19:27:37.599+02:00 | RsCdpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214300 | transition | 2023-03-06T19:27:37.599+02:00 | RsL2IfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214961 | transition | 2023-03-06T19:27:37.599+02:00 | RsCoppIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214288 | transition | 2023-03-06T19:27:37.599+02:00 | RsFcIfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4215159 | transition | 2023-03-06T19:27:37.599+02:00 | RsDwdmIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214294 | transition | 2023-03-06T19:27:37.599+02:00 | RsHIfPol created                             | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4212194 | transition | 2023-03-06T19:27:37.598+02:00 | AccPortGrp nidemo-bare-metal created         | annotation:orchestrator:terraform, descr:VANNIEW temporary demo feel free to     | 
|                           |      |          |            |                               |                                              | destroy, name:nidemo-bare-metal, userdom::all:common:                            | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4218186 | transition | 2023-03-06T19:27:37.517+02:00 | RsSynceEthIfPol deleted                      |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214347 | transition | 2023-03-06T19:27:37.516+02:00 | RsStormctrlIfPol deleted                     |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214335 | transition | 2023-03-06T19:27:37.516+02:00 | RsQosPfcIfPol deleted                        |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214338 | transition | 2023-03-06T19:27:37.516+02:00 | RsQosSdIfPol deleted                         |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214350 | transition | 2023-03-06T19:27:37.516+02:00 | RsStpIfPol deleted                           |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214332 | transition | 2023-03-06T19:27:37.515+02:00 | RsQosIngressDppIfPol deleted                 |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4218088 | transition | 2023-03-06T19:27:37.515+02:00 | RsQosLlfcIfPol deleted                       |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214320 | transition | 2023-03-06T19:27:37.514+02:00 | RsMonIfInfraPol deleted                      |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214326 | transition | 2023-03-06T19:27:37.514+02:00 | RsQosDppIfPol deleted                        |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214329 | transition | 2023-03-06T19:27:37.514+02:00 | RsQosEgressDppIfPol deleted                  |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214317 | transition | 2023-03-06T19:27:37.513+02:00 | RsMcpIfPol deleted                           |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214314 | transition | 2023-03-06T19:27:37.513+02:00 | RsLldpIfPol deleted                          |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214969 | transition | 2023-03-06T19:27:37.513+02:00 | RsMacsecIfPol deleted                        |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214308 | transition | 2023-03-06T19:27:37.512+02:00 | RsL2PortSecurityPol deleted                  |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4217529 | transition | 2023-03-06T19:27:37.512+02:00 | RsLinkFlapPol deleted                        |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214296 | transition | 2023-03-06T19:27:37.511+02:00 | RsHIfPol deleted                             |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214966 | transition | 2023-03-06T19:27:37.511+02:00 | RsL2PortAuthPol deleted                      |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214302 | transition | 2023-03-06T19:27:37.511+02:00 | RsL2IfPol deleted                            |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214290 | transition | 2023-03-06T19:27:37.510+02:00 | RsFcIfPol deleted                            |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4215161 | transition | 2023-03-06T19:27:37.510+02:00 | RsDwdmIfPol deleted                          |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214281 | transition | 2023-03-06T19:27:37.509+02:00 | RsCdpIfPol deleted                           |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214963 | transition | 2023-03-06T19:27:37.509+02:00 | RsCoppIfPol deleted                          |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4212196 | transition | 2023-03-06T19:27:37.508+02:00 | AccPortGrp nidemo-bare-metal deleted         |                                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214328 | transition | 2023-03-06T19:17:22.667+02:00 | RsQosEgressDppIfPol modified                 | annotation (Old: , New: orchestrator:terraform), tnQosDppPolName (Old: , New:    | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214349 | transition | 2023-03-06T19:17:22.514+02:00 | RsStpIfPol modified                          | annotation (Old: , New: orchestrator:terraform), tnStpIfPolName (Old: , New:     | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214301 | transition | 2023-03-06T19:17:22.412+02:00 | RsL2IfPol modified                           | annotation (Old: , New: orchestrator:terraform), tnL2IfPolName (Old: , New:      | 
|                           |      |          |            |                               |                                              | L2-global)                                                                       | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214280 | transition | 2023-03-06T19:17:22.290+02:00 | RsCdpIfPol modified                          | annotation (Old: , New: orchestrator:terraform), tnCdpIfPolName (Old: , New:     | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214331 | transition | 2023-03-06T19:17:22.181+02:00 | RsQosIngressDppIfPol modified                | annotation (Old: , New: orchestrator:terraform), tnQosDppPolName (Old: , New:    | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214289 | transition | 2023-03-06T19:17:22.076+02:00 | RsFcIfPol modified                           | annotation (Old: , New: orchestrator:terraform), tnFcIfPolName (Old: , New:      | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214319 | transition | 2023-03-06T19:17:21.947+02:00 | RsMonIfInfraPol modified                     | annotation (Old: , New: orchestrator:terraform), tnMonInfraPolName (Old: , New:  | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214337 | transition | 2023-03-06T19:17:21.840+02:00 | RsQosSdIfPol modified                        | annotation (Old: , New: orchestrator:terraform), tnQosSdIfPolName (Old: , New:   | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214334 | transition | 2023-03-06T19:17:21.743+02:00 | RsQosPfcIfPol modified                       | annotation (Old: , New: orchestrator:terraform), tnQosPfcIfPolName (Old: , New:  | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4215160 | transition | 2023-03-06T19:17:21.650+02:00 | RsDwdmIfPol modified                         | annotation (Old: , New: orchestrator:terraform), tnDwdmIfPolName (Old: , New:    | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214962 | transition | 2023-03-06T19:17:21.539+02:00 | RsCoppIfPol modified                         | annotation (Old: , New: orchestrator:terraform), tnCoppIfPolName (Old: , New:    | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214307 | transition | 2023-03-06T19:17:21.434+02:00 | RsL2PortSecurityPol modified                 | annotation (Old: , New: orchestrator:terraform), tnL2PortSecurityPolName (Old:   | 
|                           |      |          |            |                               |                                              | , New: default)                                                                  | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214316 | transition | 2023-03-06T19:17:21.336+02:00 | RsMcpIfPol modified                          | annotation (Old: , New: orchestrator:terraform), tnMcpIfPolName (Old: , New:     | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214965 | transition | 2023-03-06T19:17:21.229+02:00 | RsL2PortAuthPol modified                     | annotation (Old: , New: orchestrator:terraform), tnL2PortAuthPolName (Old: ,     | 
|                           |      |          |            |                               |                                              | New: default)                                                                    | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214295 | transition | 2023-03-06T19:17:21.153+02:00 | RsHIfPol modified                            | annotation (Old: , New: orchestrator:terraform), tnFabricHIfPolName (Old: ,      | 
|                           |      |          |            |                               |                                              | New: 10G-auto)                                                                   | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214325 | transition | 2023-03-06T19:17:21.047+02:00 | RsQosDppIfPol modified                       | annotation (Old: , New: orchestrator:terraform), tnQosDppPolName (Old: , New:    | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214968 | transition | 2023-03-06T19:17:20.952+02:00 | RsMacsecIfPol modified                       | annotation (Old: , New: orchestrator:terraform), tnMacsecIfPolName (Old: , New:  | 
|                           |      |          |            |                               |                                              | default)                                                                         | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214313 | transition | 2023-03-06T19:17:20.851+02:00 | RsLldpIfPol modified                         | annotation (Old: , New: orchestrator:terraform), tnLldpIfPolName (Old: , New:    | 
|                           |      |          |            |                               |                                              | LLDP-enable)                                                                     | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214346 | transition | 2023-03-06T19:17:20.749+02:00 | RsStormctrlIfPol modified                    | annotation (Old: , New: orchestrator:terraform), tnStormctrlIfPolName (Old: ,    | 
|                           |      |          |            |                               |                                              | New: default)                                                                    | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214333 | transition | 2023-03-06T19:17:18.523+02:00 | RsQosPfcIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214345 | transition | 2023-03-06T19:17:18.523+02:00 | RsStormctrlIfPol created                     | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214336 | transition | 2023-03-06T19:17:18.523+02:00 | RsQosSdIfPol created                         | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4218086 | transition | 2023-03-06T19:17:18.523+02:00 | RsQosLlfcIfPol created                       | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214348 | transition | 2023-03-06T19:17:18.523+02:00 | RsStpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4218184 | transition | 2023-03-06T19:17:18.523+02:00 | RsSynceEthIfPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214324 | transition | 2023-03-06T19:17:18.522+02:00 | RsQosDppIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214967 | transition | 2023-03-06T19:17:18.522+02:00 | RsMacsecIfPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214318 | transition | 2023-03-06T19:17:18.522+02:00 | RsMonIfInfraPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214315 | transition | 2023-03-06T19:17:18.522+02:00 | RsMcpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214327 | transition | 2023-03-06T19:17:18.522+02:00 | RsQosEgressDppIfPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214330 | transition | 2023-03-06T19:17:18.522+02:00 | RsQosIngressDppIfPol created                 | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214312 | transition | 2023-03-06T19:17:18.521+02:00 | RsLldpIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214306 | transition | 2023-03-06T19:17:18.521+02:00 | RsL2PortSecurityPol created                  | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214964 | transition | 2023-03-06T19:17:18.521+02:00 | RsL2PortAuthPol created                      | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4217527 | transition | 2023-03-06T19:17:18.521+02:00 | RsLinkFlapPol created                        | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214294 | transition | 2023-03-06T19:17:18.521+02:00 | RsHIfPol created                             | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214300 | transition | 2023-03-06T19:17:18.521+02:00 | RsL2IfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214279 | transition | 2023-03-06T19:17:18.520+02:00 | RsCdpIfPol created                           | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4215159 | transition | 2023-03-06T19:17:18.520+02:00 | RsDwdmIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4212194 | transition | 2023-03-06T19:17:18.520+02:00 | AccPortGrp nidemo-bare-metal created         | annotation:orchestrator:terraform, descr:VANNIEW temporary demo feel free to     | 
|                           |      |          |            |                               |                                              | destroy, name:nidemo-bare-metal, userdom::all:common:                            | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214288 | transition | 2023-03-06T19:17:18.520+02:00 | RsFcIfPol created                            | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
| nidemo-bare-metal         | Info | E4214961 | transition | 2023-03-06T19:17:18.520+02:00 | RsCoppIfPol created                          | userdom:all                                                                      | 
+---------------------------+------+----------+------------+-------------------------------+----------------------------------------------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci pg access intf port --apic apic21 --when any --view all

{
    "duration": 65855,
    "apic": {
        "read": true,
        "success": 142,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 141,
        "connect_time": 419,
        "disconnect_time": 0,
        "mo_time": 58163,
        "total_time": 58582
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

True	419	-	connect apic21o.emea-sp.cisco.com:443
True	377	8	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
True	351	15	apic21o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	321	16	apic21o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	349	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	356	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	355	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	712	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	337	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	497	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-ESX-CDC-22_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	367	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1886	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	397	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ethpmPhysIf
True	324	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	455	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	291	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vlanCktEp
True	333	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	358	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	344	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	369	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	293	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	294	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/37] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	347	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/38] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	318	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/39] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/40] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	341	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/41] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	300	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/42] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	386	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/43] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	326	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/44] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	331	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/45] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	423	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/46] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	319	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/47] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1937	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	380	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ethpmPhysIf
True	316	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	278	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vlanCktEp
True	332	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	369	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	335	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	388	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	300	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	313	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/37] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/38] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	311	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/39] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	314	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/40] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	334	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/41] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	321	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/42] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	311	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/43] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	319	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/44] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	366	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/45] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	294	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/46] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	347	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/47] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	383	0	apic21o.emea-sp.cisco.com:443 class infraAccPortGrp query rsp-subtree-include=faults,no-scoped,subtree
True	546	0	apic21o.emea-sp.cisco.com:443 class infraAccPortGrp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	537	8	apic21o.emea-sp.cisco.com:443 class infraAccPortGrp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	640	309	apic21o.emea-sp.cisco.com:443 class infraAccPortGrp query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
True	494	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-ESX-R7DC_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	1380	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	400	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ethpmPhysIf
True	339	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	402	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/vlanCktEp
True	314	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	308	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	326	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	313	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	296	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	349	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	299	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	310	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	355	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	316	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	309	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	348	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1390	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	406	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ethpmPhysIf
True	281	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	287	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/vlanCktEp
True	470	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	539	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	459	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	504	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	407	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	327	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	368	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	318	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	369	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	322	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	314	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	320	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	469	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-Infra-L3_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	899	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	350	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	342	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	981	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	356	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ethpmPhysIf
True	307	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	314	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	289	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	456	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-k8s_sriov_2207_bm_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	1400	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	335	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ethpmPhysIf
True	314	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/3/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	322	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vlanCktEp
True	330	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/3/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	374	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/4/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	336	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/4/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	333	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/4/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	411	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/5/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	376	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/5/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	276	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/6/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	306	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/6/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	363	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/6/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	457	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-k8s_sriov_2207_esx_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	366	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/3/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	326	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/3/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	342	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/5/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	360	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/5/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	529	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-k8s_sriov_2208_bm_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	1179	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	322	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ethpmPhysIf
True	266	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/3/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	286	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vlanCktEp
True	278	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/3/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	335	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/4/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	316	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/4/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/4/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	299	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/5/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	282	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/5/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	302	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/6/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	322	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/6/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	328	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/6/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	447	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-k8s_sriov_2208_esx_PolGrp query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	329	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/3/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	284	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/3/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	281	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/5/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	325	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/5/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	446	1	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof/accportgrp-nidemo-bare-metal query rsp-subtree-include=full-deployment&target-node=all&target-path=AccBaseGrpToEthIf
True	274	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	280	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	284	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	276	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./PgAccessInterfacePort.md)