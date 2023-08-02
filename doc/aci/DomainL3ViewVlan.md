# L3 Domain

## VLAN view

```
# iserver get aci domain l3 --apic apic21 --view vlan

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call
[INFO] Requires per-interface api call

L3 Domain - Interfaces VLAN [#7]
--------------------------------

+---------+-----------------------+------------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| Faults  | Domain                | AAEP                   | VLAN Pool              | Encapsulation Block   | Node           | Interface | State | Mode  | VLANs                                   |
+---------+-----------------------+------------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | Infra_L3Dom           | TEST-AAP               | Infra_VlanPool         | [1-1000] (static)     | bl2205-eu-spdc | eth1/25   | up    | trunk |                                         | 
|         |                       | Infra_AAEP             |                        |                       | bl2206-eu-spdc | eth1/25   | up    | trunk |                                         | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/25   | down  | trunk |                                         | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/96   | up    | trunk |                                         | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/25   | down  | trunk |                                         | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/96   | up    | trunk |                                         | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/31   | down  | trunk |                                         | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/31   | down  | trunk |                                         | 
+---------+-----------------------+------------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | k8s_phys_L3Dom        | k8s_phys_AAEP          | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | eth1/1/3  | up    | trunk | 801,809                                 | 
|         |                       |                        |                        | [810-813] (static)    | cl2207-eu-spdc | eth1/1/4  | up    | trunk | 802,809                                 | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/2/1  | down  | trunk | 809                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/2/2  | up    | trunk | 809                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/2/3  | up    | trunk | 809                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/3/1  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/3/2  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/3/3  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/3/4  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/4/1  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/4/2  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/4/3  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/5/1  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/5/2  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/5/3  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/5/4  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/6/1  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/6/2  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/6/3  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/1/3  | up    | trunk | 801,809                                 | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/1/4  | up    | trunk | 802,809                                 | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/2/1  | down  | trunk | 809                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/2/2  | up    | trunk | 809                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/2/3  | up    | trunk | 809                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/3/1  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/3/2  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/3/3  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/3/4  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/4/1  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/4/2  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/4/3  | up    | trunk | 808                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/5/1  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/5/2  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/5/3  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/5/4  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/6/1  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/6/2  | up    | trunk | 807                                     | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/6/3  | down  | trunk | 807                                     | 
+---------+-----------------------+------------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | L3_Domain_vsfo        |                        | Infra_VlanPool         | [1-1000] (static)     |                |           |       |       |                                         | 
+---------+-----------------------+------------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | multipodL3out_L3Dom   | multipodL3out_AAEP     | multipodL3out_VlanPool | [4-4] (dynamic)       |                |           |       |       |                                         | 
+---------+-----------------------+------------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | RL-L3Out_RoutedDomain | RL-L3Out_EntityProfile | RL-L3Out_VlanPool      | [4-4] (dynamic)       |                |           |       |       |                                         | 
+---------+-----------------------+------------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | UCSB1_L3Dom           | UCSB1_AAEP             | UCSB1_VlanPool         | [2-100] (static)      | bl2205-eu-spdc | eth1/1    | up    | trunk |                                         | 
|         |                       |                        |                        | [3701-4000] (dynamic) | bl2205-eu-spdc | eth1/2    | up    | trunk |                                         | 
|         |                       |                        |                        |                       | bl2206-eu-spdc | eth1/1    | up    | trunk |                                         | 
|         |                       |                        |                        |                       | bl2206-eu-spdc | eth1/2    | up    | trunk |                                         | 
+---------+-----------------------+------------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | vEPC_ESX              | ESX-CDC-22_AAEP        | ESX-CDC-22_VlanPool    | [2501-2502] (static)  | bl2205-eu-spdc | eth1/19   | up    | trunk | 2700-2701,2800,2900                     | 
|         |                       | vEPC-ESX21-22_AAEP     |                        | [2503-2509] (static)  | bl2206-eu-spdc | eth1/19   | up    | trunk | 2700-2701,2800,2900                     | 
|         |                       |                        |                        | [2700-2999] (dynamic) | cl2201-eu-spdc | eth1/31   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/32   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/33   | down  | trunk | 2701-2704,2708,2902                     | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/34   | up    | trunk | 2701-2704,2708,2800-2801,2804,2900-2902 | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/35   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/36   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/37   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/38   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/39   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/40   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/41   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/42   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/43   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/44   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/45   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/46   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/47   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2201-eu-spdc | eth1/90   | up    | trunk |                                         | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/31   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/32   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/33   | down  | trunk | 2701-2704,2708,2902                     | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/34   | up    | trunk | 2701-2704,2708,2800-2801,2804,2900-2902 | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/35   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/36   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/37   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/38   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/39   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/40   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/41   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/42   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/43   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/44   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/45   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/46   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/47   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                        |                        |                       | cl2202-eu-spdc | eth1/90   | up    | trunk |                                         | 
|         |                       |                        |                        |                       | cl2207-eu-spdc | eth1/19   | up    | trunk |                                         | 
|         |                       |                        |                        |                       | cl2208-eu-spdc | eth1/19   | up    | trunk |                                         | 
+---------+-----------------------+------------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
```

