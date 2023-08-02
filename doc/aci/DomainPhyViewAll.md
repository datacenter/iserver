# Physical Domain

## All view

```
# iserver get aci domain phy --apic apic21 --name UCSB* --when any --view all

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call
[INFO] Requires per-interface api call

Physical Domain [#2]
--------------------

+---------+--------------------+-----------------+---------------------+---------+-----------------------+------------+
| Faults  | Domain             | AAEP            | VLAN Pool           | Mode    | Encapsulation Block   | Sec Domain |
+---------+--------------------+-----------------+---------------------+---------+-----------------------+------------+
| 0 0 0 0 | UCSB1-R7DC_PhysDom | UCSB1-R7DC_AAEP | UCSB1-R7DC_VlanPool | dynamic | [2-100] (static)      | --         | 
|         |                    |                 |                     |         | [1701-1899] (dynamic) |            | 
+---------+--------------------+-----------------+---------------------+---------+-----------------------+------------+
| 0 0 0 0 | UCSB1_PhysDom      | UCSB1_AAEP      | UCSB1_VlanPool      | dynamic | [2-100] (static)      | --         | 
|         |                    |                 |                     |         | [3701-4000] (dynamic) |            | 
+---------+--------------------+-----------------+---------------------+---------+-----------------------+------------+

Physical Domain - Node [#2]
---------------------------

+---------+--------------------+-----------------+---------------------+----------------+------------+
| Faults  | Domain             | AAEP            | VLAN Pool           | Node           | Interfaces |
+---------+--------------------+-----------------+---------------------+----------------+------------+
| 0 0 0 0 | UCSB1-R7DC_PhysDom | UCSB1-R7DC_AAEP | UCSB1-R7DC_VlanPool | rl2701-eu-spdc | 2          | 
|         |                    |                 |                     | rl2702-eu-spdc | 2          | 
+---------+--------------------+-----------------+---------------------+----------------+------------+
| 0 0 0 0 | UCSB1_PhysDom      | UCSB1_AAEP      | UCSB1_VlanPool      | bl2205-eu-spdc | 2          | 
|         |                    |                 |                     | bl2206-eu-spdc | 2          | 
+---------+--------------------+-----------------+---------------------+----------------+------------+

Physical Domain - Interfaces [#2]
---------------------------------

+---------+--------------------+-----------------+---------------------+----------------+-----------+
| Faults  | Domain             | AAEP            | VLAN Pool           | Node           | Interface |
+---------+--------------------+-----------------+---------------------+----------------+-----------+
| 0 0 0 0 | UCSB1-R7DC_PhysDom | UCSB1-R7DC_AAEP | UCSB1-R7DC_VlanPool | rl2701-eu-spdc | eth1/49   | 
|         |                    |                 |                     | rl2701-eu-spdc | eth1/50   | 
|         |                    |                 |                     | rl2702-eu-spdc | eth1/49   | 
|         |                    |                 |                     | rl2702-eu-spdc | eth1/50   | 
+---------+--------------------+-----------------+---------------------+----------------+-----------+
| 0 0 0 0 | UCSB1_PhysDom      | UCSB1_AAEP      | UCSB1_VlanPool      | bl2205-eu-spdc | eth1/1    | 
|         |                    |                 |                     | bl2205-eu-spdc | eth1/2    | 
|         |                    |                 |                     | bl2206-eu-spdc | eth1/1    | 
|         |                    |                 |                     | bl2206-eu-spdc | eth1/2    | 
+---------+--------------------+-----------------+---------------------+----------------+-----------+

Physical Domain - Interfaces VLAN [#2]
--------------------------------------

+---------+--------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+-------+
| Faults  | Domain             | AAEP            | VLAN Pool           | Encapsulation Block   | Node           | Interface | State | Mode  | VLANs |
+---------+--------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+-------+
| 0 0 0 0 | UCSB1-R7DC_PhysDom | UCSB1-R7DC_AAEP | UCSB1-R7DC_VlanPool | [2-100] (static)      | rl2701-eu-spdc | eth1/49   | up    | trunk |       | 
|         |                    |                 |                     | [1701-1899] (dynamic) | rl2701-eu-spdc | eth1/50   | up    | trunk |       | 
|         |                    |                 |                     |                       | rl2702-eu-spdc | eth1/49   | up    | trunk |       | 
|         |                    |                 |                     |                       | rl2702-eu-spdc | eth1/50   | up    | trunk |       | 
+---------+--------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+-------+
| 0 0 0 0 | UCSB1_PhysDom      | UCSB1_AAEP      | UCSB1_VlanPool      | [2-100] (static)      | bl2205-eu-spdc | eth1/1    | up    | trunk |       | 
|         |                    |                 |                     | [3701-4000] (dynamic) | bl2205-eu-spdc | eth1/2    | up    | trunk |       | 
|         |                    |                 |                     |                       | bl2206-eu-spdc | eth1/1    | up    | trunk |       | 
|         |                    |                 |                     |                       | bl2206-eu-spdc | eth1/2    | up    | trunk |       | 
+---------+--------------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+-------+

Physical Domain - Policy Relationships [#2]
-------------------------------------------

+---------+--------------------+-----------------+------------------------------+
| Faults  | Domain             | Policy Type     | Policy Name                  |
+---------+--------------------+-----------------+------------------------------+
| 0 0 0 0 | UCSB1-R7DC_PhysDom | AAEP            | UCSB1-R7DC_AAEP              | 
+---------+--------------------+-----------------+------------------------------+
| 0 0 0 0 | UCSB1_PhysDom      | Application EPG | vEPC_demo/vEPG_ANP/vEPG_MGMT | 
|         |                    | AAEP            | UCSB1_AAEP                   | 
+---------+--------------------+-----------------+------------------------------+

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
# iserver get aci domain phy --apic apic21 --name UCSB* --when any --view all

{
    "duration": 18327,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 562,
        "disconnect_time": 0,
        "mo_time": 15776,
        "total_time": 16338
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

True	562	-	connect apic21o.emea-sp.cisco.com:443
True	386	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	395	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	674	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-UCSB1-R7DC_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	385	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1615	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	404	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ethpmPhysIf
True	477	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/49] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	385	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/50] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1814	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	501	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ethpmPhysIf
True	443	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/49] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	437	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/50] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	495	0	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree-include=faults,no-scoped,subtree
True	933	14	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	817	0	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	812	182	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
True	612	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-UCSB1_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	991	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	376	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	329	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	386	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	944	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	380	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ethpmPhysIf
True	414	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	371	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./DomainPhy.md)