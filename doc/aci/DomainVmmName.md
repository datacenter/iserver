# VMM Domain

## Filter by name

```
# iserver get aci domain vmm --apic apic11 --name *r3dc*

Apic: apic11 (mode:online, cache:off)

+--------------+-----------------+-------------------+-----------------------+-----------+---------+
| Domain Name  | AAEP            | VLAN Pool         | Encapsulation Block   | EPG Usage | Uplinks |
+--------------+-----------------+-------------------+-----------------------+-----------+---------+
| EU-SPDC-R3DC | UCSB1-R3DC_AAEP | ESX-R3DC_VlanPool | [2300-2309] (static)  | 5/410     | 2       | 
|              | ESX-R3DC_AAEP   |                   | [2310-2310] (static)  |           |         | 
|              |                 |                   | [3001-3399] (inherit) |           |         | 
+--------------+-----------------+-------------------+-----------------------+-----------+---------+
```

Developer

```
# iserver get aci domain vmm --apic apic11 --name *r3dc*

{
    "duration": 1517,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 396,
        "disconnect_time": 0,
        "mo_time": 997,
        "total_time": 1393
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

True	396	-	connect apic11o.emea-sp.cisco.com
True	313	2	apic11o.emea-sp.cisco.com class vmmDomP query rsp-subtree=children&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont
True	356	25	apic11o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	328	39	apic11o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./DomainVmm.md)