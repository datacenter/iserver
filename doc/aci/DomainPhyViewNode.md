# Physical Domain

## Node view

```
# iserver get aci domain phy --apic apic21 --view node

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call

Physical Domain - Node [#12]
----------------------------

+---------+-----------------------+--------------------+------------------------+----------------+------------+
| Faults  | Domain                | AAEP               | VLAN Pool              | Node           | Interfaces |
+---------+-----------------------+--------------------+------------------------+----------------+------------+
| 0 0 0 0 | ESX-CDC-22_PhysDom    | ESX-CDC-22_AAEP    | ESX-CDC-22_VlanPool    | cl2201-eu-spdc | 17         | 
|         |                       |                    |                        | cl2202-eu-spdc | 17         | 
+---------+-----------------------+--------------------+------------------------+----------------+------------+
| 0 0 0 0 | ESX-R7DC_PhysDom      | ESX-R7DC_AAEP      | ESX-R7DC_VlanPool      | rl2701-eu-spdc | 13         | 
|         |                       |                    |                        | rl2702-eu-spdc | 13         | 
+---------+-----------------------+--------------------+------------------------+----------------+------------+
| 0 0 0 0 | HX1_PhysDom           | HX1_AAEP           | HX1_VlanPool           | bl2205-eu-spdc | 2          | 
|         |                       |                    |                        | bl2206-eu-spdc | 2          | 
+---------+-----------------------+--------------------+------------------------+----------------+------------+
| 0 0 0 0 | Infra_PhysDom         | vEPC-ESX21-22_AAEP | Infra_VlanPool         | bl2205-eu-spdc | 2          | 
|         |                       | Infra_AAEP         |                        | bl2206-eu-spdc | 2          | 
|         |                       |                    |                        | cl2201-eu-spdc | 3          | 
|         |                       |                    |                        | cl2202-eu-spdc | 3          | 
|         |                       |                    |                        | cl2207-eu-spdc | 1          | 
|         |                       |                    |                        | cl2208-eu-spdc | 1          | 
+---------+-----------------------+--------------------+------------------------+----------------+------------+
| 0 0 0 0 | k8s_esx_PhysDom       | k8s_esx_AAEP       | k8s_esx_VlanPool       | cl2207-eu-spdc | 2          | 
|         |                       |                    |                        | cl2208-eu-spdc | 2          | 
+---------+-----------------------+--------------------+------------------------+----------------+------------+
| 0 0 0 0 | k8s_phys_PhysDom      | k8s_phys_AAEP      | k8s_phys_VlanPool      | cl2207-eu-spdc | 19         | 
|         |                       |                    |                        | cl2208-eu-spdc | 19         | 
+---------+-----------------------+--------------------+------------------------+----------------+------------+
| 0 0 0 0 | nidemo                | nidemo             | nidemo-3000-3001       | rl2701-eu-spdc | 2          | 
|         |                       |                    |                        | rl2702-eu-spdc | 2          | 
+---------+-----------------------+--------------------+------------------------+----------------+------------+
| 0 0 0 0 | SPN_PhysDom           | SPN_AAEP           | SPN_VlanPool           | bl2205-eu-spdc | 1          | 
|         |                       |                    |                        | bl2206-eu-spdc | 1          | 
+---------+-----------------------+--------------------+------------------------+----------------+------------+
| 0 0 0 0 | UCSB1-R7DC_PhysDom    | UCSB1-R7DC_AAEP    | UCSB1-R7DC_VlanPool    | rl2701-eu-spdc | 2          | 
|         |                       |                    |                        | rl2702-eu-spdc | 2          | 
+---------+-----------------------+--------------------+------------------------+----------------+------------+
| 0 0 0 0 | UCSB1_PhysDom         | UCSB1_AAEP         | UCSB1_VlanPool         | bl2205-eu-spdc | 2          | 
|         |                       |                    |                        | bl2206-eu-spdc | 2          | 
+---------+-----------------------+--------------------+------------------------+----------------+------------+
| 0 0 0 0 | vEPC-ESX20_PhysDom    | vEPC-ESX21-22_AAEP | vEPC-ESX21-22_VlanPool | bl2205-eu-spdc | 1          | 
|         |                       |                    |                        | bl2206-eu-spdc | 1          | 
|         |                       |                    |                        | cl2201-eu-spdc | 1          | 
|         |                       |                    |                        | cl2202-eu-spdc | 1          | 
|         |                       |                    |                        | cl2207-eu-spdc | 1          | 
|         |                       |                    |                        | cl2208-eu-spdc | 1          | 
+---------+-----------------------+--------------------+------------------------+----------------+------------+
| 0 0 0 0 | vEPC-ESX21-22_PhysDom | vEPC-ESX21-22_AAEP | vEPC-ESX21-22_VlanPool | bl2205-eu-spdc | 1          | 
|         |                       |                    |                        | bl2206-eu-spdc | 1          | 
|         |                       |                    |                        | cl2201-eu-spdc | 1          | 
|         |                       |                    |                        | cl2202-eu-spdc | 1          | 
|         |                       |                    |                        | cl2207-eu-spdc | 1          | 
|         |                       |                    |                        | cl2208-eu-spdc | 1          | 
+---------+-----------------------+--------------------+------------------------+----------------+------------+
```

Developer

```
# iserver get aci domain phy --apic apic21 --view node

{
    "duration": 12085,
    "apic": {
        "read": true,
        "success": 15,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 14,
        "connect_time": 448,
        "disconnect_time": 0,
        "mo_time": 10696,
        "total_time": 11144
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

True	448	-	connect apic21o.emea-sp.cisco.com:443
True	399	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	729	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-k8s_esx_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	375	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	689	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-k8s_phys_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	659	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-UCSB1-R7DC_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	762	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-vEPC-ESX20_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	735	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-vEPC-ESX21-22_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	980	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-Infra_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	1804	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-nidemo query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	703	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-SPN_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	712	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-UCSB1_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	673	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-HX1_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	712	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-ESX-CDC-22_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	764	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-ESX-R7DC_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
```

[[Back]](./DomainPhy.md)