Developer

```
# iserver get aci domain l3 --apic apic21 --view vlan

{
    "duration": 61621,
    "apic": {
        "read": true,
        "success": 120,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 119,
        "connect_time": 483,
        "disconnect_time": 0,
        "mo_time": 55461,
        "total_time": 55944
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

True	483	-	connect apic21o.emea-sp.cisco.com:443
True	406	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	1372	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	444	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-L3_Domain_vsfo query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	669	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-multipodL3out_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	768	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-Infra_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	369	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1124	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	372	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	356	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1055	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	443	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ethpmPhysIf
True	450	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	2158	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	467	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ethpmPhysIf
True	361	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	320	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/96] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	2048	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	407	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ethpmPhysIf
True	360	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	431	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/96] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1331	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	387	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ethpmPhysIf
True	336	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1322	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	379	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ethpmPhysIf
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	740	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-k8s_phys_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	364	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	512	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	346	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vlanCktEp
True	341	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	366	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/2/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	361	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/2/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	389	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/2/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	400	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/3/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	392	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/3/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	386	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/3/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	421	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/3/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/4/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	382	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/4/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	446	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/4/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/5/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	369	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/5/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	448	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/5/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	336	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/5/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	357	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/6/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	327	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/6/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	330	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/6/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	333	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	338	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vlanCktEp
True	418	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	374	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/2/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	431	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/2/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	367	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/2/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	381	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/3/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	397	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/3/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	378	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/3/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	352	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/3/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	349	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/4/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	330	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/4/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	363	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/4/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	382	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/5/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	363	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/5/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	384	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/5/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	340	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/5/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/6/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	380	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/6/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	371	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/6/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	638	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-RL-L3Out_RoutedDomain query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	852	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-vEPC_ESX query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	424	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	373	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	418	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vlanCktEp
True	392	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	371	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vlanCktEp
True	379	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	375	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	366	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	393	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	409	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	380	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/37] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	395	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/38] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/39] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	363	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/40] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	423	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/41] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	382	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/42] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	402	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/43] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	365	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/44] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	390	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/45] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	419	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/46] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	401	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/47] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	368	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/90] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	342	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vlanCktEp
True	365	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	464	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	413	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	342	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	395	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	329	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/37] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	391	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/38] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	350	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/39] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	374	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/40] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	416	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/41] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	441	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/42] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	475	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/43] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	375	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/44] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	394	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/45] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	415	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/46] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	390	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/47] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	453	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/90] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	361	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	770	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-UCSB1_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	346	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	377	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	375	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	410	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./DomainL3.md)