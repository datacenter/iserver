# VMM Domain

## VLAN view

```
# iserver get aci domain vmm --apic apic21 --view vlan

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call
[INFO] Requires per-interface api call

VMM Domain - Interfaces VLAN [#4]
---------------------------------

+---------+----------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| Faults  | Domain         | AAEP               | VLAN Pool              | Encapsulation Block   | Node           | Interface | State | Mode  | VLANs                                   |
+---------+----------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 6 0 0 | EU-SPDC-CDC-22 | ESX-CDC-22_AAEP    | ESX-CDC-22_VlanPool    | [2501-2502] (static)  | cl2201-eu-spdc | eth1/31   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                |                    |                        | [2503-2509] (static)  | cl2201-eu-spdc | eth1/32   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                |                    |                        | [2700-2999] (dynamic) | cl2201-eu-spdc | eth1/33   | down  | trunk | 2701-2704,2708,2902                     | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/34   | up    | trunk | 2701-2704,2708,2800-2801,2804,2900-2902 | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/35   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/36   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/37   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/38   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/39   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/40   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/41   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/42   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/43   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/44   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/45   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/46   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/47   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/31   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/32   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/33   | down  | trunk | 2701-2704,2708,2902                     | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/34   | up    | trunk | 2701-2704,2708,2800-2801,2804,2900-2902 | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/35   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/36   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/37   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/38   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/39   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/40   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/41   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/42   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/43   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/44   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/45   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/46   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/47   | up    | trunk | 2701-2704,2708,2804,2902                | 
+---------+----------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 1 0 0 | EU-SPDC-POD2B  |                    | k8s_esx_VlanPool       | [800-809] (static)    |                |           |       |       |                                         | 
|         |                |                    |                        | [1300-1499] (dynamic) |                |           |       |       |                                         | 
+---------+----------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 4 0 0 | EU-SPDC-R7DC   | ESX-R7DC_AAEP      | ESX-R7DC_VlanPool      | [3701-3800] (dynamic) | rl2701-eu-spdc | eth1/1    | down  | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2701-eu-spdc | eth1/10   | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2701-eu-spdc | eth1/11   | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2701-eu-spdc | eth1/12   | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2701-eu-spdc | eth1/13   | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2701-eu-spdc | eth1/2    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2701-eu-spdc | eth1/3    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2701-eu-spdc | eth1/4    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2701-eu-spdc | eth1/5    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2701-eu-spdc | eth1/6    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2701-eu-spdc | eth1/7    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2701-eu-spdc | eth1/8    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2701-eu-spdc | eth1/9    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/1    | down  | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/10   | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/11   | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/12   | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/13   | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/2    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/3    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/4    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/5    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/6    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/7    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/8    | up    | trunk | 3735-3736                               | 
|         |                |                    |                        |                       | rl2702-eu-spdc | eth1/9    | up    | trunk | 3735-3736                               | 
+---------+----------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 5 0 0 | vEPC-Dataplane | vEPC-ESX21-22_AAEP | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  | bl2205-eu-spdc | eth1/19   | up    | trunk | 2700-2701,2800,2900                     | 
|         |                |                    |                        | [2700-2999] (dynamic) | bl2206-eu-spdc | eth1/19   | up    | trunk | 2700-2701,2800,2900                     | 
|         |                |                    |                        |                       | cl2201-eu-spdc | eth1/90   | up    | trunk |                                         | 
|         |                |                    |                        |                       | cl2202-eu-spdc | eth1/90   | up    | trunk |                                         | 
|         |                |                    |                        |                       | cl2207-eu-spdc | eth1/19   | up    | trunk |                                         | 
|         |                |                    |                        |                       | cl2208-eu-spdc | eth1/19   | up    | trunk |                                         | 
+---------+----------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --view vlan

{
    "duration": 52868,
    "apic": {
        "read": true,
        "success": 98,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 97,
        "connect_time": 486,
        "disconnect_time": 0,
        "mo_time": 47941,
        "total_time": 48427
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

True	486	-	connect apic21o.emea-sp.cisco.com:443
True	373	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	769	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	350	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	621	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-EU-SPDC-CDC-22 query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	362	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1998	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	456	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ethpmPhysIf
True	414	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	507	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	378	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vlanCktEp
True	371	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	401	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	377	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	365	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	402	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	375	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/37] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	419	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/38] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	400	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/39] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	389	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/40] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	424	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/41] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/42] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	376	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/43] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	405	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/44] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	332	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/45] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	375	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/46] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	418	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/47] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	2271	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	574	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ethpmPhysIf
True	340	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	354	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vlanCktEp
True	613	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	407	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	378	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	388	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	428	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	372	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/37] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	410	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/38] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	413	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/39] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	367	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/40] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	341	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/41] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	367	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/42] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	416	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/43] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	357	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/44] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	357	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/45] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	397	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/46] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	370	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/47] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	651	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-EU-SPDC-R7DC query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	1517	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	398	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ethpmPhysIf
True	328	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	344	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/vlanCktEp
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	370	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	450	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	379	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	404	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	433	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	364	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	422	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	412	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	357	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1645	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	367	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ethpmPhysIf
True	362	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	379	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/vlanCktEp
True	364	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	456	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	398	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	354	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	365	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	421	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	364	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	406	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	370	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	377	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	400	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	357	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-EU-SPDC-POD2B query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	681	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-vEPC-Dataplane query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	1050	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	367	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	434	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	347	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	1009	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	339	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ethpmPhysIf
True	349	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vlanCktEp
True	449	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/90] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/90] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1396	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	431	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ethpmPhysIf
True	358	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1262	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	386	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ethpmPhysIf
True	411	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./DomainVmm.md)