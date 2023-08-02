# VMM Domain

## Filter by domain name

```
# iserver get aci domain vmm --apic apic21 --name *cdc*

Apic: apic21 (mode:online, cache:off)

VMM Domain [#1]
---------------

+---------+----------------+-----------------+---------------------+---------+-----------------------+-----+--------------+
| Faults  | Domain         | AAEP            | VLAN Pool           | Mode    | Encapsulation Block   | EPG | Sec Domain   |
+---------+----------------+-----------------+---------------------+---------+-----------------------+-----+--------------+
| 0 6 0 0 | EU-SPDC-CDC-22 | ESX-CDC-22_AAEP | ESX-CDC-22_VlanPool | dynamic | [2501-2502] (static)  | 11  | UCSB1_SecDom | 
|         |                |                 |                     |         | [2503-2509] (static)  |     |              | 
|         |                |                 |                     |         | [2700-2999] (dynamic) |     |              | 
+---------+----------------+-----------------+---------------------+---------+-----------------------+-----+--------------+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --name *cdc*

{
    "duration": 2675,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 567,
        "disconnect_time": 0,
        "mo_time": 1575,
        "total_time": 2142
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

True	567	-	connect apic21o.emea-sp.cisco.com:443
True	452	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	781	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	342	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainVmm.md)