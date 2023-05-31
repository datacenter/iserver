# VMM Domain

## Properties specific output

```
# iserver get aci domain vmm --apic apic11 --view prop

Apic: apic11

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
    "duration": 1871,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 552,
        "disconnect_time": 0,
        "mo_time": 1089,
        "total_time": 1641
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
    }
}

Log: apic
----------

True	552	-	connect apic11o.emea-sp.cisco.com
True	332	2	apic11o.emea-sp.cisco.com class vmmDomP query rsp-subtree=children&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont
True	368	25	apic11o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	389	39	apic11o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./DomainVmm.md)