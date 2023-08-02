# VMM Domain

## State view

```
# iserver get aci domain vmm --apic apic21

Apic: apic21 (mode:online, cache:off)

VMM Domain [#4]
---------------

+---------+----------------+--------------------+------------------------+---------+-----------------------+-----+------------------------+
| Faults  | Domain         | AAEP               | VLAN Pool              | Mode    | Encapsulation Block   | EPG | Sec Domain             |
+---------+----------------+--------------------+------------------------+---------+-----------------------+-----+------------------------+
| 0 6 0 0 | EU-SPDC-CDC-22 | ESX-CDC-22_AAEP    | ESX-CDC-22_VlanPool    | dynamic | [2501-2502] (static)  | 11  | UCSB1_SecDom           | 
|         |                |                    |                        |         | [2503-2509] (static)  |     |                        | 
|         |                |                    |                        |         | [2700-2999] (dynamic) |     |                        | 
+---------+----------------+--------------------+------------------------+---------+-----------------------+-----+------------------------+
| 0 1 0 0 | EU-SPDC-POD2B  |                    | k8s_esx_VlanPool       | dynamic | [800-809] (static)    | 15  | --                     | 
|         |                |                    |                        |         | [1300-1499] (dynamic) |     |                        | 
+---------+----------------+--------------------+------------------------+---------+-----------------------+-----+------------------------+
| 0 4 0 0 | EU-SPDC-R7DC   | ESX-R7DC_AAEP      | ESX-R7DC_VlanPool      | dynamic | [3701-3800] (dynamic) | 2   | UCSB1-R7DC-ACI2_SecDom | 
+---------+----------------+--------------------+------------------------+---------+-----------------------+-----+------------------------+
| 0 5 0 0 | vEPC-Dataplane | vEPC-ESX21-22_AAEP | vEPC-ESX21-22_VlanPool | dynamic | [2501-2509] (static)  | 4   | --                     | 
|         |                |                    |                        |         | [2700-2999] (dynamic) |     |                        | 
+---------+----------------+--------------------+------------------------+---------+-----------------------+-----+------------------------+
```

Developer

```
# iserver get aci domain vmm --apic apic21

{
    "duration": 2806,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 509,
        "disconnect_time": 0,
        "mo_time": 1822,
        "total_time": 2331
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

True	509	-	connect apic21o.emea-sp.cisco.com:443
True	475	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	911	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	436	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainVmm.md)