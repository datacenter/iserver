# VMM Domain

## Node view

```
# iserver get aci domain vmm --apic apic21 --view node

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call

VMM Domain - Nodes [#4]
-----------------------

+---------+----------------+--------------------+------------------------+----------------+------------+
| Faults  | Domain         | AAEP               | VLAN Pool              | Node           | Interfaces |
+---------+----------------+--------------------+------------------------+----------------+------------+
| 0 6 0 0 | EU-SPDC-CDC-22 | ESX-CDC-22_AAEP    | ESX-CDC-22_VlanPool    | cl2201-eu-spdc | 17         | 
|         |                |                    |                        | cl2202-eu-spdc | 17         | 
+---------+----------------+--------------------+------------------------+----------------+------------+
| 0 1 0 0 | EU-SPDC-POD2B  |                    | k8s_esx_VlanPool       |                |            | 
+---------+----------------+--------------------+------------------------+----------------+------------+
| 0 4 0 0 | EU-SPDC-R7DC   | ESX-R7DC_AAEP      | ESX-R7DC_VlanPool      | rl2701-eu-spdc | 13         | 
|         |                |                    |                        | rl2702-eu-spdc | 13         | 
+---------+----------------+--------------------+------------------------+----------------+------------+
| 0 5 0 0 | vEPC-Dataplane | vEPC-ESX21-22_AAEP | vEPC-ESX21-22_VlanPool | bl2205-eu-spdc | 1          | 
|         |                |                    |                        | bl2206-eu-spdc | 1          | 
|         |                |                    |                        | cl2201-eu-spdc | 1          | 
|         |                |                    |                        | cl2202-eu-spdc | 1          | 
|         |                |                    |                        | cl2207-eu-spdc | 1          | 
|         |                |                    |                        | cl2208-eu-spdc | 1          | 
+---------+----------------+--------------------+------------------------+----------------+------------+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --view node

{
    "duration": 5130,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 516,
        "disconnect_time": 0,
        "mo_time": 3861,
        "total_time": 4377
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

True	516	-	connect apic21o.emea-sp.cisco.com:443
True	382	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	777	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	665	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-EU-SPDC-CDC-22 query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	355	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	667	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-EU-SPDC-R7DC query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	368	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-EU-SPDC-POD2B query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	647	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-vEPC-Dataplane query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
```

[[Back]](./DomainVmm.md)