# L2 Domain

## All view

```
# iserver get aci domain l2 --apic apic21 --name infra* --when any --view all

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call
[INFO] Requires per-interface api call

L2 Domain [#1]
--------------

+---------+-------------+------------+----------------+--------+---------------------+------------+
| Faults  | Domain      | AAEP       | VLAN Pool      | Mode   | Encapsulation Block | Sec Domain |
+---------+-------------+------------+----------------+--------+---------------------+------------+
| 0 0 0 0 | Infra_L2dom | Infra_AAEP | Infra_VlanPool | static | [1-1000] (static)   | --         | 
+---------+-------------+------------+----------------+--------+---------------------+------------+

L2 Domain - Nodes [#1]
----------------------

+---------+-------------+------------+----------------+----------------+------------+
| Faults  | Domain      | AAEP       | VLAN Pool      | Node           | Interfaces |
+---------+-------------+------------+----------------+----------------+------------+
| 0 0 0 0 | Infra_L2dom | Infra_AAEP | Infra_VlanPool | bl2205-eu-spdc | 1          | 
|         |             |            |                | bl2206-eu-spdc | 1          | 
|         |             |            |                | cl2201-eu-spdc | 2          | 
|         |             |            |                | cl2202-eu-spdc | 2          | 
+---------+-------------+------------+----------------+----------------+------------+

L2 Domain - Interfaces [#1]
---------------------------

+---------+-------------+------------+----------------+----------------+-----------+
| Faults  | Domain      | AAEP       | VLAN Pool      | Node           | Interface |
+---------+-------------+------------+----------------+----------------+-----------+
| 0 0 0 0 | Infra_L2dom | Infra_AAEP | Infra_VlanPool | bl2205-eu-spdc | eth1/25   | 
|         |             |            |                | bl2206-eu-spdc | eth1/25   | 
|         |             |            |                | cl2201-eu-spdc | eth1/25   | 
|         |             |            |                | cl2201-eu-spdc | eth1/96   | 
|         |             |            |                | cl2202-eu-spdc | eth1/25   | 
|         |             |            |                | cl2202-eu-spdc | eth1/96   | 
+---------+-------------+------------+----------------+----------------+-----------+

L2 Domain - Interfaces VLAN [#1]
--------------------------------

+---------+-------------+------------+----------------+---------------------+----------------+-----------+-------+-------+-------+
| Faults  | Domain      | AAEP       | VLAN Pool      | Encapsulation Block | Node           | Interface | State | Mode  | VLANs |
+---------+-------------+------------+----------------+---------------------+----------------+-----------+-------+-------+-------+
| 0 0 0 0 | Infra_L2dom | Infra_AAEP | Infra_VlanPool | [1-1000] (static)   | bl2205-eu-spdc | eth1/25   | up    | trunk |       | 
|         |             |            |                |                     | bl2206-eu-spdc | eth1/25   | up    | trunk |       | 
|         |             |            |                |                     | cl2201-eu-spdc | eth1/25   | down  | trunk |       | 
|         |             |            |                |                     | cl2201-eu-spdc | eth1/96   | up    | trunk |       | 
|         |             |            |                |                     | cl2202-eu-spdc | eth1/25   | down  | trunk |       | 
|         |             |            |                |                     | cl2202-eu-spdc | eth1/96   | up    | trunk |       | 
+---------+-------------+------------+----------------+---------------------+----------------+-----------+-------+-------+-------+

L2 Domain - Policy Relationships [#1]
-------------------------------------

+---------+-------------+-------------+-------------+
| Faults  | Domain      | Policy Type | Policy Name |
+---------+-------------+-------------+-------------+
| 0 0 0 0 | Infra_L2dom | AAEP        | Infra_AAEP  | 
|         |             | L2 Out      | k8s/Test    | 
+---------+-------------+-------------+-------------+

L2 Domain - Faults [#0]
-----------------------
None

L2 Domain - Fault Records last 10y [#0]
---------------------------------------
None

L2 Domain - Event Logs last 10y [#0]
------------------------------------
None

L2 Domain - Audit Logs last 10y [#0]
------------------------------------
None
```

Developer

```
# iserver get aci domain l2 --apic apic21 --name infra* --when any --view all

{
    "duration": 15615,
    "apic": {
        "read": true,
        "success": 23,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 22,
        "connect_time": 426,
        "disconnect_time": 0,
        "mo_time": 13562,
        "total_time": 13988
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

True	426	-	connect apic21o.emea-sp.cisco.com:443
True	335	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	377	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	688	1	apic21o.emea-sp.cisco.com:443 mo uni/l2dom-Infra_L2dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	376	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	973	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	361	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	317	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1042	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	453	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ethpmPhysIf
True	392	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1998	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	423	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ethpmPhysIf
True	353	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	398	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/96] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	2340	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	428	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ethpmPhysIf
True	371	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	368	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/96] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	364	0	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree-include=faults,no-scoped,subtree
True	433	0	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	379	0	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	393	5	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./DomainL2.md)