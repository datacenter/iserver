# VMM Domain

## vCenter specific output

```
# iserver get aci domain vmm --apic apic11 --view vc

Apic: apic11 (mode:online, cache:off)

+--------------+--------------+-------------+-------------------+
| Domain Name  | vCenter Name | vCenter IP  | vCenter Username  |
+--------------+--------------+-------------+-------------------+
| EU-SPDC-CDC  | EU-SPDC-CDC  | 10.58.28.18 | admin@admin.local | 
+--------------+--------------+-------------+-------------------+
| EU-SPDC-R3DC | EU-SPDC-R3DC | 10.58.28.18 | admin@admin.local | 
+--------------+--------------+-------------+-------------------+
```

Developer

```
# iserver get aci domain vmm --apic apic11 --view vc

{
    "duration": 1494,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 963,
        "total_time": 1362
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

True	399	-	connect apic11o.emea-sp.cisco.com
True	302	2	apic11o.emea-sp.cisco.com class vmmDomP query rsp-subtree=children&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont
True	333	25	apic11o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	328	39	apic11o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./DomainVmm.md)