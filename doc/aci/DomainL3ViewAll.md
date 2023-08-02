# L3 Domain

## All view

```
# iserver get aci domain l3 --apic apic21 --name UCSB* --when any --view all

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call
[INFO] Requires per-interface api call

L3 Domain [#1]
--------------

+---------+-------------+------------+----------------+---------+-----------------------+------------+
| Faults  | Domain      | AAEP       | VLAN Pool      | Mode    | Encapsulation Block   | Sec Domain |
+---------+-------------+------------+----------------+---------+-----------------------+------------+
| 0 0 0 0 | UCSB1_L3Dom | UCSB1_AAEP | UCSB1_VlanPool | dynamic | [2-100] (static)      | --         | 
|         |             |            |                |         | [3701-4000] (dynamic) |            | 
+---------+-------------+------------+----------------+---------+-----------------------+------------+

L3 Domain - Nodes [#1]
----------------------

+---------+-------------+------------+----------------+----------------+------------+
| Faults  | Domain      | AAEP       | VLAN Pool      | Node           | Interfaces |
+---------+-------------+------------+----------------+----------------+------------+
| 0 0 0 0 | UCSB1_L3Dom | UCSB1_AAEP | UCSB1_VlanPool | bl2205-eu-spdc | 2          | 
|         |             |            |                | bl2206-eu-spdc | 2          | 
+---------+-------------+------------+----------------+----------------+------------+

L3 Domain - Interfaces [#1]
---------------------------

+---------+-------------+------------+----------------+----------------+-----------+
| Faults  | Domain      | AAEP       | VLAN Pool      | Node           | Interface |
+---------+-------------+------------+----------------+----------------+-----------+
| 0 0 0 0 | UCSB1_L3Dom | UCSB1_AAEP | UCSB1_VlanPool | bl2205-eu-spdc | eth1/1    | 
|         |             |            |                | bl2205-eu-spdc | eth1/2    | 
|         |             |            |                | bl2206-eu-spdc | eth1/1    | 
|         |             |            |                | bl2206-eu-spdc | eth1/2    | 
+---------+-------------+------------+----------------+----------------+-----------+

L3 Domain - Interfaces VLAN [#1]
--------------------------------

+---------+-------------+------------+----------------+-----------------------+----------------+-----------+-------+-------+-------+
| Faults  | Domain      | AAEP       | VLAN Pool      | Encapsulation Block   | Node           | Interface | State | Mode  | VLANs |
+---------+-------------+------------+----------------+-----------------------+----------------+-----------+-------+-------+-------+
| 0 0 0 0 | UCSB1_L3Dom | UCSB1_AAEP | UCSB1_VlanPool | [2-100] (static)      | bl2205-eu-spdc | eth1/1    | up    | trunk |       | 
|         |             |            |                | [3701-4000] (dynamic) | bl2205-eu-spdc | eth1/2    | up    | trunk |       | 
|         |             |            |                |                       | bl2206-eu-spdc | eth1/1    | up    | trunk |       | 
|         |             |            |                |                       | bl2206-eu-spdc | eth1/2    | up    | trunk |       | 
+---------+-------------+------------+----------------+-----------------------+----------------+-----------+-------+-------+-------+

L3 Domain - Policy Relationships [#1]
-------------------------------------

+---------+-------------+-------------+-------------+
| Faults  | Domain      | Policy Type | Policy Name |
+---------+-------------+-------------+-------------+
| 0 0 0 0 | UCSB1_L3Dom | AAEP        | UCSB1_AAEP  | 
+---------+-------------+-------------+-------------+

L3 Domain - Faults [#0]
-----------------------
None

L3 Domain - Fault Records last 10y [#0]
---------------------------------------
None

L3 Domain - Event Logs last 10y [#0]
------------------------------------
None

L3 Domain - Audit Logs last 10y [#2]
------------------------------------

+-------------+------+----------+------------+-------------------------------+--------------------------+---------------------------------------------------------------------+
| Domain      | Sev  | Code     | Cause      | Created Time                  | Description              | Change Set                                                          |
+-------------+------+----------+------------+-------------------------------+--------------------------+---------------------------------------------------------------------+
| UCSB1_L3Dom | Info | E4214354 | transition | 2022-11-03T20:05:44.726+02:00 | RsVlanNs created         | tDn:uni/infra/vlanns-[UCSB1_VlanPool]-dynamic, userdom::all:common: | 
+-------------+------+----------+------------+-------------------------------+--------------------------+---------------------------------------------------------------------+
| UCSB1_L3Dom | Info | E4212452 | transition | 2022-11-03T20:05:44.725+02:00 | DomP UCSB1_L3Dom created | name:UCSB1_L3Dom, userdom::all:common:                              | 
+-------------+------+----------+------------+-------------------------------+--------------------------+---------------------------------------------------------------------+
```

Developer

```
# iserver get aci domain l3 --apic apic21 --name UCSB* --when any --view all

{
    "duration": 11060,
    "apic": {
        "read": true,
        "success": 17,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 16,
        "connect_time": 492,
        "disconnect_time": 0,
        "mo_time": 9639,
        "total_time": 10131
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

True	492	-	connect apic21o.emea-sp.cisco.com:443
True	416	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	370	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	837	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-UCSB1_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	429	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1108	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	403	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	395	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	487	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1128	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	374	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ethpmPhysIf
True	382	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	395	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	412	0	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree-include=faults,no-scoped,subtree
True	829	0	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	814	0	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	860	13	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./DomainL3.md)