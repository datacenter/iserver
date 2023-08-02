# VLAN Pool

## Default output

```
# iserver get aci pool vlan --apic apic21

Apic: apic21 (mode:online, cache:off)

Pool VLAN [#13]
---------------

+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| Faults  | VLAN Pool Name         | Allocation Mode | Encapsulation Block   | Role     | Domain                | EPG Usage |
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | ESX-CDC-22_VlanPool    | dynamic         | [2501-2502] (static)  | external | ESX-CDC-22_PhysDom    | 11/309    | 
|         |                        |                 | [2503-2509] (static)  | external | EU-SPDC-CDC-22        |           | 
|         |                        |                 | [2700-2999] (dynamic) | external | vEPC_ESX              |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | ESX-R7DC_VlanPool      | dynamic         | [3701-3800] (dynamic) | external | ESX-R7DC_PhysDom      | 2/100     | 
|         |                        |                 |                       |          | EU-SPDC-R7DC          |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | HX1_VlanPool           | static          | [70-79] (static)      | external | HX1_PhysDom           | 0/3059    | 
|         |                        |                 | [1000-4048] (static)  | external |                       |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | Infra_VlanPool         | static          | [1-1000] (static)     | external | Infra_L2dom           | 0/1000    | 
|         |                        |                 |                       |          | Infra_L3Dom           |           | 
|         |                        |                 |                       |          | Infra_PhysDom         |           | 
|         |                        |                 |                       |          | L3_Domain_vsfo        |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | k8s_esx_VlanPool       | dynamic         | [800-809] (static)    | external | EU-SPDC-POD2B         | 15/210    | 
|         |                        |                 | [1300-1499] (dynamic) | external | k8s_esx_PhysDom       |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | k8s_phys_VlanPool      | static          | [800-809] (static)    | external | k8s_phys_L3Dom        | 0/14      | 
|         |                        |                 | [810-813] (static)    | external | k8s_phys_PhysDom      |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | multipodL3out_VlanPool | dynamic         | [4-4] (dynamic)       | external | multipodL3out_L3Dom   | 0/1       | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | nidemo-3000-3001       | static          | [3000-3001] (static)  | external | nidemo                | 0/2       | 
|         |                        |                 |                       |          | test                  |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | RL-L3Out_VlanPool      | dynamic         | [4-4] (dynamic)       | external | RL-L3Out_RoutedDomain | 0/1       | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | SPN_VlanPool           | static          | [2600-2699] (static)  | external | SPN_PhysDom           | 0/100     | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | UCSB1-R7DC_VlanPool    | dynamic         | [2-100] (static)      | external | UCSB1-R7DC_PhysDom    | 0/298     | 
|         |                        |                 | [1701-1899] (dynamic) | external |                       |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | UCSB1_VlanPool         | dynamic         | [2-100] (static)      | external | UCSB1_L3Dom           | 0/399     | 
|         |                        |                 | [3701-4000] (dynamic) | external | UCSB1_PhysDom         |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | vEPC-ESX21-22_VlanPool | dynamic         | [2501-2509] (static)  | external | vEPC-Dataplane        | 4/309     | 
|         |                        |                 | [2700-2999] (dynamic) | external | vEPC-ESX20_PhysDom    |           | 
|         |                        |                 |                       |          | vEPC-ESX21-22_PhysDom |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
```

Developer

```
# iserver get aci pool vlan --apic apic21

{
    "duration": 1153,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 609,
        "total_time": 1006
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

True	397	-	connect apic21o.emea-sp.cisco.com:443
True	306	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	303	32	apic21o.emea-sp.cisco.com:443 class vmmEpPD
```

[[Back]](./PoolVlan.md)