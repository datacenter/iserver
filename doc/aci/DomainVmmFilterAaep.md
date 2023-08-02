# VMM Domain

## Filter by aaep name

```
# iserver get aci domain vmm --apic apic21 --aaep *r7*

Apic: apic21 (mode:online, cache:off)

VMM Domain [#1]
---------------

+---------+--------------+---------------+-------------------+---------+-----------------------+-----+------------------------+
| Faults  | Domain       | AAEP          | VLAN Pool         | Mode    | Encapsulation Block   | EPG | Sec Domain             |
+---------+--------------+---------------+-------------------+---------+-----------------------+-----+------------------------+
| 0 4 0 0 | EU-SPDC-R7DC | ESX-R7DC_AAEP | ESX-R7DC_VlanPool | dynamic | [3701-3800] (dynamic) | 2   | UCSB1-R7DC-ACI2_SecDom | 
+---------+--------------+---------------+-------------------+---------+-----------------------+-----+------------------------+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --aaep *r7*

{
    "duration": 2543,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 448,
        "disconnect_time": 0,
        "mo_time": 1559,
        "total_time": 2007
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

True	448	-	connect apic21o.emea-sp.cisco.com:443
True	360	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	813	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	386	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainVmm.md)