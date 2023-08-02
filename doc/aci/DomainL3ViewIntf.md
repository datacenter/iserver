# L3 Domain

## Interface view

```
# iserver get aci domain l3 --apic apic21 --view intf

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call

L3 Domain - Interfaces [#7]
---------------------------

+---------+-----------------------+------------------------+------------------------+----------------+-----------+
| Faults  | Domain                | AAEP                   | VLAN Pool              | Node           | Interface |
+---------+-----------------------+------------------------+------------------------+----------------+-----------+
| 0 0 0 0 | Infra_L3Dom           | TEST-AAP               | Infra_VlanPool         | bl2205-eu-spdc | eth1/25   | 
|         |                       | Infra_AAEP             |                        | bl2206-eu-spdc | eth1/25   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/25   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/96   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/25   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/96   | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/31   | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/31   | 
+---------+-----------------------+------------------------+------------------------+----------------+-----------+
| 0 0 0 0 | k8s_phys_L3Dom        | k8s_phys_AAEP          | k8s_phys_VlanPool      | cl2207-eu-spdc | eth1/1/3  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/1/4  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/2/1  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/2/2  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/2/3  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/3/1  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/3/2  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/3/3  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/3/4  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/4/1  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/4/2  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/4/3  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/5/1  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/5/2  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/5/3  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/5/4  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/6/1  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/6/2  | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/6/3  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/1/3  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/1/4  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/2/1  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/2/2  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/2/3  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/3/1  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/3/2  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/3/3  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/3/4  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/4/1  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/4/2  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/4/3  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/5/1  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/5/2  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/5/3  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/5/4  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/6/1  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/6/2  | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/6/3  | 
+---------+-----------------------+------------------------+------------------------+----------------+-----------+
| 0 0 0 0 | L3_Domain_vsfo        |                        | Infra_VlanPool         |                |           | 
+---------+-----------------------+------------------------+------------------------+----------------+-----------+
| 0 0 0 0 | multipodL3out_L3Dom   | multipodL3out_AAEP     | multipodL3out_VlanPool |                |           | 
+---------+-----------------------+------------------------+------------------------+----------------+-----------+
| 0 0 0 0 | RL-L3Out_RoutedDomain | RL-L3Out_EntityProfile | RL-L3Out_VlanPool      |                |           | 
+---------+-----------------------+------------------------+------------------------+----------------+-----------+
| 0 0 0 0 | UCSB1_L3Dom           | UCSB1_AAEP             | UCSB1_VlanPool         | bl2205-eu-spdc | eth1/1    | 
|         |                       |                        |                        | bl2205-eu-spdc | eth1/2    | 
|         |                       |                        |                        | bl2206-eu-spdc | eth1/1    | 
|         |                       |                        |                        | bl2206-eu-spdc | eth1/2    | 
+---------+-----------------------+------------------------+------------------------+----------------+-----------+
| 0 0 0 0 | vEPC_ESX              | ESX-CDC-22_AAEP        | ESX-CDC-22_VlanPool    | bl2205-eu-spdc | eth1/19   | 
|         |                       | vEPC-ESX21-22_AAEP     |                        | bl2206-eu-spdc | eth1/19   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/31   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/32   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/33   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/34   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/35   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/36   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/37   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/38   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/39   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/40   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/41   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/42   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/43   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/44   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/45   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/46   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/47   | 
|         |                       |                        |                        | cl2201-eu-spdc | eth1/90   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/31   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/32   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/33   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/34   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/35   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/36   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/37   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/38   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/39   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/40   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/41   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/42   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/43   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/44   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/45   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/46   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/47   | 
|         |                       |                        |                        | cl2202-eu-spdc | eth1/90   | 
|         |                       |                        |                        | cl2207-eu-spdc | eth1/19   | 
|         |                       |                        |                        | cl2208-eu-spdc | eth1/19   | 
+---------+-----------------------+------------------------+------------------------+----------------+-----------+
```

Developer

```
# iserver get aci domain l3 --apic apic21 --view intf

{
    "duration": 7036,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 471,
        "disconnect_time": 0,
        "mo_time": 5691,
        "total_time": 6162
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

True	471	-	connect apic21o.emea-sp.cisco.com:443
True	335	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	374	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-L3_Domain_vsfo query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	748	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-multipodL3out_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	839	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-Infra_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	387	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	709	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-k8s_phys_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	652	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-RL-L3Out_RoutedDomain query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	911	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-vEPC_ESX query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	736	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-UCSB1_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
```

[[Back]](./DomainL3.md)