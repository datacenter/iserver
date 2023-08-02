# Physical Domain

## Interface view

```
# iserver get aci domain phy --apic apic21 --view intf

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call

Physical Domain - Interfaces [#12]
----------------------------------

+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| Faults  | Domain                | AAEP               | VLAN Pool              | Node           | Interface |
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| 0 0 0 0 | ESX-CDC-22_PhysDom    | ESX-CDC-22_AAEP    | ESX-CDC-22_VlanPool    | cl2201-eu-spdc | eth1/31   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/32   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/33   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/34   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/35   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/36   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/37   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/38   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/39   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/40   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/41   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/42   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/43   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/44   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/45   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/46   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/47   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/31   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/32   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/33   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/34   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/35   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/36   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/37   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/38   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/39   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/40   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/41   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/42   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/43   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/44   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/45   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/46   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/47   | 
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| 0 0 0 0 | ESX-R7DC_PhysDom      | ESX-R7DC_AAEP      | ESX-R7DC_VlanPool      | rl2701-eu-spdc | eth1/1    | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/10   | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/11   | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/12   | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/13   | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/2    | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/3    | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/4    | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/5    | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/6    | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/7    | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/8    | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/9    | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/1    | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/10   | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/11   | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/12   | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/13   | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/2    | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/3    | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/4    | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/5    | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/6    | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/7    | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/8    | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/9    | 
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| 0 0 0 0 | HX1_PhysDom           | HX1_AAEP           | HX1_VlanPool           | bl2205-eu-spdc | eth1/11   | 
|         |                       |                    |                        | bl2205-eu-spdc | eth1/12   | 
|         |                       |                    |                        | bl2206-eu-spdc | eth1/11   | 
|         |                       |                    |                        | bl2206-eu-spdc | eth1/12   | 
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| 0 0 0 0 | Infra_PhysDom         | vEPC-ESX21-22_AAEP | Infra_VlanPool         | bl2205-eu-spdc | eth1/19   | 
|         |                       | Infra_AAEP         |                        | bl2205-eu-spdc | eth1/25   | 
|         |                       |                    |                        | bl2206-eu-spdc | eth1/19   | 
|         |                       |                    |                        | bl2206-eu-spdc | eth1/25   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/25   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/90   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/96   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/25   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/90   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/96   | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/19   | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/19   | 
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| 0 0 0 0 | k8s_esx_PhysDom       | k8s_esx_AAEP       | k8s_esx_VlanPool       | cl2207-eu-spdc | eth1/1/1  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/1/2  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/1/1  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/1/2  | 
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| 0 0 0 0 | k8s_phys_PhysDom      | k8s_phys_AAEP      | k8s_phys_VlanPool      | cl2207-eu-spdc | eth1/1/3  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/1/4  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/2/1  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/2/2  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/2/3  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/3/1  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/3/2  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/3/3  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/3/4  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/4/1  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/4/2  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/4/3  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/5/1  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/5/2  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/5/3  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/5/4  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/6/1  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/6/2  | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/6/3  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/1/3  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/1/4  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/2/1  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/2/2  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/2/3  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/3/1  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/3/2  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/3/3  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/3/4  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/4/1  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/4/2  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/4/3  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/5/1  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/5/2  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/5/3  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/5/4  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/6/1  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/6/2  | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/6/3  | 
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| 0 0 0 0 | nidemo                | nidemo             | nidemo-3000-3001       | rl2701-eu-spdc | eth1/19   | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/20   | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/19   | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/20   | 
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| 0 0 0 0 | SPN_PhysDom           | SPN_AAEP           | SPN_VlanPool           | bl2205-eu-spdc | eth1/27   | 
|         |                       |                    |                        | bl2206-eu-spdc | eth1/27   | 
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| 0 0 0 0 | UCSB1-R7DC_PhysDom    | UCSB1-R7DC_AAEP    | UCSB1-R7DC_VlanPool    | rl2701-eu-spdc | eth1/49   | 
|         |                       |                    |                        | rl2701-eu-spdc | eth1/50   | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/49   | 
|         |                       |                    |                        | rl2702-eu-spdc | eth1/50   | 
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| 0 0 0 0 | UCSB1_PhysDom         | UCSB1_AAEP         | UCSB1_VlanPool         | bl2205-eu-spdc | eth1/1    | 
|         |                       |                    |                        | bl2205-eu-spdc | eth1/2    | 
|         |                       |                    |                        | bl2206-eu-spdc | eth1/1    | 
|         |                       |                    |                        | bl2206-eu-spdc | eth1/2    | 
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| 0 0 0 0 | vEPC-ESX20_PhysDom    | vEPC-ESX21-22_AAEP | vEPC-ESX21-22_VlanPool | bl2205-eu-spdc | eth1/19   | 
|         |                       |                    |                        | bl2206-eu-spdc | eth1/19   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/90   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/90   | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/19   | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/19   | 
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
| 0 0 0 0 | vEPC-ESX21-22_PhysDom | vEPC-ESX21-22_AAEP | vEPC-ESX21-22_VlanPool | bl2205-eu-spdc | eth1/19   | 
|         |                       |                    |                        | bl2206-eu-spdc | eth1/19   | 
|         |                       |                    |                        | cl2201-eu-spdc | eth1/90   | 
|         |                       |                    |                        | cl2202-eu-spdc | eth1/90   | 
|         |                       |                    |                        | cl2207-eu-spdc | eth1/19   | 
|         |                       |                    |                        | cl2208-eu-spdc | eth1/19   | 
+---------+-----------------------+--------------------+------------------------+----------------+-----------+
```

Developer

```
# iserver get aci domain phy --apic apic21 --view intf

{
    "duration": 11137,
    "apic": {
        "read": true,
        "success": 15,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 14,
        "connect_time": 452,
        "disconnect_time": 0,
        "mo_time": 9570,
        "total_time": 10022
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

True	452	-	connect apic21o.emea-sp.cisco.com:443
True	371	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	671	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-k8s_esx_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	379	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	732	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-k8s_phys_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	634	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-UCSB1-R7DC_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	717	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-vEPC-ESX20_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	728	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-vEPC-ESX21-22_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	906	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-Infra_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	840	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-nidemo query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	674	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-SPN_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	694	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-UCSB1_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	667	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-HX1_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	701	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-ESX-CDC-22_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	856	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-ESX-R7DC_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
```

[[Back]](./DomainPhy.md)