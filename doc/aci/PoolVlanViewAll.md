# VLAN Pool

## All view

```
# iserver get aci pool vlan --apic apic21 --name HX* --when any --view all

Apic: apic21 (mode:online, cache:off)

Pool VLAN [#1]
--------------

+---------+----------------+-----------------+----------------------+----------+-------------+-----------+
| Faults  | VLAN Pool Name | Allocation Mode | Encapsulation Block  | Role     | Domain      | EPG Usage |
+---------+----------------+-----------------+----------------------+----------+-------------+-----------+
| 0 0 0 0 | HX1_VlanPool   | static          | [70-79] (static)     | external | HX1_PhysDom | 0/3059    | 
|         |                |                 | [1000-4048] (static) | external |             |           | 
+---------+----------------+-----------------+----------------------+----------+-------------+-----------+

Pool VLAN - Associated EPG [#0]
-------------------------------

+-----------+-----+-----------+------------+------+------------+------------+-----------+
| Pool Name | EPG | VLAN Pool | Alloc Mode | VLAN | Deployment | Resolution | Switching |
+-----------+-----+-----------+------------+------+------------+------------+-----------+

Pool VLAN - Faults [#0]
-----------------------
None

Pool VLAN - Fault Records last 10y [#0]
---------------------------------------
None

Pool VLAN - Event Logs last 10y [#0]
------------------------------------
None

Pool VLAN - Audit Logs last 10y [#5]
------------------------------------

+--------------+------+----------+------------+-------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------+
| Name         | Sev  | Code     | Cause      | Created Time                  | Description                                      | Change Set                                                                     |
+--------------+------+----------+------------+-------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------+
| HX1_VlanPool | Info | E4214208 | transition | 2022-07-07T15:26:14.403+02:00 | EncapBlk vlan-1000 vlan-4048 modified            | name (Old: , New: blk2)                                                        | 
+--------------+------+----------+------------+-------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------+
| HX1_VlanPool | Info | E4214208 | transition | 2022-07-07T15:26:13.871+02:00 | EncapBlk vlan-70 vlan-79 modified                | name (Old: , New: blk1)                                                        | 
+--------------+------+----------+------------+-------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------+
| HX1_VlanPool | Info | E4214207 | transition | 2021-12-09T23:58:28.140+02:00 | EncapBlk vlan-1000 vlan-4048 created             | allocMode:static, descr:HX1-eu-spdc VLAN pool, from:vlan-1000, role:external,  | 
|              |      |          |            |                               |                                                  | to:vlan-4048, userdom::all:common:                                             | 
+--------------+------+----------+------------+-------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------+
| HX1_VlanPool | Info | E4214207 | transition | 2021-12-09T23:58:28.140+02:00 | EncapBlk vlan-70 vlan-79 created                 | allocMode:static, descr:IWE Usage, from:vlan-70, role:external, to:vlan-79,    | 
|              |      |          |            |                               |                                                  | userdom::all:common:                                                           | 
+--------------+------+----------+------------+-------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------+
| HX1_VlanPool | Info | E4212059 | transition | 2021-12-09T23:58:28.139+02:00 | VlanInstP Static Allocation HX1_VlanPool created | allocMode:static, name:HX1_VlanPool, userdom::all:common:                      | 
+--------------+------+----------+------------+-------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci pool vlan --apic apic21 --name HX* --when any --view all

{
    "duration": 4448,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 366,
        "disconnect_time": 0,
        "mo_time": 3826,
        "total_time": 4192
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

True	366	-	connect apic21o.emea-sp.cisco.com:443
True	316	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	295	32	apic21o.emea-sp.cisco.com:443 class vmmEpPD
True	290	0	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree-include=faults,no-scoped,subtree
True	635	0	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	1607	0	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	683	209	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./PoolVlan.md)