# VMM Domain

## Properties specific output

```
# iserver get aci domain vmm --apic apic11 --view prop

Apic: apic11 (mode:online, cache:off)

+--------------+-------------+---------------+----------------+----------------+--------------+-------------------+
| Domain Name  | Access Mode | Cfg Infra PGs | Tag Collection | VM Folder Data | Ep Inventory | Ep Retention Time |
+--------------+-------------+---------------+----------------+----------------+--------------+-------------------+
| EU-SPDC-CDC  | read-write  | no            | no             | no             | on-link      | 0                 | 
+--------------+-------------+---------------+----------------+----------------+--------------+-------------------+
| EU-SPDC-R3DC | read-write  | no            | no             | no             | on-link      | 0                 | 
+--------------+-------------+---------------+----------------+----------------+--------------+-------------------+
```

Developer

```
# iserver get aci domain vmm --apic apic11 --view prop

{
    "duration": 1498,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 389,
        "disconnect_time": 0,
        "mo_time": 983,
        "total_time": 1372
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

True	389	-	connect apic11o.emea-sp.cisco.com
True	328	2	apic11o.emea-sp.cisco.com class vmmDomP query rsp-subtree=children&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont
True	340	25	apic11o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	315	39	apic11o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./DomainVmm.md)