# Attachable Access Entity Profile (AAEP)

## Filter by name

```
# iserver get aci aaep --apic apic11 --name UCSB*

Apic: apic11 (mode:online, cache:off)

Attachable Access Entity Profile (AAEP) [#2]
--------------------------------------------

+---------+-----------------+------------+-------------+--------------------+--------------+-----+-------------------+------------------------+
| Faults  | Name            | Infra VLAN | Domain Type | Domain Name        | Domain State | EPG | PG Interface Type | PG Name                |
+---------+-----------------+------------+-------------+--------------------+--------------+-----+-------------------+------------------------+
| 0 0 0 0 | UCSB1-R3DC_AAEP | X          | VMM         | EU-SPDC-R3DC       | formed       | --  | PC/VPC Interface  | UCSB1-R3DC-FI-A_PolGrp | 
|         |                 |            | L3          | Infra_L3Dom        | formed       |     | PC/VPC Interface  | UCSB1-R3DC-FI-B_PolGrp | 
|         |                 |            | Physical    | UCSB1-R3DC_PhysDom | formed       |     |                   |                        | 
+---------+-----------------+------------+-------------+--------------------+--------------+-----+-------------------+------------------------+
| 0 0 0 0 | UCSB1_AAEP      | X          | VMM         | EU-SPDC-CDC        | formed       | --  | PC/VPC Interface  | UCSB1-FI-A_PolGrp      | 
|         |                 |            | L3          | Infra_L3Dom        | formed       |     | PC/VPC Interface  | UCSB1-FI-B_PolGrp      | 
|         |                 |            | L3          | UCSB1_L3Dom        | formed       |     |                   |                        | 
|         |                 |            | Physical    | UCSB1_PhysDom      | formed       |     |                   |                        | 
+---------+-----------------+------------+-------------+--------------------+--------------+-----+-------------------+------------------------+
```

Developer

```
# iserver get aci aaep --apic apic11 --name UCSB*

{
    "duration": 3639,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 442,
        "disconnect_time": 0,
        "mo_time": 2886,
        "total_time": 3328
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

True	442	-	connect apic11o.emea-sp.cisco.com:443
True	406	30	apic11o.emea-sp.cisco.com:443 class infraAttEntityP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	327	31	apic11o.emea-sp.cisco.com:443 mo uni/infra query query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg
True	331	2	apic11o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	722	2	apic11o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	374	25	apic11o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	328	18	apic11o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	398	23	apic11o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
```

[[Back]](./Aaep.md)