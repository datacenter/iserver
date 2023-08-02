# Physical Domain

## Default output

```
# iserver get aci domain phy --apic apic21

Apic: apic21 (mode:online, cache:off)

Physical Domain [#12]
---------------------

+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| Faults  | Domain                | AAEP               | VLAN Pool              | Mode    | Encapsulation Block   | Sec Domain |
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | ESX-CDC-22_PhysDom    | ESX-CDC-22_AAEP    | ESX-CDC-22_VlanPool    | dynamic | [2501-2502] (static)  | --         | 
|         |                       |                    |                        |         | [2503-2509] (static)  |            | 
|         |                       |                    |                        |         | [2700-2999] (dynamic) |            | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | ESX-R7DC_PhysDom      | ESX-R7DC_AAEP      | ESX-R7DC_VlanPool      | dynamic | [3701-3800] (dynamic) | --         | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | HX1_PhysDom           | HX1_AAEP           | HX1_VlanPool           | static  | [70-79] (static)      | --         | 
|         |                       |                    |                        |         | [1000-4048] (static)  |            | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | Infra_PhysDom         | vEPC-ESX21-22_AAEP | Infra_VlanPool         | static  | [1-1000] (static)     | --         | 
|         |                       | Infra_AAEP         |                        |         |                       |            | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | k8s_esx_PhysDom       | k8s_esx_AAEP       | k8s_esx_VlanPool       | dynamic | [800-809] (static)    | --         | 
|         |                       |                    |                        |         | [1300-1499] (dynamic) |            | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | k8s_phys_PhysDom      | k8s_phys_AAEP      | k8s_phys_VlanPool      | static  | [800-809] (static)    | --         | 
|         |                       |                    |                        |         | [810-813] (static)    |            | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | nidemo                | nidemo             | nidemo-3000-3001       | static  | [3000-3001] (static)  | --         | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | SPN_PhysDom           | SPN_AAEP           | SPN_VlanPool           | static  | [2600-2699] (static)  | --         | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | UCSB1-R7DC_PhysDom    | UCSB1-R7DC_AAEP    | UCSB1-R7DC_VlanPool    | dynamic | [2-100] (static)      | --         | 
|         |                       |                    |                        |         | [1701-1899] (dynamic) |            | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | UCSB1_PhysDom         | UCSB1_AAEP         | UCSB1_VlanPool         | dynamic | [2-100] (static)      | --         | 
|         |                       |                    |                        |         | [3701-4000] (dynamic) |            | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | vEPC-ESX20_PhysDom    | vEPC-ESX21-22_AAEP | vEPC-ESX21-22_VlanPool | dynamic | [2501-2509] (static)  | --         | 
|         |                       |                    |                        |         | [2700-2999] (dynamic) |            | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | vEPC-ESX21-22_PhysDom | vEPC-ESX21-22_AAEP | vEPC-ESX21-22_VlanPool | dynamic | [2501-2509] (static)  | --         | 
|         |                       |                    |                        |         | [2700-2999] (dynamic) |            | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
```

Developer

```
# iserver get aci domain phy --apic apic21

{
    "duration": 2868,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 670,
        "disconnect_time": 0,
        "mo_time": 1749,
        "total_time": 2419
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

True	670	-	connect apic21o.emea-sp.cisco.com:443
True	1391	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	358	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainPhy.md)