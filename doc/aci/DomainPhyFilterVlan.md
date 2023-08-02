# Physical Domain

## Filter by vlan id

```
# iserver get aci domain phy --apic apic21 --vlan 801

Apic: apic21 (mode:online, cache:off)

Physical Domain [#3]
--------------------

+---------+------------------+--------------------+-------------------+---------+-----------------------+------------+
| Faults  | Domain           | AAEP               | VLAN Pool         | Mode    | Encapsulation Block   | Sec Domain |
+---------+------------------+--------------------+-------------------+---------+-----------------------+------------+
| 0 0 0 0 | Infra_PhysDom    | vEPC-ESX21-22_AAEP | Infra_VlanPool    | static  | [1-1000] (static)     | --         | 
|         |                  | Infra_AAEP         |                   |         |                       |            | 
+---------+------------------+--------------------+-------------------+---------+-----------------------+------------+
| 0 0 0 0 | k8s_esx_PhysDom  | k8s_esx_AAEP       | k8s_esx_VlanPool  | dynamic | [800-809] (static)    | --         | 
|         |                  |                    |                   |         | [1300-1499] (dynamic) |            | 
+---------+------------------+--------------------+-------------------+---------+-----------------------+------------+
| 0 0 0 0 | k8s_phys_PhysDom | k8s_phys_AAEP      | k8s_phys_VlanPool | static  | [800-809] (static)    | --         | 
|         |                  |                    |                   |         | [810-813] (static)    |            | 
+---------+------------------+--------------------+-------------------+---------+-----------------------+------------+
```

Developer

```
# iserver get aci domain phy --apic apic21 --vlan 801

{
    "duration": 1589,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 460,
        "disconnect_time": 0,
        "mo_time": 778,
        "total_time": 1238
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

True	460	-	connect apic21o.emea-sp.cisco.com:443
True	393	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	385	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainPhy.md)