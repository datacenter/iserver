# L3 Domain

## Filter by vlan pool name

```
# iserver get aci domain l3 --apic apic21 --pool *l3*

Apic: apic21 (mode:online, cache:off)

L3 Domain [#2]
--------------

+---------+-----------------------+------------------------+------------------------+---------+---------------------+------------+
| Faults  | Domain                | AAEP                   | VLAN Pool              | Mode    | Encapsulation Block | Sec Domain |
+---------+-----------------------+------------------------+------------------------+---------+---------------------+------------+
| 0 0 0 0 | multipodL3out_L3Dom   | multipodL3out_AAEP     | multipodL3out_VlanPool | dynamic | [4-4] (dynamic)     | --         | 
+---------+-----------------------+------------------------+------------------------+---------+---------------------+------------+
| 0 0 0 0 | RL-L3Out_RoutedDomain | RL-L3Out_EntityProfile | RL-L3Out_VlanPool      | dynamic | [4-4] (dynamic)     | --         | 
+---------+-----------------------+------------------------+------------------------+---------+---------------------+------------+
```

Developer

```
# iserver get aci domain l3 --apic apic21 --pool *l3*

{
    "duration": 1558,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 470,
        "disconnect_time": 0,
        "mo_time": 740,
        "total_time": 1210
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

True	470	-	connect apic21o.emea-sp.cisco.com:443
True	378	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	362	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainL3.md)