# Physical Domain

## Fault history view

```
# iserver get aci domain phy --apic apic21 --name UCSB* --when any --view hfault

Apic: apic21 (mode:online, cache:off)

Physical Domain - Fault Records last 10y [#9]
---------------------------------------------

+---------------+------+-------+-------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| Domain        | Sev  | Code  | Cause             | Created Time                  | Lifecycle | Description                                                                      |
+---------------+------+-------+-------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| UCSB1_PhysDom | --   | F0981 | resolution-failed | 2022-07-07T16:49:26.019+02:00 |           | Failed to form relation to MO uni/infra/vlanns-[UCSB1_VlanPool]-static of class  | 
|               |      |       |                   |                               |           | fvnsVlanInstP                                                                    | 
| UCSB1_PhysDom | --   | F0981 | resolution-failed | 2022-07-07T15:48:57.396+02:00 | retaining | Failed to form relation to MO uni/infra/vlanns-[UCSB1_VlanPool]-static of class  | 
|               |      |       |                   |                               |           | fvnsVlanInstP                                                                    | 
| UCSB1_PhysDom | Warn | F0981 | resolution-failed | 2022-07-07T15:48:33.382+02:00 | raised    | Failed to form relation to MO uni/infra/vlanns-[UCSB1_VlanPool]-static of class  | 
|               |      |       |                   |                               |           | fvnsVlanInstP                                                                    | 
| UCSB1_PhysDom | --   | F0981 | resolution-failed | 2022-07-07T15:40:21.093+02:00 | retaining | Failed to form relation to MO uni/infra/vlanns-[UCSB1_VlanPool]-static of class  | 
|               |      |       |                   |                               |           | fvnsVlanInstP                                                                    | 
| UCSB1_PhysDom | Warn | F0981 | resolution-failed | 2022-07-07T15:38:03.031+02:00 | raised    | Failed to form relation to MO uni/infra/vlanns-[UCSB1_VlanPool]-static of class  | 
|               |      |       |                   |                               |           | fvnsVlanInstP                                                                    | 
| UCSB1_PhysDom | --   | F0981 | resolution-failed | 2022-07-07T15:34:56.914+02:00 | retaining | Failed to form relation to MO uni/infra/vlanns-[UCSB1_VlanPool]-static of class  | 
|               |      |       |                   |                               |           | fvnsVlanInstP                                                                    | 
| UCSB1_PhysDom | Warn | F0981 | resolution-failed | 2022-07-07T15:33:35.933+02:00 | raised    | Failed to form relation to MO uni/infra/vlanns-[UCSB1_VlanPool]-static of class  | 
|               |      |       |                   |                               |           | fvnsVlanInstP                                                                    | 
| UCSB1_PhysDom | --   | F0981 | resolution-failed | 2022-07-07T15:26:08.640+02:00 | retaining | Failed to form relation to MO uni/infra/vlanns-[UCSB1_VlanPool]-static of class  | 
|               |      |       |                   |                               |           | fvnsVlanInstP                                                                    | 
| UCSB1_PhysDom | Warn | F0981 | resolution-failed | 2022-07-07T14:44:55.314+02:00 | raised    | Failed to form relation to MO uni/infra/vlanns-[UCSB1_VlanPool]-static of class  | 
|               |      |       |                   |                               |           | fvnsVlanInstP                                                                    | 
+---------------+------+-------+-------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci domain phy --apic apic21 --name UCSB* --when any --view hfault

{
    "duration": 2331,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 534,
        "disconnect_time": 0,
        "mo_time": 1190,
        "total_time": 1724
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

True	534	-	connect apic21o.emea-sp.cisco.com:443
True	390	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	800	14	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./DomainPhy.md)