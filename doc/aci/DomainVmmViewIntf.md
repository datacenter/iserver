# VMM Domain

## Interface view

```
# iserver get aci domain vmm --apic apic21 --view intf

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call

VMM Domain - Interfaces [#4]
----------------------------

+---------+----------------+--------------------+------------------------+----------------+-----------+
| Faults  | Domain         | AAEP               | VLAN Pool              | Node           | Interface |
+---------+----------------+--------------------+------------------------+----------------+-----------+
| 0 6 0 0 | EU-SPDC-CDC-22 | ESX-CDC-22_AAEP    | ESX-CDC-22_VlanPool    | cl2201-eu-spdc | eth1/31   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/32   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/33   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/34   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/35   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/36   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/37   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/38   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/39   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/40   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/41   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/42   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/43   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/44   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/45   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/46   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/47   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/31   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/32   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/33   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/34   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/35   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/36   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/37   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/38   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/39   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/40   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/41   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/42   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/43   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/44   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/45   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/46   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/47   | 
+---------+----------------+--------------------+------------------------+----------------+-----------+
| 0 1 0 0 | EU-SPDC-POD2B  |                    | k8s_esx_VlanPool       |                |           | 
+---------+----------------+--------------------+------------------------+----------------+-----------+
| 0 4 0 0 | EU-SPDC-R7DC   | ESX-R7DC_AAEP      | ESX-R7DC_VlanPool      | rl2701-eu-spdc | eth1/1    | 
|         |                |                    |                        | rl2701-eu-spdc | eth1/10   | 
|         |                |                    |                        | rl2701-eu-spdc | eth1/11   | 
|         |                |                    |                        | rl2701-eu-spdc | eth1/12   | 
|         |                |                    |                        | rl2701-eu-spdc | eth1/13   | 
|         |                |                    |                        | rl2701-eu-spdc | eth1/2    | 
|         |                |                    |                        | rl2701-eu-spdc | eth1/3    | 
|         |                |                    |                        | rl2701-eu-spdc | eth1/4    | 
|         |                |                    |                        | rl2701-eu-spdc | eth1/5    | 
|         |                |                    |                        | rl2701-eu-spdc | eth1/6    | 
|         |                |                    |                        | rl2701-eu-spdc | eth1/7    | 
|         |                |                    |                        | rl2701-eu-spdc | eth1/8    | 
|         |                |                    |                        | rl2701-eu-spdc | eth1/9    | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/1    | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/10   | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/11   | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/12   | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/13   | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/2    | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/3    | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/4    | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/5    | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/6    | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/7    | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/8    | 
|         |                |                    |                        | rl2702-eu-spdc | eth1/9    | 
+---------+----------------+--------------------+------------------------+----------------+-----------+
| 0 5 0 0 | vEPC-Dataplane | vEPC-ESX21-22_AAEP | vEPC-ESX21-22_VlanPool | bl2205-eu-spdc | eth1/19   | 
|         |                |                    |                        | bl2206-eu-spdc | eth1/19   | 
|         |                |                    |                        | cl2201-eu-spdc | eth1/90   | 
|         |                |                    |                        | cl2202-eu-spdc | eth1/90   | 
|         |                |                    |                        | cl2207-eu-spdc | eth1/19   | 
|         |                |                    |                        | cl2208-eu-spdc | eth1/19   | 
+---------+----------------+--------------------+------------------------+----------------+-----------+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --view intf

{
    "duration": 5177,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 461,
        "disconnect_time": 0,
        "mo_time": 3873,
        "total_time": 4334
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

True	461	-	connect apic21o.emea-sp.cisco.com:443
True	418	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	816	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	657	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-EU-SPDC-CDC-22 query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	353	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	647	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-EU-SPDC-R7DC query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	319	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-EU-SPDC-POD2B query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	663	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-vEPC-Dataplane query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
```

[[Back]](./DomainVmm.md)