# L3 Domain

## Default output

```
# iserver get aci domain l3 --apic apic21

Apic: apic21 (mode:online, cache:off)

L3 Domain [#7]
--------------

+---------+-----------------------+------------------------+------------------------+---------+-----------------------+------------+
| Faults  | Domain                | AAEP                   | VLAN Pool              | Mode    | Encapsulation Block   | Sec Domain |
+---------+-----------------------+------------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | Infra_L3Dom           | TEST-AAP               | Infra_VlanPool         | static  | [1-1000] (static)     | --         | 
|         |                       | Infra_AAEP             |                        |         |                       |            | 
+---------+-----------------------+------------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | k8s_phys_L3Dom        | k8s_phys_AAEP          | k8s_phys_VlanPool      | static  | [800-809] (static)    | --         | 
|         |                       |                        |                        |         | [810-813] (static)    |            | 
+---------+-----------------------+------------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | L3_Domain_vsfo        |                        | Infra_VlanPool         | static  | [1-1000] (static)     | --         | 
+---------+-----------------------+------------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | multipodL3out_L3Dom   | multipodL3out_AAEP     | multipodL3out_VlanPool | dynamic | [4-4] (dynamic)       | --         | 
+---------+-----------------------+------------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | RL-L3Out_RoutedDomain | RL-L3Out_EntityProfile | RL-L3Out_VlanPool      | dynamic | [4-4] (dynamic)       | --         | 
+---------+-----------------------+------------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | UCSB1_L3Dom           | UCSB1_AAEP             | UCSB1_VlanPool         | dynamic | [2-100] (static)      | --         | 
|         |                       |                        |                        |         | [3701-4000] (dynamic) |            | 
+---------+-----------------------+------------------------+------------------------+---------+-----------------------+------------+
| 0 0 0 0 | vEPC_ESX              | ESX-CDC-22_AAEP        | ESX-CDC-22_VlanPool    | dynamic | [2501-2502] (static)  | --         | 
|         |                       | vEPC-ESX21-22_AAEP     |                        |         | [2503-2509] (static)  |            | 
|         |                       |                        |                        |         | [2700-2999] (dynamic) |            | 
+---------+-----------------------+------------------------+------------------------+---------+-----------------------+------------+
```

Developer

```
# iserver get aci domain l3 --apic apic21

{
    "duration": 1547,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 479,
        "disconnect_time": 0,
        "mo_time": 765,
        "total_time": 1244
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

True	479	-	connect apic21o.emea-sp.cisco.com:443
True	382	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	383	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainL3.md)