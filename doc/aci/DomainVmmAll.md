# VMM Domain

## All domains

```
# iserver get aci domain vmm --apic apic11

Apic: apic11 (mode:online, cache:off)

+--------------+-----------------+-------------------+-----------------------+-----------+---------+
| Domain Name  | AAEP            | VLAN Pool         | Encapsulation Block   | EPG Usage | Uplinks |
+--------------+-----------------+-------------------+-----------------------+-----------+---------+
| EU-SPDC-CDC  | UCSB1_AAEP      | ESX-CDC_VlanPool  | [418-419] (static)    | 20/524    | 2       | 
|              | ESX-CDC_AAEP    |                   | [500-519] (static)    |           |         | 
|              |                 |                   | [520-520] (static)    |           |         | 
|              |                 |                   | [1108-1108] (static)  |           |         | 
|              |                 |                   | [2001-2500] (dynamic) |           |         | 
+--------------+-----------------+-------------------+-----------------------+-----------+---------+
| EU-SPDC-R3DC | UCSB1-R3DC_AAEP | ESX-R3DC_VlanPool | [2300-2309] (static)  | 5/410     | 2       | 
|              | ESX-R3DC_AAEP   |                   | [2310-2310] (static)  |           |         | 
|              |                 |                   | [3001-3399] (inherit) |           |         | 
+--------------+-----------------+-------------------+-----------------------+-----------+---------+
```

Developer

```
# iserver get aci domain vmm --apic apic11

{
    "duration": 1538,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 401,
        "disconnect_time": 0,
        "mo_time": 1007,
        "total_time": 1408
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

True	401	-	connect apic11o.emea-sp.cisco.com
True	323	2	apic11o.emea-sp.cisco.com class vmmDomP query rsp-subtree=children&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont
True	344	25	apic11o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	340	39	apic11o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./DomainVmm.md)