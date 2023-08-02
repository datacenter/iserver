# Physical Domain

## Audit view

```
# iserver get aci domain phy --apic apic21 --name UCSB* --when any --view audit

Apic: apic21 (mode:online, cache:off)

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
# iserver get aci domain phy --apic apic21 --name UCSB* --when any --view audit

{
    "duration": 2218,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 469,
        "disconnect_time": 0,
        "mo_time": 1250,
        "total_time": 1719
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

True	469	-	connect apic21o.emea-sp.cisco.com:443
True	403	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	847	182	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./DomainPhy.md)