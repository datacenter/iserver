# VMM Domain

## Filter by vlan id

```
# iserver get aci domain vmm --apic apic21 --vlan 801

Apic: apic21 (mode:online, cache:off)

VMM Domain [#1]
---------------

+---------+---------------+------+------------------+---------+-----------------------+-----+------------+
| Faults  | Domain        | AAEP | VLAN Pool        | Mode    | Encapsulation Block   | EPG | Sec Domain |
+---------+---------------+------+------------------+---------+-----------------------+-----+------------+
| 0 1 0 0 | EU-SPDC-POD2B |      | k8s_esx_VlanPool | dynamic | [800-809] (static)    | 15  | --         | 
|         |               |      |                  |         | [1300-1499] (dynamic) |     |            | 
+---------+---------------+------+------------------+---------+-----------------------+-----+------------+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --vlan 801

{
    "duration": 2637,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 481,
        "disconnect_time": 0,
        "mo_time": 1549,
        "total_time": 2030
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

True	481	-	connect apic21o.emea-sp.cisco.com:443
True	389	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	775	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	385	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainVmm.md)