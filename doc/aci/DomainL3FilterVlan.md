# L3 Domain

## Filter by vlan id

```
# iserver get aci domain l3 --apic apic21 --vlan 801

Apic: apic21 (mode:online, cache:off)

L3 Domain [#3]
--------------

+---------+----------------+---------------+-------------------+--------+---------------------+------------+
| Faults  | Domain         | AAEP          | VLAN Pool         | Mode   | Encapsulation Block | Sec Domain |
+---------+----------------+---------------+-------------------+--------+---------------------+------------+
| 0 0 0 0 | Infra_L3Dom    | TEST-AAP      | Infra_VlanPool    | static | [1-1000] (static)   | --         | 
|         |                | Infra_AAEP    |                   |        |                     |            | 
+---------+----------------+---------------+-------------------+--------+---------------------+------------+
| 0 0 0 0 | k8s_phys_L3Dom | k8s_phys_AAEP | k8s_phys_VlanPool | static | [800-809] (static)  | --         | 
|         |                |               |                   |        | [810-813] (static)  |            | 
+---------+----------------+---------------+-------------------+--------+---------------------+------------+
| 0 0 0 0 | L3_Domain_vsfo |               | Infra_VlanPool    | static | [1-1000] (static)   | --         | 
+---------+----------------+---------------+-------------------+--------+---------------------+------------+
```

Developer

```
# iserver get aci domain l3 --apic apic21 --vlan 801

{
    "duration": 1565,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 463,
        "disconnect_time": 0,
        "mo_time": 785,
        "total_time": 1248
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

True	463	-	connect apic21o.emea-sp.cisco.com:443
True	367	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	418	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainL3.md)