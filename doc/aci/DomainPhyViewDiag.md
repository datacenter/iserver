# Physical Domain

## Diag view

```
# iserver get aci domain phy --apic apic21 --name UCSB* --when any --view diag

Apic: apic21 (mode:online, cache:off)

Physical Domain - Faults [#0]
-----------------------------
None

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

Physical Domain - Event Logs last 10y [#0]
------------------------------------------
None

Physical Domain - Audit Logs last 10y [#12]
-------------------------------------------

+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| Domain             | Sev  | Code     | Cause      | Created Time                  | Description                     | Change Set                                                               |
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| UCSB1-R7DC_PhysDom | Info | E4214354 | transition | 2022-07-11T10:14:34.440+02:00 | RsVlanNs created                | tDn:uni/infra/vlanns-[UCSB1-R7DC_VlanPool]-dynamic, userdom::all:common: | 
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| UCSB1-R7DC_PhysDom | Info | E4212794 | transition | 2022-07-11T10:14:14.666+02:00 | DomP UCSB1-R7DC_PhysDom created | name:UCSB1-R7DC_PhysDom, userdom::all:common:                            | 
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| UCSB1_PhysDom      | Info | E4214355 | transition | 2022-07-07T15:48:56.490+02:00 | RsVlanNs modified               | tDn (Old: uni/infra/vlanns-[UCSB1_VlanPool]-static, New:                 | 
|                    |      |          |            |                               |                                 | uni/infra/vlanns-[UCSB1_VlanPool]-dynamic)                               | 
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| UCSB1_PhysDom      | Info | E4214355 | transition | 2022-07-07T15:48:31.664+02:00 | RsVlanNs modified               | tDn (Old: uni/infra/vlanns-[UCSB1_VlanPool]-dynamic, New:                | 
|                    |      |          |            |                               |                                 | uni/infra/vlanns-[UCSB1_VlanPool]-static)                                | 
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| UCSB1_PhysDom      | Info | E4214355 | transition | 2022-07-07T15:40:19.249+02:00 | RsVlanNs modified               | tDn (Old: uni/infra/vlanns-[UCSB1_VlanPool]-static, New:                 | 
|                    |      |          |            |                               |                                 | uni/infra/vlanns-[UCSB1_VlanPool]-dynamic)                               | 
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| UCSB1_PhysDom      | Info | E4214355 | transition | 2022-07-07T15:38:00.045+02:00 | RsVlanNs modified               | tDn (Old: uni/infra/vlanns-[UCSB1_VlanPool]-dynamic, New:                | 
|                    |      |          |            |                               |                                 | uni/infra/vlanns-[UCSB1_VlanPool]-static)                                | 
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| UCSB1_PhysDom      | Info | E4214355 | transition | 2022-07-07T15:34:54.621+02:00 | RsVlanNs modified               | tDn (Old: uni/infra/vlanns-[UCSB1_VlanPool]-static, New:                 | 
|                    |      |          |            |                               |                                 | uni/infra/vlanns-[UCSB1_VlanPool]-dynamic)                               | 
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| UCSB1_PhysDom      | Info | E4214355 | transition | 2022-07-07T15:33:34.639+02:00 | RsVlanNs modified               | tDn (Old: uni/infra/vlanns-[UCSB1_VlanPool]-dynamic, New:                | 
|                    |      |          |            |                               |                                 | uni/infra/vlanns-[UCSB1_VlanPool]-static)                                | 
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| UCSB1_PhysDom      | Info | E4214355 | transition | 2022-07-07T15:28:29.349+02:00 | RsVlanNs modified               | tDn (Old: uni/infra/vlanns-[UCSB1_VlanPool]-static, New:                 | 
|                    |      |          |            |                               |                                 | uni/infra/vlanns-[UCSB1_VlanPool]-dynamic)                               | 
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| UCSB1_PhysDom      | Info | E4214355 | transition | 2022-07-07T14:44:52.217+02:00 | RsVlanNs modified               | tDn (Old: uni/infra/vlanns-[UCSB1_VlanPool]-dynamic, New:                | 
|                    |      |          |            |                               |                                 | uni/infra/vlanns-[UCSB1_VlanPool]-static)                                | 
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| UCSB1_PhysDom      | Info | E4214354 | transition | 2022-07-05T16:43:18.866+02:00 | RsVlanNs created                | tDn:uni/infra/vlanns-[UCSB1_VlanPool]-dynamic, userdom::all:common:      | 
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
| UCSB1_PhysDom      | Info | E4212794 | transition | 2022-07-05T16:43:18.865+02:00 | DomP UCSB1_PhysDom created      | name:UCSB1_PhysDom, userdom::all:common:                                 | 
+--------------------+------+----------+------------+-------------------------------+---------------------------------+--------------------------------------------------------------------------+
```

Developer

```
# iserver get aci domain phy --apic apic21 --name UCSB* --when any --view diag

{
    "duration": 4614,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 533,
        "disconnect_time": 0,
        "mo_time": 3368,
        "total_time": 3901
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

True	533	-	connect apic21o.emea-sp.cisco.com:443
True	414	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	412	0	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree-include=faults,no-scoped,subtree
True	862	14	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	823	0	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	857	182	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./DomainPhy.md)