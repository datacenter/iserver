# VLAN Pool

## Show all vlan pools

```
# iserver get aci pool vlan --apic apic21

Apic: apic21 (mode:online, cache:off)

+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| VLAN Pool Name         | Allocation Mode | Encapsulation Block   | Role     | Domain                | EPG Usage |
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| ESX-CDC-22_VlanPool    | dynamic         | [2501-2502] (static)  | external | ESX-CDC-22_PhysDom    | 11/309    | 
|                        |                 | [2503-2509] (static)  | external | vEPC_ESX              |           | 
|                        |                 | [2700-2999] (dynamic) | external | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| ESX-R7DC_VlanPool      | dynamic         | [3701-3800] (dynamic) | external | ESX-R7DC_PhysDom      | 2/100     | 
|                        |                 |                       |          | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| HX1_VlanPool           | static          | [70-79] (static)      | external | HX1_PhysDom           | 0/3059    | 
|                        |                 | [1000-4048] (static)  | external |                       |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| Infra_VlanPool         | static          | [1-1000] (static)     | external | Infra_L3Dom           | 0/1000    | 
|                        |                 |                       |          | Infra_PhysDom         |           | 
|                        |                 |                       |          | L3_Domain_vsfo        |           | 
|                        |                 |                       |          | uni/l2dom-Infra_L2dom |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| k8s_esx_VlanPool       | dynamic         | [800-809] (static)    | external | k8s_esx_PhysDom       | 15/210    | 
|                        |                 | [1300-1499] (inherit) | external | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| k8s_phys_VlanPool      | static          | [800-809] (inherit)   | external | k8s_phys_L3Dom        | 0/14      | 
|                        |                 | [810-813] (static)    | external | k8s_phys_PhysDom      |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| multipodL3out_VlanPool | dynamic         | [4-4] (inherit)       | external | multipodL3out_L3Dom   | 0/1       | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| nidemo-3000-3001       | static          | [3000-3001] (inherit) | external | nidemo                | 0/2       | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| RL-L3Out_VlanPool      | dynamic         | [4-4] (inherit)       | external | RL-L3Out_RoutedDomain | 0/1       | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| SPN_VlanPool           | static          | [2600-2699] (static)  | external | SPN_PhysDom           | 0/100     | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| UCSB1-R7DC_VlanPool    | dynamic         | [2-100] (static)      | external | UCSB1-R7DC_PhysDom    | 0/298     | 
|                        |                 | [1701-1899] (inherit) | external |                       |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| UCSB1_VlanPool         | dynamic         | [2-100] (static)      | external | UCSB1_L3Dom           | 0/399     | 
|                        |                 | [3701-4000] (inherit) | external | UCSB1_PhysDom         |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| vEPC-ESX21-22_VlanPool | dynamic         | [2501-2509] (static)  | external | vEPC-ESX20_PhysDom    | 4/309     | 
|                        |                 | [2700-2999] (dynamic) | external | vEPC-ESX21-22_PhysDom |           | 
|                        |                 |                       |          | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
```

Developer

```
# iserver get aci pool vlan --apic apic21

{
    "duration": 1492,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 454,
        "disconnect_time": 0,
        "mo_time": 722,
        "total_time": 1176
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

True	454	-	connect apic21o.emea-sp.cisco.com
True	355	13	apic21o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	367	32	apic21o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./PoolVlan.md)