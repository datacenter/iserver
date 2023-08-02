# L3 Domain

## Node view

```
# iserver get aci domain l3 --apic apic21 --view node

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call

L3 Domain - Nodes [#7]
----------------------

+---------+-----------------------+------------------------+------------------------+----------------+------------+
| Faults  | Domain                | AAEP                   | VLAN Pool              | Node           | Interfaces |
+---------+-----------------------+------------------------+------------------------+----------------+------------+
| 0 0 0 0 | Infra_L3Dom           | TEST-AAP               | Infra_VlanPool         | bl2205-eu-spdc | 1          | 
|         |                       | Infra_AAEP             |                        | bl2206-eu-spdc | 1          | 
|         |                       |                        |                        | cl2201-eu-spdc | 2          | 
|         |                       |                        |                        | cl2202-eu-spdc | 2          | 
|         |                       |                        |                        | cl2207-eu-spdc | 1          | 
|         |                       |                        |                        | cl2208-eu-spdc | 1          | 
+---------+-----------------------+------------------------+------------------------+----------------+------------+
| 0 0 0 0 | k8s_phys_L3Dom        | k8s_phys_AAEP          | k8s_phys_VlanPool      | cl2207-eu-spdc | 19         | 
|         |                       |                        |                        | cl2208-eu-spdc | 19         | 
+---------+-----------------------+------------------------+------------------------+----------------+------------+
| 0 0 0 0 | L3_Domain_vsfo        |                        | Infra_VlanPool         |                |            | 
+---------+-----------------------+------------------------+------------------------+----------------+------------+
| 0 0 0 0 | multipodL3out_L3Dom   | multipodL3out_AAEP     | multipodL3out_VlanPool |                |            | 
+---------+-----------------------+------------------------+------------------------+----------------+------------+
| 0 0 0 0 | RL-L3Out_RoutedDomain | RL-L3Out_EntityProfile | RL-L3Out_VlanPool      |                |            | 
+---------+-----------------------+------------------------+------------------------+----------------+------------+
| 0 0 0 0 | UCSB1_L3Dom           | UCSB1_AAEP             | UCSB1_VlanPool         | bl2205-eu-spdc | 2          | 
|         |                       |                        |                        | bl2206-eu-spdc | 2          | 
+---------+-----------------------+------------------------+------------------------+----------------+------------+
| 0 0 0 0 | vEPC_ESX              | ESX-CDC-22_AAEP        | ESX-CDC-22_VlanPool    | bl2205-eu-spdc | 1          | 
|         |                       | vEPC-ESX21-22_AAEP     |                        | bl2206-eu-spdc | 1          | 
|         |                       |                        |                        | cl2201-eu-spdc | 18         | 
|         |                       |                        |                        | cl2202-eu-spdc | 18         | 
|         |                       |                        |                        | cl2207-eu-spdc | 1          | 
|         |                       |                        |                        | cl2208-eu-spdc | 1          | 
+---------+-----------------------+------------------------+------------------------+----------------+------------+
```

Developer

```
# iserver get aci domain l3 --apic apic21 --view node

{
    "duration": 7038,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 476,
        "disconnect_time": 0,
        "mo_time": 5853,
        "total_time": 6329
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

True	476	-	connect apic21o.emea-sp.cisco.com:443
True	395	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	408	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-L3_Domain_vsfo query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	692	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-multipodL3out_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	907	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-Infra_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	370	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	687	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-k8s_phys_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	639	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-RL-L3Out_RoutedDomain query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	986	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-vEPC_ESX query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	769	1	apic21o.emea-sp.cisco.com:443 mo uni/l3dom-UCSB1_L3Dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
```

[[Back]](./DomainL3.md)