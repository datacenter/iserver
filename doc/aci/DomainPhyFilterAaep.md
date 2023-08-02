# Physical Domain

## Filter by aaep name

```
# iserver get aci domain phy --apic apic21 --aaep *esx*

Apic: apic21 (mode:online, cache:off)

Physical Domain [#6]
--------------------

+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| Faults  | Domain                | AAEP               | VLAN Pool              | Mode    | Encapsulation Block   | Sec Domain |
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | ESX-CDC-22_PhysDom    | ESX-CDC-22_AAEP    | ESX-CDC-22_VlanPool    | dynamic | [2501-2502] (static)  | --         | 
|         |                       |                    |                        |         | [2503-2509] (static)  |            | 
|         |                       |                    |                        |         | [2700-2999] (dynamic) |            | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | ESX-R7DC_PhysDom      | ESX-R7DC_AAEP      | ESX-R7DC_VlanPool      | dynamic | [3701-3800] (dynamic) | --         | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | Infra_PhysDom         | vEPC-ESX21-22_AAEP | Infra_VlanPool         | static  | [1-1000] (static)     | --         | 
|         |                       | Infra_AAEP         |                        |         |                       |            | 
+---------+-----------------------+--------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | k8s_esx_PhysDom       | k8s_esx_AAEP       | k8s_esx_VlanPool       | dynamic | [800-809] (static)    | --         | 
|         |                       |                    |                        |         | [1300-1499] (dynamic) |            | 
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
# iserver get aci domain phy --apic apic21 --aaep *esx*

{
    "duration": 1571,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 461,
        "disconnect_time": 0,
        "mo_time": 752,
        "total_time": 1213
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

True	461	-	connect apic21o.emea-sp.cisco.com:443
True	380	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	372	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainPhy.md)