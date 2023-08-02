# L2 Domain

## VLAN view

```
# iserver get aci domain l2 --apic apic21 --view vlan

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call
[INFO] Requires per-interface api call

L2 Domain - Interfaces VLAN [#2]
--------------------------------

+---------+-------------+------------+------------------+----------------------+----------------+-----------+-------+-------+-------+
| Faults  | Domain      | AAEP       | VLAN Pool        | Encapsulation Block  | Node           | Interface | State | Mode  | VLANs |
+---------+-------------+------------+------------------+----------------------+----------------+-----------+-------+-------+-------+
| 0 0 0 0 | Infra_L2dom | Infra_AAEP | Infra_VlanPool   | [1-1000] (static)    | bl2205-eu-spdc | eth1/25   | up    | trunk |       | 
|         |             |            |                  |                      | bl2206-eu-spdc | eth1/25   | up    | trunk |       | 
|         |             |            |                  |                      | cl2201-eu-spdc | eth1/25   | down  | trunk |       | 
|         |             |            |                  |                      | cl2201-eu-spdc | eth1/96   | up    | trunk |       | 
|         |             |            |                  |                      | cl2202-eu-spdc | eth1/25   | down  | trunk |       | 
|         |             |            |                  |                      | cl2202-eu-spdc | eth1/96   | up    | trunk |       | 
+---------+-------------+------------+------------------+----------------------+----------------+-----------+-------+-------+-------+
| 0 0 0 0 | test        | nidemo     | nidemo-3000-3001 | [3000-3001] (static) | rl2701-eu-spdc | eth1/19   | down  | trunk |       | 
|         |             |            |                  |                      | rl2701-eu-spdc | eth1/20   | down  | trunk |       | 
|         |             |            |                  |                      | rl2702-eu-spdc | eth1/19   | down  | trunk | 3000  | 
|         |             |            |                  |                      | rl2702-eu-spdc | eth1/20   | down  | trunk |       | 
+---------+-------------+------------+------------------+----------------------+----------------+-----------+-------+-------+-------+
```

Developer

```
# iserver get aci domain l2 --apic apic21 --view vlan

{
    "duration": 21245,
    "apic": {
        "read": true,
        "success": 30,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 29,
        "connect_time": 500,
        "disconnect_time": 0,
        "mo_time": 18676,
        "total_time": 19176
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

True	500	-	connect apic21o.emea-sp.cisco.com:443
True	407	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	362	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	685	1	apic21o.emea-sp.cisco.com:443 mo uni/l2dom-Infra_L2dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	363	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1003	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	351	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	403	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1083	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	374	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ethpmPhysIf
True	324	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	2099	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	405	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ethpmPhysIf
True	455	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	348	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/96] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	2055	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	382	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ethpmPhysIf
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	328	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/96] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	592	1	apic21o.emea-sp.cisco.com:443 mo uni/l2dom-test query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	1572	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	471	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ethpmPhysIf
True	405	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	322	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1571	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	370	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ethpmPhysIf
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	509	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	402	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/vlanCktEp
True	317	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./DomainL2.md)